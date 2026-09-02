---
node_type: card
kind: method
name: pricing-strategy
steps: [3]
prerequisites: [uvp-cpv, segments, competitor pricing scan]
reads: [section:uvp-cpv, section:segments, section:competitor-pricing, register:hypotheses, source:interview, source:kb, source:research]
writes: [worklog, section:pricing, register:hypotheses]
opinionated: true
method_basis: "Value-based pricing & packaging — value metric selection, tiering/fences (good-better-best), willingness-to-pay (van Westendorp / direct WTP), price relative to the next-best alternative; price is a strategic choice, cost is a floor not the method"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.5
updated: 2026-09-02
---
# Pricing & Packaging (strategy)

Decide **what we charge and how we package it**: the **value metric** you meter on, the
**packaging** (tiers / fences), the **willingness-to-pay** evidence, and the **price points**
relative to the customer's next-best alternative. Fills `{#pricing}` at Step 3 — the qualitative
choice plus first numbers; Step 4's `pricing-strategic-plan` quantifies it against the margin.

**Method basis.** Value-based pricing: price is anchored to the *value delivered to a segment vs
its alternative*, not to cost (cost is a floor, not a method) and not to a competitor's number
copied blindly. Package with a **value metric** that scales with the value the customer gets
(seats, usage, workspaces…), and **fences** that let different segments self-select into tiers
(good-better-best). Willingness-to-pay is estimated from evidence — van Westendorp bands, direct
WTP questions, or observed pilot/price-talk behaviour — never guessed.

> **Relation to neighbours (one mechanism, one way).**
> - `competitor-pricing` captures **what others charge** (the Step-2 dated scan) —
>   that is an *input* to this tool, not the decision.
> - **`pricing-strategic-plan` (Step 4)** only re-checks the price points against unit economics
>   (the margin: contribution incl. LLM inference COGS, free-tier burn) and re-projects `{#pricing}`;
>   WTP is fixed **here**, at Step 3, behind the data gate — Step 4 gathers none. `financial-model`
>   projects the price forward. Those *validate* the decision; they do not set it. If the margin
>   check fails, the iteration comes back **here** — the choice of value metric and packaging is
>   this skill's and no one else's.
> - `uvp-cpv` states the value; `pricing-strategy` puts a number and a package on that value.

## When to apply
- **Step 3 — the decision (qualitative + first numbers).** Once the value proposition and segments
  are set: choose the value metric, the packaging/tiers, and the price positioning vs the
  alternative. This is a strategic choice, so it lives at Step 3.
- On repricing, a new tier, entering a new segment, or when discounting has become the norm
  (a signal the packaging is wrong).

## Prerequisites
- **Value proposition (`uvp-cpv`)** — price anchors to value vs an alternative. *Missing → run `uvp-cpv`.*
- **Segments** — different segments have different WTP and fences. *Missing → run `segmentation`.*
- **Competitor pricing scan** — the reference points customers compare against. *Missing → run
  `competitor-pricing` (Step 2).*

## How to do it
1. **Pick the value metric — and test it three ways.** What you meter on should rise with the
   value the customer receives (per seat, per workspace, per active user, per unit of usage). In the
   worklog, score the candidate on **tracks value · predictable for the buyer · cheap to meter**; a
   metric failing one is recorded with the failure.
2. **Design the packaging (fences).** Good-better-best or feature/usage tiers, with fences that let
   each segment self-select. Name what's in each tier and *why a segment picks it* — packaging is
   how one product serves several WTP levels without one price fitting no one.
3. **Anchor to the next-best alternative.** For each segment, price relative to what they'd pay/do
   instead (rival, substitute, do-nothing). **Quantify the value gap in the buyer's currency** —
   hours × rate, revenue uplift — not adjectives; that number justifies the delta.
4. **Estimate willingness-to-pay — behind a data gate.** Van Westendorp bands (too cheap / cheap /
   expensive / too expensive) **only with ≥~30 responses on file** (`source:kb`); fewer →
   `— to clarify —` naming the survey that would settle it, **never constructed bands**. Otherwise
   direct WTP, price talks (`source:interview`), pilot records (`source:kb`), published benchmarks
   (`source:research`). Tag each price point `[sourced: …]` or `[assumption]`; at Step 3 most are
   `[assumption]`, and that is fine — Step 4 checks them against the margin, it does not
   re-evidence them; the test of its `H-…` at Step 5 is what firms a price point up.
5. **Set price points and the model.** Subscription / usage / hybrid / one-off; the actual numbers
   per tier. Note free/trial mechanics and how they convert to the first paid action.
6. **Hand off and seed hypotheses.** Pass the decision to Step 4's `pricing-strategic-plan` (which
   routes it through `unit-economics` and `financial-model`). Each unproven price/packaging choice
   → `H-…` (`type: viability`) to validate (a price test, a pilot, a WTP survey).

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
  and treating it as fact — including van Westendorp bands drawn from a dozen answers.
- **Deciding price downstream.** The Step-4 margin check validates the price; it isn't where the
  price is chosen — a failed check iterates here.

## Worklog & projection
Worklog: `3-strategy/pricing-strategy.md` — the value metric with its three-way test, the tiers and fences, the anchoring per segment with the value gap in the buyer's currency, the WTP evidence with its tags (or the data-gate `— to clarify —`), the price points and model. Projects `{#pricing}`; face: the **Price stance** line, via [`template-fragment.md`](template-fragment.md). Primary of the `{#pricing}` marker; `pricing-strategic-plan` (Step 4) re-projects the section from its own worklog with the same slot. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#pricing}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). The decision feeds Step 4's `pricing-strategic-plan` (margin
check via `unit-economics`, projection via `financial-model`); unproven choices seed `H-…`
(`type: viability`).
