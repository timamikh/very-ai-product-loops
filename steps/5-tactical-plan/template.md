---
node_type: artifact-template
artifact: tactical-plan
step: 5
title: "Tactical Plan — <Product> · <period>"
status: template
version: 0.4.0
updated: 2026-08-23
---

<!--
  5-tactical-plan.md assembly shell. Each section is filled by its recommended library tool
  (see steps/5-tactical-plan/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md.
  Goals are grouped by work DIRECTION (instance config; default development · go-to-market · back-office).
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Tactical Plan — <Product> · <period>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Period: <start–end>
> Inputs: `4-strategic-plan.md` · registers. Feeds: `6-sprint-plan.md`.

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see the repo's agent rules `AGENTS.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Period goals {#period-goals}
<!-- tool: prioritization-tactical-plan -->
<!-- rests-on: 4#metric-tree -->
_Measurable goals for the period, grouped by direction._

| Direction <!--c:direction--> | Goal (measurable) <!--c:goal--> | Why now <!--c:why--> | Confidence <!--c:conf--> |
|-----------|-------------------|---------|------------|
| development | … | … | [assumption] |
| go-to-market | … | … | [assumption] |
| back-office | … | … | [assumption] |

## Goal targets {#goal-targets}
<!-- tool: goal-targets -->
<!-- rests-on: 4#metric-tree, 4#strategic-targets -->
_What each goal maps to: go-to-market → a metric node (`M-…`); technical & back-office → a Definition
of Done. Each target is a step toward `4#strategic-targets` — a period in which no horizon target
moves is drift._

| Goal <!--c:goal--> | Direction <!--c:direction--> | Target: `M-…` or DoD <!--c:target--> | Baseline → target <!--c:baseline--> | Confidence <!--c:conf--> |
|------|-----------|----------------------|-------------------|------------|
| … | go-to-market | `M-…` | … → … | [assumption] |
| … | back-office | DoD: … | — | [assumption] |

## Guardrails {#guardrails}
<!-- tool: guardrails -->
<!-- rests-on: 4#metric-tree -->
_What must **not** drop while hitting the goals — protected metrics / red lines._

| Guardrail (`M-…`) <!--c:guardrail--> | Must stay <!--c:muststay--> | Red line <!--c:redline--> | Why <!--c:why--> | Confidence <!--c:conf--> |
|-------------------|-----------|----------|-----|------------|
| `M-…` | ≥ … | … | … | [assumption] |

## Resources {#resources}
<!-- tool: resource-check -->
_Resources available this period (people, budget, time) — via survey._

| Resource <!--c:resource--> | Available this period <!--c:available--> | Constraint <!--c:constraint--> | Confidence <!--c:conf--> |
|----------|-----------------------|------------|------------|
| people | … | … | [sourced: …] |
| budget | … | … | [sourced: …] |

## Market-entry bundles {#market-bundles}
<!-- tool: segment-cvp -->
<!-- rests-on: 1#segments, 3#uvp-cpv -->
_Candidate go-to-market entries, gated on test-readiness (6 filters + three-things test).
The top 3–5 by readiness score are staged; `prioritization-tactical-plan` decides whether they fit
the period's capacity; `hypothesis-test-design` designs the chosen ones._

| ID <!--c:id--> | Segment <!--c:segment--> | Situation <!--c:situation--> | Pain <!--c:pain--> | CVP <!--c:cvp--> | Offer <!--c:offer--> | Channel <!--c:channel--> | Signal · tier <!--c:signal--> | Readiness <!--c:readiness--> | `H-…` <!--c:register--> | Confidence <!--c:conf--> |
|----|---------|-----------|------|-----|-------|---------|---------------|-----------|-------|------------|
| B-01 | … | … | … | … | demo / diagnostic / trial | named community / partner | trial · **strong** | ready / `not-ready: <filter>` | H-… | [assumption] |

**Staged for test this period:** B-…, B-… (seed `type: desirability` `H-…`).

## Hypotheses to test {#hypotheses-to-test}
<!-- tool: hypothesis-test-design, ab-test -->
<!-- rests-on: 4#global-hypotheses -->
_One row per `H-…` tested this period: a pre-registered read — metric · threshold · sample · decision rule fixed before running. A split-traffic read follows `ab-test`._

| `H-…` <!--c:register--> | Metric node (`M-…`) <!--c:node--> | Success <!--c:success--> | Failure <!--c:failure--> | Sample / duration <!--c:sample--> | Decision rule <!--c:decision--> | Confidence <!--c:conf--> |
|-------|---------------------|---------|---------|-------------------|---------------|------------|
| H-… | M-… | ≥ … | < … | n = … / … wk | ≥ success → validated; < failure → refuted; between → <next> | [assumption] |

## Readouts {#readouts}
<!-- tool: experiment-readout -->
_Verdicts of tests that finished this period, read against their pre-registered rules;
signal/decision flow to the register._

| `H-…` <!--c:register--> | Test <!--c:test--> | Result vs rule <!--c:result--> | Signal <!--c:signal--> | Decision <!--c:decision--> | Follow-up <!--c:followup--> | Confidence <!--c:conf--> |
|-------|------|----------------|--------|----------|-----------|------------|
| H-… | … | … vs "≥ … / < …" → validated / refuted / inconclusive | weak / medium / strong | scale / iterate / reject / research | research → named learning item; refuted → section it invalidates | [sourced: …] |

## Item readouts {#item-readouts}
<!-- tool: impact-readout -->
<!-- rests-on: 6#must -->
_Shipped sprint items of the last period, read against the expectations pre-registered on them in
`6#must`; verdicts flip the feature register (`planned → live`). A check-by not reached is
`pending`, never skipped; an `H-…` verdict is cited from `{#readouts}`, never re-judged._

| Item (sprint · №) <!--c:item--> | Feature <!--c:feature--> | Expected <!--c:expected--> | Fact <!--c:fact--> | Verdict <!--c:verdict--> | Estimate: est → actual <!--c:estimate--> | Follow-up <!--c:followup--> | Confidence <!--c:conf--> |
|-------------------|---------|----------|------|---------|------------------------|-----------|------------|
| S<n> · 1 | F-… | `M-…` … → … · check-by … | … [sourced: metrics.csv] | confirmed / missed / inconclusive / pending | M (~…) → … | missed → names the section it invalidates | [sourced: …] |

## Blockers {#blockers}
<!-- open -->
_Dependencies / blockers with an owner (link back to `R-…`)._

| Blocker <!--c:blocker--> | Owner <!--c:owner--> | Links (`R-…`) <!--c:links--> | Status <!--c:status--> | Confidence <!--c:conf--> |
|---------|-------|---------------|--------|------------|
| … | … | R-… | open | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
- … — *the human chooses* · *nobody knows yet* · *a later step owns it* (name the step):
  keep exactly one (`process/CONVENTIONS.md` → the `open` bullet)

## Change log

### <date> — created
- **From → To:** — → initial tactical-plan draft for <period>
- **Why:** …
- **Trigger:** …
