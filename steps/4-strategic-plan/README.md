---
node_type: step
step: 4
name: strategic-plan
title: "Step 4 — Strategic Plan"
output: strategic-plan.md
cadence: "~3–12 mo; with strategy / on a financial or metric shift"
method_basis: "North Star Framework (metric tree) · cohort retention curve · unit economics incl. LLM inference COGS · simple projection · pre-mortem (risk mitigation)"
status: draft
version: 0.2.0
updated: 2026-07-18
---

# Step 4 — Strategic Plan

**Goal (quantitative instruments).** Make the strategy **measurable, financed, and de-risked**.
This is where the strategy's choices get numbers, a metric tree, and mitigations.

> **Boundary 3 ↔ 4:** choices live in Step 3; this step is instruments and resources.

## Inputs (source slots)
The strategy (`[[strategy]]`), `metrics`, `analytics-search`, `kb`.

## Output
`strategic-plan.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).
The active [status](../../statuses/README.md) sets how far to push the
instruments: `concept-viability` keeps the metric tree and model light (few real numbers yet);
`pmf` builds the economics and North Star from first data; `growth` re-forecasts and optimizes
against a working model.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `architecture-instrumentation` | Refined C4 architecture + instrumentation from Step 3 — where metric data comes from, and what drives infra cost | `architecture-c4`, `product-surface` |
| `metric-tree` | North Star → drivers → input metrics | `metric-tree` |
| `retention` | Cohort retention curve + engagement loop — the real churn/retention input to LTV (where usage history exists) | `retention-analysis` |
| `unit-economics` | CAC / LTV / payback / contribution — incl. LLM inference COGS | `unit-economics` |
| `financial-model` | A simple projection tied to the metric tree | `financial-model` |
| `risk-mitigation` | Each key risk → an owned mitigation (pre-mortem) | `risk-mitigation` |
| `global-hypotheses` | Strategy bets, now quantified & tied to metric nodes | `hypothesis-test-design` |
| `open-questions` | What's still unknown, explicitly | — |

## Register touchpoints
- **Metric tree** — **built here** (`M-…`); the canonical decomposition all lower steps reference.
  `retention-analysis` appends cohort retention/churn readings to `metrics.csv` against their `M-…`.
- **Hypotheses** — `global-hypotheses` quantify existing `H-…` and link them to `M-…`; retention
  drivers to act on seed new `H-…`.
- **Risks** — `risk-mitigation` attaches owners/mitigations to `R-…`.

## Gate checklist (soft) — each item ↔ artifact section
- [ ] architecture & instrumentation refined; metric data sources and infra cost drivers identified → `strategic-plan#architecture-instrumentation`
- [ ] a North-Star metric tree exists with defined nodes (data sources traced to instrumentation) → `strategic-plan#metric-tree` → metric register
- [ ] retention read by cohort where usage history exists (curve shape; churn input to LTV, not an assumed %) → `strategic-plan#retention` → metric register
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

## Change log

### 2026-07-18 — added `retention` section
- **From → To:** skeleton gained `retention` (cohort curve + engagement loop), filled by the new
  `retention-analysis` tool; gate + register touchpoints updated.
- **Why:** `unit-economics` (LTV) and `financial-model` (churn scenarios) both *consumed* a churn
  input that was, until now, an assumption — no tool *measured* the retention curve. The flattening
  cohort curve is also the PMF signal, so it belongs in the quantitative-instruments step.
- **Trigger:** missing-tools pass, 2026-07-18.

### 2026-07-16 — created
- **From → To:** — → Step 4 skeleton (metric tree · unit economics · model · mitigation)
- **Trigger:** Phase 1 / PR #5.
