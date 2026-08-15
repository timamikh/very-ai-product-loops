---
node_type: artifact
artifact: strategic-plan
step: 4
title: "Strategic Plan — Decksmith (fictional sample)"
status: draft
version: 0.1.0
updated: 2026-08-14
---

# Strategic Plan — Decksmith (fictional sample)

> Status: concept-viability · Owner: — · Last review: 2026-08-14
> Inputs: `3-strategy.md` · registers. Feeds: `5-tactical-plan.md`.
> Projection of `4-strategic-plan/` worklogs + registers. No section confirmed (autonomous walk). At
> concept-viability the data-dependent sections (retention, unit-economics, financial-model) are **deferred** —
> no product in market, no cohorts, no actuals.

## Architecture & instrumentation {#architecture-instrumentation}
<!-- tool: architecture-c4, product-surface -->
_Refined C4 architecture + instrumentation — where metric data comes from, and what drives infra cost._

| Surface / component | Instrumentation | Data it produces | Infra cost driver | Confidence |
|---------------------|-----------------|------------------|-------------------|------------|
| Web app (generate/edit/export) | not-instrumented | generate/export/keep events → `M-ns-kept-decks-wk`, `M-activation` | app hosting | [assumption] |
| Native fidelity render/export engine | not-instrumented | `M-edit-fidelity` (editable-object share) | compute (render) | [assumption] |
| LLM provider(s) | not-instrumented | draft content/structure; `M-cogs-per-deck` | **LLM inference (main COGS)** → `R-004` | [assumption] |
| Landing / onboarding | not-instrumented | funnel, time-to-first-export | analytics, email provider | [assumption] |
| Billing | not-instrumented | `M-free-paid-conv` | payments fees | [assumption] |

_The not-instrumented list above **is** the Step-5/6 instrumentation backlog._

## Metric tree {#metric-tree}
<!-- tool: metric-tree -->
_Node **definitions** in `registers/metric-tree.md`, **values** in `registers/metrics.csv` (empty — no product).
This section is the shape + rationale._

**North Star:** `M-ns-kept-decks-wk` — decks generated → exported → **kept & edited** per active deck-maker per
week · [decision: ⚙️ candidate, human approves]
_Why this one: **leading** (moves before revenue) · **value-repeating** (counts repeat value, not one-off
generation) · **strategy-encoding** (a "kept" deck means editable AND designed succeeded — the wedge)._
(3 candidates rejected — weekly-generators, decks-exported, revenue — see worklog.)

| Driver | Node | Inputs (nodes) | Instrumentation |
|--------|------|----------------|-----------------|
| activation | `M-activation` | signup, first export ≤7d | not-instrumented |
| quality (the wedge) | `M-edit-fidelity` | editable-object share on export | not-instrumented |
| retention | `M-wk-retention` | return + re-export next week | not-instrumented |
| conversion | `M-free-paid-conv` | free→paid ≤30d | not-instrumented |

**Guardrails:** `M-edit-fidelity` (quality floor ⚙️ ≥ 90%), `M-cogs-per-deck` (cost cap, ties `R-004`).
**Not instrumented (→ Steps 5–6):** every node — closing them is the instrumentation work.

## Retention {#retention}
_**Deferred at concept-viability** — no product in market, no cohorts. `M-wk-retention` is defined
(not-instrumented); the curve is read once usage history exists (`pmf`). No assumed churn % is invented here._

## Unit economics {#unit-economics}
_**Deferred at concept-viability** — no CAC, no LTV, no actual COGS yet. The structure is known: main COGS =
LLM inference per deck (`M-cogs-per-deck`); price points from `3-strategy.md#pricing` (~$18 Pro) feed the margin
check once real inference cost + CAC exist. Computed at `pmf`._

## Financial model {#financial-model}
_**Deferred at concept-viability** — a projection with no real drivers would be theatre. Built once activation,
conversion, and COGS have first readings. Capacity ceiling to model then: LLM inference throughput/cost._

## Risk mitigation {#risk-mitigation}
<!-- tool: risk-mitigation -->
_Each key risk → an owned mitigation (pre-mortem). Full detail + ranking in `registers/risks.md`._

| `R-…` | Risk | Likelihood | Impact | Mitigation | Owner ⚙️ | Due | Status |
|-------|------|------------|--------|------------|----------|-----|--------|
| R-001 | Gamma dominant + profitable | H | H | don't fight head-on; compete on the fidelity gap | founder | ongoing | accepted |
| R-002 | Incumbents bundle + own distribution | H | H | move fast on the gap; position on "actually editable"; track releases | founder | ongoing | mitigating |
| R-004 | LLM provider dependency (cost/availability) | M | H | multi-model abstraction; cap `M-cogs-per-deck`; engine in-house | eng | Q+1 | mitigating |
| R-006 | PLG virality doesn't fire | M | H | early inner-ring tests with kill thresholds; paid fallback | growth | Q+1 | mitigating |
| R-007 | Quality-at-scale fails → wedge collapses | M | H | prototype fidelity+design eval before scaling (`H-001` gate) | eng | Q+1 | mitigating |

_(R-003, R-005 carried — see register.)_

## Global hypotheses {#global-hypotheses}
<!-- tool: hypothesis-test-design -->
_Strategy bets, quantified & tied to metric nodes (threshold here; test design at Step 5)._

| `H-…` | Bet | Metric node (`M-…`) | Success threshold | Failure threshold | Confidence |
|-------|-----|---------------------|-------------------|-------------------|------------|
| H-001 | engine editable-AND-designed at scale | `M-edit-fidelity` | ≥ 90% | < 70% | [assumption] |
| H-010 | segment prefers native fidelity enough to switch | `M-activation` | ≥ 30% | < 10% | [assumption] |
| H-009 | engine stays ahead → retention | `M-wk-retention` | flattens > 0 | decays to 0 | [assumption] |
| H-012 | packaging converts free→Pro at ~$18 | `M-free-paid-conv` | ≥ 4% | < 1% | [assumption] |

_H-001 (feasibility gate) and H-010 (demand) are the two testable now (no product needed); Step 5 leads with them._

## Open questions {#open-questions}
<!-- open -->
_What's still unknown, explicitly._

- **Feasibility eval** for `H-001` — no prototype fidelity/design measurement yet.
- **Demand signal** for `H-010` — no interviews/probe run.
- **WTP evidence** for `H-008`/`H-012` — price points are `[assumption]`.
- **CAC** for `H-011` — needs the (deferred) unit-economics.

**Checked, not confirmed.**

| What we checked | What the data said | Why it is not a verdict | Moved |
|-----------------|--------------------|-------------------------|-------|
| — nothing read yet — | pre-data (concept-viability, no product in market) | no test has run | — |

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → architecture instrumented (on paper), metric register born (North Star + drivers, all
  not-instrumented), risk mitigations owned (`R-001…R-007`), bets quantified (`H-001/H-009/H-010/H-012`);
  retention/unit-economics/financial-model deferred.
- **Why:** make the strategy measurable and de-risked as far as pre-data honesty allows.
- **Trigger:** Step-4 strategic plan, rebuild.
