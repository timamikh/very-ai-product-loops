---
node_type: worklog
tool: impact-readout
artifact: tactical-plan
updated: 2026-08-23
---

# impact-readout — worklog (Period 1)

## Inputs

- `6-sprint-plan.md#must` — the pre-registered expectations: four must items, each with an
  `Expected impact` + check-by (items 1–2 dev · 1 g2m · 1 back-office) and an S/M/L estimate.
- `registers/features.md` — all rows `planned` (pre-build product, Sprint 1 not yet shipped).
- `registers/metrics.csv` — no readings yet (the analytics panel ships with the prototype).

## Reasoning

Nothing to read: Sprint 1 is the **first** sprint of the first period — no item has shipped, no
check-by has arrived. The honest output is an explicitly empty readout (stated, not skipped), the
exact twin of `{#readouts}`'s "no test finished" row. Reading item impact before anything ships
would be the peeking this method's pre-registration exists to prevent.

What the next gate will read (queued, not judged):

| Item | Feature | Expected (verbatim from 6#must) | Check-by |
|------|---------|--------------------------------|----------|
| S1 · dev 1 | F-001 | `H-001` measurable — `M-design-acceptance` readable on the ~10-brief smoke set | Sprint-2 gate |
| S1 · dev 2 | F-002 | closes `R-012` — `M-design-acceptance` computable | Sprint-2 gate |
| S1 · g2m 1 | F-003 | tests `H-011` — `M-activated` 0 → ≥6 activated (≥8 recruited) | end of period |
| S1 · b/o 1 | F-004 | `M-activated` capture enabled — events fire, a recruit countable | Sprint-2 gate |

## Written back

- Register: **no flips** — no item shipped, every `F-…` row stays `planned`. No verdicts, no
  estimate actuals (calibration starts with the first shipped item).
- Artifact: `5-tactical-plan.md#item-readouts` — one explicit empty row.

## Open

- The Sprint-2 gate is undated (the horizon-date gap, `4#open-questions`) — the check-bys are
  length-bounded, and the founder's calendar decision dates them.
