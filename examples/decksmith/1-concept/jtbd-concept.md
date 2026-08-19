---
node_type: worklog
tool: jtbd-concept
step: 1
title: "jtbd-concept — the working"
updated: 2026-08-16
version: 0.1.0
---

# jtbd-concept — the working

_Source of truth for `1-concept.md#jtbd`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Routed here by `source-intake` from `../sources/`. Each row is a fact the method works from; the
analysis and conclusions are worked below and projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-------------|---------------------------|---------------|----------|------------|
| `../sources/originals/founder-brief.md` | The push away from the status quo | Users who make client-facing decks regenerate AI output **by hand** because it "looks templated"; the tool saves less time than promised. | 2026-07-16 | [sourced: founder brief] |
| `../sources/originals/founder-brief.md` | An anxiety/habit signal around switching | Editability is table-stakes; locked/image output is a non-starter — a new tool that locks output will be rejected regardless of looks. | 2026-07-16 | [sourced: founder brief] |
| `../sources/originals/founder-brief.md` | The outcome judged | Output must be both genuinely editable **and** genuinely well-designed, with the right structure/story for the audience. | 2026-07-16 | [sourced: founder brief] |

## The working

_Customer the job is framed for: the lead segment named in `#segments` — a salesperson/marketer who
produces client-facing decks (pitches, proposals, QBRs). The job is read for that specific situation,
per the method's prerequisite._

### 1 · Job statement

> **When** I need to produce a client-facing deck (pitch / proposal / QBR) that has to look credible
> to an external audience, usually on a deadline, **I want to** turn my raw content into a finished,
> on-brand, well-structured deck **without hand-fixing every slide**, **so that** I come across as
> professional and spend my time on the message, not on formatting. [assumption]

The middle clause is *progress* (get to a client-ready deck without the manual restyling tax), not a
product. Note it is a job people already do today — with a designer, with their own templates, or by
grinding through PowerPoint by hand.

### 2 · Four forces (status quo → Decksmith)

- **Push** (away from the current way): today's AI slide tools return output that "looks templated"
  and often has the **wrong structure/story**, so the maker regenerates or rebuilds by hand — the
  promised time saving evaporates. [sourced: founder brief] Manual deck-building is slow; a human
  designer is expensive and not on-demand. [assumption]
- **Pull** (toward Decksmith): a deck that is **editable AND designed** — good-looking and correctly
  structured, yet still a native file you tweak like your own. The maker keeps control *and* the
  polish. [assumption]
- **Anxiety** (resists switching): "Will it really be editable, or locked/images like the others?"
  "Will the design hold up on **my** content, not just the demo?" "Will it match our brand?" "Another
  tool to learn." [assumption] (Editability-as-gate is [sourced: founder brief].)
- **Habit / inertia** (resists leaving the status quo): the maker already knows
  PowerPoint / Google Slides / Keynote, has their own decks and templates, and defaults to "I'll just
  fix the AI draft myself" or "I'll do it manually like always." [assumption]

Read together: **push is strong and pull is strong, but so are anxiety (will design hold on my
content? is it truly editable?) and habit (I already own the tools).** Progress needs push + pull to
beat anxiety + habit — which is exactly why the feasibility bet H-001 (design actually holds at
scale) doubles as the desirability lever: it is the single fact that most collapses the anxiety term.

### 3 · Desired outcomes (ODI — measurable directions)

- **Minimize** the time from raw content → client-ready deck. [assumption]
- **Minimize** the share of generated slides that need manual restyling before they can be sent.
  [assumption]
- **Minimize** rework to get the structure/story right for the audience. [assumption]
- **Increase** the likelihood the deck reads as credible and on-brand to the external audience.
  [assumption]

These are what `segment-pains` scores and what Step-4 metrics later track (e.g. an activation metric
around "deck sent with little/no manual restyle").

### 4 · Hypotheses (jtbd sharpens more than it adds)

- Sharpens the desirability side of the concept. Candidate desirability bets carried to the register
  at step 7 (reconciled against `#problems`): **editability is a hard gate** — locked/image output is
  disqualifying regardless of looks; and **the structure/story pain is real**, not only cosmetic.
  These are worked and scored in `#problems`; jtbd supplies the job frame they sit in. No new id is
  minted here that `segment-pains` doesn't already carry.

## Change log

### 2026-08-19 — sources layout migrated
- **From → To:** `../sources/founder-brief.md` → `../sources/originals/founder-brief.md`
- **Why:** reorganized sources layout into originals/ · snapshots/ · access/ subfolders
- **Trigger:** framework 0.10 boundary layer

### 2026-08-16 — jtbd worked and projected
- **From → To:** intake only → `#jtbd` worked (job statement, four forces, desired outcomes) and projected
- **Why:** Step 1 Act pass on `jtbd-concept`; anchors segments/pains and feeds Step 2 substitutes
- **Trigger:** Step 1 operating-loop pass, section `#jtbd`

### 2026-08-16 — created (intake)
- **From → To:** — → founder-brief facts dispatched into the intake block
- **Why:** seed the jtbd-concept worklog with its evidence before the Step 1 Act pass
- **Trigger:** `source-intake` at instance setup
