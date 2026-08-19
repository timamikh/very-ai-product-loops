---
node_type: card
kind: step
name: strategic-plan
step: 4
title: "Step 4 — Strategic Plan"
output: 4-strategic-plan.md
prerequisites: [the strategy artifact `3-strategy.md` exists]
reads: [file:3-strategy.md, source:metrics, source:research, source:kb]
writes: [section:*]
surfaces: [ticks, register:hypotheses, register:risks, register:metric-tree, sign-off, change-log]
cadence: "~3–12 mo; with strategy / on a financial or metric shift"
method_basis: "Instrumentation mapping · North Star Framework (metric tree) · cohort retention curve · unit economics incl. LLM inference COGS · simple projection · horizon targets off the projection · pricing margin revisit · capabilities & management systems (PTW choices 4–5) · risk mitigation (owner · trigger · due) · hypothesis thresholds"
status: draft
version: 0.5.1
updated: 2026-08-19
---
# Step 4 — Strategic Plan

**Goal (quantitative instruments).** Make the strategy **measurable, financed, and de-risked**.
This is where the strategy's choices get numbers, a metric tree, and mitigations.

> **Boundary 3 ↔ 4:** choices live in Step 3; this step is instruments and resources.

## Inputs (source slots)
The strategy (`3-strategy.md`), `metrics`, `research`, `kb`.

## Output
`4-strategic-plan.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).
The active [status](../../statuses/README.md) sets how far to push the
instruments: `concept-viability` keeps the metric tree and model light (few real numbers yet);
`pmf` builds the economics and North Star from first data; `growth` re-forecasts and optimizes
against a working model.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `architecture-instrumentation` | Refined C4 architecture + instrumentation from Step 3 — where metric data comes from, and what drives infra cost | `instrumentation-plan` |
| `metric-tree` | North Star → drivers → input metrics | `metric-tree` |
| `retention` | Cohort retention curve + engagement loop — the real churn/retention input to LTV (where usage history exists) | `retention-analysis` |
| `unit-economics` | CAC / LTV / payback / contribution — incl. LLM inference COGS | `unit-economics` |
| `financial-model` | A simple projection tied to the metric tree | `financial-model` |
| `strategic-targets` | Horizon commitments: 3–5 nodes × value at the horizon date, read off the projection; the top of the target ladder Step-5 `goal-targets` climbs | `strategic-targets` |
| `capabilities` | Must-have capabilities behind the winning logic + the management system per capability (PTW choices 4–5); gaps seed `R-…` | `capabilities-systems` |
| `risk-mitigation` | Each key risk → an owned mitigation (pre-mortem) | `risk-mitigation` |
| `global-hypotheses` | Strategy bets, now quantified & tied to metric nodes (thresholds set here; test design at Step 5 via `hypothesis-test-design`) | `hypothesis-thresholds` |
| `open-questions` | What's still unknown, explicitly | — |

**Contributing method (no section of its own):** `pricing-strategic-plan` — once `unit-economics`
exists, re-reads the Step-3 pricing decision against contribution margin, inference COGS per tier,
and free-tier burn; the verdict is "holds" (logged) or a ⚙️ proposed change to `3-strategy.md#pricing`
(triggering that section's re-confirmation). It is reached as the **second tool** of the `{#pricing}`
marker, works in its own worklog (`3-strategy/pricing-strategic-plan.md`), and re-reads the step-4
economics workings as **declared worklog inputs** (its card's `reads`).

## Register touchpoints
- **Metric tree** — **built here** (`M-…`); the canonical decomposition all lower steps reference.
  `retention-analysis` appends cohort retention/churn readings to `metrics.csv` against their `M-…`.
- **Hypotheses** — `global-hypotheses` quantify existing `H-…` and link them to `M-…`; retention
  drivers to act on seed new `H-…`.
- **Risks** — `risk-mitigation` attaches mitigation · owner · trigger · due to the carried `R-…`
  (surfaced upstream by `pre-mortem` at Step 3 / `niche-risks` at Step 2); capability gaps seed
  new execution `R-…` here via `capabilities-systems`.

## Gate checklist (soft) — each item ↔ artifact section
- [ ] architecture & instrumentation refined; metric data sources and infra cost drivers identified → `strategic-plan#architecture-instrumentation`
- [ ] a North-Star metric tree exists with defined nodes (data sources traced to instrumentation) → `strategic-plan#metric-tree` → metric register
- [ ] retention read by cohort where usage history exists (curve shape; churn input to LTV, not an assumed %) → `strategic-plan#retention` → metric register
- [ ] unit economics computed, LLM inference as an explicit COGS line → `strategic-plan#unit-economics`
- [ ] a projection ties to the metric tree → `strategic-plan#financial-model`
- [ ] horizon targets committed on 3–5 nodes, each read off a named scenario, decision-attributed → `strategic-plan#strategic-targets`
- [ ] every winning-logic element has a capability behind it; each gap has a close and an `R-…` → `strategic-plan#capabilities` → risk register
- [ ] each key risk has an owned mitigation → `strategic-plan#risk-mitigation` → risk register
- [ ] bets are quantified and linked to metric nodes → `strategic-plan#global-hypotheses`
- [ ] open questions are listed, not hidden → `strategic-plan#open-questions`

## Cadence & invalidation
- **Cadence:** with strategy, or on a financial/metric shift.
- **Invalidates downward:** a changed metric tree or economics flags the Tactical Plan (5).
- **From below:** actuals diverging from the model trigger a revisit here.

## The human's role
Approve targets, economics assumptions, and mitigations; the agent builds the tree, the model, and the math.
