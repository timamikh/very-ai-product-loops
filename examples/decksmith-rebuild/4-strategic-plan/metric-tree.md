---
node_type: worklog
tool: metric-tree
step: 4
fills: [metric-tree]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — metric-tree (fills `#metric-tree`; builds the metric register)

Opinionated: North Star Framework. Anti-lamppost — the right metric even if not measured yet (no product in
market → **every node not-instrumented**, `metrics.csv` empty). The not-instrumented list IS the Step-5/6
instrumentation plan.

## Candidate North Stars (2–4, three filters; rejects with the filter they failed)

| Candidate | leading | value-repeating | strategy-encoding | Verdict |
|-----------|---------|-----------------|-------------------|---------|
| **M-ns-kept-decks-wk** — decks generated → exported → **kept & edited** (used as the real deliverable, not rebuilt) per active deck-maker per week | ✓ | ✓ (repeat value) | ✓ a "kept" deck = editable AND designed succeeded — **encodes the wedge** | **CHOSEN** |
| Weekly active generators | ✓ | ✗ generating ≠ value (Gamma has millions of generations that get rebuilt) | ✗ | rejected (value-repeating) |
| Decks exported | ✓ | ✗ | ✗ an exported-then-rebuilt deck is a *failure*, not a win | rejected (strategy-encoding) |
| MRR / revenue | ✗ | — | — | rejected (revenue is the outcome, never the North Star) |

## Drivers (3–5) + guardrails

- **Acquisition/activation:** `M-activation` — signup → generate+export first editable deck ≤ 7d.
- **Quality (the wedge):** `M-edit-fidelity` — share of exported objects natively editable (anti-Gamma). Both a
  driver of "kept" and the quality **guardrail**. ⚙️ target ≥ 90% (fail < 70%) — **the concept-proving metric**.
- **Retention:** `M-wk-retention` — activated users who return & export another deck next week.
- **Conversion:** `M-free-paid-conv` — free → paid ≤ 30d.
- **Cost guardrail:** `M-cogs-per-deck` — LLM inference $ per generated deck; cap it (ties to `R-004`).

All parents set to `M-ns-kept-decks-wk` (except the North Star itself and the cost guardrail, which caps the
pursuit). Every node **not-instrumented** — closing them is Step-5/6 instrumentation work.

## Register writes

New nodes → `../registers/metric-tree.md` (definitions), `../registers/metrics.csv` header only (no readings).
North Star `M-ns-kept-decks-wk` is a ⚙️ candidate (human approves).

## Change log
### 2026-08-14 — created (rebuild); metric register born
- **From → To:** — → North Star chosen from 4 candidates (3 rejected with filter); 4 drivers + cost guardrail;
  all not-instrumented.
- **Why:** one decomposition that encodes *this* strategy (editable-AND-designed), not generic SaaS.
- **Trigger:** Step-4 strategic plan, rebuild.
