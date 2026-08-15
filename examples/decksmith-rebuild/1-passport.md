---
node_type: artifact
artifact: passport
step: 1
title: "Product Passport — Decksmith (fictional sample)"
status: draft
version: 0.1.0
updated: 2026-08-14
---

# Product Passport — Decksmith (fictional sample)

> Status: concept-viability · Owner: — · Last review: 2026-08-14
>
> Projection of the Step-1 worklogs in `1-idea/`. No section carries a `confirmed:` marker: this rebuild was
> walked by the agent with no human present to sign off, and `theses` never self-issues confirmation.

## Concept {#concept}
<!-- tool: concept-formation -->
_What it is, and the shift it makes._

- **Decksmith is an AI deck generator that outputs native, fully-editable `.pptx`/`.key` files that also look
  designed** — real shapes, text and layouts you edit like your own, not images or a locked template.
  [sourced: founder brief]
- **The shift:** from "pick *pretty-but-locked* **or** *editable-but-ugly*" → **editable AND designed** — AI
  speed without the hand-rebuild tax. [sourced: founder brief]
- **Riskiest assumption:** the engine can *reliably* produce editable-and-designed files **at scale**, not one
  hand-tuned demo. [assumption] → `H-001`

## Job-to-be-Done {#jtbd}
<!-- tool: jtbd -->
_The job, the four switching forces, the outcomes success is judged by._

**Job statement.** _When_ I must produce a client-facing deck under time pressure, _I want to_ get a first
draft that is already on-brand and well-designed *and* that I can finish in my own slide tool, _so that_ I
deliver something client-ready without rebuilding it from scratch. [assumption]

| Force | Direction | For this job | Confidence |
|-------|-----------|--------------|------------|
| Push | away from status quo | AI output "looks templated" / wrong structure → hand-rebuild → tool saves less time than promised | [sourced: founder brief] |
| Pull | toward this product | native-editable *and* designed = AI speed kept, rebuild tax gone | [sourced: founder brief] |
| Anxiety | resists switching | "will it really be editable in my tool? will the design hold? trust for client work" | [assumption] |
| Habit / inertia | resists leaving status quo | start from a past deck / company template / hand to a designer | [assumption] |

**Desired outcomes:** minimize time-to-client-ready · minimize rework after generation · maximize
"looks designed / on-brand" · maximize editability in the native tool. [assumption; last one sourced]

## Segments {#segments}
<!-- tool: segmentation -->
_Who it's for and how segments are cut (use-context × stakes/frequency; org-default "company size" cut
rejected — see worklog)._

| Priority | Segment | How it's cut | Why it matters | Where to reach them | Confidence |
|----------|---------|--------------|----------------|---------------------|------------|
| 1 (lead) | Salespeople & marketers making client-facing decks | use-context × stakes/frequency | recurring high-stakes decks; design *and* editability both bite; company budget | LinkedIn, sales/marketing & RevOps communities | [assumption] |
| 2 | Founders / consultants making pitch & client decks | same cut | highest design stakes, lower frequency, individual buyer | founder/accelerator & consulting networks | [assumption] |
| 3 | Internal / corporate deck-makers (PMs, analysts, ops) | same cut | high frequency, lower design stakes, editability still required | inside companies (seat expansion) | [assumption] |

_Evidence basis: founder desk-observation only — the weakest of the three evidence kinds; not validated._

## Problems {#problems}
<!-- tool: segment-pains -->
_Lead segment's problems, severity × frequency; editability fixed as table-stakes, look & structure as the
differentiators. Top-3 carried forward; full ranking in the worklog._

| Problem | Severity | Frequency | Class | Confidence |
|---------|----------|-----------|-------|------------|
| Looks templated → hand-redesign before it's client-safe | H | H | differentiator | [sourced: founder brief] |
| Wrong structure/story for the audience | H | M | differentiator | [sourced: founder brief] |
| Locked/image output can't be edited | H | H | table-stakes | [sourced: founder brief] |
| Rebuilding eats the promised time saving | H | H | differentiator | [sourced: founder brief] |
| Off-brand (fonts/colors vs company brand) | M | H | table-stakes | [assumption] |

## Customer Journey {#cjm}
_Optional lens — **omitted** at concept stage. The flat pain list above is sufficient; there is no unexplained
drop-off to map (no product in market). Revisit if a specific stage-level breakage needs explaining._

## Solution {#solution}
<!-- tool: concept-formation -->
_How the product solves each carried-forward problem. No orphan features._

| Problem | How the product solves it | Confidence |
|---------|---------------------------|------------|
| Looks templated | design layer: layout/spacing/type rules learned from a curated corpus → output looks designed | [assumption] |
| Wrong structure/story | audience-aware outline/story shaping, not a generic dump | [assumption] |
| Locked/image output | native renderer emits real slide objects (not images) → editable in the user's own tool | [assumption] |

## Value & Defensibility {#value-defensibility}
<!-- tool: value-definition -->
_Post-AI lens (software isn't the moat, position is). The moat here is honestly thin._

- **Base values (what we have/can build):** design taste + design-community brand (most durable, but small &
  person-dependent); a native-editable rendering pipeline (execution edge — buys lead time, not a wall); a
  curated design corpus (a moat *only if* genuinely proprietary + hard to assemble). [assumption]
- **Killed by the post-AI test:** "the AI generation itself" — any LLM does it. Kept on the record so it isn't
  re-proposed as a moat next quarter.
- **Intended moat(s):** execution speed + design taste/brand now; a *conditional* data moat if the corpus is
  real. [assumption] → `H-005` (tags: moat)
- **Derivatives:** deferred to Step 3 — distribution via the design community, and brand-kit/template lock-in
  once customers save brand systems. Not claimed at concept stage (no customers/scale).

## Seeded hypotheses {#hypotheses}
_Everything above starts as an assumption. Carried into the hypothesis register (`registers/hypotheses.md`)._

| ID | Hypothesis | Type | From section | Confidence |
|----|------------|------|--------------|------------|
| H-001 | The engine reliably produces editable-AND-designed files at scale | feasibility | concept | [assumption] |
| H-002 | Salespeople/marketers feel "looks templated / rebuild tax" strongly enough to switch | desirability | problems | [assumption] |
| H-003 | The wrong-structure pain is real and valued | desirability | problems | [assumption] |
| H-004 | Editability is a hard gate (locked output is a non-starter) | desirability | problems | [assumption] |
| H-005 | Design corpus + taste is a defensible-enough edge | viability | value-defensibility | [assumption] |
| H-006 | Users can finish the generated deck in their native tool without a rebuild | usability | jtbd | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced for the human._

- **Willingness-to-pay / buyer** — deferred to Step 3 by the founder; do not invent a price. [founder decision]
- **Demand signal for the lead segment** — no interviews/analytics yet; needed to move `H-002`/`H-003` off
  `[assumption]`. Source: discovery interviews + analytics search.
- **Feasibility evidence** — no prototype quality eval yet; needed for `H-001`. Source: a prototype slice +
  design eval.

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → initial passport projected from the Step-1 worklogs (`1-idea/`).
- **Why:** capture the concept, job, segments, pains, solution and value/moat as the long-lived source of truth.
- **Trigger:** rebuild-from-brief walkthrough. Sources: `sources/founder-brief.md`.
