---
node_type: worklog
tool: concept-formation
step: 1
fills: [concept, solution]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — concept-formation (fills `#concept`, `#solution`)

Source of truth for the concept and the solution stub. The passport sections are projections of this.

## Input reached

- `sources/founder-brief.md` — the raw idea + the founder's observations + honest inventory. Read directly
  (Step-1 sources not yet dispatched into worklogs). [sourced: founder brief 2026-07-16]

## 1 · One-line concept

> **Decksmith is an AI deck generator that outputs native, fully-editable `.pptx`/`.key` files that also
> look designed** — real shapes, text and layouts you edit like your own, not images or a locked template.
> [sourced: founder brief]

Reads in one breath; no feature list. Passes the "a stranger repeats it correctly" test.

## 2 · The shift (Dunford)

- **Today's alternative:** every AI slide tool forces a bad trade — *pretty but locked* (exports images or a
  rigid template you can't really edit) **or** *editable but ugly* (dumps text into default PowerPoint).
  [sourced: founder brief]
- **The shift Decksmith makes:** editable **AND** designed — you keep AI speed without the hand-rebuild tax.
  The spine of the concept is collapsing that either/or. [sourced: founder brief]

## 3 · Riskiest assumption (seeds a hypothesis)

- The single belief that sinks it if false: **feasibility** — can the engine *reliably* emit files that are
  both genuinely editable and genuinely well-designed, at scale (not one hand-tuned demo)? [assumption]
  → seeded as **H-001** (feasibility), the center of gravity at concept-viability.

## 4 · Solution stub (seeds `#solution`, per-problem mapping done in segment-pains)

The shift is delivered by three moves, each answering a stated pain (pains scored in `segment-pains.md`):

- **Native renderer** — emits real slide objects (shapes/text/layouts), not images, so output is editable
  in the user's own tool. Answers the *locked output* pain (table-stakes, baked into the concept). [assumption]
- **Design layer** — layout/spacing/type rules learned from a curated corpus of well-designed decks, so
  output *looks designed*, not templated. Answers the *looks templated* pain (the differentiator). [assumption]
- **Audience-aware structure** — outline/story shaped for the target audience, not a generic dump. Answers
  the *wrong structure/story* pain. [assumption]

> Not designing features here (Dunford: solution stub only). The per-problem table is projected into
> `#solution` after `segment-pains` ranks the pains.

## Confidence

Concept + shift: `[sourced: founder brief]`. Feasibility, quality-at-scale, and each solution move: `[assumption]`
until a prototype eval exists (no product in market — `config.yaml` active_status: concept-viability).

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → concept + shift + riskiest assumption + solution stub drafted from the founder brief.
- **Why:** Step-1 first pass; everything downstream leans on a crisp concept.
- **Trigger:** rebuild-from-brief walkthrough.
