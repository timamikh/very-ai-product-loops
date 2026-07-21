---
node_type: artifact-template
artifact: passport
step: 1
title: "Product Passport — <Product>"
status: template
version: 0.3.2
updated: 2026-07-21
---

<!--
  Passport assembly shell. Each section is filled by its recommended library tool
  (see steps/1-idea/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md
  for confidence tags, sources, IDs, links, and the change log.
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Product Passport — <Product>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Last review: <date>

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see `CLAUDE.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Concept {#concept}
<!-- tool: concept-formation -->
_What it is, and the shift it makes, in a few lines._

- …  [assumption]

## Job-to-be-Done {#jtbd}
<!-- tool: jtbd (lens — anchors #segments and #problems; the job feeds Step 2 substitutes) -->
_The job the customer hires the product for, the four forces around switching, and the outcomes
they judge success by. States the job; the pains inside it are scored in #problems._

**Job statement.** _When_ <circumstance>, _I want to_ <make this progress>, _so that_ <outcome>.  [assumption]

| Force | Direction | For this job | Confidence |
|-------|-----------|--------------|------------|
| Push | away from status quo | … | [assumption] |
| Pull | toward this product | … | [assumption] |
| Anxiety | resists switching | … | [assumption] |
| Habit / inertia | resists leaving status quo | … | [assumption] |

## Segments {#segments}
<!-- tool: segmentation -->
_Who it's for and how segments are cut._

| Priority | Segment | How it's cut | Why it matters | Where to reach them | Confidence |
|----------|---------|--------------|----------------|---------------------|------------|
| 1 (lead) | … | … | … | … | [assumption] |

## Problems {#problems}
<!-- tool: segment-pains -->
_Each segment's problems, scored by severity × frequency._

| Problem | Severity | Frequency | Class | Confidence |
|---------|----------|-----------|-------|------------|
| … | H/M/L | H/M/L | differentiator / table-stakes | [assumption] |

## Customer Journey {#cjm}
<!-- tool: cjm (optional lens — the temporal view behind #problems; fill when a drop-off needs explaining) -->
_Optional. One segment's end-to-end journey doing the job over time — the stages and where it
breaks. Fill when a flat pain list isn't enough (e.g. an unexplained drop-off). Its pains feed
`#problems`; its touchpoints feed Step-3 `#product-surface`. Omit it if not needed — it is not a
required passport section._

| Stage | Actions | Touchpoints | Thoughts / emotions | Pains | Emotion (▲/▼) | Confidence |
|-------|---------|-------------|---------------------|-------|---------------|------------|
| … | … | … | … | … | ▼ | [assumption] |

## Solution {#solution}
<!-- tool: concept-formation -->
_How the product solves each problem above. No orphan features._

| Problem | How the product solves it | Confidence |
|---------|---------------------------|------------|
| … | … | [assumption] |

## Value & Defensibility {#value-defensibility}
<!-- tool: value-definition -->
_The value and the moat(s). See the tool for the base/derivative taxonomy._

- Intended moat(s): …  [assumption]
- Why it holds post-AI: …

## Seeded hypotheses {#hypotheses}
_Everything above starts as an assumption. List the ones to carry into the hypothesis register._

| ID | Hypothesis | Type | From section | Confidence |
|----|------------|------|--------------|------------|
| H-001 | … | desirability / feasibility / viability / usability | segments | [assumption] |

## To clarify {#to-clarify}
_Open items surfaced by the agent for the human to resolve._

- …

## Change log

### <date> — created
- **From → To:** — → initial passport draft
- **Why:** …
- **Trigger:** …
