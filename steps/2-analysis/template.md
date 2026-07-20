---
node_type: artifact-template
artifact: analysis
step: 2
title: "Market & Competitive Analysis — <Product>"
status: template
version: 0.2.1
updated: 2026-07-21
---

<!--
  analysis.md assembly shell. Each section is filled by its recommended library tool
  (see steps/2-analysis/README.md). Keep section IDs stable. Follow process/CONVENTIONS.md
  for confidence tags, sources, IDs, links, and the change log.
  The point of this step is the CONCLUSION (#opportunity) — analysis without a "so what" is inert.
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Market & Competitive Analysis — <Product>

> Status: <concept-viability | pmf | growth> · Owner: <name> · Last review: <date>
> Feeds: [[strategy]] · seeds the risk register.

> ⚠️ **Fill each section through its method — not from this shell.** Every `{#section}` names its
> library method in a `<!-- tool: … -->` note: open that method's `SKILL.md` under
> `tool-skills/library/`, check its prerequisites, clarify real forks as options, then fill. Filling
> straight from this template bypasses the method (see `CLAUDE.md` → "Read the tool before filling").
> The shell is for structure and stable IDs only.

## Market sizing {#market-sizing}
<!-- tool: market-sizing -->
_TAM / SAM / SOM with an explicit method and named assumptions (bottom-up preferred)._

| Layer | Value | Method | Key assumptions | Source | Confidence |
|-------|-------|--------|-----------------|--------|------------|
| TAM | … | bottom-up / top-down | … | … | [assumption] |
| SAM | … | … | … | … | [assumption] |
| SOM | … | … | … | … | [assumption] |

## Competitors {#competitors}
<!-- tool: competitor-analysis -->
_Direct & indirect competitors (substitutes are separate, below)._

| Competitor | Direct/Indirect | What they offer | Confidence |
|------------|-----------------|-----------------|------------|
| … | direct | … | [sourced: …] |

## Competitor strategy {#competitor-strategy}
<!-- tool: competitor-analysis -->
_What game each plays (revenue / profit / share / social capital — and how), vs our moats._

| Competitor | Game | How they play it | Their moats vs ours | Confidence |
|------------|------|------------------|---------------------|------------|
| … | … | … | … | [assumption] |

## Competitor pricing {#competitor-pricing}
<!-- tool: competitor-analysis -->
_Input to our own pricing (Step 3 `pricing`) and the financial model — not our price._

| Competitor | Plan / model | Price | Source | Confidence |
|------------|--------------|-------|--------|------------|
| … | … | … | site / search | [sourced: …] |

## Competitor dynamics {#competitor-dynamics}
<!-- tool: competitor-analysis -->
_Trend over time — to compare whose strategy is working. Source per firm: public financials / press
/ filings (for RU legal entities, datanewton.ru/contragents/<OGRN>)._

| Competitor | Metric (revenue / headcount / …) | Trend + period | Source (+ date) | Confidence |
|------------|----------------------------------|----------------|-----------------|------------|
| … | revenue | … | public financials / press (RU: datanewton OGRN) | [sourced: …] |

## Substitutes {#substitutes}
<!-- tool: substitutes -->
_Non-obvious competition incl. "do nothing / do it manually / self-build"._

| Substitute | How it does the job today | Why a customer would stay with it | Confidence |
|------------|---------------------------|-----------------------------------|------------|
| do-nothing | … | … | [assumption] |

## Niche risks {#niche-risks}
<!-- synthesis: light Five Forces -->
_Structural risks of the niche (light Five Forces): supplier/buyer power, entry barriers, rivalry, substitution._

| Risk | Force | Likelihood | Impact | → `R-…` | Confidence |
|------|-------|------------|--------|---------|------------|
| … | rivalry / substitution / … | H/M/L | H/M/L | R-… | [assumption] |

## Opportunity {#opportunity}
<!-- synthesis -->
_The "so what" — where the white space or the threat is. This is the point of the step._

- Opportunity / threat: …  [assumption]
- Why now: …

## Seeded hypotheses {#hypotheses}
_Market/sizing assumptions carried into the hypothesis register._

| ID | Hypothesis | Type | From section | Confidence |
|----|------------|------|--------------|------------|
| H-… | … | viability | market-sizing | [assumption] |

## To clarify {#to-clarify}
_Open items surfaced by the agent for the human to resolve._

- …

## Change log

### <date> — created
- **From → To:** — → initial analysis draft
- **Why:** …
- **Trigger:** …
