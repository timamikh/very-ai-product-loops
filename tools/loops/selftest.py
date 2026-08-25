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
    tpl = T.read(os.path.join(ROOT, "steps", "1-concept", "template.md"))
    check("idea" in T.section_ids(tpl), "step-1 template exposes the {#idea} anchor")
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
    check(len(m["registers"]["features"]["rows"]) >= 8, "the feature register is read")
    check(len(m["registers"]["surfaces"]["rows"]) >= 9, "the surface register is read")

    # the product axis (v0.12): a 6#must item names its feature-register row on its `Feature:` line,
    # and the reader lifts the F-… onto the item — the step-6 board and the Surfaces board key on it
    items = m["sprint_items"]
    check(items and all(it["feature"].startswith("F-") for it in items),
          "every 6#must sprint item carries its feature-register F-id (got %d items)" % len(items))

    # a register's columns are addressed by their stable <!--c:key--> keys, not by header prose — the
    # register twin of a section {#anchor}, so the console and linter find the enum column the same way
    # in any language. The example's registers carry keys, so a row is reachable by canonical key.
    hyp = m["registers"]["hypotheses"]
    check("type" in hyp["col_keys"] and "status" in hyp["col_keys"],
          "the example's hypothesis register declares its column keys")
    check(all("type" in r for r in hyp["rows"]),
          "a register row is addressable by its column key, not only its header prose")

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

    # -- a register in a language the code never enumerated is still read by column key: the enum
    #    column is found by its <!--c:key--> mark, not a hardcoded header alias, so a bad value is
    #    caught and a Russian header raises no false "column missing". This is the register half of the
    #    "every cell is a dash" fix — the console reads the same column the linter validates.
    ru_tmp = tempfile.mkdtemp(prefix="loops-selftest-ru-")
    try:
        inst = os.path.join(ru_tmp, "product")
        os.makedirs(os.path.join(inst, "registers"))
        io.open(os.path.join(inst, "config.yaml"), "w", encoding="utf-8").write(
            'product: "На русском"\nlanguage: ru\nactive_status: pmf\ndirections: [development]\n')
        io.open(os.path.join(inst, "registers", "hypotheses.md"), "w", encoding="utf-8").write(
            "| ИД <!--c:id--> | Гипотеза | Тип <!--c:type--> | Статус <!--c:status--> |\n"
            "|----|----------|-----|--------|\n"
            "| H-001 | first | viability | open |\n"
            "| H-002 | second | nonsense | open |\n")
        ru = I.load(inst, ROOT)
        codes = [(hh["code"], hh["message"]) for hh in ru["health"]]
        check(any(c == "enum" and "H-002" in msg for c, msg in codes),
              "a keyed non-English register still catches a bad enum value (found by key, not alias)")
        check(not any(c == "register-column" and ("hypothesis type" in msg or "hypothesis status" in msg)
                      for c, msg in codes),
              "type/status are found by their key despite Russian headers (no false 'column missing')")
        check(ru["registers"]["hypotheses"]["rows"][0].get("type") == "viability",
              "a non-English register row reads by its canonical column key")
    finally:
        shutil.rmtree(ru_tmp, ignore_errors=True)

    # -- the product-axis registers are guarded the same way: a feature `state` outside its enum
    #    (planned/live/retired) is an error keyed on the row's id, and the good row still reads by
    #    its <!--c:state--> column key
    ft_tmp = tempfile.mkdtemp(prefix="loops-selftest-feat-")
    try:
        inst = os.path.join(ft_tmp, "product")
        os.makedirs(os.path.join(inst, "registers"))
        io.open(os.path.join(inst, "config.yaml"), "w", encoding="utf-8").write(
            'product: "Axis"\nlanguage: en\nactive_status: pmf\ndirections: [development]\n')
        io.open(os.path.join(inst, "registers", "features.md"), "w", encoding="utf-8").write(
            "| ID <!--c:id--> | Name <!--c:name--> | State <!--c:state--> |\n"
            "|----|------|-------|\n"
            "| F-001 | first | planned |\n"
            "| F-002 | second | shipped |\n")
        fx = I.load(inst, ROOT)
        check(any(hh["code"] == "enum" and "F-002" in hh["message"] for hh in fx["health"]),
              "a feature state outside its enum is caught (feature state is validated)")
        check(fx["registers"]["features"]["rows"][0].get("state") == "planned",
              "a feature row reads its state by the canonical column key")
    finally:
        shutil.rmtree(ft_tmp, ignore_errors=True)

    # -- the trail of one item is assembled from the change logs that name its id — no second store
    hist = m["history"]
    check(hist.get("H-001"), "a hypothesis' trail is assembled from the change logs naming it")
    check(all(e["date"] >= f["date"] for e, f in zip(hist["H-001"], hist["H-001"][1:])),
          "a trail reads newest first")

    # -- a `<!-- card -->` mark names a section's showcase headline. Both forms name a BLOCK, never a
    #    physical line: above-the-line collects the paragraph below, trailing collects the whole
    #    paragraph or bullet the marked line sits in (real instances hard-wrap prose, and a mark on a
    #    wrapped paragraph's last line was surfacing the mid-sentence tail as the card face).
    above = "<!-- card -->\nA statement wrapped\nacross two lines.\n\n- next\n"
    check(T.card_line(above) == "A statement wrapped across two lines.", "above-line card collects the paragraph")
    oneline = "- A single-line headline. <!-- card -->\n"
    check(T.card_line(oneline) == "A single-line headline.", "trailing card on a one-line bullet drops the marker")
    wrapped = "- A headline that runs on past the <!-- card -->\n  edge of the first line.\n\n- other\n"
    check(T.card_line(wrapped) == "A headline that runs on past the edge of the first line.",
          "trailing card on a wrapped bullet returns the whole bullet, not the cut line")
    wrapped_tail = "- A headline that runs on past the\n  edge of the first line. <!-- card -->\n\n- other\n"
    check(T.card_line(wrapped_tail) == "A headline that runs on past the edge of the first line.",
          "the mark on the wrapped bullet's last line still returns the whole bullet")
    adjacent = ("- Prior item that itself wraps onto\n  a second line.\n"
                "- The marked item runs past the <!-- card -->\n  first line too.\n")
    check(T.card_line(adjacent) == "The marked item runs past the first line too.",
          "a mark on a bullet abutting a wrapped prior bullet returns its own bullet, not the prior one")
    prose = "First sentence. <!-- card -->\nSecond, separate sentence.\n"
    check(T.card_line(prose) == "First sentence. Second, separate sentence.",
          "trailing card on prose collects the whole paragraph, not one physical line")
    tail = "A paragraph that wraps across\nthree physical lines and ends\nwith the mark. [assumption] <!-- card -->\n"
    check(T.card_line(tail) == "A paragraph that wraps across three physical lines and ends with the mark. [assumption]",
          "the mark on a wrapped paragraph's LAST line returns the whole paragraph (the hub-v012 case)")
    check(T.card_line("no mark here at all\n") is None, "no mark yields no card")
    # a hard break (trailing backslash) lays an enumeration one-item-per-line; soft wraps still join
    enum = "<!-- card -->\nFive doors: \\\nagent (A) \\\npipeline (B) \\\nwallet (C)\n"
    check(T.card_line(enum) == "Five doors:\nagent (A)\npipeline (B)\nwallet (C)",
          "a backslash hard break becomes a newline; the last line has none")
    softwrap = "<!-- card -->\nOne sentence that merely wraps\nfor file width, no break.\n"
    check(T.card_line(softwrap) == "One sentence that merely wraps for file width, no break.",
          "a soft wrap (no hard break) still joins with a space")

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
