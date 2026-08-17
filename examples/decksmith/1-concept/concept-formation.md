---
node_type: worklog
tool: concept-formation
step: 1
title: "concept-formation — the working"
updated: 2026-08-16
version: 0.1.0
---

# concept-formation — the working

_Source of truth for `1-concept.md#idea`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Routed here by `source-intake` from `../sources/`. Each row is a fact the method works from; the
analysis and conclusions are worked below and projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-------------|---------------------------|---------------|----------|------------|
| `../sources/founder-brief.md` | The core positioning shift the concept makes | Every AI slide tool forces a choice between **pretty-but-locked** (exports images / a rigid template) and **editable-but-ugly** (plain text dumped into default PowerPoint). Decksmith's bet: output **native, fully editable** `.pptx`/`.key` (real shapes, text, layouts) that **also look designed**. | 2026-07-16 | [sourced: founder brief] |
| `../sources/founder-brief.md` | What "the shift" replaces | Today's tools "save less time than promised" because output "looks templated" and comes back with the **wrong structure/story** for the audience — so users regenerate by hand. | 2026-07-16 | [sourced: founder brief] |
| `../sources/founder-brief.md` | The non-negotiable frame | Editability is **table-stakes** for this crowd — locked/image output is a non-starter. | 2026-07-16 | [sourced: founder brief] |

## The working

### 1 · One-line concept

> **Decksmith is an AI deck generator that produces native, fully editable `.pptx`/`.key` slides
> that also look designed — for people who make client-facing decks.** [sourced: founder brief]

Category = *AI deck generator* (the crowded, understood category). The differentiator rides in the
two adjectives the category usually can't hold together: **native/editable** and **designed**. Who =
people who make client-facing decks; the lead segment is ranked in `#segments` (`segmentation`).

### 2 · The shift (Dunford — define by what it replaces)

- **Current alternative.** Every AI slide tool today forces one of two bad trades
  [sourced: founder brief]:
  - **pretty-but-locked** — exports images or a rigid template you can't really edit; or
  - **editable-but-ugly** — dumps plain text into default PowerPoint styling.
  - The fallback under both is *regenerate / fix it by hand*, so the tool "saves less time than
    promised." The pain is not only visual — decks also come back with the **wrong structure/story**
    for the audience. [sourced: founder brief]
- **The shift.** With Decksmith the output is **editable AND designed** at once: real shapes, text
  and layouts you edit like your own file, that already look designed and carry a structure fit for
  the audience. The either/or collapses. [assumption]

The spine of the concept is that collapse. If a buyer doesn't experience "I got a good-looking deck
I can still fully edit" as *one* thing, there is no shift — just another entrant on one side of the
old trade.

### 3 · Riskiest assumption (the center of gravity at concept-viability)

The founder names it and I agree: the bet most likely to sink the concept is **feasibility**, not
demand. [sourced: founder brief]

> **H-001 (feasibility):** the engine can *reliably* produce slide files that are **both** genuinely
> editable (native objects, not images or a locked template) **and** genuinely well-designed, **at
> scale** — across arbitrary user content, not just cherry-picked demos. [assumption]

If H-001 is false, the shift is a demo, not a product: quality collapses on real content and the
output drifts back to one side of the old trade. This is the lead hypothesis to test — everything
else (segments, pains, moat) matters only if the engine clears this bar. Seeded to the register as
`H-001`, `type: feasibility`.

### 4 · Solution stub (input to `concept-expansion`, not designed here)

Kept as raw material for the `#solution` pass, not as a feature list:

- A rendering engine that **emits native slide objects** (shapes, text frames, real layouts), never
  flattened images. [assumption]
- **Design rules learned from a curated corpus** of well-designed decks — layout, spacing,
  typographic hierarchy — applied at generation time. [assumption]
- **Narrative structuring to the audience**, so the deck comes back with the right story, not only
  the right look. [assumption]

The problem→solution mapping proper is `concept-expansion`, downstream of `#problems`.

### 5 · Confidence

The concept sentence is a `[sourced: founder brief]` PO decision; the *shift* and *H-001* are
`[assumption]` until evidenced. No claim here is validated yet — this is the earliest step.

## Change log

### 2026-08-16 — idea worked and projected
- **From → To:** intake only → `#idea` worked (concept sentence, shift, H-001, solution stub) and projected
- **Why:** Step 1 Act pass on `concept-formation`; frames the concept as a positioning shift and names the riskiest bet
- **Trigger:** Step 1 operating-loop pass, section `#idea`

### 2026-08-16 — created (intake)
- **From → To:** — → founder-brief facts dispatched into the intake block
- **Why:** seed the concept-formation worklog with its evidence before the Step 1 Act pass
- **Trigger:** `source-intake` at instance setup
