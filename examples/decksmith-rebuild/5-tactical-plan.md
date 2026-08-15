---
node_type: artifact
artifact: tactical-plan
step: 5
title: "Tactical Plan — Decksmith (fictional sample) · 2026-08 P1"
status: draft
version: 0.1.0
updated: 2026-08-14
---

# Tactical Plan — Decksmith (fictional sample) · 2026-08 P1

> Status: concept-viability · Owner: — · Period: 2026-08 (first concept-viability period, ~1 mo)
> Inputs: `4-strategic-plan.md` · registers. Feeds: `6-sprint-plan.md`.
> Written artifact-direct (this step is unmigrated to worklogs, as in the reference instance — the method
> working is shown inline). No section confirmed (autonomous walk). Focus this period: prove **H-001**
> (feasibility gate) and **H-010** (demand) — the two bets testable without a product in market.

## Period goals {#period-goals}
<!-- tool: prioritization -->
_Measurable goals grouped by direction. Ranked against the period gate = "get a readable H-001 + H-010 signal".
N = 6 candidate goals entered the ranking; 3 staged as must (see #blockers for the cut backlog)._

| Direction | Goal (measurable) | Why now | Confidence |
|-----------|-------------------|---------|------------|
| development | Ship a prototype slice that generates + exports a **native .pptx** for ≥1 deck type, with `M-edit-fidelity` measurable on it | the feasibility gate (H-001) blocks everything else | [assumption] |
| go-to-market | Run a demand probe: landing + 2 community posts + ~10 discovery interviews; recruit ≥10 qualified trial signups | reads H-010 without a full product | [assumption] |
| back-office | Stand up minimal instrumentation: generate/export/keep events + fidelity capture in the export pipeline | no signal is readable without it | [assumption] |

## Goal targets {#goal-targets}
<!-- tool: metric-tree -->
_go-to-market → metric node / signal; technical & back-office → Definition of Done._

| Goal | Direction | Target: `M-…` or DoD | Baseline → target | Confidence |
|------|-----------|----------------------|-------------------|------------|
| Prototype exports native deck | development | **DoD:** exports a native .pptx for ≥1 deck type; `M-edit-fidelity` measurable on 20 test decks | — → DoD met | [assumption] |
| Demand probe | go-to-market | signal on **H-010** (qualified trials, strong tier); `M-activation` instrumented (not yet targetable — no product) | 0 → ≥10 qualified trials | [assumption] |
| Instrumentation live | back-office | **DoD:** generate/export/keep events fire; fidelity capture writes `M-edit-fidelity` | — → DoD met | [assumption] |

## Guardrails {#guardrails}
<!-- tool: guardrails -->
_What must not drop while chasing the goals — protected metrics / red lines._

| Guardrail (`M-…`) | Must stay | Red line | Why | Confidence |
|-------------------|-----------|----------|-----|------------|
| `M-edit-fidelity` | ≥ 70% on the eval set | < 70% = not shippable | don't chase demand on a broken engine — the wedge IS fidelity | [assumption] |
| `M-cogs-per-deck` | within ⚙️ cap | cost blows up chasing quality | protects margin (ties `R-004`) | [assumption] |
| Honesty (non-metric red line) | demand probe shows only what's real | no faked/mocked output presented as shipping | faking demand corrupts the H-010 read | [assumption] |

## Resources {#resources}
<!-- tool: resource-check -->
_Available this period (survey). ⚙️ illustrative — fictional sample, no real team._

| Resource | Available this period | Constraint | Confidence |
|----------|-----------------------|------------|------------|
| people | ~1–2 engineers + founder (design + GTM) | no dedicated growth/data role yet | ⚙️ [assumption] |
| budget | small (prototype infra + LLM inference + landing) | LLM inference cost is the main variable | ⚙️ [assumption] |
| time | ~1 month | feasibility gate must land mid-period to run B-01 | ⚙️ [assumption] |

## Market-entry bundles {#market-bundles}
<!-- tool: segment-cvp -->
_Composed from segments/pains/UVP/channels; 6-filter readiness gate (binary), then scored. Both staged bundles
probe the already-registered **H-010** (not re-minted — one bet, one home)._

| ID | Segment | Situation | Pain | CVP | Offer | Channel | Signal · tier | Readiness | probes | Confidence |
|----|---------|-----------|------|-----|-------|---------|---------------|-----------|--------|------------|
| B-01 | sales/marketers | preparing a client pitch on a deadline | AI decks look templated → rebuild tax | "a native deck you keep, not rebuild" | private demo/diagnostic on their real deck | sales/design communities | trial / price-talk · **strong** | `not-ready: deliverability` until the dev prototype lands mid-period | H-010 | [assumption] |
| B-02 | sales/marketers | just fought a broken Gamma → PPTX export | export flattens slides to images | "fix your Gamma export — get an editable deck" | landing + waitlist | LinkedIn content | sign-up · **medium** | **ready** (a landing needs no product) | H-010 | [assumption] |
| B-03 | founders/consultants | building a pitch/fundraise deck | highest design stakes | "an editable, designed pitch deck" | demo | accelerator networks | trial · strong | `not-ready: focus` — deprioritized this period | H-010 (later) | [assumption] |

**Readiness scores (ready bundles, 1/3/5 × 5, staged top):** B-02 = pain 3 · reach 5 · deliver 5 · WTP 3 · speed 5 = **21**; B-01 (once deliverable) = pain 5 · reach 5 · deliver 3 · WTP 5 · speed 3 = **21**. **Staged:** B-02 first (ready day 1, medium signal), B-01 mid-period (strong signal once the prototype exists). B-03 kept, not staged (focus).

## Hypotheses to test {#hypotheses-to-test}
<!-- tool: hypothesis-test-design (ab-test for split-traffic) -->
_Pre-registered: metric · threshold · sample · decision rule fixed before running._

| `H-…` | Metric node (`M-…`) | Success | Failure | Sample / duration | Decision rule | Confidence |
|-------|---------------------|---------|---------|-------------------|---------------|------------|
| H-001 | `M-edit-fidelity` | ≥ 90% | < 70% | 20 diverse test decks / the period | ≥90 → validated·scale; <70 → refuted·reject; 70–90 → iterate | [assumption] |
| H-010 | demand signal (B-01/B-02) | ≥ 10 qualified strong-tier signals (trial/price-talk) | < 3 | the probe / the period | ≥10 → validated·scale; <3 → reject·research; 3–10 → iterate | [assumption] |

## Blockers {#blockers}
<!-- open -->
_Dependencies / blockers with an owner (link back to `R-…`)._

| Blocker | Owner | Links (`R-…`) | Status | Confidence |
|---------|-------|---------------|--------|------------|
| Prototype slice not built → blocks B-01 + H-001 | ⚙️ eng | R-007 | open | [assumption] |
| No instrumentation → `M-edit-fidelity` unreadable | ⚙️ eng | — | open | [assumption] |
| LLM provider access + cost cap | ⚙️ eng | R-004 | open | [assumption] |
| _Cut from must (backlog): brand-kit tier, Team/admin surface, SEO — none move this period's gate_ | — | — | backlog | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
- **Team/resources are ⚙️ illustrative** — a real instance sets actual capacity, which moves the must/backlog line.
- **Trial mechanics** for B-01 (what "trial access" means before a full product) — define with eng.

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → P1 goals per direction (dev prototype gate · gtm demand probe · back-office instrumentation);
  guardrails on fidelity/cost/honesty; bundles B-01/B-02 staged (probe H-010); H-001/H-010 pre-registered.
- **Why:** turn the strategy into one period that produces a readable feasibility + demand signal.
- **Trigger:** Step-5 tactical plan, rebuild.
