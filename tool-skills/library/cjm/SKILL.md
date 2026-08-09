---
name: cjm
kind: method
produces: cjm
prerequisites: [the segment/persona whose journey this is, the job they are doing]
reads_registers: [hypotheses]
writes_registers: [hypotheses, risks]
inputs: [interview, analytics-search]
used_by_steps: [1, 3]
opinionated: false
method_basis: "Journey mapping — stages · actions · touchpoints · thoughts/emotions · pains → opportunities; moments that matter"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.1
updated: 2026-08-09
---

# Customer Journey Map

Map **one segment's end-to-end journey doing the job, over time** — the stages, actions,
touchpoints, and how it feels — to find where it breaks and where value can be added. Fills
`{#cjm}`.

**Method basis.** Classic journey mapping: lay the customer's experience out as a timeline of
**stages**, and for each capture **actions · touchpoints · thoughts/emotions · pains**, then read
the **emotional curve** and the **moments that matter** to convert pains into opportunities.

**Relation to neighbours.** `jtbd` frames *the job and the forces* (why they move); `product-surface`
lists *the interaction surfaces and their instrumentation* (what/where, static). `cjm` is the
**temporal sequence with the emotional curve and drop-off points** (when, and how it feels). It
takes the job from `jtbd` as its frame; downstream, its pains feed step-1 `problems` and its
touchpoints feed step-3 `product-surface`. Don't restate those — link to them.

## When to apply
- **Step 1**, to surface a segment's problems as they actually occur along the journey, not as a flat list.
- **Step 3**, to decide which touchpoints the product must own and instrument (feeds `product-surface`).
- When a funnel drop-off is unexplained and you need to see the experience around it.

## Prerequisites
- **The segment/persona whose journey this is** — one segment, not "the user" in the abstract.
  *Missing → run `segmentation`.*
- **The job they are doing** — the progress they're trying to make, which frames the whole map.
  *Missing → run `jtbd`.*

## How to do it
1. **Fix the scope.** One segment/persona, one job, a defined start and end. A CJM for "everyone"
   maps no one.
2. **Lay out the real stages.** The phases the customer moves through in *their* terms (e.g. aware
   → evaluate → onboard → habitual use → renew), not a projection of your internal funnel.
3. **Fill each stage.** Actions taken, touchpoints used, thoughts/emotions, and pains. Anchor each
   in evidence (interviews, analytics); mark anything unverified `[assumption]`.
4. **Plot the emotional curve and the moments that matter.** The highs, the lows, and the
   make-or-break moments where the journey is won or lost.
5. **Turn pains into opportunities.** Each significant pain → an opportunity/bet; each drop-off →
   a risk. This is the point of the map — a CJM that ends with no opportunities changed nothing.
6. **Seed registers.** Opportunity bets → `H-…`; journey risks (drop-off, dependency, hand-off
   gaps) → `R-…`.

## Anti-patterns
- **One map for all segments.** Averaging distinct journeys into a meaningless composite.
- **Inside-out.** Mapping *your* process instead of *their* experience.
- **Emotion theater.** An emotional curve drawn from imagination, not marked as assumption.
- **A map with no opportunities.** A pretty diagram that changes no decision.
- **Reinventing `product-surface`.** Listing static touchpoints without the timeline and the
  feeling — if that's all you need, use `product-surface`.

## Output
Fills `{#cjm}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml). Its pains feed step-1 `problems`; its touchpoints feed step-3
`product-surface`; seeds the hypotheses and risk registers.
