---
node_type: register
register: risks
product: "Decksmith (fictional sample)"
updated: 2026-08-08
---

# Risk register — Decksmith

> **Born at Step 2 (Analysis).** Refined downward: product risks (Step 3) → mitigation + owner/due
> (Step 4) → period blockers (Step 5). Mitigation/owner/due are added at Step 4 — `—` until then.

| ID <!--c:id--> | Risk | Category <!--c:category--> | Tags | Likelihood | Impact | Mitigation | Owner / Due | Status <!--c:status--> | Source |
|----|------|----------|------|------------|--------|------------|-------------|--------|--------|
| R-001 | Gamma is a dominant, profitable leader ($100M ARR, 70M users) — head-on displacement is hard | market | monitored | H | H | Don't fight head-on — compete on the native-fidelity gap; monitor | ⚙️ founder | accepted | Step 2 (`../2-analysis.md#niche-risks`) |
| R-002 | Incumbents (Microsoft Copilot in PPT, Canva AI 2.0) bundle native-editable AI generation with distribution — closes our wedge | market | — | H | H | Move fast on the fidelity gap; position sharply on "actually editable"; track their releases | ⚙️ founder · ongoing | mitigating | Step 2 (`../2-analysis.md#substitutes`) |
| R-003 | Capable buyers self-build with general LLMs (ChatGPT/Claude) → caps willingness to pay for "just generate slides" | market | monitored | M | M | — (monitored) | ⚙️ founder | accepted | Step 2 (`../2-analysis.md#substitutes`) |
| R-004 | Engine quality and COGS depend on third-party LLM providers (cost/availability outside our control) | dependency | — | M | H | Abstract the provider (multi-model); cap `M-cogs-per-deck`; keep the fidelity engine in-house | ⚙️ eng · ongoing | mitigating | Step 2 (`../2-analysis.md#niche-risks`) |
| R-005 | Low entry barrier for "AI slide wrappers" → crowded, fast-moving rivalry | market | monitored | H | M | — (monitored; the moat is the fidelity engine, not the app) | ⚙️ founder | accepted | Step 2 (`../2-analysis.md#niche-risks`) |
| R-006 | Manual build / hiring a designer keeps the high-stakes, brand-critical flagship decks | market | monitored | M | M | — (monitored) | ⚙️ founder | accepted | Step 2 (`../2-analysis.md#substitutes`) |
| R-007 | The engine never reliably hits native-fidelity + design at scale — the whole strategy rests on one feasibility bet (`H-001`) | product | execution | M | H | Build the fidelity engine as a thin vertical slice first; gate on `M-edit-fidelity` ≥ 90% before investing further | ⚙️ founder/eng · next sprint | mitigating | Step 3 (`../3-strategy.md#product-risks`) |
| R-008 | The beachhead won't pay standalone vs bundled incumbents (Copilot/Canva at $15–30 bundled) → no viable revenue | financial | — | M | H | Test WTP early (Step 5 pilot) before building billing; don't scale spend until the wedge is validated | ⚙️ founder · Step 5 | open | Step 3 (`../3-strategy.md#pricing`) |
| R-009 | Community + product-led virality doesn't materialize → CAC too high to grow | market | execution | M | M | Test inner-ring channels cheaply with a pre-set CAC threshold (`H-010`) | ⚙️ founder · Step 5 | open | Step 3 (`../3-strategy.md#channels-expansion`) |

_Accumulates downward, never rewritten. `Category` is exactly one of: market · product · execution ·
legal · financial · dependency; a secondary theme (e.g. an execution angle on a product risk) goes in
`Tags`, not compounded into the category. Mitigation/owner/due are added at Step 4 (`risk-mitigation`) — `—` until then._

## Change log

### 2026-08-08 — statuses cleaned of compound values
- **From → To:** `R-001`, `R-003`, `R-005`, `R-006` read `accepted (monitored)` → `Status: accepted`, `Tags: monitored`
- **Why:** an enum cell holds the bare value; "monitored" is a theme, and themes live in `Tags` — the
  same rule that already governs `Category`.
- **Trigger:** linter check D, extended to `status` and `confidence` columns.

### 2026-07-20 — product & execution risks added at Step 3
- **From → To:** `R-001`–`R-006` (market/dependency, from the analysis) → plus `R-007`, `R-008`, `R-009`
- **Why:** every bet carries the risk of its own failure — the feasibility bet `H-001` becomes `R-007`,
  the pricing bet becomes `R-008`, the channel bet `H-010` becomes `R-009`.
- **Trigger:** Step 3 (`../3-strategy.md#product-risks`).

### 2026-07-18 — born at Step 2
- **From → To:** — → `R-001`–`R-006`
- **Why:** the analysis named real threats (a dominant leader, bundling incumbents, self-build
  substitutes, provider dependency); unrecorded, they come back as surprises.
- **Trigger:** Step 2 (`../2-analysis.md#niche-risks`, `#substitutes`).
