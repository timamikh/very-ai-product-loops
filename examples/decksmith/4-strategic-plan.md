---
node_type: artifact
artifact: strategic-plan
product: Decksmith (fictional sample)
step: 4
status_stage: concept-viability
owner: sample
updated: 2026-07-21
version: 0.1.0
---

# Strategic Plan — Decksmith (fictional sample)

> Status: `concept-viability` · Owner: sample · Last review: 2026-07-21
> Inputs: `3-strategy.md` · registers. Feeds: `5-tactical-plan.md`.
> **Quantitative instruments — but at concept stage there is no product data.** So the metric tree is
> the *plan of what to measure* (all nodes `not-instrumented`), unit economics are placeholders with
> WTP/COGS as hypotheses, retention and the financial model are deferred (no cohorts, no run-rate),
> and the emphasis is de-risking: mitigations for the 2–3 concept-killers. Node defs live in
> `registers/metric-tree.md`; there are no readings in `registers/metrics.csv` yet.

## Architecture & instrumentation {#architecture-instrumentation}
<!-- tool: architecture-c4, product-surface -->
_Refined from `3-strategy.md#architecture` / `#product-surface`: where metric data will come from, and what drives infra cost._

| Surface / component | Instrumentation | Data it will produce | Infra cost driver | Confidence |
|---------------------|-----------------|----------------------|-------------------|------------|
| Generator app | not-instrumented (to build) | generate→export funnel → `M-activation` | LLM inference | [assumption] |
| **Export pipeline** (`.pptx`/`.key` writer) | not-instrumented (to build) | **`M-edit-fidelity`** (% objects natively editable) — the key signal | render compute (in-house engine) | [assumption] |
| LLM provider(s) | external | tokens/deck → `M-cogs-per-deck` | **yes — COGS** (`R-004`) | [assumption] |
| Billing | not-instrumented | `M-free-paid-conv` | small | [assumption] |

_The export pipeline is both the moat and the primary instrumentation point — edit-fidelity is measured there._

## Metric tree {#metric-tree}
<!-- tool: metric-tree -->
_Shape + rationale; node definitions in `registers/metric-tree.md`, values (none yet) in `registers/metrics.csv`._

**North Star:** `M-ns-kept-decks-wk` — decks generated → exported → **kept and edited** (not rebuilt by
hand) per active deck-maker per week · [decision: ⚙️ candidate, not approved]
_Why this one: **leading** (moves before revenue) · **value-repeating** (a repeat "kept" deck = repeat value) · **strategy-encoding** (a redo means "editable+designed" failed — it measures the wedge itself)._

| Driver | Node | Inputs (nodes) | Instrumentation |
|--------|------|----------------|-----------------|
| activation | `M-activation` | first generate+export ≤7d | not-instrumented |
| value (strategy axis) | **`M-edit-fidelity`** — the ONE concept-proving metric | % objects natively editable | not-instrumented |
| retention | `M-wk-retention` | return + export next week | not-instrumented (needs cohorts) |
| conversion | `M-free-paid-conv` | free→paid ≤30d | not-instrumented |

**Guardrails:** `M-cogs-per-deck` (LLM+render cost/deck must not break margin) · `M-gross-margin` (⚙️ ≥ 70%).
**Not instrumented (→ Steps 5–6):** all nodes — the first build slice must stand up `M-activation` + `M-edit-fidelity` capture at the export pipeline.

## Retention {#retention}
<!-- tool: retention-analysis -->
_**Deferred at concept-viability — no usage history, no cohorts.** `M-wk-retention` is defined in the
tree but `not-instrumented`; the cohort curve is measured from `pmf` onward and becomes the real churn
input to LTV. Until then, LTV uses churn **scenarios** (below), never an assumed constant._

## Unit economics {#unit-economics}
<!-- tool: unit-economics -->
_Sketch with placeholders; WTP and COGS are explicit hypotheses, not facts. **Single basis:** Decksmith
runs on third-party LLM APIs (no own GPU), so "honest" = "operational" (compute is already market price)._

| Metric | Value (single basis — API compute) | Assumptions |
|--------|------------------------------------|-------------|
| Revenue per payer ($/mo) | ⚙️ ~$20 | pricing hypothesis `H-009` (WTP unproven) |
| COGS per payer ($/mo) | ⚙️ ~$3–6 | LLM inference + render per deck × decks/mo [assumption] — `M-cogs-per-deck` |
| Contribution ($/mo · %) | ⚙️ ~$14–17 · ~70–80% | revenue − COGS [assumption] |
| CAC (by channel) | — to clarify — | community/PLG aimed low; unproven `H-010` |
| Payback | ⚙️ < 2 mo *if* CAC stays low | depends on CAC |
| LTV | churn **scenarios** 3 / 5 / 10%/mo ⚙️ | no instrumented retention (`#retention`) |

