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
| H-001 | The engine can reliably produce native files that are both genuinely editable **and** genuinely well-designed, at scale | feasibility | open | Step 1 | concept (`../passport.md#concept`) | prototype slice + design/edit-fidelity eval (Step 5/6) | [assumption] |
| H-002 | Salespeople & marketers are a reachable segment who feel "AI decks look templated" (P1) strongly enough to switch | desirability | open | Step 1 | segments/problems (`../passport.md#problems`) | discovery interviews + a demand test (Step 5) | [assumption] |
| H-003 | "Wrong structure/framing" (P2) is a top pain worth solving, not just styling slides | desirability | open | Step 1 | problems (`../passport.md#problems`) | discovery interviews (Step 5) | [assumption] |
| H-004 | The engine's editable-and-beautiful quality is defensible — hard to replicate cheaply, survives an LLM rebuild. **Pressured at Step 2:** incumbents (Copilot/Canva) are entering the wedge, so the moat must be the fidelity+design *engine*, not the app | viability/moat | open | Step 1 | value (`../passport.md#value-defensibility`); pressured by `../analysis.md#competitor-strategy` | observe replication attempts / sustained quality gap (Step 3+) | [assumption] |
| H-005 | A native, high-fidelity editable-and-designed deck is a real unmet need the lead segment values over web-format generation (Gamma's `.pptx` export flattens 30–40% of slides) | desirability/viability | open | Step 2 | opportunity/substitutes (`../analysis.md#opportunity`) | interviews + a demand test framed on "actually editable" (Step 5) | [assumption] |
| H-006 | The obtainable market is large enough to build a business on (bottom-up SAM ~$750M; realistic SOM) | viability | open | Step 2 | market-sizing (`../analysis.md#market-sizing`) | validate reachable-count + price + adoption assumptions (Step 4) | [assumption] |

_Refuted hypotheses stay as `refuted` rows (a guard against re-litigating them). At
concept-viability the whole register is `[assumption]` by design — there is no product data yet.
H-005 is the key hypothesis this stage turns on: the native-fidelity white space the analysis surfaced._
