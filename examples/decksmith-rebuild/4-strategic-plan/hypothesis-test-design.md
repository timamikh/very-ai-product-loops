---
node_type: worklog
tool: hypothesis-test-design
step: 4
fills: [global-hypotheses]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — hypothesis-test-design (fills `#global-hypotheses`)

At Step 4 this **quantifies** the strategy bets: tie each to a metric node and set success/failure thresholds
(full test design is Step 5). Priority score (1/3/5 on pain acuteness · reach · fit · pay potential · test
speed) decides which bets enter a test first.

## Quantified bets (threshold tied to `M-…`)

| H- | Bet | Node | Success | Failure | Priority (1/3/5 sum) |
|----|-----|------|---------|---------|----------------------|
| H-001 | engine editable-AND-designed at scale | `M-edit-fidelity` | ≥ 90% | < 70% | 25 — the gate; test first |
| H-010 | segment prefers native fidelity enough to switch | `M-activation` | ≥ 30% | < 10% | 21 |
| H-009 | native-fidelity engine stays ahead → retention | `M-wk-retention` | flattens > 0 | decays to 0 | 17 |
| H-012 | packaging converts free→Pro at ~$18 | `M-free-paid-conv` | ≥ 4% | < 1% | 15 |
| H-011 | communities + PLG at viable CAC | (CAC — no node yet; unit-economics deferred) | CAC < LTV/3 | CAC ≥ LTV | 13 — needs the economics first |

## Readiness note

Only `H-001` and `H-010` are *ready to test cheaply now* (a prototype fidelity eval + a demand probe need no
product in market). `H-009`/`H-012` need product usage; `H-011` needs the economics (deferred). So Step 5 leads
with H-001 (feasibility gate) and H-010 (demand). Register `test` columns updated with these thresholds.

## Change log
### 2026-08-14 — created (rebuild)
- **From → To:** bets qualitative → quantified against `M-…` with success/failure thresholds; priority-scored.
- **Why:** a bet with no metric + threshold can't be read as pass/fail.
- **Trigger:** Step-4 strategic plan, rebuild.
