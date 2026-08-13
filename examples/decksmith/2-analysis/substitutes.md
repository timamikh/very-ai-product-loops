---
node_type: worklog
tool: substitutes
step: 2
title: "Substitutes — the working"
updated: 2026-08-13
version: 0.1.0
---

# Substitutes — the working

_Source of truth for `2-analysis.md#substitutes`; that section is the projection of this file._
_Method: `tool-skills/library/substitutes`. Scored against the customer's **job**
(`../1-passport.md#jtbd`: a credible client deck fast, without redoing it by hand), not our category.
External inputs are dispatched here from `../sources/market-research.md` (see CONVENTIONS → Raw data &
access), never linked from the artifact._

## The job, restated

What is being hired: *get a credible, on-brand client deck fast, without rebuilding it by hand.* Every
substitute below is something a buyer already uses to get that job done — the baseline three
(do-nothing / do-it-manually / self-build) are always listed, then the market alternatives.

## Alternatives scored against the job

| Substitute | Whose job it does | Why the customer chooses it | When it wins against us | → Risk | Confidence |
|------------|-------------------|-----------------------------|-------------------------|--------|------------|
| Do nothing (status quo) | Present a plain/templated deck as-is | "Good enough" for low-stakes meetings | Meeting is low-stakes; look doesn't matter | — | [assumption] |
| Do it manually | Build in PowerPoint/Keynote/Canva by hand, or brief a designer | Full control, on-brand, trusted result | High-stakes flagship decks; brand-critical | `R-006` | [assumption] |
| Self-serve via a general LLM | Prompt ChatGPT/Claude for outline+copy, then hand-format | Already paying for the LLM; flexible | Capable user, low deck volume | `R-003` | [sourced: market-research] |
| Gamma (web-format generation) | Fast AI decks that live on the web | Speed + polish if native `.pptx`/`.key` isn't required | Native format not needed; audience views a link | `R-001` | [sourced: market-research] |
| Copilot in PowerPoint | AI edits your *real* native PPT | Native + bundled; no new tool to buy | M365 shops; native editing is the priority | `R-002` | [sourced: market-research] |

## Two thresholds that bound willingness to pay

- **Self-build threshold:** a capable individual with low deck volume who already pays for a general
  LLM — at that point "just prompt it and format myself" beats paying us. Caps WTP; feeds `R-003`. [assumption]
- **Switching friction:** company-standard templates and brand kits locked into incumbents (Canva/M365),
  plus habit — the barrier our native-fidelity + design quality has to clearly beat. [assumption]

## Open

- No quantified split between "do nothing" and "do it manually" — both are `[assumption]`. A few buyer
  interviews would separate them and firm up `R-006`.

## Change log

### 2026-08-13 — created
- **From → To:** — → first substitutes working, reconstructed from `2-analysis.md`.
- **Why:** stand up the worklog layer so the board drills into where the job-based read was worked out.
- **Trigger:** step-2 worklog migration (see `DESIGN-console-rework.md` → Transition A).
