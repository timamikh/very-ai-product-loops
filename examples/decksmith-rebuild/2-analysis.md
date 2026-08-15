---
node_type: artifact
artifact: analysis
step: 2
title: "Market & Competitive Analysis — Decksmith (fictional sample)"
status: draft
version: 0.1.0
updated: 2026-08-14
---

# Market & Competitive Analysis — Decksmith (fictional sample)

> Status: concept-viability · Owner: — · Last review: 2026-08-14
> Feeds: `3-strategy.md` · seeds the risk register.
> Projection of the `2-analysis/` worklogs. No section is confirmed (autonomous walk, no human sign-off).

## Market sizing {#market-sizing}
<!-- tool: market-sizing -->
_Bottom-up SAM is the answer; top-down is a cross-check. Published AI-segment figures diverge 2–3× — not averaged._

| Layer <!--c:layer--> | Value <!--c:value--> | Method <!--c:method--> | Key assumptions <!--c:assumptions--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|-------|-------|--------|-----------------|--------|------------|
| TAM | ~$2–3B (2025) → ~$4–5B (2026), CAGR ~23–26% | top-down, wide error bars | whole AI deck-generation market, global; figures **[CONFLICT]** across reports | market-research | [sourced] range |
| SAM | ~$390M/yr (range $300–500M) | **bottom-up** (1.8M reachable payers × ~$216/yr), cross-checked top-down (~$360–450M) — agree within ~20% | 15M NA+EU sales/marketing deck-makers × ~12% standalone-paying adoption | market-research | [assumption] |
| SOM | ~$4–12M ARR (~1–3% of SAM, ~3-yr) | share obtainable vs incumbents | crowded; incumbents bundle + own distribution; standalone-slides is hard (Tome exited) | derived | [assumption] |

## Competitors {#competitors}
<!-- tool: competitor-analysis -->
_Direct & indirect (substitutes are separate, below). All surfaced by the sweep — the founder brief named none._

| Competitor <!--c:name--> | Direct/Indirect <!--c:type--> | What they offer <!--c:offer--> | Confidence <!--c:conf--> |
|------------|-----------------|-----------------|------------|
| Gamma | direct | web-first AI deck generator; category leader | [sourced: market-research] |
| Microsoft Copilot in PowerPoint | direct | agentic AI that edits native PPT in place; owns the format | [sourced: market-research] |
| Canva (AI 2.0) | direct | conversational AI building fully-editable design objects | [sourced: market-research] |
| Beautiful.ai | direct | template/rule-driven design-automation deck tool | [sourced: market-research] |
| Pitch | indirect | collaboration-first deck tool, team-oriented | [sourced: market-research] |
| Tome | excluded | **shut its Slides product Apr 2025** — a signal, not a rival | [sourced: market-research] |

## Competitor strategy {#competitor-strategy}
<!-- tool: competitor-analysis -->
_What game each plays vs our moats (execution speed on the fidelity engine + design taste — thin vs distribution)._

| Competitor <!--c:name--> | Game <!--c:game--> | How they play it <!--c:play--> | Their moats vs ours <!--c:moat--> | Confidence <!--c:conf--> |
|------------|------|------------------|---------------------|------------|
| Gamma | share + rare profit | web-first speed, viral PLG | distribution + brand; **weak on native-editable export ← our wedge** | [sourced: market-research] |
| Copilot | revenue via bundle | edit-in-place inside native PPT | **owns PowerPoint + M365 distribution — biggest threat** | [sourced: market-research] |
| Canva | share / ecosystem | conversational editable objects | 100M+ distribution; closing the "editable" wedge | [sourced: market-research] |
| Beautiful.ai | niche revenue | rule-driven design automation | design rules; less AI-native, smaller | [sourced: market-research] |
| Pitch | team revenue | collaboration workflow | team lock-in; not a fidelity play | [sourced: market-research] |

## Competitor pricing {#competitor-pricing}
<!-- tool: competitor-analysis -->
_Input to Step-3 pricing and the Step-4 model — not our price. Read 2026; the fastest-ageing table here._

| Competitor <!--c:name--> | Plan / model <!--c:plan--> | Price <!--c:price--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|------------|--------------|-------|--------|------------|
| Gamma | Pro | ~$20/mo | deckary 2026 | [sourced] secondary |
| Canva | Pro / Business | ~$15 / ~$25 per user | Canva 2026 | [sourced] |
| Beautiful.ai | Pro / Team | $12/mo annual / $40 user | g2 2026 | [sourced] secondary |
| Pitch | entry | ~$13/mo | nextdocs 2026 | [sourced] secondary |
| Copilot | via M365 / Copilot Pro | ~$20–30 user (bundled) | Microsoft 2026 | [sourced] |

_Band ~$13–25/mo standalone; the real price pressure is the **bundled** options at $0 marginal (M365/Canva seats)._

## Competitor dynamics {#competitor-dynamics}
<!-- tool: competitor-analysis -->
_Trend over time — to compare whose strategy is working. as_of 2026._

