---
node_type: sources-index
product: "Decksmith (fictional sample)"
updated: 2026-07-20
---

# Source navigation — Decksmith

> Entry point into the knowledge. The agent reads **this file first** and opens only the sources a
> task needs — it does not re-read the whole folder. The "Out of scope" column keeps boundaries from
> getting lost on re-reading raw material. ⚙️ = agent proposal; the human decides.

| File | Contains | In scope | Out of scope | Feeds steps | Confidence |
|------|----------|----------|--------------|-------------|------------|
| `founder-brief.md` | The raw idea, the founder's observations of the sales/marketing crowd, an honest have/can-build inventory, and the early bets (lead segment, riskiest = feasibility, pricing deferred) | Concept, lead segment, the pains to test, the value/moat inventory | Pricing (deferred to Step 3), collaboration/co-editing, non-slide formats | 1 | [sourced: founder brief 2026-07-16] |
| `market-research.md` | Triangulated desk-research digest (real, public): market size/dynamics, players (Gamma, Copilot, Canva, Beautiful.ai, Pitch, Tome), pricing, trends, barriers; the Gamma `.pptx` export-fidelity gap | Sizing inputs, competitor game/pricing/dynamics, substitutes, niche risks | Anything about Decksmith's own (fictional) metrics — none exist | 2, 3, 4 | [sourced] primary press for funding; secondary for pricing/export |

## Open sources (not yet obtained)

- **Demand signal for the lead segment** — no interviews or analytics run yet. Needed to move
  `H-002`/`H-003` (salespeople & marketers feel the pains strongly enough to switch) past
  `[assumption]`. Source — discovery interviews + analytics search (Step 2 / Step 5 test). [agent 2026-07-20]
- **Feasibility evidence** — no prototype quality evaluation yet. Needed for `H-001` (engine
  reliably produces editable-and-beautiful files at scale). Source — a prototype slice + design
  eval (Step 5/6 test). [agent 2026-07-20]

## Boundaries stated explicitly

- **Editability is a baseline, not the differentiator.** It's in the concept; the product competes
  on *look* (P1) and *structure/framing* (P2). See `../1-passport.md#problems`.
- **Pricing is deferred.** The founder brief deliberately leaves willingness-to-pay open — do not
  invent a price; it's a Step 3 decision. See `../1-passport.md#to-clarify`.
