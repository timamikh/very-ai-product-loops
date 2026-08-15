---
node_type: worklog
tool: jtbd
step: 1
fills: [jtbd]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — jtbd (fills `#jtbd`)

States the job and the four forces for the lead segment. One level above `segment-pains` (which scores the
pains *inside* this job). Feeds `#segments`, `#problems`, and Step-2 `substitutes`.

## Prerequisite

- A customer to frame the job for → lead segment = salespeople & marketers making client-facing decks
  (`segmentation.md`, founder's early bet). [sourced: founder brief]

## 1 · Job statement

> **When** I have to produce a client-facing deck under time pressure (a pitch, a proposal, a campaign
> readout), **I want to** get a first draft that is already on-brand and well-designed *and* that I can
> finish in my own slide tool, **so that** I deliver something client-ready without rebuilding it from
> scratch. [assumption — stated, not yet from interviews]

Middle clause is *progress* (a client-ready draft without a rebuild), not a feature. Circumstance is named
(time-pressured client deck), so the forces can be read.

## 2 · Four forces (switch from "AI tool + hand-rebuild / a designer / a past deck" → Decksmith)

| Force | For this job |
|-------|--------------|
| **Push** (away from status quo) | AI output "looks templated" and often has the wrong structure → user regenerates by hand → the tool saves less time than promised. [sourced: founder brief] |
| **Pull** (toward Decksmith) | native-editable *and* designed = AI speed kept, rebuild tax removed. [sourced: founder brief] |
| **Anxiety** (resists switching) | "will it *actually* be editable in my tool?"; "will the design hold on my content?"; trust in a new tool for a client-facing deliverable. [assumption] |
| **Habit / inertia** (resists leaving status quo) | starting from a past deck, a company template, or handing it to a designer — the known-good path. [assumption] |

Progress needs push+pull > anxiety+habit. The two under-evidenced forces (anxiety, habit) are exactly the
JTBD warning: teams fill them from intuition. Both are `[assumption]` until discovery interviews run.

## 3 · Desired outcomes (ODI — measurable directions)

- Minimize **time to a client-ready deck**. [assumption]
- Minimize **rework after generation** (edits/rebuild needed before it's usable). [assumption]
- Maximize **"looks designed / on-brand"** as judged by the sender and their client. [assumption]
- Maximize **editability in the native tool** (no locked objects, no image dumps). [sourced: founder brief]

These are what `segment-pains` scores and what Step-4 metrics later track.

## 4 · Seeds

- The job itself is real for this segment → **H-002** (desirability).
- The wrong-structure push is real and valued → **H-003** (desirability).
- Editability is a hard gate → **H-004** (desirability, table-stakes).
- "Finish in my own tool without a rebuild" (the pull actually lands) → **H-006** (usability).

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → job statement, four forces, desired outcomes drafted for the lead segment.
- **Why:** anchors segments and problems; feeds Step-2 substitutes.
- **Trigger:** rebuild-from-brief walkthrough.
