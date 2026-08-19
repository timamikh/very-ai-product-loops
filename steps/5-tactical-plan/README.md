---
node_type: card
kind: step
name: tactical-plan
step: 5
title: "Step 5 — Tactical Plan"
output: 5-tactical-plan.md
prerequisites: [the strategic plan `4-strategic-plan.md` exists]
reads: [file:4-strategic-plan.md, register:metrics, register:hypotheses, source:metrics]
writes: [section:*]
surfaces: [ticks, register:hypotheses, register:risks, register:metrics, sign-off, change-log]
cadence: "~1–3 mo; stage-gate ~monthly"
method_basis: "OKR-style goals per direction · targets = metric nodes (go-to-market) or DoD (technical & back-office) · guardrails / red lines (steering-committee reconciliation) · resource survey · go-to-market bundle composition + readiness gate · experiment design · pre-registered readout · prioritization (RICE/ICE)"
status: draft
version: 0.3.0
updated: 2026-08-16
---
# Step 5 — Tactical Plan

**Goal.** Set **measurable goals for the period, per work direction**, decide **which
hypotheses to test**, and surface **blockers**. This is the stage-gate that turns strategy into
a period of focused work.

Work **directions** are an instance config (default `development · go-to-market · back-office`);
the number can change with the product. The active [status](../../statuses/README.md) sets which
goals take priority (e.g. `concept-viability` → building a prototype, not traction metrics).

## Inputs (source slots)
The strategic plan (`4-strategic-plan.md`), the metric register, the hypothesis register,
`metrics`, backlog export.

## Output
`5-tactical-plan.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `period-goals` | Measurable goals **grouped by direction** | `prioritization-tactical-plan` |
| `goal-targets` | What each goal maps to: **go-to-market → metric node (`M-…`); technical & back-office → a Definition of Done** | `goal-targets` |
| `guardrails` | What must **not** drop while hitting the goals — protected metrics / red lines | `guardrails` |
| `resources` | Resources available this period (people, budget, time) — via survey | `resource-check` |
| `market-bundles` | Candidate go-to-market entries (segment · situation · pain · CVP · offer · channel · signal), gated on test-readiness | `segment-cvp` |
| `hypotheses-to-test` | Which `H-…` we test now + the test design | `hypothesis-test-design` (`ab-test` when the test is a split-traffic experiment) |
| `readouts` | Verdicts of tests that finished this period, read against their pre-registered rules | `experiment-readout` |
| `blockers` | Dependencies/blockers with an owner | — |

## Register touchpoints
- **Metric tree** — go-to-market goals select nodes to move (`M-…`); guardrails are protected `M-…` nodes.
- **Hypotheses** — `market-bundles` seed go-to-market bets (`H-…`, `type: desirability`);
  `hypotheses-to-test` picks `H-…` and attaches a test design; `readouts` write `signal` and
  `decision` back to the register. `segment-cvp` stages the ready bundles;
  `prioritization-tactical-plan` decides whether they fit the period's capacity.
- **Risks** — period `blockers` link back to `R-…`; guardrails encode risks-not-to-realize.

## Gate checklist (soft) — each item ↔ artifact section
- [ ] each direction has measurable goals for the period → `tactical-plan#period-goals`
- [ ] go-to-market goals map to metric nodes; technical & back-office goals map to a DoD → `tactical-plan#goal-targets` → metric register
- [ ] guardrails set — what must not drop → `tactical-plan#guardrails`
- [ ] available resources assessed (survey) → `tactical-plan#resources`
- [ ] go-to-market entries composed as bundles and gated on readiness (6 filters + three-things test) → `tactical-plan#market-bundles` → hypothesis register
- [ ] hypotheses to test have a test design → `tactical-plan#hypotheses-to-test` → hypothesis register
- [ ] tests that finished this period are read against their pre-registered rules, with signal and decision recorded → `tactical-plan#readouts` → hypothesis register
- [ ] blockers listed with an owner → `tactical-plan#blockers`

## Cadence & invalidation
- **Cadence:** ~monthly stage-gate.
- **Invalidates downward:** the period goals define the Sprint Plan (6).
- **From below:** a sprint result (hit/miss, refuted hypothesis) triggers a re-plan here.

## The human's role
Set the period's priorities and accept the goals; the agent proposes goals from the metric tree and ranks the work.
