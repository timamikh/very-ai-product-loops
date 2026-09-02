---
node_type: card
kind: method
name: cjm-concept
steps: [1]
prerequisites: [the segment/persona whose journey this is, the job they are doing]
reads: [section:segments, section:jtbd, register:hypotheses, register:metrics, source:interview, source:kb]
writes: [worklog, section:cjm, register:hypotheses]
opinionated: false
method_basis: "Journey mapping — stages · actions · touchpoints · thoughts/emotions · pains → opportunities; moments that matter"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.4.1
updated: 2026-09-02
---
# Customer Journey Map (concept)

Map **one segment's end-to-end journey doing the job, over time** — the stages, actions,
touchpoints, and how it feels — to surface where it breaks and where value can be added. Fills
`{#cjm}` at Step 1, as an **optional lens**: the temporal view behind `{#problems}`, filled when
the journey's **time structure matters to the concept** — a flat list would hide **where** pains
bite. An assumption-tagged map is a legal first pass: the map is drawn from what the step already
has, and the breakage points it finds become `H-…` rows — **the map produces the interview plan,
it does not wait for one**. Interviews are sprint work planned against those hypotheses.

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
- **Step 1, optionally**, when the journey's **time structure matters to the concept**: the path
  is long and multi-actor (initiator → approver → payer), the pains live at different stages, or a
  stall somewhere along the path is suspected — a flat `{#problems}` list would average that away.
- When interviews exist and contradict the pain ranking: walking the journey often shows the pain
  sits at a different stage than reported.
- When the instance **has** readings (`register:metrics`) and they show an unexplained drop-off —
  one more stage-bound signal *when it exists*, never the defining trigger.

**When to skip — and how to say it.** Skip when the journey is trivial or its time structure
changes nothing in the concept — a short single-actor path whose pains mean the same whenever they
occur. The call is a statement about the **concept and the evidence in `reads`**, never about a
source the instance lacks: "no interviews yet" is not a skip reason, because producing the
interview plan is this map's job; "no funnel data" imports a running-product signal into a step
that never had one. The `evidence_standard` governs when a row may claim `[sourced]` — it is an
honesty bar for the tags, not an entry bar for the method: an all-`[assumption]` map is a legal
first pass. A recorded skip names an **in-perimeter** return trigger.

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
   These `H-…` rows are what the sprint's interviews are planned against — the map's output *is*
   the interview plan. Risks are not born at Step 1 — the Step-3 revisit (`cjm-strategy`) seeds
   `R-…` once a strategy exists to put at risk.

## Anti-patterns
- **Skipping by a source you lack.** Justifying n/a with an absent funnel or dashboard — the
  trigger and the skip are both read off the evidence in `reads`, and the return trigger names an
  in-perimeter signal, not the arrival of a data source the concept never had.
- **One map for all segments.** Averaging distinct journeys into a meaningless composite.
- **Inside-out.** Mapping *your* process instead of *their* experience.
- **Emotion theater.** An emotional curve drawn from imagination, not marked as assumption.
- **A map with no opportunities.** A pretty diagram that changes no decision.
- **Seeding risks at concept stage.** An `R-…` minted from a drop-off before any strategy exists —
  there is nothing yet for the risk to threaten; phrase it as a hypothesis or a `— to clarify —`.
- **Reinventing `product-surface`.** Listing static touchpoints without the timeline and the
  feeling — if that's all you need, that tool exists at Step 3.

## Worklog & projection
Worklog: `1-concept/cjm-concept.md` — the scoped journey, the stages with their evidence and n, the emotional curve and moments that matter, pains → opportunities, drop-offs → `H-…` or `— to clarify —`. Projects `{#cjm}`; face: the **Journey read** line, via [`template-fragment.md`](template-fragment.md). Revisited at Step 3 by `cjm-strategy` from its own worklog, same slot; the marker names both. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#cjm}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Its pains feed Step-1 `{#problems}`; its map is what
`cjm-strategy` re-walks at Step 3 (touchpoints → `product-surface`); seeds the hypothesis register
only.
