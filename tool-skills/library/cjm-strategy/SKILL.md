---
node_type: card
kind: method
name: cjm-strategy
steps: [3]
prerequisites: [the step-1 journey map (cjm), strategy choices (where-to-play / how-to-win), channels]
reads: [register:hypotheses, register:risks, source:interview, source:research]
writes: [worklog, section:cjm, register:hypotheses, register:risks]
opinionated: false
method_basis: "Journey mapping as a revisit lens — re-walk the step-1 map against the chosen strategy and channels; touchpoints → product-surface; drop-offs → risks (step 3 births risks)"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.0
updated: 2026-08-16
---
# Customer Journey Map (strategy revisit)

**Re-walk the Step-1 journey against the chosen strategy** — the arena, the winning logic, and the
channels now decided — and update the map where they change it. A journey drawn at concept stage
assumed nothing about *how* the customer arrives or *what* they touch; once `where-to-play`,
`how-to-win`, and `channels-expansion` are chosen, the early stages (aware · evaluate) and the
touchpoints are no longer hypothetical. This skill updates the Step-1 `{#cjm}` section and feeds
the touchpoints to `product-surface`.

**Method basis.** The same journey-mapping frame as `cjm-concept` (stages · actions · touchpoints ·
thoughts/emotions · pains; emotional curve; moments that matter), applied as a **revisit lens**: the
map is not redrawn from scratch — it is walked once more with the strategy in hand, and every stage
is asked *does the chosen strategy change what happens here?*

> **Relation to neighbours (one mechanism, one way).**
> - **`cjm-concept` (Step 1)** drew the map; this skill *revises* it. One journey, one map, one
>   section — `{#cjm}` in the Step-1 artifact. There is no second CJM section at Step 3.
> - **`product-surface` (Step 3)** owns the static surface + instrumentation list. This skill's
>   touchpoint findings are its input — they land in `product-surface`'s worklog as a contribution,
>   not in a rival list here.
> - **Registers.** Step 3 births risks: a drop-off or dependency the strategy now walks into seeds
>   `R-…` here (unlike `cjm-concept`, which may only seed `H-…`). Triage and disposition of the
>   full risk set is `pre-mortem`'s job — seed the journey risks, don't run the pre-mortem here.

## When to apply
- **Step 3, after the strategy choices** — once `where-to-play-how-to-win` and
  `channels-expansion` have decided how the customer will actually arrive and be served, and before
  `product-surface` fixes the surfaces to build and instrument.
- When a chosen channel implies a journey the Step-1 map never drew (e.g. partner-led onboarding vs
  self-serve).

## Prerequisites
- **The Step-1 journey map** — the `{#cjm}` section and its worklog. *Missing → run `cjm-concept`
  first; there is nothing to revisit.*
- **Strategy choices** — the chosen arena and winning logic. *Missing → run
  `where-to-play-how-to-win`.*
- **Channels** — how this segment is reached. *Missing → run `channels-expansion`, or mark the
  aware/evaluate stages `[assumption]` and flag the gap.*

## How to do it
1. **Re-walk every stage with the strategy in hand.** For each stage of the Step-1 map ask: does
   the chosen arena, winning logic, or channel change what the customer does, touches, or feels
   here? Update the rows that change; leave the rest — and their confidence tags — alone.
2. **Redraw the arrival.** The aware/evaluate stages are where strategy bites hardest: the chosen
   channels replace the generic "they find us" with a concrete path. Name the touchpoints per
   chosen channel.
3. **Extract the touchpoint list for `product-surface`.** Every touchpoint the strategy now commits
   to owning is an input to the surface + instrumentation table. This lands in `product-surface`'s
   worklog (that section's primary owns it), referenced from here — not duplicated.
4. **Convert drop-offs and dependencies into risks.** A stage where the chosen journey can break —
   a drop-off the channel makes likely, a hand-off to a partner, a dependency on an integration —
   seeds `R-…` (Step 3 births risks). Check the register first; `pre-mortem` may already carry it —
   no duplicate `R-` for the same failure. New opportunities still seed `H-…`.
5. **Update the Step-1 section — and say what that costs.** Project the revised map back into the
   Step-1 artifact's `{#cjm}` section. **Re-projection drops the section's `confirmed:` marker**
   (`process/CONVENTIONS.md` → *Section confirmation*): the revised map is a new thesis the human
   has not signed — walk it back through confirmation rather than leaving a stale sign-off on a
   changed section.

## Anti-patterns
- **Redrawing from scratch.** Discarding the Step-1 evidence and re-imagining the journey — the
  revisit changes what the strategy changes, and keeps the sourced rows it doesn't.
- **A second map.** Writing a "strategic CJM" beside the concept one. One journey, one section;
  two maps drift within a quarter.
- **Touchpoints restated, not fed.** Building a touchpoint table here that rivals
  `product-surface` instead of feeding it.
- **Silent re-projection.** Updating the Step-1 section and leaving its old `confirmed:` marker
  standing — a signed-off thesis that no longer says what was signed.
- **Running the pre-mortem here.** Journey risks are seeded here; the ≥8 failure modes and the
  triage are `pre-mortem`'s method.

## Worklog & projection
This skill revises a section owned at Step 1, so its working **continues the map's one source of
truth**: `1-concept/cjm-concept.md` — the worklog of the `{#cjm}` section's primary tool
(`process/CONVENTIONS.md` → *Step folders & worklogs*; a second worklog for the same section would
be the drift the layer exists to stop). The revisit adds the strategy-informed pass — the stages
re-walked, what changed and why, the drop-offs converted to `R-…` — to that worklog with a dated
change-log entry, and re-projects `{#cjm}` from it via
[`template-fragment.md`](template-fragment.md). The touchpoint contribution to `{#product-surface}`
lands in `3-strategy/product-surface.md`, that section's primary worklog. External inputs arrive
dispatched from `sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Re-projects the Step-1 `{#cjm}` via [`template-fragment.md`](template-fragment.md) (the update drops
the section's `confirmed:` marker — it awaits re-confirmation); inputs via
[`questions.yaml`](questions.yaml). Touchpoints feed `{#product-surface}` through its worklog;
drop-offs/dependencies seed `R-…` (reconciled with `pre-mortem`), opportunities seed `H-…`.
