---
node_type: register
register: risks
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Risk register — Decksmith (rebuild)

> **Born at Step 2 (Analysis).** Refined downward: product risks (Step 3) → mitigation + owner/due (Step 4) →
> period blockers (Step 5). Owners are ⚙️ proposals until the human confirms.

| ID <!--c:id--> | Risk | Category <!--c:category--> | Tags | Likelihood | Impact | Mitigation | Owner / Due | Status <!--c:status--> | Source |
|----|------|----------|------|------------|--------|------------|-------------|--------|--------|
| R-001 | Gamma is a dominant, profitable leader ($100M ARR, 70M users, $2.1B val) — head-on displacement is hard | market | — | H | H | Don't fight head-on — compete on the native-fidelity gap; monitor | ⚙️ founder · ongoing | accepted | Step 2 (`../2-analysis.md#niche-risks`) |
| R-002 | Incumbents (Copilot in PPT, Canva) bundle native-editable AI generation + own distribution — closes our wedge | market | — | H | H | Move fast on the fidelity gap; position sharply on "actually editable"; track incumbent releases | ⚙️ founder · ongoing | mitigating | Step 2 (`../2-analysis.md#substitutes`) |
| R-003 | Capable users self-build with general LLMs → caps willingness to pay for "just generate slides" | market | — | M | M | Lean value on native fidelity (what self-build does worst); monitor WTP | ⚙️ founder · ongoing | accepted | Step 2 (`../2-analysis.md#substitutes`) |
| R-004 | Engine quality and COGS depend on third-party LLM providers (cost/availability outside our control) | dependency | — | M | H | Multi-model provider abstraction; cap `M-cogs-per-deck`; keep the fidelity engine in-house | ⚙️ eng · Q+1 | mitigating | Step 2 (`../2-analysis.md#niche-risks`) |
| R-005 | Low entry barrier for "AI slide wrappers" — only a true native-fidelity engine is a real barrier | market | moat | M | M | The moat is the fidelity engine, not the app — ship fast, widen the quality gap | ⚙️ eng · ongoing | mitigating | Step 2 (`../2-analysis.md#niche-risks`) |
| R-006 | PLG virality doesn't fire → CAC too high without distribution | execution | — | M | H | Test inner-ring channels early with kill thresholds (k ≥ 0.3); keep a paid fallback | ⚙️ growth · Q+1 | mitigating | Step 3 (`../3-strategy.md#product-risks`) |
| R-007 | The fidelity engine can't hold design quality across arbitrary content at scale → the wedge collapses | product | — | M | H | Prototype fidelity+design eval before scaling (the `H-001` gate); design-eval on 20 test decks | ⚙️ eng · Q+1 | mitigating | Step 3 (`../3-strategy.md#product-risks`) |

_Carried risks are ranked by likelihood × impact on the 5/3/1 backing: R-001 (H·H=25), R-002 (H·H=25) top;
R-004/R-006/R-007 (M·H=15); R-003, R-005 (M·M=9). R-007 and R-002 are the two that can kill the wedge — earliest owned work._

## Change log

### 2026-08-14 — Step 4 (rebuild): mitigations owned
- **From → To:** `R-001…R-007` mitigation/owner/due `—` → filled; statuses set (accepted / mitigating).
- **Why:** a risk with no owned mitigation is a hope; the pre-mortem attaches one to each.
- **Trigger:** Step-4 strategic plan, rebuild.

### 2026-08-14 — Step 3 (rebuild): +R-006/R-007
- **From → To:** `R-001…R-005` → `R-001…R-007`; added strategy-specific risks (PLG doesn't fire; quality-at-scale).
- **Why:** the chosen cascade leans on PLG and on the engine holding quality — both are risks worth registering.
- **Trigger:** Step-3 strategy, rebuild.

### 2026-08-14 — born (Step 2, rebuild)
- **From → To:** — → `R-001`…`R-005` born from the niche-risks/substitutes synthesis.
- **Why:** the analysis surfaced structural threats (incumbent bundling, self-build, LLM dependency); the
  register is their home so mitigation can be attached downward.
- **Trigger:** Step-2 analysis, rebuild.
