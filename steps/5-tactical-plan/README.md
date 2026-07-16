---
node_type: step
step: 5
name: tactical-plan
title: "Step 5 — Tactical Plan"
output: tactical-plan.md
cadence: "~1–3 mo; stage-gate ~monthly"
method_basis: "OKR-style measurable goals per direction · experiment design · prioritization (RICE/ICE) by contribution to the gate"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Step 5 — Tactical Plan

**Goal.** Set **measurable goals for the period, per work direction**, decide **which
hypotheses to test**, and surface **blockers**. This is the stage-gate that turns strategy into
a period of focused work.

Work **directions** are an instance config (default `development · growth · back-office`); the
number can change with the product. The active [status](../../statuses/README.md) sets which
goals take priority (e.g. `concept-viability` → building a prototype, not growth metrics).

## Inputs (source slots)
The strategic plan (`[[strategic-plan]]`), the metric register, the hypothesis register,
`metrics`, backlog export.

## Output
`tactical-plan.md`.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `period-goals` | Measurable goals **grouped by direction** | `prioritization` |
| `selected-metric-nodes` | Which `M-…` nodes this period moves | `metric-tree` |
| `hypotheses-to-test` | Which `H-…` we test now + the test design | `hypothesis-test-design` |
| `blockers` | Dependencies/blockers with an owner | — |

## Register touchpoints
- **Metric tree** — selects the nodes to move (no new tree; references `M-…`).
- **Hypotheses** — picks `H-…` to test and attaches a test design.
- **Risks** — period `blockers` link back to `R-…` where relevant.

## Gate checklist (soft) — each item ↔ artifact section
- [ ] each direction has measurable goals for the period → `tactical-plan#period-goals`
- [ ] goals map to specific metric nodes → `tactical-plan#selected-metric-nodes` → metric register
- [ ] hypotheses to test have a test design → `tactical-plan#hypotheses-to-test` → hypothesis register
- [ ] blockers listed with an owner → `tactical-plan#blockers`

## Cadence & invalidation
- **Cadence:** ~monthly stage-gate.
- **Invalidates downward:** the period goals define the Sprint Plan (6).
- **From below:** a sprint result (hit/miss, refuted hypothesis) triggers a re-plan here.

## The human's role
Set the period's priorities and accept the goals; the agent proposes goals from the metric tree and ranks the work.
