---
node_type: artifact-template
artifact: strategy
step: 3
title: "Strategy — <Product>"
status: template
version: 0.2.3
updated: 2026-07-21
---

<!--
  3-strategy.md assembly shell. Each section is filled by its recommended library tool
  (see steps/3-strategy/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md.
  This step is CHOICES (qualitative). Numbers, models, mitigations belong to Step 4.
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Strategy — <Product>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Last review: <date>
> Inputs: `1-concept.md` · `2-analysis.md`. Feeds: `4-strategic-plan.md`.

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see the repo's agent rules `AGENTS.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Winning aspiration {#winning-aspiration}
<!-- tool: where-to-play-how-to-win -->
_What winning looks like this horizon._

- …  [assumption]

## Where to play {#where-to-play}
<!-- tool: where-to-play-how-to-win -->
<!-- rests-on: 1#segments, 2#opportunity -->
_Segments / markets / arena chosen — and what's explicitly excluded._

| Chosen arena <!--c:arena--> | Why <!--c:why--> | Excluded (and why) <!--c:excluded--> | Confidence <!--c:conf--> |
|--------------|-----|--------------------|------------|
| … | … | … | [assumption] |

## How to win {#how-to-win}
<!-- tool: where-to-play-how-to-win, value-definition -->
_The winning logic + which moats we leverage._

- Winning logic: …  [assumption]
- Moats leveraged: …  [assumption]

## UVP & CPV {#uvp-cpv}
<!-- tool: uvp-cpv -->
_For [best-fit customer] who [job/pain], we [value] — unlike [alternative], because [why us]._

| Best-fit customer <!--c:customer--> | Job / pain <!--c:job--> | Value (outcome) <!--c:value--> | vs alternative <!--c:alt--> | Customer-perceived value <!--c:cpv--> | Confidence <!--c:conf--> |
|-------------------|------------|-----------------|----------------|--------------------------|------------|
| … | … | … | … | … | [assumption] |

## Pricing & Packaging {#pricing}
<!-- tool: pricing -->
_What we charge and how we package it — anchored to value vs the alternative. Quantified at Step 4._

- **Value metric:** … (what we meter on, and why it scales with value) [assumption]

| Tier <!--c:tier--> | For which segment <!--c:segment--> | Included <!--c:included--> | Fence (why they pick it) <!--c:fence--> | Price point <!--c:price--> | Model <!--c:model--> | Confidence <!--c:conf--> |
|------|-------------------|----------|--------------------------|-------------|-------|------------|
| good | … | … | … | … | subscription / usage / hybrid | [assumption] |
| better | … | … | … | … | … | [assumption] |
| best | … | … | … | … | … | [assumption] |

## Channels & expansion {#channels-expansion}
<!-- tool: channels-expansion -->
_Acquisition/comms channels (Bullseye) + expansion paths._

| Channel <!--c:channel--> | Stage (traction / scale) <!--c:stage--> | Why it fits the segment <!--c:fit--> | Confidence <!--c:conf--> |
|---------|--------------------------|-------------------------|------------|
| … | … | … | [assumption] |

- Expansion path: …  [assumption]

## Product surface {#product-surface}
<!-- tool: product-surface -->
_Every user-interaction surface + instrumentation (sketched here, refined at Step 4)._

| Surface <!--c:surface--> | Purpose <!--c:purpose--> | Instrumentation (what/where data comes from) <!--c:instrumentation--> | Confidence <!--c:conf--> |
|---------|---------|----------------------------------------------|------------|
| … | … | … | [assumption] |

## Architecture {#architecture}
<!-- tool: architecture-c4 -->
_System architecture at C4 **Context** level (product, its users, external systems). Refined at Step 4._

- Context sketch: …  (product · users · external systems)  [assumption]

## Bets {#bets}
<!-- tool: jtbd, value-definition -->
_The strategic hypotheses we're wagering on (framed on the customer's job + forces)._

| ID <!--c:id--> | Bet <!--c:bet--> | Type <!--c:type--> | Job / circumstance <!--c:job--> | Why it wins (pull > anxiety + habit) <!--c:whywins--> | Outcome it moves <!--c:outcome--> | Confidence <!--c:conf--> |
|----|-----|------|--------------------|--------------------------------------|------------------|------------|
| H-… | … | desirability / viability / … | … | … | … | [assumption] |

## Product risks {#product-risks}
<!-- tool: risk-mitigation -->
_Risks specific to this strategy (mitigations owned at Step 4)._

| ID <!--c:id--> | Risk <!--c:risk--> | Category <!--c:category--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | Confidence <!--c:conf--> |
|----|------|----------|------------|--------|------------|
| R-… | … | market / product / execution / … | H/M/L | H/M/L | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced for the human to resolve._

- …

## Change log

### <date> — created
- **From → To:** — → initial strategy draft
- **Why:** …
- **Trigger:** …