**Who bears free-tier consumption:** free-tier generation is a real LLM cost — cap free exports so `M-cogs-per-deck` on free users stays bounded. [assumption]

## Financial model {#financial-model}
<!-- tool: financial-model -->
_**Light / illustrative at concept-viability — no run-rate to project from.** Drivers are named so the
model can be built the moment real values exist; a full projection is a `pmf` output._

**Drivers (all [assumption] — no `metrics.csv` values yet):** new payers/mo · churn %/mo (scenario axis 3/5/10%) · ARPPU ≈ $20 (`H-009`) · COGS/deck (`M-cogs-per-deck`) · fixed (infra + build).

- **Capacity ceiling:** LLM API rate limits + render throughput — not binding at concept scale; revisit at `pmf`.
- **Scenarios:** deferred — with zero run-rate a 12-month MRR projection would be theatre. Built at `pmf` from first readings.

## Risk mitigation {#risk-mitigation}
<!-- tool: risk-mitigation -->
_Pre-mortem: the 2–3 risks that would kill the concept get an owned mitigation + trigger now (existing
R- risks pulled from the register; owners are ⚙️ role placeholders in this sample)._

| `R-…` | Risk | Likelihood | Impact | Mitigation | Owner | Due | Status |
|-------|------|------------|--------|------------|-------|-----|--------|
| **R-007** | Engine never hits native-fidelity+design at scale (the concept-killer; whole strategy rests on `H-001`) | M | H | Build the fidelity engine as a thin vertical slice **first**; gate everything on `M-edit-fidelity` ≥ 90% before investing further | ⚙️ founder/eng | next sprint | mitigating |
| **R-002** | Incumbents (Copilot/Canva) close the editable+designed wedge with distribution | H | H | Move fast on the native-fidelity gap; position sharply on "actually editable"; track their releases | ⚙️ founder | ongoing | mitigating |
| **R-008** | Beachhead won't pay standalone vs bundled incumbents | M | H | Test WTP early (Step 5 pilot) **before** building billing; don't scale spend until the wedge is validated | ⚙️ founder | Step 5 | open |
| R-004 | LLM dependency — cost/availability outside our control | M | H | Abstract the provider (multi-model); cap `M-cogs-per-deck`; keep the fidelity engine (the moat) in-house | ⚙️ eng | ongoing | mitigating |
| R-009 | Community + PLG virality doesn't materialize → CAC too high | M | M | Test inner-ring channels cheaply with a pre-set CAC threshold (`H-010`) | ⚙️ founder | Step 5 | open |

_`R-001` / `R-003` / `R-005` / `R-006` are consciously **accepted/monitored** at concept stage (not the concept-killers). Register updated with these mitigations/owners._

## Global hypotheses {#global-hypotheses}
<!-- tool: hypothesis-test-design -->
_Strategy bets quantified: a threshold tied to a metric node (⚙️ — thresholds unproven). The **test
design** (sample/duration/decision rule) is attached at Step 5._

| `H-…` | Bet | Metric node (`M-…`) | Success threshold | Failure threshold | Confidence |
|-------|-----|---------------------|-------------------|-------------------|------------|
| H-001 | The engine reliably produces editable+designed native files | `M-edit-fidelity` | ⚙️ ≥ 90% objects natively editable | < 70% | [assumption] |
| H-005 | The editable+designed wedge is valued (users keep/edit, don't redo) | `M-activation` / `M-ns-kept-decks-wk` | ⚙️ ≥ 30% activate (generate+export+keep) | < 10% | [assumption] |
| H-007 | The beachhead switches for the wedge | `M-wk-retention` | ⚙️ retention curve flattens > 0 | decays to 0 | [assumption] |
| H-009 | Beachhead pays a standalone subscription | (WTP → `M-free-paid-conv`) | ⚙️ WTP ≥ $15/mo in pilot | < $10/mo | [assumption] |

## Open questions {#open-questions}

- **Edit-fidelity threshold** — is ≥90% the right bar for "actually editable", or does the beachhead need ~100%? (sets `H-001`'s success line)
- **Activation definition** — does "kept" require an edit event, or is export enough? (affects `M-activation` / North Star)
- **Free-tier cost exposure** — how many free generations before `M-cogs-per-deck` on free users is unsustainable?
- **WTP floor** — the price below which the standalone model doesn't work vs bundled incumbents (feeds `H-009`).
