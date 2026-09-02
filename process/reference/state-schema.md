---
node_type: reference
title: Instance state (state.yaml) — the pinned shape
status: draft
version: 0.1.0
updated: 2026-09-02
---

# Instance state (`state.yaml`) — the pinned shape

*Read this when writing or reconstructing an instance's **`state.yaml`** (loop move 0 reads it, move 5
writes it). The one-line pointer stays in* [`CONVENTIONS.md`](../CONVENTIONS.md) → *Instance config
and state*; *the console and the linter read the file by this shape.*

`state.yaml` is the **agent-written position** of the cycle — the single home of *where we are*,
never of rules or truth. Human decisions live in `config.yaml` ([`config-schema.md`](config-schema.md)).
It is rewritten at move 5 of every pass; a missing file is reconstructed from the artifacts and
confirmed with the human (OPERATING-LOOP move 0).

```yaml
current_step: 3                 # the step the loop is in, 1–6
last_pass: 2026-08-16           # date of the last recorded pass

last_run:                       # one line per instance exchange skill (skills/<slug>/), if any
  pull-analytics-weekly: 2026-08-18

gates:                          # gate ticks, grouped by step folder
  1-concept:
    "concept#idea": done
    "concept#cjm": n/a          # a comment may carry the reason
  3-strategy:
    "strategy#bets": open
```

| Key | Shape | What it is |
|-----|-------|------------|
| `current_step` | integer 1–6 | the step whose gate the commonest row works |
| `last_pass` | `YYYY-MM-DD` | when the last pass recorded (move 5) |
| `last_run` | map `<exchange-slug>: YYYY-MM-DD` | last run of each instance exchange skill; `start-work` compares it against the skill's `cadence:` to surface an overdue pull/push ([`boundary-layout.md`](boundary-layout.md)) |
| `gates` | map `<step-folder>: { <tick-id>: <tick> }` | the gate ticks. The step key is the step folder (`1-concept`) — a bare number (`1`) is read too. A **tick id** is the gate item's `artifact#section` target, or the explicit `tick-id` the step README gives an item that spans sections. A **tick** is one of `done` · `open` · `n/a` · `deferred` (the machine home is `framework.TICK_VALUES`); an item absent from the map reads as `open` |

Rules:

- **Ticks are conditional writes.** A tick on a section resting mainly on the agent's own reasoning
  waits for a `verify` that did not write it (OPERATING-LOOP move 5); `n/a` carries its reason as a
  comment, `deferred` names when in the change log of the artifact.
- **An `open` tick on a written section has one legal meaning besides "Record not finished":** the section
  was **reopened for re-sign** — its content changed and the owner's sign-off is awaited. A reopen is
  recorded, never implied: the artifact's change-log entry names the section (`#<id>`) and is dated on
  or after `last_pass`; without that entry the linter reads the tick as an unfinished Record (check G2).
- **Nothing else is load-bearing.** Extra keys are tolerated by the reader and reported by the
  linter, so a private key cannot quietly become schema.
- **The console reads the same file.** A step's gate view is `gates` merged onto the step README's
  checklist; a tick the README does not name is shown as drift, never dropped.
