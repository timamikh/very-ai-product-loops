---
node_type: worklog
tool: risk-mitigation
step: 4
fills: [risk-mitigation]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — risk-mitigation (fills `#risk-mitigation`; attaches mitigation/owner/due to `R-…`)

Pre-mortem → each key risk gets an owned mitigation. Likelihood × impact on the 5/3/1 backing (ranking in the
register). Owners ⚙️ (human confirms).

| R- | Mitigation | Owner ⚙️ | Due | Status |
|----|------------|----------|-----|--------|
| R-001 | Don't fight Gamma head-on — compete on the native-fidelity gap; monitor | founder | ongoing | accepted |
| R-002 | Move fast on the fidelity gap; position sharply on "actually editable"; track incumbent releases | founder | ongoing | mitigating |
| R-003 | Lean value on native fidelity (what self-build does worst); monitor WTP | founder | ongoing | accepted |
| R-004 | Multi-model provider abstraction; cap `M-cogs-per-deck`; keep the fidelity engine in-house | eng | Q+1 | mitigating |
| R-005 | The moat is the fidelity engine, not the app — ship fast, widen the quality gap | eng | ongoing | mitigating |
| R-006 | Test inner-ring channels early with kill thresholds (k ≥ 0.3); keep a paid fallback | growth | Q+1 | mitigating |
| R-007 | Prototype fidelity+design eval **before** scaling (the `H-001` gate); design-eval on 20 test decks | eng | Q+1 | mitigating |

Top by L×I: R-001/R-002 (25); R-004/R-006/R-007 (15). R-007 and R-002 are the two that can kill the wedge —
they get the earliest owned work.

## Change log
### 2026-08-14 — created (rebuild)
- **From → To:** `R-001…R-007` mitigation/owner/due `—` → filled; statuses set (accepted/mitigating).
- **Why:** a risk with no owned mitigation is a hope; the pre-mortem attaches one to each.
- **Trigger:** Step-4 strategic plan, rebuild.
