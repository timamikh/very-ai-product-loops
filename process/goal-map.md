---
node_type: goal-map
title: Goal map — from trigger and goal to a card
status: draft
version: 0.5.0
updated: 2026-09-02
---

# Goal map — from trigger and goal to a card

What move 1 of the [operating loop](OPERATING-LOOP.md) reads. A **trigger** is an event now or a debt
recorded when it was found (move 0) — the loop never scans for work. A row is **(trigger, goal) → a
card**. Rules: **one row per trigger**; **an event matching two rows is two passes**; a trigger
routes only to a **pass** — the *moves* below are invoked from inside moves 2–5, never run bare.

## Passes — a trigger and a goal name one card

| Trigger (an event now, or a recorded debt) | Goal — what this pass is for | Card |
|---|---|---|
| The current step's gate has open items | close one named section (`concept#idea`) | the step `README` + that section's method (below) |
| The step's own sections are all worked | read the step whole and land what only the whole shows | [`step-close`](../tool-skills/operations/step-close/SKILL.md) |
| A file/URL arrives; setup finds legacy material; a source changed under its worklogs | get outside material into the worklogs that need it | [`source-intake`](../tool-skills/operations/source-intake/SKILL.md) |
| A gate/hypothesis/decision waits on a number; a reading is stale when leaned on | land one trustworthy value in the metric register | [`metrics-capture`](../tool-skills/operations/metrics-capture/SKILL.md) |
| An instance procedure's cadence is due; the human asks for a pull/push | move data across the boundary, in one direction | `<instance>/skills/<slug>/SKILL.md` |
| A document must leave the framework | put one file in the human's hands | [`tool-skills/outputs/`](../tool-skills/outputs/README.md) |
| Session end, agent change, imminent compaction | carry state the files don't hold to the next agent | [`handoff`](../tool-skills/operations/handoff/SKILL.md) |
| The human asks what is signed and what rests on what | give a verdict on the instance's confirmation state | [`theses`](../tool-skills/operations/theses/SKILL.md) (`scope: instance`) |

**The goal is what makes a row a plan** — one trigger with two goals is two passes, and the goal is
what move 1 says aloud. Whichever card, the pass runs the whole skeleton and ends at move 5 with a
change-log entry and open items — unconditionally; **what else move 5 owes is the card's own
`surfaces:`** (a fact about a card lives in the card, so this table carries no surfaces column).

## The header is the plan — and the law of ranks

The router hands over a card; everything after comes from its frontmatter (`prerequisites` → move 3 ·
`reads` → move 2 · `writes` → move 4 · `surfaces` → move 5 — types and slots, instances from the
data; [`reference/card-schema.md`](reference/card-schema.md)). **The law of ranks:** a `method` is
bound to its step and is **never** a routing target — it is reached from inside a pass, through its
section's marker. An `operation`, `output` or `exchange` is reached **only** through this file.

## The commonest row, resolved to the end

*The current step's gate has open items* is the row an agent walks most days. Its goal is always
**one named section** — "close `concept#idea`" — and the plan is a **pair, not a choice**: the
**step card** gives the gate, the artifact, the input map and the `surfaces` owed; the **method**
from that section's `<!-- tool: X -->` marker (several named → the first —
[`reference/worklog-resolution.md`](reference/worklog-resolution.md)) gives the `prerequisites`, the
read types and the `writes`. Both halves feed move 2, whose perimeter is their **union**.

Not every gate item is such a section: an item that is another pass's `surfaces` (`#to-clarify`,
`#hypotheses`) or an optional section closes at **move 5** of the passes that feed it, or at
[`step-close`](../tool-skills/operations/step-close/SKILL.md). **No gate item has a router row of
its own** — one pass per *section*, not per gate item.

**Moves — invoked from inside a pass, never routed to:** *ask the human* (move 3; the card's
`questions.yaml`) · *delegate* (moves 2·4 —
[`orchestration`](../tool-skills/operations/orchestration/SKILL.md)) · *project* (move 4 —
[`projection`](../tool-skills/operations/projection/SKILL.md)) · *propose sign-off* (move 5 —
[`theses`](../tool-skills/operations/theses/SKILL.md)) · *verify* (moves 4·5 — recount, return gate,
`python3 tools/lint.py <instance>`).

**Outside the loop** (no pass, no card): `start-work` / `product-setup`
(session start) · [`EXTENDING.md`](../EXTENDING.md) (changing the framework itself) · the environment —
the read-only console, git, the chat rules (N9).
