---
node_type: step
step: 4
name: strategic-plan
title: "Step 4 — Strategic Plan"
output: strategic-plan.md
cadence: "~3–12 mo; with strategy / on a financial or metric shift"
method_basis: "North Star Framework (metric tree) · unit economics incl. LLM inference COGS · simple projection · pre-mortem (risk mitigation)"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Step 4 — Strategic Plan

**Goal (quantitative instruments).** Make the strategy **measurable, financed, and de-risked**.
This is where the strategy's choices get numbers, a metric tree, and mitigations.

> **Boundary 3 ↔ 4:** choices live in Step 3; this step is instruments and resources.

## Inputs (source slots)
The strategy (`[[strategy]]`), `metrics`, `analytics-search`, `kb`.

## Output
`strategic-plan.md`.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `metric-tree` | North Star → drivers → input metrics | `metric-tree` |
| `unit-economics` | CAC / LTV / payback / contribution — incl. LLM inference COGS | `unit-economics` |
| `financial-model` | A simple projection tied to the metric tree | `financial-model` |
| `risk-mitigation` | Each key risk → an owned mitigation (pre-mortem) | `risk-mitigation` |
| `global-hypotheses` | Strategy bets, now quantified & tied to metric nodes | `hypothesis-test-design` |
| `open-questions` | What's still unknown, explicitly | — |

## Register touchpoints
- **Metric tree** — **built here** (`M-…`); the canonical decomposition all lower steps reference.
- **Hypotheses** — `global-hypotheses` quantify existing `H-…` and link them to `M-…`.
- **Risks** — `risk-mitigation` attaches owners/mitigations to `R-…`.

## Gate checklist (soft) — each item ↔ artifact section
- [ ] a North-Star metric tree exists with defined nodes → `strategic-plan#metric-tree` → metric register
- [ ] unit economics computed, LLM inference as an explicit COGS line → `strategic-plan#unit-economics`
- [ ] a projection ties to the metric tree → `strategic-plan#financial-model`
- [ ] each key risk has an owned mitigation → `strategic-plan#risk-mitigation` → risk register
- [ ] bets are quantified and linked to metric nodes → `strategic-plan#global-hypotheses`
- [ ] open questions are listed, not hidden → `strategic-plan#open-questions`

## Cadence & invalidation
- **Cadence:** with strategy, or on a financial/metric shift.
- **Invalidates downward:** a changed metric tree or economics flags the Tactical Plan (5).
- **From below:** actuals diverging from the model trigger a revisit here.

## The human's role
Approve targets, economics assumptions, and mitigations; the agent builds the tree, the model, and the math.
