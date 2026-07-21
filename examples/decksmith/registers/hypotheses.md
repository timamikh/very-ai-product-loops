---
node_type: register
register: hypotheses
product: "Decksmith (fictional sample)"
updated: 2026-07-21
---

# Hypothesis register — Decksmith

> Born at Step 1, refined downward (Step 4 quantify → Step 5 test design → Step 6 experiment tasks).
> Refuted hypotheses are never deleted — they flip to `refuted` and become a trigger to revisit above.
> Confidence is a column here (not inline prose) — see `process/CONVENTIONS.md` matrix.

| ID | Hypothesis | Type | Tags | Status | Born | Source | Test | Confidence |
|----|------------|------|------|--------|------|--------|------|------------|
| H-001 | The engine can reliably produce native files that are both genuinely editable **and** genuinely well-designed, at scale | feasibility | — | **testing** | Step 1 | concept (`../1-passport.md#concept`) | **Step 4:** `M-edit-fidelity` ≥ 90% (fail < 70%) · **Step 5:** 20 test decks, decision rule set (`../5-tactical-plan.md#hypotheses-to-test`) · **Step 6:** `F-1`+`T-1` produce first read (`../6-sprint-plan.md#must`) | [assumption] |
| H-002 | Salespeople & marketers are a reachable segment who feel "AI decks look templated" (P1) strongly enough to switch | desirability | — | open | Step 1 | segments/problems (`../1-passport.md#problems`) | discovery interviews + a demand test (Step 5) | [assumption] |
| H-003 | "Wrong structure/framing" (P2) is a top pain worth solving, not just styling slides | desirability | — | open | Step 1 | problems (`../1-passport.md#problems`) | discovery interviews (Step 5) | [assumption] |
| H-004 | The engine's editable-and-beautiful quality is defensible — hard to replicate cheaply, survives an LLM rebuild. **Pressured at Step 2:** incumbents (Copilot/Canva) are entering the wedge, so the moat must be the fidelity+design *engine*, not the app | viability | moat | open | Step 1 | value (`../1-passport.md#value-defensibility`); pressured by `../2-analysis.md#competitor-strategy` | observe replication attempts / sustained quality gap (Step 3+) | [assumption] |
| H-005 | A native, high-fidelity editable-and-designed deck is a real unmet need the lead segment feels and prefers over web-format generation (Gamma's `.pptx` export flattens 30–40% of slides) — this is the *desire*; whether they'll **pay** for it is `H-009` | desirability | — | **testing** | Step 2 | opportunity/substitutes (`../2-analysis.md#opportunity`) | **Step 4:** `M-activation` ≥ 30% (fail < 10%) · **Step 5:** demand probe B-01/B-03, ≥ 10 qualified trials (`../5-tactical-plan.md#hypotheses-to-test`) · **Step 6:** `A-1` seeds B-01 probe (`../6-sprint-plan.md#must`) | [assumption] |
| H-006 | The obtainable market is large enough to build a business on (bottom-up SAM ~$750M; realistic SOM) | viability | — | open | Step 2 | market-sizing (`../2-analysis.md#market-sizing`) | validate reachable-count + price + adoption assumptions (Step 4) | [assumption] |
| H-007 | For the beachhead job, "actually-editable + designed native decks" is a strong enough wedge that salespeople & marketers switch (pull beats the "I'll still have to fix it" anxiety + PowerPoint habit) | desirability | — | open | Step 3 | bets (`../3-strategy.md#bets`); job/forces (`../1-passport.md#jtbd`) | **Step 4:** `M-wk-retention` flattens > 0; demand test (Step 5) | [assumption] |
| H-008 | A standalone native-fidelity+design engine can stay ahead of incumbents (Copilot/Canva) closing the wedge long enough to build lock-in | viability | moat | open | Step 3 | bets (`../3-strategy.md#bets`); `../2-analysis.md#opportunity` | sustained quality gap + retention once customers exist (pmf) | [assumption] |
| H-009 | The beachhead will pay a standalone subscription (~$15–25) despite incumbents bundling | viability | — | open | Step 3 | pricing (`../3-strategy.md#pricing`) | **Step 4:** WTP ≥ $15/mo (fail < $10); price-talk pilot (Step 5) | [assumption] |
| H-010 | Sales/marketing communities + product-led virality acquire the beachhead at viable CAC | viability | — | open | Step 3 | channels (`../3-strategy.md#channels-expansion`) | channel tests with pre-set CAC threshold (Step 5) | [assumption] |

_Refuted hypotheses stay as `refuted` rows (a guard against re-litigating them). At
concept-viability the whole register is `[assumption]` by design — there is no product data yet.
H-005 is the key hypothesis this stage turns on: the native-fidelity white space the analysis surfaced._