| Competitor <!--c:name--> | Metric (revenue / headcount / …) <!--c:metric--> | Trend + period <!--c:trend--> | Source (+ date) <!--c:source--> | Confidence <!--c:conf--> |
|------------|----------------------------------|----------------|-----------------|------------|
| Gamma | ARR / users / valuation | $100M+ ARR, 70M users, profitable 2+yr, $2.1B val — rising fast | BusinessWire/TechCrunch 2025-11-10 | [sourced] primary |
| Tome | product line | shut Slides product Apr 2025 after $81M raised | market coverage 2025-04 | [sourced] secondary |
| Copilot / Canva | feature cadence | 2026 agentic modes shipping — accelerating into the wedge | Microsoft/Canva 2026 | [sourced] |

## Substitutes {#substitutes}
<!-- tool: substitutes -->
<!-- rests-on: 1#jtbd -->
_Non-obvious competition, framed by the job. The strongest is "do it manually" (habit); self-build caps WTP._

| Substitute <!--c:substitute--> | How it does the job today <!--c:job--> | Why a customer would stay with it <!--c:why--> | Confidence <!--c:conf--> |
|------------|---------------------------|-----------------------------------|------------|
| do-nothing | reuse an old deck / send a rough one | low-stakes/internal decks are "good enough" | [assumption] |
| do it manually | build from scratch in PPT/Keynote or a company template | brand control; **the habit / known-good path** | [sourced: founder brief] |
| self-build with a general LLM | prompt ChatGPT/Claude + hand-format | capable users; **caps WTP for "just generate"** → R-003 | [sourced: market-research] |
| designer / agency | hire it out | highest-stakes decks (board, fundraise) | [assumption] |
| template marketplaces / Canva templates | buy a template, fill it in | when template + manual fill beats generation | [sourced: market-research] |

## Niche risks {#niche-risks}
<!-- synthesis: light Five Forces -->
_Structural risks of the niche (light Five Forces). Born into the risk register `R-001…R-005`._

| Risk <!--c:risk--> | Force <!--c:force--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | → `R-…` <!--c:register--> | Confidence <!--c:conf--> |
|------|-------|------------|--------|---------|------------|
| Gamma dominant + profitable — head-on displacement hard | rivalry | H | H | R-001 | [sourced: market-research] |
| Incumbents bundle native-editable AI gen + own distribution → close the wedge | substitution | H | H | R-002 | [sourced: market-research] |
| Capable users self-build with general LLMs → caps WTP | substitution | M | M | R-003 | [sourced: market-research] |
| Engine quality/COGS depend on third-party LLM providers | supplier power | M | H | R-004 | [assumption] |
| Low entry barrier for "AI slide wrappers" — only a fidelity engine is a real barrier | entry | M | M | R-005 | [assumption] |

## Opportunity {#opportunity}
<!-- synthesis -->
_The "so what" — the point of the step._

- **Opportunity (white space):** the leader is weak exactly where we're strong — Gamma's `.pptx` export
  flattens 30–40% of slides into uneditable images, while the whole market races toward "editable + designed."
  Native-fidelity editable+designed decks for the lead segment is the wedge. [sourced: market-research]
- **Threat (real and closing):** Copilot owns PowerPoint, Canva owns distribution; both ship agentic
  edit-my-file modes in 2026. We have neither. Tome's 2025 exit shows standalone-slides can fail. [sourced]
- **Why now:** AI-deck demand accelerating (CAGR ~23–26%, 2–4× broad market); enterprise adoption >60%; the
  "editable" bar is the new, still-unwon battleground. [sourced]
- **Conclusion (⚙️):** a narrow, fast wedge defended by execution speed on the fidelity engine — viable **only
  if** we outrun incumbents closing the gap. Moat reframed to *speed* (`H-009`), taste/corpus (`H-005`)
  necessary but not sufficient.

## Seeded hypotheses {#hypotheses}
_Market/sizing/competitive assumptions carried into the register._

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | From section <!--c:from--> | Confidence <!--c:conf--> |
|----|------------|------|--------------|------------|
| H-007 | SAM (~$390M, lead segment NA+EU payers) is large enough to build a business on | viability | market-sizing | [assumption] |
| H-008 | The lead segment will pay a standalone ~$15–20/mo despite incumbents bundling | viability | market-sizing | [assumption] |
| H-009 | A standalone native-fidelity engine can stay ahead of incumbents closing the wedge long enough to matter | viability | opportunity | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
- **Adoption-share assumption (~12%)** in the SAM is load-bearing and unvalidated — needs a demand probe.
- **Reachable-count (~15M NA+EU deck-makers)** is desk-estimated — refine with a real segment source.

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → initial analysis projected from `2-analysis/` worklogs; risk register born (`R-001…R-005`);
  H-007/H-008/H-009 seeded.
- **Why:** conclude where the opportunity/threat is — the native-fidelity wedge under closing incumbent pressure.
- **Trigger:** Step-2 analysis, rebuild. Evidence routed through the `2-analysis/` worklogs (per source-intake).
