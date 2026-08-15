---
node_type: register
register: hypotheses
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Hypothesis register — Decksmith (rebuild)

> Born at Step 1, refined downward (Step 4 quantify → Step 5 test design → Step 6 experiment tasks).
> Refuted hypotheses are never deleted — they flip to `refuted` and become a trigger to revisit above.
> Confidence is a column here (not inline prose). `signal`/`decision` (post-test gradations) are omitted:
> at concept-viability no test has been read, so they would be empty in every row.

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | Tags | Status <!--c:status--> | Born | Source | Test | Confidence <!--c:confidence--> |
|----|------------|------|------|--------|------|--------|------|------------|
| H-001 | The engine reliably produces native files that are both genuinely editable **and** genuinely well-designed, at scale (not one hand-tuned demo) | feasibility | — | open | Step 1 | concept (`../1-passport.md#concept`) | **Step 4:** `M-edit-fidelity` ≥ 90% (fail < 70%) · **Step 5/6:** prototype slice + design/fidelity eval | [assumption] |
| H-002 | Salespeople & marketers feel "looks templated / rebuild tax" (P1) strongly enough to switch | desirability | — | open | Step 1 | problems (`../1-passport.md#problems`) | discovery interviews + demand probe (Step 5) | [assumption] |
| H-003 | The "wrong structure/story" pain (P2) is real and valued, not just styling | desirability | — | open | Step 1 | problems (`../1-passport.md#problems`) | discovery interviews (Step 5) | [assumption] |
| H-004 | Editability is a hard gate — locked/image output is a non-starter (table-stakes) | desirability | table-stakes | open | Step 1 | problems (`../1-passport.md#problems`) | discovery interviews (Step 5) | [assumption] |
| H-005 | Design corpus + founder taste is a defensible-enough edge (survives an LLM rebuild) | viability | moat | open | Step 1 | value (`../1-passport.md#value-defensibility`) | observe replication attempts / sustained quality gap (Step 3+) | [assumption] |
| H-006 | Users can finish the generated deck in their native tool without a rebuild (the pull actually lands) | usability | — | open | Step 1 | jtbd (`../1-passport.md#jtbd`) | usability test on generated files (Step 5/6) | [assumption] |
| H-007 | SAM (~$390M, lead segment NA+EU payers) is large enough to build a business on | viability | — | open | Step 2 | market-sizing (`../2-analysis.md#market-sizing`) | validate reachable-count + adoption-share + price (Step 4) | [assumption] |
| H-008 | The lead segment will pay a standalone ~$15–20/mo despite incumbents bundling | viability | pricing | open | Step 2 | market-sizing (`../2-analysis.md#market-sizing`) | WTP probe / price-talk pilot (Step 5) | [assumption] |
| H-009 | A standalone native-fidelity engine can stay ahead of incumbents closing the wedge long enough to matter | viability | moat | open | Step 2 | opportunity (`../2-analysis.md#opportunity`) | **Step 4:** `M-wk-retention` flattens > 0 · sustained quality gap + replication-attempt watch (Step 3+) | [assumption] |
| H-010 | The lead segment prefers native-fidelity editable+designed decks over web-first generators enough to switch | desirability | — | open | Step 3 | bets (`../3-strategy.md#bets`); jtbd (`../1-passport.md#jtbd`) | **Step 4:** `M-activation` ≥ 30% (fail < 10%) · demand probe + switch test (Step 5) | [assumption] |
| H-011 | Sales/marketing communities + PLG virality acquire the beachhead at viable CAC | viability | — | open | Step 3 | channels (`../3-strategy.md#channels-expansion`) | inner-ring channel tests with pre-set CAC/k thresholds (Step 5) | [assumption] |
| H-012 | The good-better-best packaging (seat value metric) converts free→Pro at a viable rate at ~$18/mo | viability | pricing | open | Step 3 | pricing (`../3-strategy.md#pricing`) | **Step 4:** `M-free-paid-conv` ≥ 4% (fail < 1%); margin holds · price-talk pilot (Step 5) | [assumption] |

_At concept-viability the whole register is `[assumption]` by design — no product data yet. Step 4 quantifies
(WTP, margin, targets); Steps 5–6 design and run the tests._

## Change log

### 2026-08-14 — Step 4 (rebuild): bets quantified
- **From → To:** `H-001`/`H-009`/`H-010`/`H-012` `test` → tied to `M-…` nodes with success/failure thresholds
  (global-hypotheses). Status stays `open` — thresholds set, no test running yet (pre-data).
- **Why:** a bet with no metric + threshold can't be read pass/fail.
- **Trigger:** Step-4 strategic plan, rebuild.

### 2026-08-14 — Step 3 (rebuild): +H-010…H-012
- **From → To:** `H-001…H-009` → `H-001…H-012`; added the switch bet, the channel/CAC bet, and the pricing/
  packaging bet from the strategy cascade.
- **Why:** each strategic choice is a wager that must be testable.
- **Trigger:** Step-3 strategy, rebuild.

### 2026-08-14 — Step 2 (rebuild): +H-007…H-009
- **From → To:** `H-001…H-006` → `H-001…H-009`; added market/viability/moat bets from the analysis.
- **Why:** sizing and competitive assumptions must be testable, not asserted.
- **Trigger:** Step-2 analysis, rebuild.

### 2026-08-14 — born (Step 1, rebuild)
- **From → To:** — → `H-001`…`H-006` seeded from the passport (concept, problems, value, jtbd).
- **Why:** every Step-1 claim is an assumption; the register is its home so results can flow back up.
- **Trigger:** rebuild-from-brief walkthrough, Step 1.
