---
node_type: card
kind: method
name: cjm-concept
steps: [1]
prerequisites: [the segment/persona whose journey this is, the job they are doing]
reads: [section:segments, section:jtbd, register:hypotheses, register:metrics, source:interview, source:research, source:kb]
writes: [worklog, section:cjm, register:hypotheses]
opinionated: false
method_basis: "Journey mapping — stages · actions · touchpoints · thoughts/emotions · pains → opportunities; moments that matter"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.0
updated: 2026-08-25
---
# Customer Journey Map (concept)

Map **one segment's end-to-end journey doing the job, over time** — the stages, actions,
touchpoints, and how it feels — to surface where it breaks and where value can be added. Fills
`{#cjm}` at Step 1, as an **optional lens**: the temporal view behind `{#problems}`, filled when a
flat pain list isn't enough (e.g. an unexplained drop-off).

**Method basis.** Classic journey mapping: lay the customer's experience out as a timeline of
**stages**, and for each capture **actions · touchpoints · thoughts/emotions · pains**, then read
the **emotional curve** and the **moments that matter** to convert pains into opportunities.

> **Relation to neighbours (one mechanism, one way).**
> - **`jtbd-concept`** frames *the job and the forces* (why they move) — this map takes that job
>   as its frame; don't restate it.
> - **`product-surface` (Step 3)** lists *the interaction surfaces and their instrumentation*
>   (what/where, static). `cjm-concept` is the **temporal sequence with the emotional curve and
>   drop-off points** (when, and how it feels). Its pains feed Step-1 `{#problems}`; its
>   touchpoints are picked up at Step 3 by `cjm-strategy`, which re-walks this map against the
>   chosen strategy and feeds `product-surface`.
> - **Registers.** Step 1 births *hypotheses*, not risks (`steps/1-concept/README.md` → *Register
>   touchpoints*). A drop-off found here seeds an `H-…` — "customers survive stage X" is a
>   desirability claim to test — or lands as a `— to clarify —` if it can't yet be phrased as one.
>   **Never seed `R-…` from this skill**; journey risks are born at Step 3, in `cjm-strategy` and
>   `pre-mortem`.

## When to apply
- **Step 1, optionally**, to surface a segment's problems as they actually occur along the journey,
  not as a flat list — especially when a drop-off or an abandonment needs explaining before the
  concept's problems can be trusted.
- When interviews contradict the pain ranking: walking the journey often shows the pain sits at a
  different stage than reported.

## Prerequisites
- **The segment/persona whose journey this is** — one segment, not "the user" in the abstract.
  *Missing → run `segmentation`.*
- **The job they are doing** — the progress they're trying to make, which frames the whole map.
  *Missing → run `jtbd-concept`.*

## How to do it
1. **Fix the scope.** One segment/persona, one job, a defined start and end. A CJM for "everyone"
   maps no one.
2. **Lay out the real stages.** The phases the customer moves through in *their* terms (e.g. aware
   → evaluate → onboard → habitual use → renew), not a projection of your internal funnel.
3. **Fill each stage.** Actions taken, touchpoints used, thoughts/emotions, and pains. Anchor each
   in evidence (interviews, analytics); mark anything unverified `[assumption]`. Say **how many**
   people each stage rests on and how they were selected — a stage backed by three power users and a
   stage backed by fifty logged sessions look identical on the map and mean very different things.
   Prefer observed behaviour over reported intent: what people said they would do at renewal is a
   forecast, not a fact.
4. **Plot the emotional curve and the moments that matter.** The highs, the lows, and the
   make-or-break moments where the journey is won or lost.
5. **Turn pains into opportunities.** Each significant pain → an opportunity/bet. This is the point
   of the map — a CJM that ends with no opportunities changed nothing. Feed the pains into
   `{#problems}` for scoring; don't re-score them here.
6. **Seed the hypothesis register — not the risk register.** Opportunity bets and drop-off findings
   → `H-…` (`type: desirability` — "customers get past stage X", "removing pain Y changes the
   decision"). A drop-off that can't yet be phrased as a testable claim goes to `— to clarify —`.
   Risks are not born at Step 1 — the Step-3 revisit (`cjm-strategy`) seeds `R-…` once a strategy
   exists to put at risk.

## Anti-patterns
- **One map for all segments.** Averaging distinct journeys into a meaningless composite.
- **Inside-out.** Mapping *your* process instead of *their* experience.
- **Emotion theater.** An emotional curve drawn from imagination, not marked as assumption.
- **A map with no opportunities.** A pretty diagram that changes no decision.
- **Seeding risks at concept stage.** An `R-…` minted from a drop-off before any strategy exists —
  there is nothing yet for the risk to threaten; phrase it as a hypothesis or a `— to clarify —`.
- **Reinventing `product-surface`.** Listing static touchpoints without the timeline and the
  feeling — if that's all you need, that tool exists at Step 3.

## Worklog & projection
The working is done in the step's **worklog** `1-concept/cjm-concept.md` (`node_type: worklog`): the
scoped journey (one segment, one job, defined start and end), the real stages each filled with
actions · touchpoints · thoughts/emotions · pains and the evidence behind them, the emotional curve
and the moments that matter, and the conversion of pains into opportunities and drop-offs into
hypotheses (or `— to clarify —` items). That worklog is the **source of truth**; the artifact
section `{#cjm}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the
step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External inputs arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#cjm}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Its pains feed Step-1 `{#problems}`; its map is what
`cjm-strategy` re-walks at Step 3 (touchpoints → `product-surface`); seeds the hypothesis register
only.
