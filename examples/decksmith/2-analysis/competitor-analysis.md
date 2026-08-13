---
node_type: worklog
tool: competitor-analysis
step: 2
title: "Competitors — the working"
updated: 2026-08-13
version: 0.1.0
---

# Competitors — the working

_Source of truth for `2-analysis.md#competitors`, `#competitor-strategy`, `#competitor-pricing` and
`#competitor-dynamics`; those sections are the projection of this file._
_Method: `tool-skills/library/competitor-analysis`. External inputs are dispatched here from
`../sources/market-research.md` (see CONVENTIONS → Raw data & access), never linked from the artifact._

## Field — who is in the arena

Scanned the paying AI-deck-generation segment (`market-sizing.md#arena`). Kept the players that touch
the customer's job (`../1-passport.md#jtbd`): a web-first leader, two native-format incumbents, two
niche design/collab tools, general LLMs as an indirect route, and one instructive exit.

| Competitor | Direct/Indirect | What they offer | Confidence |
|------------|-----------------|-----------------|------------|
| Gamma | direct | Web-first AI generator; fast, polished decks/sites/docs (category leader) | [sourced: market-research] |
| Microsoft Copilot in PowerPoint | direct (incumbent) | Agentic AI that generates/edits **native PPT** in place | [sourced: market-research] |
| Canva (AI 2.0 / Magic Design) | direct (incumbent) | Conversational AI building **editable design objects** | [sourced: market-research] |
| Beautiful.ai | direct | Rule/template-driven design automation for decks | [sourced: market-research] |
| Pitch | direct | Collaborative, team-oriented deck tool | [sourced: market-research] |
| General LLMs (ChatGPT / Claude) | indirect | Outline + copy; the user formats the slides | [sourced: market-research] |
| Tome | (exited) | Raised $81M, then **shut its Slides product (Apr 2025)** — a cautionary exit | [sourced: market-research] |

## Strategy — the game each is playing

The load-bearing read: where is each strong, and where is the wedge for a native-fidelity
editable-and-designed engine (`../1-passport.md#value-defensibility`, `H-004`)?

- **Gamma** — growth + profitable share; web-first speed, agentic design, own format; $100M ARR. Strong
  on brand/distribution/design-corpus, **weak on native `.pptx`/`.key` fidelity** → our wedge.
- **Microsoft Copilot** — ecosystem lock-in; agentic edits in the *native* format, bundled into M365.
  Owns the format + distribution (very strong); design taste / narrative generic.
- **Canva** — share + ecosystem; freemium scale, AI across a design suite. Huge audience; a generalist,
  not a deck-*narrative* specialist.
- **Beautiful.ai** — niche profit via design-rule automation; less AI-native, weaker narrative. [assumption]
- **Pitch** — collaboration-first niche; not a design/fidelity leader. [assumption]

Conclusion: Gamma is weak exactly at native fidelity; Copilot is strong on native but weak on
design/narrative. The gap between them is where Decksmith's thesis sits — feeds `#opportunity` in
`synthesis.md`.

## Pricing — input to our own pricing (Step 3), not our price

| Competitor | Plan / model | Price | Source | Confidence |
|------------|--------------|-------|--------|------------|
| Gamma | Pro | ~$20 / mo | `../sources/market-research.md` (deckary) | [sourced] |
| Canva | Pro / Business | ~$15 / mo · ~$25 / user | `../sources/market-research.md` | [sourced] |
| Beautiful.ai | Pro / Team | $12/mo annual ($45 monthly) · $40/user (Team) | `../sources/market-research.md` | [sourced] |
| Pitch | Entry | from ~$13 / mo | `../sources/market-research.md` | [sourced] |
| Microsoft Copilot | Bundled (M365 / Copilot Pro) | ~$20–30 / user/mo | `../sources/market-research.md` | [sourced] |

The ~$150/yr price anchor in `market-sizing.md` is derived from this band.

## Dynamics — whose strategy is working

| Competitor | Metric | Trend + period | Source (+ date) | Confidence |
|------------|--------|----------------|-----------------|------------|
| Gamma | ARR / users / valuation | $0 → **$100M ARR in ~3 yr**; 70M users; **$2.1B** valuation (Series B) — profitable 2+ yrs | BusinessWire / TechCrunch, 2025-11-10 | [sourced] |
| Tome | Product line | **Shut its Slides product, Apr 2025** after an $81M raise — pivoted away | market coverage, 2025 | [sourced] |
| Microsoft / Canva | Feature velocity | Shipping agentic / AI-2.0 deck generation through 2026 | vendor, 2026 | [sourced] |

## Open

- Beautiful.ai / Pitch strategy reads are `[assumption]` — no primary financials pulled yet.
- Pricing is a snapshot; incumbents re-bundle often. Revisit before Step-3 pricing locks.

## Change log

### 2026-08-13 — created
- **From → To:** — → first competitor-analysis working, reconstructed from `2-analysis.md`.
- **Why:** stand up the worklog layer so the analysis board drills into where the read was worked out,
  and move the raw `sources/` citations off the artifact and onto the worklog.
- **Trigger:** step-2 worklog migration (see `DESIGN-console-rework.md` → Transition A).
