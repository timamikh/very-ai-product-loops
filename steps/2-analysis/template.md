---
node_type: artifact-template
artifact: analysis
step: 2
title: "Market & Competitive Analysis — <Product>"
status: template
version: 0.4.0
updated: 2026-08-16
---

<!--
  2-analysis.md assembly shell. Each section is filled by its recommended library tool
  (see steps/2-analysis/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md
  for confidence tags, sources, IDs, links, and the change log.
  The point of this step is the CONCLUSION (#opportunity) — analysis without a "so what" is inert.
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Market & Competitive Analysis — <Product>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Last review: <date>
> Feeds: `3-strategy.md` · seeds the risk register.

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see the repo's agent rules `AGENTS.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Market sizing {#market-sizing}
<!-- tool: market-sizing -->
<!-- rests-on: 1#segments -->
_TAM / SAM / SOM with an explicit method and named assumptions (bottom-up preferred).
First pass: the price input is an `[assumption]` from Step-1 value work; once `#competitor-pricing`
is filled, revisit the sizing with the observed anchor._

| Layer <!--c:layer--> | Value <!--c:value--> | Method <!--c:method--> | Key assumptions <!--c:assumptions--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|-------|-------|--------|-----------------|--------|------------|
| TAM | … | bottom-up / top-down | … | … | [assumption] |
| SAM | … | … | … | … | [assumption] |
| SOM | … | … | … | … | [assumption] |

## Competitors {#competitors}
<!-- tool: competitor-analysis -->
<!-- rests-on: 1#segments, 1#jtbd -->
_Direct & indirect competitors (substitutes are separate, below)._

| Competitor <!--c:name--> | Direct/Indirect <!--c:type--> | What they offer <!--c:offer--> | Confidence <!--c:conf--> |
|------------|-----------------|-----------------|------------|
| … | direct | … | [sourced: …] |

## Competitor strategy {#competitor-strategy}
<!-- tool: competitor-analysis -->
<!-- rests-on: 1#value-defensibility -->
_What game each plays (revenue / profit / share / social capital — and how), vs our moats._

| Competitor <!--c:name--> | Game <!--c:game--> | How they play it <!--c:play--> | Their moats vs ours <!--c:moat--> | Confidence <!--c:conf--> |
|------------|------|------------------|---------------------|------------|
| … | … | … | … | [assumption] |

## Competitor pricing {#competitor-pricing}
<!-- tool: competitor-pricing -->
_Input to our own pricing (Step 3 `pricing-strategy`), `#market-sizing`'s price anchor, and the
financial model — not our price. Every price carries the date it was read._

| Competitor <!--c:name--> | Plan / model <!--c:plan--> | Price (+ read date) <!--c:price--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|------------|--------------|-------|--------|------------|
| … | … | … | site / search | [sourced: …] |

## Competitor dynamics {#competitor-dynamics}
<!-- tool: competitor-dynamics -->
_Trend over time — to compare whose strategy is working. Source per firm: public financials / press
/ filings / public company registries appropriate to the jurisdiction. (Region-specific registry
lookups are a regional/company adapter concern, not the base.)_

| Competitor <!--c:name--> | Metric (revenue / headcount / …) <!--c:metric--> | Trend + period <!--c:trend--> | Source (+ date) <!--c:source--> | Confidence <!--c:conf--> |
|------------|----------------------------------|----------------|-----------------|------------|
| … | revenue | … | public financials / registry | [sourced: …] |

## Substitutes {#substitutes}
<!-- tool: substitutes -->
<!-- rests-on: 1#jtbd -->
_Non-obvious competition incl. "do nothing / do it manually / self-build"._

| Substitute <!--c:substitute--> | How it does the job today <!--c:job--> | Why a customer would stay with it <!--c:why--> | Confidence <!--c:conf--> |
|------------|---------------------------|-----------------------------------|------------|
| do-nothing | … | … | [assumption] |

## Niche risks {#niche-risks}
<!-- synthesis: light Five Forces -->
_Structural risks of the niche (light Five Forces): supplier/buyer power, entry barriers, rivalry, substitution._

| Risk <!--c:risk--> | Force <!--c:force--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | → `R-…` <!--c:register--> | Confidence <!--c:conf--> |
|------|-------|------------|--------|---------|------------|
| … | rivalry / substitution / … | H/M/L | H/M/L | R-… | [assumption] |

## Opportunity {#opportunity}
<!-- synthesis -->
_The "so what" — where the white space or the threat is. This is the point of the step._

- Opportunity / threat: …  [assumption]
- Why now: …

## Seeded hypotheses {#hypotheses}
_Market/sizing assumptions carried into the hypothesis register._

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | From section <!--c:from--> | Confidence <!--c:conf--> |
|----|------------|------|--------------|------------|
| H-… | … | viability | market-sizing | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced by the agent for the human to resolve._

- … — *the human chooses* · *nobody knows yet* · *a later step owns it* (name the step):
  keep exactly one (`process/CONVENTIONS.md` → the `open` bullet)

## Change log

### <date> — created
- **From → To:** — → initial analysis draft
- **Why:** …
- **Trigger:** …
