---
node_type: artifact-template
artifact: concept
step: 1
title: "Product Concept — <Product>"
status: template
version: 0.8.1
updated: 2026-08-19
---

<!--
  Concept assembly shell. Each section is filled by its recommended library tool
  (see steps/1-concept/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md
  for confidence tags, sources, IDs, links, and the change log.
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Product Concept — <Product>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Last review: <date>

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see the repo's agent rules `AGENTS.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Idea {#idea}
<!-- tool: concept-formation -->
_What it is, and the shift it makes, in a few lines._

- …  [assumption]

## Job-to-be-Done {#jtbd}
<!-- tool: jtbd-concept -->
_The job the customer hires the product for, the four forces around switching, and the outcomes
they judge success by. A lens that anchors `#segments` and `#problems`; the job feeds Step 2
`substitutes`. States the job; the pains inside it are scored in #problems.
First iteration: frame the job for the customer named in `#idea`; once `#segments` ranks a tier-1
segment, re-read the job for it._

**Job statement.** _When_ <circumstance>, _I want to_ <make this progress>, _so that_ <outcome>.  [assumption]

| Force <!--c:force--> | Direction <!--c:dir--> | For this job <!--c:forjob--> | Confidence <!--c:conf--> |
|-------|-----------|--------------|------------|
| Push | away from status quo | … | [assumption] |
| Pull | toward this product | … | [assumption] |
| Anxiety | resists switching | … | [assumption] |
| Habit / inertia | resists leaving status quo | … | [assumption] |

## Segments {#segments}
<!-- tool: segmentation -->
_Who it's for and how segments are cut._

| Priority <!--c:priority--> | Segment <!--c:segment--> | How it's cut <!--c:cut--> | Buyer / user <!--c:buyer--> | Why it matters <!--c:why--> | Where to reach them <!--c:reach--> | Confidence <!--c:conf--> |
|----------|---------|--------------|--------------|----------------|---------------------|------------|
| 1 (lead) | … | … | same / <buyer> vs <user> | … | … | [assumption] |

## Problems {#problems}
<!-- tool: segment-pains -->
_Each segment's problems, scored by severity × frequency._

| Problem <!--c:problem--> | Severity <!--c:severity--> | Frequency <!--c:frequency--> | Cost of inaction <!--c:inaction--> | Class <!--c:class--> | Confidence <!--c:conf--> |
|---------|----------|-----------|------------------|-------|------------|
| … | H/M/L | H/M/L | nice-to-have / recurring irritation / already paying or improvising | differentiator / table-stakes | [assumption] |

<!-- enum:c:severity: H | M | L -->
<!-- enum:c:frequency: H | M | L -->
<!-- enum:c:inaction: nice-to-have | recurring irritation | already paying or improvising -->
<!-- enum:c:class: differentiator | table-stakes -->

## Customer Journey {#cjm}
<!-- tool: cjm-concept, cjm-strategy -->
_Optional lens — the temporal view behind `#problems`; fill when the journey's time structure
matters to the concept (a long multi-actor path, pains living at different stages). One segment's
end-to-end journey doing the job over time — the stages and where it breaks; an assumption-tagged
map is a legal first pass, and the breakage points it finds seed `H-…` for the sprint's interviews
to test. Its pains feed `#problems`; its touchpoints feed Step-3 `#product-surface`. Skipping is a
statement about the concept, never about a source the instance lacks — it is not a required
concept section._

| Stage <!--c:stage--> | Actions <!--c:actions--> | Touchpoints <!--c:touchpoints--> | Thoughts / emotions <!--c:thoughts--> | Pains <!--c:pains--> | Emotion (▲/▼) <!--c:emotion--> | Confidence <!--c:conf--> |
|-------|---------|-------------|---------------------|-------|---------------|------------|
| … | … | … | … | … | ▼ | [assumption] |

## Solution {#solution}
<!-- tool: concept-expansion -->
_How the product solves each problem above. No orphan features._

| Problem <!--c:problem--> | How the product solves it <!--c:solution--> | Confidence <!--c:conf--> |
|---------|---------------------------|------------|
| … | … | [assumption] |

## Value & Defensibility {#value-defensibility}
<!-- tool: value-definition-concept -->
_The value and the moat(s). See the tool for the base/derivative taxonomy._

- Intended moat(s): …  [assumption]
- Why it holds post-AI: …

## Seeded hypotheses {#hypotheses}
_Everything above starts as an assumption. List the ones to carry into the hypothesis register._

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | From section <!--c:from--> | Confidence <!--c:conf--> |
|----|------------|------|--------------|------------|
| H-001 | … | desirability / feasibility / viability / usability | segments | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced by the agent for the human to resolve._

- … — *the human chooses* · *nobody knows yet* · *a later step owns it* (name the step):
  keep exactly one (`process/CONVENTIONS.md` → the `open` bullet)

## Change log

### <date> — created
- **From → To:** — → initial concept draft
- **Why:** …
- **Trigger:** …
