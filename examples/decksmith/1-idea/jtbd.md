---
node_type: worklog
tool: jtbd
step: 1
title: "Jobs-to-be-Done — the working"
updated: 2026-08-14
version: 0.1.0
---

# Jobs-to-be-Done — the working

_Source of truth for `1-idea.md#jtbd`; that section is the projection of this file._
_Method: `tool-skills/library/jtbd`. Single input: `../sources/founder-brief.md` (read 2026-08-14)._
_Lead segment (given, do not re-derive): salespeople & marketers who make client-facing decks
`[sourced: founder brief]`. Concept (given): an AI deck generator that outputs native, fully-editable
`.pptx`/`.key` that also look designed `[sourced: founder brief]`._
_This job is the frame Step 2 `substitutes` scores indirect competition against._

## Job statement

⚙️ **When** I have to produce a client-facing deck (pitch / proposal) for a specific audience on a
deadline, **I want to** get a deck that already looks professionally designed *and* carries the right
structure/story for that audience — and that I can still edit natively like my own file — **so that** I
can present credibly and move the deal forward without burning hours rebuilding it by hand.

- The middle clause is *progress*, not a feature: "a credible, on-brand, audience-fit deck fast, without
  redoing it by hand." The circumstance (a specific client meeting, on a deadline) is what makes it a
  job and not a persona.
- The job has **two halves** the founder names together: it must **look designed** *and* have the
  **right story/structure** for the audience. Both are load-bearing. `[sourced: founder brief]`
- Circumstance / trigger and the deadline framing are ⚙️ my reasoning `[assumption]`; the brief states
  the crowd and the two-halves progress, not the exact trigger.

## The four forces (switch from the current way → this product)

Read for the switch **from** today's way (hand-built decks, or AI output the user then hand-rebuilds)
**to** this generator. Progress happens only when **push + pull > anxiety + habit**.

| Force | Direction | For this job | Confidence |
|-------|-----------|--------------|------------|
| **Push** | away from status quo | Today's AI slide tools force a bad choice — **pretty-but-locked** (images / rigid template you can't really edit) or **editable-but-ugly** (plain text in default PowerPoint styling). Output "looks templated" and comes back with the **wrong structure/story** for the audience, so the user hand-rebuilds it — the tool saves less time than promised. | [sourced: founder brief] |
| **Pull** | toward the new solution | One tool that removes the trade-off: **native, fully-editable** `.pptx`/`.key` (real shapes, text, layouts) that **also looks designed**. Editable AND designed, in the format they already present from. | [sourced: founder brief] |
| **Anxiety** | resists the new solution | "Will it *actually* be both genuinely editable and genuinely well-designed this time — and get the story right for *my* audience — or will I end up redoing it by hand again?" Trust that output quality holds at scale. ⚙️ inferred from the observed rebuild behaviour + the founder's own "quality-at-scale is unproven" inventory; the brief does not quote customer fears directly. | [assumption] |
| **Habit / inertia** | resists leaving the status quo | An established, controllable workflow already exists — build it by hand in PowerPoint / Keynote / Canva, lean on company templates & brand kits, or prompt a general LLM and format it themselves. Because editability is table-stakes, the manual path feels safe and fully in their control. | [assumption] |

### Which force gates adoption

⚙️ **Anxiety is the adoption-killer** — specifically *distrust that the output will be good enough
(designed + right story) that I won't have to redo it.* The segment is **not** blocked by habit from
*trying* AI tools: the founder observed they already do try, then rebuild by hand. So the barrier is not
"they won't touch it" — it's "they touched it, got burned, and now expect to be burned again." Every
hand-rebuild is a data point *against* the promise. The pull ("designed AND editable") only converts if
this anxiety is beaten, and the anxiety is well-founded because the engine's quality-at-scale is itself
unproven (the founder's own stated riskiest thing is feasibility). Push and pull are already strong and
sourced; the switch turns on retiring the trust gap. `[assumption]` (reasoning), resting on
`[sourced: founder brief]` push/pull observations.

## Desired outcomes (ODI)

Measurable directions the segment judges success by (these are what `segment-pains` later scores and
what metrics later track — stated as directions, not features):

- **Minimize** the time from AI draft to presentation-ready deck (i.e. minimize hand-rebuild / rework
  time — the founder's core "saves less time than promised" complaint). `[sourced: founder brief]`
- **Minimize** the number of slides that must be manually re-designed after generation. `[assumption]`
- **Maximize** the likelihood the structure/story fits the specific audience without restructuring.
  `[sourced: founder brief]` (the "wrong structure/story" complaint)
- **Maximize** the likelihood the deck reads as *designed*, not templated, to the client. `[sourced: founder brief]`
- **Maximize** native editability of the output — editable like their own file, minimal locked elements
  (table-stakes; locked/image output is a non-starter). `[sourced: founder brief]`
- **Increase** the likelihood of winning / advancing the client meeting the deck is for (the ultimate
  motivation behind the job). `[assumption]`

## Implied beliefs for the orchestrator to mint as hypotheses (no ids allocated here)

Per the write rule I describe these in words; the orchestrator mints the `H-…` ids and `type`.

1. **Desirability — the job itself.** This segment truly hires for "designed AND editable, with the
   right audience story, without hand-rebuild" — i.e. both halves matter together, not just visuals.
   `[sourced: founder brief]` for the observation; unproven as a *job* claim.
2. **Desirability — push strength.** Hand-rebuilding AI deck output is a widespread, painful, frequent
   behaviour in this segment (not a one-off gripe). `[sourced: founder brief]`, single-observer.
3. **Desirability — the gating force.** Anxiety (distrust that output is good enough to not redo) is the
   force that gates adoption, above habit and above the pull's strength. `[assumption]`
4. **Desirability — story weight.** The "wrong structure/story" half of the job is at least as
   important to buyers as the "looks templated" half. `[sourced: founder brief]`, needs ranking (that
   ranking is `segment-pains`' job, not this one).

## Open forks — for the human, not decided here

- **Which half of the job leads the positioning?** The brief names two halves — *look designed* and
  *right story/structure*. They imply different products and different proof.
  - (a) **Design-led** — "AI decks that finally look designed *and* stay editable." Trades on the
    visual pain that's most visible; risk: the story/structure gap becomes an unmet expectation.
  - (b) **Story-led** — "AI decks with the right structure for your audience, natively editable."
    Trades on the deeper complaint; risk: harder to demo, and "looks templated" still sinks first
    impressions.
  - (c) **Both-as-one** — "editable, designed, and audience-right — no rebuild." Truest to the brief;
    risk: a broad promise that's harder to prove and raises the anxiety bar.
  - ⚙️ **Recommendation:** (c) as the job frame, because the founder states both halves as the point of
    the concept; treat design-led (a) as the likely *wedge* for first demos. This is a positioning
    call the human owns — surfaced, not closed.

## Change log

### 2026-08-14 — created
- **From → To:** — → first JTBD working for the lead segment, drafted from `../sources/founder-brief.md`.
- **Why:** stand up `1-idea.md#jtbd` — the job frame that anchors segments/problems and feeds Step 2
  `substitutes`.
- **Trigger:** draft brief (rebuild examples/decksmith).
