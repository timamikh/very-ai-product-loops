---
node_type: artifact-template
artifact: strategic-plan
step: 4
title: "Strategic Plan — <Product>"
status: template
version: 0.2.1
updated: 2026-07-21
---

<!--
  strategic-plan.md assembly shell. Each section is filled by its recommended library tool
  (see steps/4-strategic-plan/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md.
  This step is INSTRUMENTS & RESOURCES (quantitative). Metric NODE DEFINITIONS live in
  registers/metric-tree.md and VALUES in registers/metrics.csv — this artifact references them,
  never duplicates the values (one mechanism, one way).
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Strategic Plan — <Product>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Last review: <date>
> Inputs: [[strategy]] · registers. Feeds: [[tactical-plan]].

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see `CLAUDE.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Architecture & instrumentation {#architecture-instrumentation}
<!-- tool: architecture-c4, product-surface -->
_Refined C4 architecture + instrumentation from Step 3 — where metric data comes from, and what drives infra cost._

| Surface / component | Instrumentation (instrumented / proxy / not) | Data it produces | Infra cost driver | Confidence |
|---------------------|----------------------------------------------|------------------|-------------------|------------|
| … | … | … | … | [assumption] |

## Metric tree {#metric-tree}
<!-- tool: metric-tree -->
_North Star → drivers → input metrics. Node **definitions** live in `registers/metric-tree.md`,
**values** in `registers/metrics.csv` — this section is the shape + rationale, not a value store._

**North Star:** `M-…` — <definition/formula> · [decision: ⚙️ / approved <who, when>]
_Why this one: leading · value-repeating · strategy-encoding (one line each)._

| Driver | Node | Inputs (nodes) | Instrumentation |
|--------|------|----------------|-----------------|
| acquisition / activation | `M-…` | `M-…` | instrumented / proxy / not |
| conversion | … | … | … |
| retention | `M-…` | … | … |

**Not instrumented (→ Steps 5–6):** nodes + how to close them.

## Retention {#retention}
<!-- tool: retention-analysis -->
_Cohort retention curve + engagement loop. The real churn input to LTV (where usage history exists).
Readings land in `registers/metrics.csv` against their `M-…`._

| Cohort (join period) | P1 | P3 | P6 | P12 | Flattens at | Shape read | Confidence |
|----------------------|----|----|----|-----|-------------|------------|------------|
| … | …% | …% | …% | …% | …% floor / decays to 0 | flattening / decaying | [sourced: metrics …] |

- Engagement loop (retained core): trigger → action → reward → investment. …
- Drop-off point / resurrection path: …

## Unit economics {#unit-economics}
<!-- tool: unit-economics -->
_Contribution margin; LLM inference as an explicit COGS line. Two bases: operational / honest._

| Metric | Operational | Honest (+depreciation / market compute) | Assumptions |
|--------|-------------|------------------------------------------|-------------|
| Revenue per payer ($/mo) | … | … | … |
| COGS per payer ($/mo) | … | … | [assumption: allocation rule] |
| Contribution ($/mo · %) | … | … | … |
| CAC (by channel) | … | … | [sourced / ⚙️] |
| Payback | … | … | … |
| LTV | — churn scenarios X/Y/Z% ⚙️ — | … | uses the `#retention` curve |

## Financial model {#financial-model}
<!-- tool: financial-model -->
_A simple projection tied to the metric-tree drivers; churn as a scenario axis; capacity caps as a first-class ceiling._

| Driver | Base | Assumption | Confidence |
|--------|------|------------|------------|
| … | … | … | [assumption] |

- Capacity ceiling: … (what caps growth, and when it binds)
- Scenarios: base / optimistic / conservative — key deltas …

## Risk mitigation {#risk-mitigation}
<!-- tool: risk-mitigation -->
_Each key risk → an owned mitigation (pre-mortem)._

| `R-…` | Risk | Likelihood | Impact | Mitigation | Owner | Due | Status |
|-------|------|------------|--------|------------|-------|-----|--------|
| R-… | … | H/M/L | H/M/L | … | … | … | open / mitigating |

## Global hypotheses {#global-hypotheses}
<!-- tool: hypothesis-test-design -->
_Strategy bets, now quantified & tied to metric nodes (threshold set here; test design at Step 5)._

| `H-…` | Bet | Metric node (`M-…`) | Success threshold | Failure threshold | Confidence |
|-------|-----|---------------------|-------------------|-------------------|------------|
| H-… | … | M-… | ≥ … | < … | [assumption] |

## Open questions {#open-questions}
_What's still unknown, explicitly — not hidden._

- …

## Change log

### <date> — created
- **From → To:** — → initial strategic-plan draft
- **Why:** …
- **Trigger:** …
