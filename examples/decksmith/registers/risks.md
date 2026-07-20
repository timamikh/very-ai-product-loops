---
node_type: register
register: risks
product: "Decksmith (fictional sample)"
updated: 2026-07-20
---

# Risk register — Decksmith

> **Born at Step 2 (Analysis).** Refined downward: product risks (Step 3) → mitigation + owner/due
> (Step 4) → period blockers (Step 5). Mitigation/owner/due are added at Step 4 — `—` until then.

| ID | Risk | Category | Likelihood | Impact | Mitigation | Owner / Due | Status | Source |
|----|------|----------|------------|--------|------------|-------------|--------|--------|
| R-001 | Gamma is a dominant, profitable leader ($100M ARR, 70M users) — head-on displacement is hard | market | H | H | — | — | open | Step 2 (`../analysis.md#niche-risks`) |
| R-002 | Incumbents (Microsoft Copilot in PPT, Canva AI 2.0) bundle native-editable AI generation with distribution — closes our wedge | market | H | H | — | — | open | Step 2 (`../analysis.md#substitutes`) |
| R-003 | Capable buyers self-build with general LLMs (ChatGPT/Claude) → caps willingness to pay for "just generate slides" | market | M | M | — | — | open | Step 2 (`../analysis.md#substitutes`) |
| R-004 | Engine quality and COGS depend on third-party LLM providers (cost/availability outside our control) | dependency | M | H | — | — | open | Step 2 (`../analysis.md#niche-risks`) |
| R-005 | Low entry barrier for "AI slide wrappers" → crowded, fast-moving rivalry | market | H | M | — | — | open | Step 2 (`../analysis.md#niche-risks`) |
| R-006 | Manual build / hiring a designer keeps the high-stakes, brand-critical flagship decks | market | M | M | — | — | open | Step 2 (`../analysis.md#substitutes`) |
| R-007 | The engine never reliably hits native-fidelity + design at scale — the whole strategy rests on one feasibility bet (`H-001`) | product/execution | M | H | — | — | open | Step 3 (`../strategy.md#product-risks`) |
| R-008 | The beachhead won't pay standalone vs bundled incumbents (Copilot/Canva at $15–30 bundled) → no viable revenue | financial | M | H | — | — | open | Step 3 (`../strategy.md#pricing`) |
| R-009 | Community + product-led virality doesn't materialize → CAC too high to grow | market/execution | M | M | — | — | open | Step 3 (`../strategy.md#channels-expansion`) |

_Accumulates downward, never rewritten. Categories: market · product · execution · legal · financial · dependency.
Mitigation/owner/due are added at Step 4 (`risk-mitigation`) — `—` until then._
