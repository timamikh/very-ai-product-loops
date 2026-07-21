---
node_type: artifact
artifact: tactical-plan
product: Decksmith (fictional sample)
step: 5
status_stage: concept-viability
owner: sample
updated: 2026-07-21
version: 0.1.0
---

# Tactical Plan — Decksmith (fictional sample) · Concept Test (6 wk)

> Status: `concept-viability` · Owner: sample · Period: 2026-07-21 → 2026-09-01 (~6 wk)
> Inputs: `4-strategic-plan.md` · registers. Feeds: `6-sprint-plan.md`.
> **ONE learning goal this period: prove the concept-killer — can the engine hit native edit-fidelity?**
> (`H-001`). Everything else is sized to *not over-invest before that signal* (status goal).

## Period goals {#period-goals}
<!-- tool: prioritization -->
_Measurable goals grouped by direction, ranked by contribution to the period gate._

**Gate of the period:** `H-001` validated — `M-edit-fidelity` ≥ 90% on representative test decks
(the concept-killer). A cheap parallel demand probe (`H-005`) runs alongside but does not gate build.

| Direction | Goal (measurable) | Why now | Confidence |
|-----------|-------------------|---------|------------|
| development | Thin vertical slice: generate → export a native `.pptx`; measure `M-edit-fidelity` on 20 test decks | The concept-killer — nothing matters if fidelity fails | [assumption] |
| go-to-market | Cheap demand probe on the "actually-editable" wedge with the beachhead (2 staged bundles) | Get a first demand signal without over-investing | [assumption] |
| back-office | Stand up event capture for `M-activation` + `M-edit-fidelity`; abstract the LLM provider | Instrument the export pipeline (the signal point); cap COGS/dependency | [assumption] |

_Ranked by gate contribution: the dev slice is the must; the demand probe is cheap and parallel; back-office is the minimum instrumentation to read the result._

## Goal targets {#goal-targets}
<!-- tool: metric-tree -->

| Goal | Direction | Target: `M-…` or DoD | Baseline → target | Confidence |
|------|-----------|----------------------|-------------------|------------|
| Fidelity slice | development | `M-edit-fidelity` | not-instrumented → ≥ 90% on 20 test decks | [assumption] |
| Demand probe | go-to-market | qualified signal → proxy for `M-activation` | 0 → ≥ 10 qualified trials (export+keep) | [assumption] |
| Instrumentation | back-office | DoD: events for `M-activation` + `M-edit-fidelity` live; LLM provider abstracted | — | [assumption] |

## Guardrails {#guardrails}
<!-- tool: guardrails -->

**Protected metrics (must not cross while chasing the goals):**

| Guardrail (`M-…`) | Threshold | Watched where / how often | Confidence |
|-------------------|-----------|---------------------------|------------|
| `M-cogs-per-deck` | ceiling ⚙️ ≤ $1/deck during the test | LLM billing, weekly | [assumption] |

**Red lines (qualitative "never"):**
- **No flatten-to-image shortcut** to fake fidelity — that defeats the entire wedge; `M-edit-fidelity` is measured honestly.
- Don't scale go-to-market spend before `H-001` is validated (protect runway / founder time).

**Breach = risk:** COGS ceiling breach → `R-004`; over-investing before signal → `R-008`/runway.

## Resources {#resources}
<!-- tool: resource-check -->
_Lightweight survey (illustrative for the sample)._

| Direction | People / capacity | Notes |
|-----------|-------------------|-------|
| development | founder + 1 eng | builds the fidelity slice + instrumentation |
| go-to-market | founder (part-time) | runs the demand probe in communities |
| back-office | 1 eng (shared) | analytics + provider abstraction |

- **Budget:** small pre-seed; earmark minimal — no paid acquisition this period. [assumption]
- **Time:** period = ~6 weeks; no fixed external dates.
- **Binding constraint:** **engineering time** — it caps how much can be built; the must-set fits one slice.

## Market-entry bundles {#market-bundles}
<!-- tool: segment-cvp -->
_Candidate go-to-market entries, gated on readiness (6 filters + three-things test). Top ones staged for the demand probe._

