---
node_type: register
register: metric-tree
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Metric register — Decksmith (rebuild)

> **Definitions here; values only in `metrics.csv`** (dated rows, append-only — `process/REGISTERS.md`).
> A changed definition mints a NEW id. Built at Step 4 (`metric-tree`).
> **Concept-viability state:** no product in market → **every node is `not-instrumented` and `metrics.csv` has
> no readings**. The tree is the *plan of what to measure*; the not-instrumented list is the Step-5/6
> instrumentation work (anti-lamppost: the right metric is named even though it isn't measured yet).

| ID <!--c:id--> | Definition <!--c:definition--> | Unit <!--c:unit--> | Kind <!--c:kind--> | Parent | Instrumentation <!--c:instrumentation--> | Target | Source |
|----|------------|------|------|--------|-----------------|--------|--------|
| M-ns-kept-decks-wk | **North Star (⚙️ candidate).** Decks generated → exported → **kept & edited** (used as the real deliverable, not rebuilt by hand) per active deck-maker per week. A redo = the value failed → encodes "editable AND designed". | count | measured | — (top) | not-instrumented | ⚙️ grow | product events (future) |
| M-edit-fidelity | **THE concept-proving metric.** Share of exported slide objects that are natively editable (real shapes/text, not flattened images) — the anti-Gamma metric; proxy for "I don't have to redo it". Also the quality guardrail. | % | measured | M-ns-kept-decks-wk | not-instrumented | ⚙️ ≥ 90% (fail < 70%) | export pipeline (future) |
| M-activation | Share of new signups who generate AND export a first editable deck ≤ 7d. | % | measured | M-ns-kept-decks-wk | not-instrumented | ⚙️ ≥ 30% (fail < 10%) | product events (future) |
| M-wk-retention | Share of activated users who return and export another deck the next week. | % | measured | M-ns-kept-decks-wk | not-instrumented | — to clarify — (no cohorts yet) | product events (future) |
| M-free-paid-conv | Free → paid conversion ≤ 30d. | % | measured | M-ns-kept-decks-wk | not-instrumented | ⚙️ ≥ 4% (fail < 1%) | billing (future) |
| M-cogs-per-deck | **Cost guardrail.** LLM inference $ per generated deck — caps the pursuit (ties to `R-004`). | $ | derived | — (guardrail) | not-instrumented | ⚙️ cap | inference logs (future) |

_North Star and targets are ⚙️ candidates until the human approves. All nodes not-instrumented by design at
concept-viability._

## Change log

### 2026-08-14 — born (Step 4, rebuild)
- **From → To:** — → `M-ns-kept-decks-wk` (North Star) + 4 drivers + `M-cogs-per-deck` guardrail; all
  not-instrumented; `metrics.csv` header only.
- **Why:** one decomposition encoding the editable-AND-designed strategy; the not-instrumented list is the
  instrumentation plan for Steps 5–6.
- **Trigger:** Step-4 strategic plan, rebuild.
