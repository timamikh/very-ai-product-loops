---
node_type: register
register: hypotheses
product: "Decksmith (fictional sample)"
updated: 2026-07-20
---

# Hypothesis register — Decksmith

> Born at Step 1, refined downward (Step 4 quantify → Step 5 test design → Step 6 experiment tasks).
> Refuted hypotheses are never deleted — they flip to `refuted` and become a trigger to revisit above.
> Confidence is a column here (not inline prose) — see `process/CONVENTIONS.md` matrix.

| ID | Hypothesis | Type | Status | Born | Source | Test | Confidence |
|----|------------|------|--------|------|--------|------|------------|
| H-001 | The engine can reliably produce native files that are both genuinely editable **and** genuinely well-designed, at scale | feasibility | **testing** | Step 1 | concept (`../passport.md#concept`) | **Step 4:** `M-edit-fidelity` ≥ 90% (fail < 70%) · **Step 5:** 20 test decks, decision rule set (`../tactical-plan.md#hypotheses-to-test`) | [assumption] |
| H-002 | Salespeople & marketers are a reachable segment who feel "AI decks look templated" (P1) strongly enough to switch | desirability | open | Step 1 | segments/problems (`../passport.md#problems`) | discovery interviews + a demand test (Step 5) | [assumption] |
| H-003 | "Wrong structure/framing" (P2) is a top pain worth solving, not just styling slides | desirability | open | Step 1 | problems (`../passport.md#problems`) | discovery interviews (Step 5) | [assumption] |
| H-004 | The engine's editable-and-beautiful quality is defensible — hard to replicate cheaply, survives an LLM rebuild. **Pressured at Step 2:** incumbents (Copilot/Canva) are entering the wedge, so the moat must be the fidelity+design *engine*, not the app | viability/moat | open | Step 1 | value (`../passport.md#value-defensibility`); pressured by `../analysis.md#competitor-strategy` | observe replication attempts / sustained quality gap (Step 3+) | [assumption] |
| H-005 | A native, high-fidelity editable-and-designed deck is a real unmet need the lead segment values over web-format generation (Gamma's `.pptx` export flattens 30–40% of slides) | desirability/viability | **testing** | Step 2 | opportunity/substitutes (`../analysis.md#opportunity`) | **Step 4:** `M-activation` ≥ 30% (fail < 10%) · **Step 5:** demand probe B-01/B-03, ≥ 10 qualified trials (`../tactical-plan.md#hypotheses-to-test`) | [assumption] |
| H-006 | The obtainable market is large enough to build a business on (bottom-up SAM ~$750M; realistic SOM) | viability | open | Step 2 | market-sizing (`../analysis.md#market-sizing`) | validate reachable-count + price + adoption assumptions (Step 4) | [assumption] |
| H-007 | For the beachhead job, "actually-editable + designed native decks" is a strong enough wedge that salespeople & marketers switch (pull beats the "I'll still have to fix it" anxiety + PowerPoint habit) | desirability | open | Step 3 | bets (`../strategy.md#bets`); job/forces (`../passport.md#jtbd`) | **Step 4:** `M-wk-retention` flattens > 0; demand test (Step 5) | [assumption] |
| H-008 | A standalone native-fidelity+design engine can stay ahead of incumbents (Copilot/Canva) closing the wedge long enough to build lock-in | viability/moat | open | Step 3 | bets (`../strategy.md#bets`); `../analysis.md#opportunity` | sustained quality gap + retention once customers exist (pmf) | [assumption] |
| H-009 | The beachhead will pay a standalone subscription (~$15–25) despite incumbents bundling | viability | open | Step 3 | pricing (`../strategy.md#pricing`) | **Step 4:** WTP ≥ $15/mo (fail < $10); price-talk pilot (Step 5) | [assumption] |
| H-010 | Sales/marketing communities + product-led virality acquire the beachhead at viable CAC | viability | open | Step 3 | channels (`../strategy.md#channels-expansion`) | channel tests with pre-set CAC threshold (Step 5) | [assumption] |

_Refuted hypotheses stay as `refuted` rows (a guard against re-litigating them). At
concept-viability the whole register is `[assumption]` by design — there is no product data yet.
H-005 is the key hypothesis this stage turns on: the native-fidelity white space the analysis surfaced._
