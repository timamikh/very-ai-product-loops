---
node_type: register
register: metric-tree
product: "Decksmith (fictional sample)"
updated: 2026-07-21
---

# Metric register — Decksmith

> **Definitions here; values only in `metrics.csv`** (dated rows, append-only — `process/REGISTERS.md`).
> A changed definition mints a NEW id. Built at Step 4 (`metric-tree`).
> **Concept-viability state:** there is no product in market, so **every node is `not-instrumented`
> and `metrics.csv` has no readings yet** — the tree is the *plan of what to measure*, and the
> not-instrumented list is the instrumentation work for Steps 5–6 (the "lamppost trap" is avoided:
> the right metric is named even though it isn't measured yet). Kept light per the status: the ONE
> concept-proving metric is `M-edit-fidelity`.

| ID | Definition | Unit | Kind | Parent | Instrumentation | Target | Source |
|----|------------|------|------|--------|-----------------|--------|--------|
| M-ns-kept-decks-wk | **North Star (⚙️ candidate).** Decks generated → exported → **kept and edited** (used as the real deliverable, not rebuilt by hand) per active deck-maker per week. A redo = the value failed, so this encodes "editable **and** designed". | count | measured | — (top) | **not-instrumented** | ⚙️ grow | product events (future) |
| M-edit-fidelity | **THE concept-proving metric.** Share of exported slide objects that are **natively editable** (real shapes/text, not flattened images) — the anti-Gamma metric; proxy for "I don't have to redo it". | % | measured | M-ns-kept-decks-wk | **not-instrumented** | ⚙️ ≥ 90% | export pipeline (future) |
| M-activation | Share of new signups who **generate AND export a first editable deck ≤ 7d**. | % | measured | M-ns-kept-decks-wk | **not-instrumented** | — to clarify — | product events (future) |
| M-wk-retention | Share of activated users who **return and export another deck the next week**. | % | measured | M-ns-kept-decks-wk | **not-instrumented** | — to clarify — (no cohorts yet) | product events (future) |
| M-free-paid-conv | Free → paid conversion ≤ 30d (full funnel). | % | measured | M-ns-kept-decks-wk | **not-instrumented** | — to clarify — | billing (future) |
| M-cogs-per-deck | LLM inference + render cost per generated deck (COGS). `basis`: metered = API list price; fact = real spend. | $ | measured | — (guardrail) | **not-instrumented** | ⚙️ ↓ | LLM/API billing (future) |
| M-gross-margin | (Revenue − COGS) / Revenue. | % | derived | — (guardrail) | **not-instrumented** | ⚙️ ≥ 70% | derived (future) |

**Not instrumented (→ Steps 5–6):** *all of the above* — nothing is instrumented at concept stage.
The first build slice must stand up event capture for `M-activation` + `M-edit-fidelity` (the export
pipeline is the instrumentation point — see `../3-strategy.md#product-surface`). `M-wk-retention`
needs cohorts (from `pmf`). No own-GPU compute → COGS is third-party API only (no depreciation basis).
