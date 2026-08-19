---
node_type: goal-map
title: Goal map — from trigger to card
status: draft
version: 0.1.0
updated: 2026-08-19
---

# Goal map — from trigger to card

What move 1 of the [operating loop](OPERATING-LOOP.md) reads. A **trigger** is an event now or a debt
recorded when it was found (move 0) — the loop never scans for work. Rules: **one row per trigger**
(nuance lives in the card); **an event matching two rows is two passes**; a trigger routes only to a
**pass** — the *moves* below are invoked from inside skeleton moves 2–5, never run bare.

## Passes — a trigger names one

| Trigger (an event now, or a recorded debt) | Card | Move-5 surfaces it must touch |
|---|---|---|
| The current step's gate has open items | the step `README` + the section's method `SKILL.md` (status refines) | ticks · registers on touchpoints · sign-off |
| A file/URL arrives; setup finds legacy material; a source changed under its worklogs | [`source-intake`](../tool-skills/operations/source-intake/SKILL.md) | `sources/INDEX.md` · worklog change logs |
| A gate/hypothesis/decision waits on a number; a reading is stale when leaned on | [`metrics-capture`](../tool-skills/operations/metrics-capture/SKILL.md) | `metrics.csv` · derivation worklog · `metric-tree.md` |
| An instance procedure's cadence is due; the human asks for a pull/push | `<instance>/skills/<slug>/SKILL.md` | the snapshot landed · `state.yaml` `last_run` |
| A document must leave the framework | [`tool-skills/outputs/`](../tool-skills/outputs/README.md) | the file in `export-files/` |
| Session end, agent change, imminent compaction | [`handoff`](../tool-skills/operations/handoff/SKILL.md) | `HANDOFF.md` |
| The human asks what is signed and what rests on what | [`theses`](../tool-skills/operations/theses/SKILL.md) (`scope: instance`) | confirmation markers |

Whichever card, the pass runs the whole skeleton and ends at move 5 with a change-log entry and open
items — unconditionally.

**Moves — invoked from inside a pass, never routed to as a trigger:** *ask the human* (move 3 —
`CONVENTIONS.md` → *Forks*; the card's `questions.yaml`) · *delegate* `gather`/`research`/`draft`/`verify`
(moves 2·4 — [`orchestration`](../tool-skills/operations/orchestration/SKILL.md)) · *project* a
worklog into its section (move 4 — [`projection`](../tool-skills/operations/projection/SKILL.md)) ·
*propose sign-off* (move 5 — [`theses`](../tool-skills/operations/theses/SKILL.md)) · *verify*
(moves 4·5 — recount, return gate, `python3 tools/lint.py <instance>`).

**Outside the loop** (no pass, no card): `start-work` / `product-setup` (session start) ·
[`EXTENDING.md`](../EXTENDING.md) (changing the framework itself) · the environment — the read-only
console, git, the chat rules (N9).