| ID | Segment | Situation | Pain | CVP | Offer | Channel | Signal · tier | Readiness | `H-…` |
|----|---------|-----------|------|-----|-------|---------|---------------|-----------|-------|
| B-01 | Salespeople | Prepping a client pitch deck under time pressure | AI decks look templated + can't edit in PPT | "A designed client deck you can actually edit in PowerPoint" | Free trial: generate + export one deck | Revenue-ops / sales-enablement Slack communities | trial → export → kept/edited · **strong** | ready | H-007 |
| B-02 | Marketers | Building an on-brand campaign deck | Off-brand, generic AI output | On-brand editable deck from your kit | Brand-kit trial | Marketing communities | trial + brand upload · medium | ready | H-007 |
| B-03 | Gamma-frustrated users | Their Gamma → PPT export broke | 30–40% of slides flattened to images | "Native editable export that doesn't break" | Import/compare demo | SEO/content on "fix Gamma PPT export" | signup from that intent → trial · medium | ready | H-005 |
| B-04 | "Everyone who makes slides" | — | — | "Make better slides with AI" | — | — | — | **not-ready: Recognize** (too broad — no self-recognition, no channel) | — |

**6-filter readiness gate** (staged bundles):

| Bundle | Find | Recognize | Pain | Alternative | CVP | Action |
|--------|------|-----------|------|-------------|-----|--------|
| B-01 | ✅ sales Slacks | ✅ "client pitch under time pressure" | ✅ redo by hand | ✅ Gamma/manual | ✅ editable designed deck | ✅ export+kept |
| B-03 | ✅ intent SEO | ✅ "my Gamma export broke" | ✅ 30–40% flattened | ✅ Gamma export | ✅ export that doesn't break | ✅ trial from intent |

**Three-things test** (B-01, B-03): ad message ✅ · landing/offer ✅ · sales first-contact script ✅ → staged.

**Staged for test this period:** **B-01** (strong signal) + **B-03** (intent-qualified). B-02 held; B-04 kept for reference, not staged. Bundles map to existing bets (`H-007` / `H-005`) — no new hypotheses seeded.

## Hypotheses to test {#hypotheses-to-test}
<!-- tool: hypothesis-test-design -->
_Pre-registered reads — metric · threshold · sample/duration · decision rule fixed before running._

| `H-…` | Metric node (`M-…`) | Success | Failure | Sample / duration | Decision rule | Confidence |
|-------|---------------------|---------|---------|-------------------|---------------|------------|
| H-001 (feasibility — the gate) | `M-edit-fidelity` | ≥ 90% objects natively editable | < 70% | 20 representative test decks / build sprint | ≥90% → `validated`, build on · <70% → `refuted`, rethink engine or pivot · 70–90% → `inconclusive`, iterate the slice | [assumption] |
| H-005 (wedge demand — probe) | qualified trials → proxy `M-activation` | ≥ 10 qualified trials that export+keep | ≤ 2 | B-01 + B-03 over ~4 wk | ≥10 → wedge real, proceed to `pmf` planning · ≤2 → weak, reframe positioning · between → `inconclusive`, more interviews | [assumption] |

_Test design chains from the Step-4 thresholds (`strategic-plan#global-hypotheses`). `H-001` is the smallest sufficient feasibility test; `H-005` is a cheap parallel demand probe — not a build gate._

## Blockers {#blockers}

| Blocker | Owner | Links (`R-…`) | Status | Confidence |
|---------|-------|---------------|--------|------------|
| Need 20 representative test decks to measure edit-fidelity | ⚙️ eng | R-007 | open | [assumption] |
| LLM provider access + quota for the slice | ⚙️ eng | R-004 | open | [assumption] |
| Access to a sales community to run the demand probe | ⚙️ founder | R-009 | open | [assumption] |

## To clarify {#to-clarify}
- **"Representative" test-deck set** — which 20 decks fairly stress edit-fidelity (layouts, charts, images)?
- **"Kept/edited" signal definition** — does a qualified trial require an edit event, or is export enough? (mirrors the Step-4 open question)
