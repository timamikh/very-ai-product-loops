---
node_type: artifact-template
artifact: tactical-plan
step: 5
title: "Tactical Plan — <Product> · <period>"
status: template
version: 0.2.0
updated: 2026-07-20
---

<!--
  tactical-plan.md assembly shell. Each section is filled by its recommended library tool
  (see steps/5-tactical-plan/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md.
  Goals are grouped by work DIRECTION (instance config; default development · go-to-market · back-office).
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Tactical Plan — <Product> · <period>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Period: <start–end>
> Inputs: [[strategic-plan]] · registers. Feeds: [[sprint-plan]].

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see `CLAUDE.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Period goals {#period-goals}
<!-- tool: prioritization -->
_Measurable goals for the period, grouped by direction._

| Direction | Goal (measurable) | Why now | Confidence |
|-----------|-------------------|---------|------------|
| development | … | … | [assumption] |
| go-to-market | … | … | [assumption] |
| back-office | … | … | [assumption] |

## Goal targets {#goal-targets}
<!-- tool: metric-tree -->
_What each goal maps to: go-to-market → a metric node (`M-…`); technical & back-office → a Definition of Done._

| Goal | Direction | Target: `M-…` or DoD | Baseline → target | Confidence |
|------|-----------|----------------------|-------------------|------------|
| … | go-to-market | `M-…` | … → … | [assumption] |
| … | back-office | DoD: … | — | [assumption] |

## Guardrails {#guardrails}
<!-- tool: guardrails -->
_What must **not** drop while hitting the goals — protected metrics / red lines._

| Guardrail (`M-…`) | Must stay | Red line | Why | Confidence |
|-------------------|-----------|----------|-----|------------|
| `M-…` | ≥ … | … | … | [assumption] |

## Resources {#resources}
<!-- tool: resource-check -->
_Resources available this period (people, budget, time) — via survey._

| Resource | Available this period | Constraint | Confidence |
|----------|-----------------------|------------|------------|
| people | … | … | [sourced: …] |
| budget | … | … | [sourced: …] |

## Market-entry bundles {#market-bundles}
<!-- tool: segment-cvp -->
_Candidate go-to-market entries, gated on test-readiness (6 filters + three-things test).
Top 3–5 by `prioritization` are staged; `hypothesis-test-design` designs the chosen ones._

| ID | Segment | Situation | Pain | CVP | Offer | Channel | Signal · tier | Readiness | `H-…` | Confidence |
|----|---------|-----------|------|-----|-------|---------|---------------|-----------|-------|------------|
| B-01 | … | … | … | … | demo / diagnostic / trial | named community / partner | trial · **strong** | ready / `not-ready: <filter>` | H-… | [assumption] |

**Staged for test this period:** B-…, B-… (seed `type: desirability` `H-…`).

## Hypotheses to test {#hypotheses-to-test}
<!-- tool: hypothesis-test-design (ab-test for split-traffic) -->
_One row per `H-…` tested this period: a pre-registered read — metric · threshold · sample · decision rule fixed before running._

| `H-…` | Metric node (`M-…`) | Success | Failure | Sample / duration | Decision rule | Confidence |
|-------|---------------------|---------|---------|-------------------|---------------|------------|
| H-… | M-… | ≥ … | < … | n = … / … wk | ≥ success → validated; < failure → refuted; between → <next> | [assumption] |

## Blockers {#blockers}
_Dependencies / blockers with an owner (link back to `R-…`)._

| Blocker | Owner | Links (`R-…`) | Status | Confidence |
|---------|-------|---------------|--------|------------|
| … | … | R-… | open | [assumption] |

## To clarify {#to-clarify}
- …

## Change log

### <date> — created
- **From → To:** — → initial tactical-plan draft for <period>
- **Why:** …
- **Trigger:** …
