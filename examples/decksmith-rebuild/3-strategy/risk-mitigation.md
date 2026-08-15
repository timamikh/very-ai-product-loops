---
node_type: worklog
tool: risk-mitigation
step: 3
fills: [product-risks]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — risk-mitigation (fills `#product-risks`)

At Step 3 this surfaces **strategy-specific** risks (a light pre-mortem on the chosen cascade); likelihood ×
impact on the H/M/L (5/3/1) backing. Mitigation/owner/due are added at Step 4 — `—` in the register until then.

Pre-mortem question: *if the beachhead-wedge cascade fails in 18 months, why?*

| ID | Risk | Category | L | I | L×I (5/3/1) |
|----|------|----------|---|---|-------------|
| R-006 | PLG virality doesn't fire → CAC too high without distribution | execution | M | H | 15 |
| R-007 | Fidelity engine can't hold design quality across arbitrary content at scale → wedge collapses | product | M | H | 15 |

Both are the shadow sides of load-bearing bets: R-006 ↔ H-011 (channels/CAC), R-007 ↔ H-001 (feasibility). The
incumbent-bundling threat is already `R-002` (Step 2); not duplicated here.

## Change log
### 2026-08-14 — created (rebuild)
- **From → To:** — → `R-006`/`R-007` born from a pre-mortem on the chosen cascade.
- **Why:** the strategy leans on PLG and on quality-at-scale; both deserve register entries.
- **Trigger:** Step-3 strategy, rebuild.
