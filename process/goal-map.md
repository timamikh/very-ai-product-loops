---
node_type: goal-map
title: Goal map — from trigger and goal to a card
status: draft
version: 0.3.0
updated: 2026-08-19
---

# Goal map — from trigger and goal to a card

What move 1 of the [operating loop](OPERATING-LOOP.md) reads. A **trigger** is an event now or a debt
recorded when it was found (move 0) — the loop never scans for work. A row is **(trigger, goal) → a
card**; the card's frontmatter is the pass plan ([`reference/card-schema.md`](reference/card-schema.md)).
Rules: **one row per trigger**; **an event matching two rows is two passes**; a trigger routes only to
a **pass** — the *moves* below are invoked from inside skeleton moves 2–5, never run bare.

## Passes — a trigger and a goal name one card

| Trigger (an event now, or a recorded debt) | Goal — what this pass is for | Card | Move-5 surfaces it must touch |
|---|---|---|---|
| The current step's gate has open items | close one named section (`concept#idea`) | the step `README` + that section's method (below) | ticks · registers on touchpoints · sign-off |
| A file/URL arrives; setup finds legacy material; a source changed under its worklogs | get outside material into the worklogs that need it | [`source-intake`](../tool-skills/operations/source-intake/SKILL.md) | `sources/INDEX.md` · worklog change logs |
| A gate/hypothesis/decision waits on a number; a reading is stale when leaned on | land one trustworthy value in the metric register | [`metrics-capture`](../tool-skills/operations/metrics-capture/SKILL.md) | `metrics.csv` · derivation worklog · `metric-tree.md` |
| An instance procedure's cadence is due; the human asks for a pull/push | move data across the boundary, in one direction | `<instance>/skills/<slug>/SKILL.md` | the snapshot landed · `state.yaml` `last_run` |
| A document must leave the framework | put one file in the human's hands | [`tool-skills/outputs/`](../tool-skills/outputs/README.md) | the file in `export-files/` |
| Session end, agent change, imminent compaction | carry state the files don't hold to the next agent | [`handoff`](../tool-skills/operations/handoff/SKILL.md) | `HANDOFF.md` |
| The human asks what is signed and what rests on what | give a verdict on the instance's confirmation state | [`theses`](../tool-skills/operations/theses/SKILL.md) (`scope: instance`) | confirmation markers |

**The goal is what makes a row a plan** — one trigger with two goals is two passes, and the goal is
what move 1 says aloud. Whichever card, the pass runs the whole skeleton and ends at move 5 with a
change-log entry and open items — unconditionally.

## The header is the plan — types, not instances

The router hands over a card; everything after comes from its frontmatter: `prerequisites` → move 3 ·
`reads` → the read perimeter of move 2 · `writes` → the write perimeter of move 4 · `surfaces` →
move 5. The header declares **types and slots**; the pass resolves the **instances** from the trigger
and the data — a `section:*` is a slot, an `H-` id is never in a header.

**The law of ranks.** A `method` is bound to its step and is **never** a routing target — it is
reached from inside a pass, through its section's marker. An `operation`, `output` or `exchange` is
reached **only** through this file.

## The commonest row, resolved to the end

*The current step's gate has open items* is the row an agent walks most days, so it is spelled out
rather than left to judgement. Its goal is always **one named section** — "close `concept#idea`" —
and that resolves the plan to a **pair, not a choice**: the **step card** gives the gate, the
artifact, the input map and the `surfaces` owed; the **method** from that section's
`<!-- tool: X -->` marker (several named → the first —
[`reference/worklog-resolution.md`](reference/worklog-resolution.md)) gives the `prerequisites`, the
read types and the `writes` — its worklog and its section. Both halves feed move 2, whose perimeter
is a **union** — narrowing it to the method's `reads` alone is the failure this row, the one that
runs most often, is spelled out to prevent.

Not every gate item is such a section. An item that is another pass's `surfaces` (`#to-clarify`,
`#hypotheses`) or an optional section closes at **move 5** of the passes that feed it, or at step
finalization — it has no router row and no pass of its own. One pass per *section*, not per gate item.

**Moves — invoked from inside a pass, never routed to as a trigger:** *ask the human* (move 3 —
`CONVENTIONS.md` → *Forks*; the card's `questions.yaml`) · *delegate* `gather`/`research`/`draft`/`verify`
(moves 2·4 — [`orchestration`](../tool-skills/operations/orchestration/SKILL.md)) · *project* a
worklog into its section (move 4 — [`projection`](../tool-skills/operations/projection/SKILL.md)) ·
*propose sign-off* (move 5 — [`theses`](../tool-skills/operations/theses/SKILL.md)) · *verify*
(moves 4·5 — recount, return gate, `python3 tools/lint.py <instance>`).

**Outside the loop** (no pass, no card, and they never become cards): `start-work` / `product-setup`
(session start) · [`EXTENDING.md`](../EXTENDING.md) (changing the framework itself) · the environment —
the read-only console, git, the chat rules (N9).
