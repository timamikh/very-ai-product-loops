---
name: risk-mitigation
kind: method
produces: [product-risks]
reads_registers: [risks]
writes_registers: [risks]
inputs: [interview, kb]
prerequisites: [strategy-choices]
used_by_steps: [3, 4]
opinionated: false
method_basis: "Pre-mortem (Klein) + risk register triage (prob × impact) + mitigation/owner"
evidence_standard: decision
volume_rule: "≥8 named failure modes from the pre-mortem before any triage"
selection_rule: "probability × impact; carried · parked · dropped, each with the reason"
rejects_shown: required
status: draft
version: 0.2.2
updated: 2026-08-09
---

# Risk & Mitigation

Surface the risks to the strategy via a **pre-mortem**, triage them into the R- register, and
give each a **mitigation, owner, and trigger**. Fills `{#product-risks}` at Step 3, and is reused
at Step 4 to attach mitigations to the plan.

**Method basis.** Klein's pre-mortem ("it's 12 months from now and the strategy failed — why?")
to elicit risks before they bite, then risk-register triage by probability × impact, and a named
mitigation + owner + trigger for each risk worth carrying.

## When to apply
- Step 3, after the strategy choices are made — before betting on them.
- Step 4, to add mitigations and owners to the plan's risks.
- Whenever a new risk surfaces or a live risk changes probability/impact.

## Prerequisites
- **Strategy choices** — the where-to-play / how-to-win / channels we're pressure-testing.
  *Missing → run `where-to-play-how-to-win` (and related Step-3 tools) first.*

## How to do it
1. **Run the pre-mortem.** Assume it's 12 months out and the strategy failed. Ask *why* — force
   concrete failure stories, not abstract worries. Cover execution and key-person risks, not just
   external/market ones.
2. **Pull existing risks.** Read the R- register for risks already logged (e.g. seeded by earlier
   tools); don't re-invent them.
3. **Triage.** Score each risk on probability × impact; keep the ones worth carrying and drop or
   park the trivial. Rank by the product.
4. **Assign mitigation + owner + trigger.** For each carried risk: what we'll do about it, *who*
   owns it, and the *trigger* (the observable signal that says "act now"). A risk with no owner or
   trigger is not managed.
5. **Write to the register.** Upsert each into R- with score, mitigation, owner, trigger, status.

## Anti-patterns
- **No owner / no trigger.** A risk logged but unassigned, with nothing that says when to act.
- **Only external risks.** Listing market/competitor risks while ignoring execution and
  key-person risks — usually the ones that actually sink it.
- **Severity theatre.** Scoring everything high so nothing is prioritized.
- **Register drift.** Risks captured here but never written back to R-.

## Output
Fills `{#product-risks}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
