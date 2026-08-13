---
node_type: worklog
tool: synthesis
step: 2
title: "Synthesis — niche risks & opportunity"
updated: 2026-08-13
version: 0.1.0
---

# Synthesis — niche risks & opportunity

_Source of truth for the `<!-- synthesis -->` sections of `2-analysis.md`: `#niche-risks`
(light Five Forces) and `#opportunity`; those sections are the projection of this file._
_This is the cross-tool read — it pulls from `market-sizing.md`, `competitor-analysis.md` and
`substitutes.md`, not from raw sources directly._

## Niche risks — a light Five Forces on the segment

Ran the five forces against the *niche* (paying AI-deck generation), not the whole software market.
Each force that bites becomes a risk seeded into `../registers/risks.md`.

| Risk | Force | Likelihood | Impact | → `R-…` | Confidence |
|------|-------|------------|--------|---------|------------|
| Gamma is a dominant, profitable leader — head-on displacement is hard | rivalry | H | H | `R-001` | [sourced: market-research] |
| Incumbents (Copilot in PPT, Canva) bundle native-editable AI generation with distribution | substitution | H | H | `R-002` | [sourced: market-research] |
| Capable buyers self-build with general LLMs → caps willingness to pay | buyer power / substitution | M | M | `R-003` | [sourced: market-research] |
| Engine quality/COGS depend on third-party LLM providers | supplier power | M | H | `R-004` | [assumption] |
| Low entry barrier for "AI slide wrappers" → crowded rivalry | entry barriers | H | M | `R-005` | [sourced: market-research] |

Rivalry and substitution are the two H/H forces — they define the opportunity below.

## Opportunity — the white space between leader and incumbents

Reading strategy (`competitor-analysis.md`) against the job (`substitutes.md`): the leader is web-first
and not truly native-editable, the native incumbents are design/narrative generalists. That gap is the
thesis.

- **Opportunity (the white space): native, high-fidelity editable `.pptx`/`.key` that also look
  designed.** Gamma's PowerPoint export **flattens 30–40% of slides into uneditable images** — not
  truly native-editable. Copilot is native but generalist on design/narrative; Canva likewise.
  Decksmith's thesis (`../1-passport.md#concept`) sits exactly in that gap: native fidelity **and**
  design quality **and** narrative. [sourced: market-research]
- **Threat (why the window is narrow):** incumbents are moving into the wedge with a distribution
  advantage, and Gamma could fix its export. This is a race — the defensible thing must be a genuinely
  hard *fidelity + design engine* (`H-004`), not the app. [sourced: market-research]
- **Why now:** AI-slide demand growing ~23–26% CAGR (`market-sizing.md`); "editable design objects" is
  the headline battleground of 2026; the native-fidelity gap is currently unmet by the leader. [sourced: market-research]

## Hypotheses this synthesis seeds

- `H-005` — a native, high-fidelity editable-and-designed deck is a real unmet need the lead segment
  values over web-format generation (Gamma's export gap). desirability/viability. [assumption]
- Pressures `H-004` (defensibility) — incumbents entering the wedge → the moat must be the fidelity
  engine, not the app; and `H-001` (feasibility) — native fidelity is exactly where the leader fails.

## Change log

### 2026-08-13 — created
- **From → To:** — → first synthesis working, reconstructed from `2-analysis.md`.
- **Why:** the `<!-- synthesis -->` sections are a cross-tool read; give them their own worklog so the
  board's risk/opportunity zones drill into where the read was made.
- **Trigger:** step-2 worklog migration (see `DESIGN-console-rework.md` → Transition A).
