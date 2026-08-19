---
node_type: worklog
tool: concept-expansion
step: 1
title: "concept-expansion — the working"
updated: 2026-08-16
version: 0.1.0
---

# concept-expansion — the working

_Source of truth for `1-concept.md#solution`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Routed here by `source-intake` from `../sources/`. Each row is a fact the method works from; the
analysis and conclusions are worked below and projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-------------|---------------------------|---------------|----------|------------|
| `../sources/originals/founder-brief.md` | The core mechanism | A prototype rendering approach emits **native slide objects** (not images) and applies layout/spacing rules. Quality-at-scale is unproven. | 2026-07-16 | [assumption] |
| `../sources/originals/founder-brief.md` | The design-learning input | Access to a small corpus of well-designed decks to learn design patterns from (to be assembled). | 2026-07-16 | [assumption] |
| `../sources/originals/founder-brief.md` | The riskiest bet the solution must clear | The riskiest thing is **feasibility**: can the engine *reliably* produce files that are both genuinely editable and genuinely well-designed, **at scale**. | 2026-07-16 | [assumption] |

## The working

Mapping runs **from the ranked pains** (`#problems`), tier-1 first — a mechanism per pain, not a
feature list. Solution stub carried from `concept-formation` (native objects · design rules from a
corpus · narrative structuring).

### Problem → mechanism

| Rank | Pain | Mechanism (how it is removed — not a feature label) | Feasibility | Confidence |
|------|------|------------------------------------------------------|-------------|------------|
| 1 | "Templated look" restyle tax | The engine **emits native slide objects styled by design rules learned from a curated corpus** (layout grids, spacing, typographic hierarchy, colour) applied *at generation* — so the first output already reads as designed, not as a default template. | hard — this IS the core bet | [assumption] → `H-001` |
| 2 | Wrong structure/story | A **narrative-structuring pass** maps the user's raw content to an audience-appropriate deck arc (e.g. situation→complication→resolution for a pitch; QBR arc for a review) before styling — structure chosen for the audience, not bullet-dumped. | hard — separable build bet from visual polish | [assumption] → `H-002` |
| 3 | Editability gate | **Native `.pptx`/`.key` emission**: real shapes, text frames and layout objects that round-trip as fully editable in PowerPoint / Keynote / Slides — never flattened images or a locked template. | moderate–hard (the "editable" half of `H-001`) | [assumption] → `H-001` |
| 4 (tier-2) | Not on-brand | **Brand-kit ingestion** (fonts, colours, logo, layout templates) fed into the design engine so output conforms to the org's system. Post-MVP: the concept commits the mechanism, not the sprint. | moderate | [assumption] |

### Orphan check (capabilities that map to no ranked pain → dropped)

| Capability | Why rejected |
|------------|--------------|
| Real-time collaboration / co-editing | no ranked pain; explicitly out of scope (founder brief) |
| Non-slide formats (docs, PDF as primary output) | no ranked pain; out of scope (founder brief) |
| AI chat "assistant" surface | no ranked pain — a UI fashion, not a mechanism for any pain here |
| Deck-view analytics / tracking | tier-3 at best; a different job (selling *with* the deck, not making it) |

### Feasibility bets surfaced (→ register)

- **H-001 (feasibility):** the engine reliably produces slides that are both native-editable **and**
  visually well-designed **at scale** (across arbitrary content). The lead bet.
- **H-002 (feasibility):** the engine reliably produces audience-appropriate **narrative structure**,
  not only visual polish. Separable from H-001 because a deck can look good yet tell the wrong story.

### Confidence

Every mapping row is a design decision / `[assumption]`; nothing here is market evidence. The two
feasibility bets are the honest build risk — stated, not hidden.

## Change log

### 2026-08-19 — sources layout migrated
- **From → To:** `../sources/founder-brief.md` → `../sources/originals/founder-brief.md`
- **Why:** reorganized sources layout into originals/ · snapshots/ · access/ subfolders
- **Trigger:** framework 0.10 boundary layer

### 2026-08-16 — solution worked and projected
- **From → To:** intake only → `#solution` worked (mechanism per ranked pain, orphan rejects, feasibility bets) and projected
- **Why:** Step 1 Act pass on `concept-expansion`; maps every carried pain to a mechanism, no orphans
- **Trigger:** Step 1 operating-loop pass, section `#solution`

### 2026-08-16 — created (intake)
- **From → To:** — → founder-brief facts dispatched into the intake block
- **Why:** seed the concept-expansion worklog with its evidence before the Step 1 Act pass
- **Trigger:** `source-intake` at instance setup
