#!/usr/bin/env python3
"""Smoke test for the shared read layer — runs in CI next to the linter.

The linter checks the *canon*; this checks that the layer which reads the canon still works. It reads
the committed example instance end to end and asserts the invariants everything downstream (the
console today, writers and the agent bridge later) depends on. Stdlib only, no test framework.

Run:  python3 tools/loops/selftest.py
"""
import os
import sys

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

    print("\n%d check(s) failed." % len(FAILED) if FAILED else "\nall checks passed.")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
