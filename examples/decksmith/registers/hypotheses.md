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
| H-004 | The engine's editable-and-beautiful quality is defensible — hard to replicate cheaply, survives an LLM rebuild | viability/moat | open | Step 1 | value (`../passport.md#value-defensibility`) | observe replication attempts / sustained quality gap (Step 3+) | [assumption] |

_Refuted hypotheses stay as `refuted` rows (a guard against re-litigating them). At
concept-viability the whole register is `[assumption]` by design — there is no product data yet._
