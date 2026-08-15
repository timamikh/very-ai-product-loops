---
node_type: worklog
tool: pricing
step: 3
fills: [pricing]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — pricing (fills `#pricing`)

Value-based. Decided here; quantified + margin-checked at Step 4 (`unit-economics`, `financial-model`). WTP has
no evidence yet → all price points `[assumption]`.

- **Value metric:** per active deck-maker (seat) — scales with the person getting value; decks as a secondary
  fair-use meter. Cost (LLM inference) is a *floor*, not the method.
- **Packaging (good-better-best, fences):**
  - Good (Free/trial, $0): few decks/mo, export cap/watermark → converts on first full native export.
  - Better (Pro ~$18/mo): unlimited decks, full native export, brand kit → the lead segment's tier.
  - Best (Team ~$30/user/mo): shared brand kits, team templates, admin → org expansion.
- **Anchor:** vs Gamma $20 (but its export breaks — we charge for the part that works); vs bundled Copilot/Canva
  ($0 marginal for M365/Canva seats) — a standalone price is justified *only* by the native-fidelity gap they
  don't close. That gap-justification is the load-bearing bet.
- **WTP:** competitor band $13–25 → target ~$15–20. No van Westendorp / pilot data yet → `[assumption]`.
- **Seeds:** `H-008` (will pay standalone despite bundling), `H-012` (packaging converts free→Pro at ~$18).

## Change log
### 2026-08-14 — created (rebuild)
- **From → To:** — → seat value metric, good-better-best tiers, anchored to Gamma/bundled options; price points
  `[assumption]` pending WTP.
- **Why:** price is a strategic value-based choice; cost is only a floor.
- **Trigger:** Step-3 strategy, rebuild.
