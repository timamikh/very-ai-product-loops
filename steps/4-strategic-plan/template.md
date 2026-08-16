---
node_type: artifact-template
artifact: strategic-plan
step: 4
title: "Strategic Plan — <Product>"
status: template
version: 0.3.2
updated: 2026-08-16
---

<!--
  4-strategic-plan.md assembly shell. Each section is filled by its recommended library tool
  (see steps/4-strategic-plan/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md.
  This step is INSTRUMENTS & RESOURCES (quantitative). Metric NODE DEFINITIONS live in
  registers/metric-tree.md and VALUES in registers/metrics.csv — this artifact references them,
  never duplicates the values (one mechanism, one way).
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Strategic Plan — <Product>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Last review: <date>
> Inputs: `3-strategy.md` · registers. Feeds: `5-tactical-plan.md`.

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see the repo's agent rules `AGENTS.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Architecture & instrumentation {#architecture-instrumentation}
<!-- tool: instrumentation-plan -->
_Refined C4 architecture + instrumentation from Step 3 — where metric data comes from, and what drives infra cost._

| Surface / component <!--c:surface--> | Instrumentation (instrumented / proxy / not) <!--c:instrumentation--> | Data it produces <!--c:data--> | Infra cost driver <!--c:cost--> | Confidence <!--c:conf--> |
|---------------------|----------------------------------------------|------------------|-------------------|------------|
| … | … | … | … | [assumption] |

## Metric tree {#metric-tree}
<!-- tool: metric-tree -->
_North Star → drivers → input metrics. Node **definitions** live in `registers/metric-tree.md`,
**values** in `registers/metrics.csv` — this section is the shape + rationale, not a value store._

**North Star:** `M-…` — <definition/formula> · [decision: ⚙️ / approved <who, when>]
_Why this one: leading · value-repeating · strategy-encoding (one line each)._

| Driver <!--c:driver--> | Node <!--c:node--> | Inputs (nodes) <!--c:inputs--> | Instrumentation <!--c:instrumentation--> |
|--------|------|----------------|-----------------|
| acquisition / activation | `M-…` | `M-…` | instrumented / proxy / not |
| conversion | … | … | … |
| retention | `M-…` | … | … |

**Not instrumented (→ Steps 5–6):** nodes + how to close them.

## Retention {#retention}
<!-- tool: retention-analysis -->
_Cohort retention curve + engagement loop. The real churn input to LTV (where usage history exists).
Readings land in `registers/metrics.csv` against their `M-…`. Each cell is read over the **observed**
(`n`) — members whose window has not elapsed are censored, not counted as churned; `—` = not
observable yet._

| Cohort (join period) <!--c:cohort--> | P1 <!--c:p1--> | P3 <!--c:p3--> | P6 <!--c:p6--> | P12 <!--c:p12--> | Flattens at <!--c:flattens--> | Shape read <!--c:shape--> | Confidence <!--c:conf--> |
|----------------------|----|----|----|-----|-------------|------------|------------|
| … | …% (n=…) | …% (n=…) | — | — | …% floor / decays to 0 | flattening / decaying | [sourced: metrics …] |

- Engagement loop (retained core): trigger → action → reward → investment. …
- Drop-off point / resurrection path: …

## Unit economics {#unit-economics}
<!-- tool: unit-economics -->
_Contribution margin; LLM inference as an explicit COGS line. The "honest" basis is **optional —
own-compute (own-GPU) products only**; on third-party/API compute the bases collapse to one._

| Metric <!--c:metric--> | Operational <!--c:operational--> | Honest (+depreciation / market compute) — own-compute only <!--c:honest--> | Assumptions <!--c:assumptions--> |
|--------|-------------|------------------------------------------------------------|-------------|
| Revenue per payer ($/mo) | … | … | … |
| COGS per payer ($/mo) | … | … | [assumption: allocation rule] |
| Contribution ($/mo · %) | … | … | … |
| CAC (by channel) | … | … | [sourced / ⚙️] |
| Payback | … | … | … |
| LTV | — churn scenarios X/Y/Z% ⚙️ — | … | uses the `#retention` curve |

## Financial model {#financial-model}
<!-- tool: financial-model -->
_A simple projection tied to the metric-tree drivers; churn as a scenario axis; capacity caps as a first-class ceiling._

| Driver <!--c:driver--> | Base <!--c:base--> | Assumption <!--c:assumption--> | Confidence <!--c:conf--> |
|--------|------|------------|------------|
| … | … | … | [assumption] |

- Capacity ceiling: … (what caps growth, and when it binds)
- Scenarios: base / optimistic / conservative — key deltas …

## Risk mitigation {#risk-mitigation}
<!-- tool: risk-mitigation -->
_Each key risk → an owned mitigation (pre-mortem)._

| `R-…` <!--c:register--> | Risk <!--c:risk--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | Mitigation <!--c:mitigation--> | Owner <!--c:owner--> | Trigger <!--c:trigger--> | Due <!--c:due--> | Status <!--c:status--> |
|-------|------|------------|--------|------------|-------|---------|-----|--------|
| R-… | … | H/M/L | H/M/L | … | … | … | … | open / mitigating |

## Global hypotheses {#global-hypotheses}
<!-- tool: hypothesis-thresholds -->
_Strategy bets, now quantified & tied to metric nodes (threshold set here; test design at Step 5)._

| `H-…` <!--c:register--> | Bet <!--c:bet--> | Metric node (`M-…`) <!--c:node--> | Success threshold <!--c:success--> | Failure threshold <!--c:failure--> | Confidence <!--c:conf--> |
|-------|-----|---------------------|-------------------|-------------------|------------|
| H-… | … | M-… | ≥ … | < … | [assumption] |

## Open questions {#open-questions}
<!-- open -->
_What's still unknown, explicitly — not hidden._

- …

**Checked, not confirmed.** A check that came back neither validated nor refuted is a result: written
down it stops the next cycle from re-running it, unwritten it is re-run forever. Name what moved —
a hypothesis split into halves closes as `superseded`, not `refuted` (`process/CONVENTIONS.md`).

| What we checked <!--c:checked--> | What the data said <!--c:said--> | Why it is not a verdict <!--c:why--> | Moved <!--c:moved--> |
|-----------------|--------------------|-------------------------|-------|
| … | … | … | `H-…` / `M-…` / — |

## Change log

### <date> — created
- **From → To:** — → initial strategic-plan draft
- **Why:** …
- **Trigger:** …
