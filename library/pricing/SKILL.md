---
name: pricing
kind: method
produces: pricing
prerequisites: [uvp-cpv, segments, competitor pricing scan]
reads_registers: [hypotheses, metrics]
writes_registers: [hypotheses]
inputs: [interview, kb, analytics-search, metrics]
used_by_steps: [3, 4]
opinionated: true
method_basis: "Value-based pricing & packaging — value metric selection, tiering/fences (good-better-best), willingness-to-pay (van Westendorp / direct WTP), price relative to the next-best alternative; price is a strategic choice, cost is a floor not the method"
status: draft
version: 0.1.0
updated: 2026-07-18
---

# Pricing & Packaging

Decide **what we charge and how we package it**: the **value metric** you meter on, the
**packaging** (tiers / fences), the **willingness-to-pay** evidence, and the **price points**
relative to the customer's next-best alternative. Fills `{#pricing}`.

**Method basis.** Value-based pricing: price is anchored to the *value delivered to a segment vs
its alternative*, not to cost (cost is a floor, not a method) and not to a competitor's number
copied blindly. Package with a **value metric** that scales with the value the customer gets
(seats, usage, workspaces…), and **fences** that let different segments self-select into tiers
(good-better-best). Willingness-to-pay is estimated from evidence — van Westendorp bands, direct
WTP questions, or observed pilot/price-talk behaviour — never guessed.

> **Relation to neighbours (one mechanism, one way).**
> - `competitor-analysis` captures **what others charge** (Step 2 `pricing` scan) — that is an
>   *input* to this tool, not the decision.
> - `unit-economics` (Step 4) checks whether the chosen price **survives the margin** (CAC/LTV/
>   contribution, incl. LLM inference COGS) — that *validates* the decision; it does not set it.
> - `financial-model` projects the chosen price forward. **`pricing` is the only place the price
>   and packaging are decided**; the others feed it or test it. If the margin check fails,
>   iterate here, not there.
> - `uvp-cpv` states the value; `pricing` puts a number and a package on that value.

## When to apply
- **Step 3 — the decision (qualitative + first numbers).** Once the value proposition and segments
  are set: choose the value metric, the packaging/tiers, and the price positioning vs the
  alternative. This is a strategic choice, so it lives at Step 3.
- **Step 4 — quantified.** Firm up price points with WTP evidence and hand them to `unit-economics`
  and `financial-model`; adjust packaging if the margin doesn't hold.
- On repricing, a new tier, entering a new segment, or when discounting has become the norm
  (a signal the packaging is wrong).

## Prerequisites
- **Value proposition (`uvp-cpv`)** — price anchors to value vs an alternative. *Missing → run `uvp-cpv`.*
- **Segments** — different segments have different WTP and fences. *Missing → run `segmentation`.*
- **Competitor pricing scan** — the reference points customers compare against. *Missing → run
  `competitor-analysis` (Step 2 `pricing`).*
- *(Step 4)* WTP evidence — interview WTP / pilot price-talk / van Westendorp responses; if none
  yet, mark price points `[assumption]` and seed a pricing hypothesis to test.

## How to do it
1. **Pick the value metric.** What you meter on should rise with the value the customer receives
   (per seat, per workspace, per active user, per unit of usage). A value metric misaligned with
   value caps growth or punishes success.
2. **Design the packaging (fences).** Good-better-best or feature/usage tiers, with fences that let
   each segment self-select. Name what's in each tier and *why a segment picks it* — packaging is
   how one product serves several WTP levels without one price fitting no one.
3. **Anchor to the next-best alternative.** For each segment, price relative to what they'd pay/do
   instead (rival, substitute, do-nothing). State the value gap that justifies the delta.
4. **Estimate willingness-to-pay.** Use the evidence you have — van Westendorp bands (too cheap /
   cheap / expensive / too expensive), direct WTP, or observed pilot behaviour. Tag each price
   point `[sourced: …]` or `[assumption]`.
5. **Set price points and the model.** Subscription / usage / hybrid / one-off; the actual numbers
   per tier. Note free/trial mechanics and how they convert to the first paid action.
6. **Hand off and seed hypotheses.** Pass price points to `unit-economics` for the margin check and
   `financial-model` for projection. Each unproven price/packaging choice → `H-…`
   (`type: viability`) to validate (a price test, a pilot, a WTP survey).

## Anti-patterns
- **Cost-plus as the method.** Pricing off cost + markup ignores the value the segment perceives —
  cost is a floor, not the price.
- **Copying a competitor's number.** Matching a rival's price without the value/segment context
  that justifies theirs.
- **Value metric that doesn't scale with value.** Metering on something orthogonal to value
  (e.g. flat seats for a usage-driven product) — growth or fairness breaks.
- **One tier for everyone.** No fences → the single price is too high for the small segment and
  leaves money on the table with the large one.
- **WTP guessed, not evidenced.** Naming a price with no interview/pilot/survey signal behind it
  and treating it as fact.
- **Deciding price in `unit-economics`.** The margin check validates the price; it isn't where the
  price is chosen.

## Output
Fills `{#pricing}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml). Price points feed `unit-economics` and `financial-model` at
Step 4; unproven choices seed `H-…` (`type: viability`).
