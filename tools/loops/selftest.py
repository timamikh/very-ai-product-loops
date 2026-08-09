#!/usr/bin/env python3
"""Smoke test for the shared read layer — runs in CI next to the linter.

The linter checks the *canon*; this checks that the layer which reads the canon still works. It reads
the committed example instance end to end and asserts the invariants everything downstream (the
console today, writers and the agent bridge later) depends on. Stdlib only, no test framework.

Run:  python3 tools/loops/selftest.py
"""
import io
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))

from loops import framework as F  # noqa: E402
from loops import instance as I  # noqa: E402
from loops import text as T  # noqa: E402
from loops import yamlite  # noqa: E402

FAILED = []


def check(cond, what):
    if cond:
        print("  ok    %s" % what)
    else:
        print("  FAIL  %s" % what)
        FAILED.append(what)


def main():
    print("loops selftest\n")

    # -- yaml subset: the two instance files must parse with nothing skipped
    for name in ("config.yaml", "state.yaml"):
        p = os.path.join(ROOT, "examples", "decksmith", name)
        data, skipped = yamlite.load(p)
        check(isinstance(data, dict) and data, "%s parses" % name)
        check(not skipped, "%s parses with no unsupported lines" % name)

    # -- markdown primitives
    tpl = T.read(os.path.join(ROOT, "steps", "1-idea", "template.md"))
    check("concept" in T.section_ids(tpl), "step-1 template exposes the {#concept} anchor")
    secs = [s for s in T.sections(tpl) if s["id"]]
    check(len(secs) >= 7, "step-1 template splits into its sections (got %d)" % len(secs))

    # -- framework side
    steps = F.steps(ROOT)
    check(len(steps) == 6, "six steps are read (got %d)" % len(steps))
    check(all(s["gate"] for s in steps), "every step exposes gate items")
    check(all(s["skeleton"] for s in steps), "every step exposes an artifact skeleton")
    statuses = F.statuses(ROOT)
    check(len(statuses) >= 3, "statuses are read (got %d)" % len(statuses))
    check(all(s["per_step"] for s in statuses), "every status exposes per-step parameters")
    check(len(F.load_tools(ROOT)) >= 30, "the library is read")

    # -- instance side, on the committed example
    ex = os.path.join(ROOT, "examples", "decksmith")
    m = I.load(ex, ROOT)
    check(m["product"] and m["active_status"], "example instance identity is read")
    check(m["state_present"] and m["current_step"] == 6, "cycle state is read from state.yaml")
    check(len(m["artifacts"]) == 6, "six artifacts are found by frontmatter (got %d)" % len(m["artifacts"]))
    check(all(a["sections"] for a in m["artifacts"]), "every artifact splits into sections")
    check(len(m["registers"]["hypotheses"]["rows"]) >= 8, "the hypothesis register is read")
    check(len(m["registers"]["risks"]["rows"]) >= 8, "the risk register is read")
    check(len(m["registers"]["metric_tree"]["rows"]) >= 5, "the metric tree is read")

    # gate ticks must key onto the step gate items — the whole gate view depends on this
    ticks = 0
    for s in m["steps"]:
        for g in s["gate"]:
            if g["tick"] in ("done", "n/a", "deferred"):
                ticks += 1
    check(ticks >= 40, "gate ticks in state.yaml resolve onto step gate items (got %d)" % ticks)
    check(not [h for h in m["health"] if h["level"] == "error"],
          "the committed example reads with no canon errors")

    # -- discovery finds the example from the repo root
    found = [c["name"] for c in I.discover(ROOT, ROOT)]
    check("decksmith" in found, "discovery finds the example instance")

    # -- a register split across two tables is ONE register (a real instance grows a second table for
    #    newly instrumented nodes; a first-table-only reader validated the top half and reported the
    #    bottom half's ids as undefined)
    two = ("| id | kind |\n|----|------|\n| M-a | measured |\n\nA paragraph between them.\n\n"
           "| id | kind |\n|----|------|\n| M-b | derived |\n")
    check(T.table_column(two, "id") == ["M-a", "M-b"], "both tables of a register are read")
    _, rows = T.table_rows(two, "id", "kind")
    check(len(rows) == 2, "table_rows spans every matching table (got %d)" % len(rows))

    # -- a blank line inside one table does not truncate it, and is reported
    split = "| id | kind |\n|----|------|\n| M-a | measured |\n\n| M-b | derived |\n"
    t = T.tables(split)
    check(len(t) == 1 and len(t[0]["rows"]) == 2, "a blank line inside a table does not cut it off")
    check(t[0]["broken"], "the accidental split is flagged for the linter (check J)")

    # -- an enum cell is compared by its value, not by the notation it is written in: confidence is
    #    `[sourced: metrics W24]` in a register cell exactly as in prose
    check(T.enum_value("[sourced: metrics W24]") == "sourced", "confidence notation reduces to its value")
    check(T.enum_value("**refuted**") == "refuted", "emphasis around an enum value is not part of it")
    check(T.enum_value("— to clarify —") == "", "a gap is not checked against the enum")
    check("superseded" in F.ENUMS["hypothesis status"][0],
          "a split hypothesis has a status to close as (`superseded`)")

    # -- the trail of one item is assembled from the change logs that name its id — no second store
    hist = m["history"]
    check(hist.get("H-001"), "a hypothesis' trail is assembled from the change logs naming it")
    check(all(e["date"] >= f["date"] for e, f in zip(hist["H-001"], hist["H-001"][1:])),
          "a trail reads newest first")

    # -- an instance OUTSIDE the framework repo is found by marker, not by folder name. This is the
    #    normal vendored layout, and the linter reported "clean" on it for weeks by checking nothing.
    tmp = tempfile.mkdtemp(prefix="loops-selftest-")
    try:
        inst = os.path.join(tmp, "product")
        os.makedirs(os.path.join(inst, "registers"))
        io.open(os.path.join(inst, "config.yaml"), "w", encoding="utf-8").write(
            'product: "Out of tree"\nlanguage: en\nactive_status: pmf\ndirections: [development]\n')
        # a csv written before observed_n/population existed must still read — the reader is
        # header-driven, so the new columns come back empty instead of shifting every field
        io.open(os.path.join(inst, "registers", "metric-tree.md"), "w", encoding="utf-8").write(
            "| id | kind |\n|----|------|\n| M-a | measured |\n")
        io.open(os.path.join(inst, "registers", "metrics.csv"), "w", encoding="utf-8").write(
            "id,period_start,period_end,measured_at,value,basis,source,note\n"
            "M-a,,,2026-08-01,42,fact,admin,\n")
        old = I.load(inst, ROOT)["metrics"]["series"]["M-a"][0]
        check(old["value"] == 42 and old["basis"] == "fact", "a pre-observed_n csv still reads")
        check(old["observed_n"] == "" and old["population"] == "",
              "the columns added later read as empty, not as a shifted row")
        check(I.looks_like_instance(inst), "an out-of-repo folder is recognised by its marker")
        check(inst in [c["path"] for c in I.discover(tmp, ROOT)],
              "discovery finds an instance outside the framework repo")
        check(I.load(inst, ROOT)["product"] == "Out of tree", "it loads and names its product")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d check(s) failed." % len(FAILED) if FAILED else "\nall checks passed.")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
