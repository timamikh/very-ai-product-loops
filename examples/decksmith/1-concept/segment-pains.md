---
node_type: worklog
tool: segment-pains
step: 1
title: "segment-pains — the working"
updated: 2026-08-16
version: 0.1.0
---

# segment-pains — the working

_Source of truth for `1-concept.md#problems`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Routed here by `source-intake` from `../sources/`. Each row is a fact the method works from; the
analysis and conclusions are worked below and projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-------------|---------------------------|---------------|----------|------------|
| `../sources/founder-brief.md` | The visual pain | AI output "looks templated," so the tool "saves less time than promised" — users regenerate by hand. | 2026-07-16 | [sourced: founder brief] |
| `../sources/founder-brief.md` | The structural pain | Decks come back with the **wrong structure/story** for the audience — not only a visual problem. | 2026-07-16 | [sourced: founder brief] |
| `../sources/founder-brief.md` | The disqualifier | Locked/image output is a **non-starter**; editability is table-stakes in this crowd. | 2026-07-16 | [sourced: founder brief] |

## The working

**Lead segment (S1):** sales & marketing professionals making client-facing decks.
**Job:** turn raw content into a finished, on-brand, well-structured, client-ready deck without
hand-fixing every slide (see `jtbd-concept`).

### ≥5 candidate pains, scored (severity × frequency), cost of inaction, class

| # | Pain (obstacle in the job) | Sev | Freq | Cost of inaction (what they do today) | Class | Confidence |
|---|----------------------------|-----|------|----------------------------------------|-------|------------|
| 1 | AI output "looks templated" → they restyle by hand, so the promised time-saving evaporates | H | H | already paying / improvising (regenerate + hand-fix) | differentiator | [sourced: founder brief] |
| 2 | Deck comes back with the **wrong structure/story** for the audience → rewrite the narrative | H | M–H | already improvising (rewrite the flow) | differentiator | [sourced: founder brief] |
| 3 | Locked / image output can't be edited → last-minute edits and reuse are impossible | H | H | already improvising (avoid such tools or rebuild from scratch) | table-stakes | [sourced: founder brief] |
| 4 | Output isn't on-brand (fonts, colours, logo, layout system) → manual re-branding every time | M–H | H | recurring irritation / improvising | differentiator | [assumption] |
| 5 | Deadline pressure → slow tools or manual rebuild risk missing the deadline | M | H | recurring irritation | table-stakes | [assumption] |
| 6 | Visual inconsistency across a deck (spacing, alignment, rhythm) → looks amateur | M | M | recurring irritation | differentiator | [assumption] |
| 7 | Getting existing content (docs, notes) into slides is tedious reformatting | M | M | recurring irritation | table-stakes | [assumption] |

### Ranking & carry-forward

**Top 3 carried forward** (lead with high×high, differentiator first):

1. **Pain 1 — the "templated look" restyle tax** (the lead pain; top differentiator by sev×freq).
2. **Pain 2 — wrong structure/story** (distinct from visual; the second differentiator).
3. **Pain 3 — the editability gate** (table-stakes but *disqualifying*: a tool that fails it is out
   regardless of looks — which is precisely the wedge against "pretty-but-locked" incumbents).

Pains 4–7 stay ranked in the table, not deleted — pain 4 (on-brand) is the strongest tier-2 and
likely rises once the lead pains are met.

### Evidence basis

Pains 1–3 are stated in the founder brief (`[sourced: founder brief]`); 4–7 are `[assumption]` from
desk reasoning. **No customer interviews yet** — so even the sourced pains are the *founder's*
observation, not behavioural evidence from the segment. That gap is exactly what H-003/H-004/H-005
exist to test.

### Seeded hypotheses (carried to register at step 7)

- **H-003 (desirability):** deck makers experience AI output as "templated" and hand-restyle it, so
  the time-saving doesn't materialise (pain 1).
- **H-004 (desirability):** the wrong-structure/story pain is significant and distinct from the
  visual pain (pain 2).
- **H-005 (desirability):** editability is a hard gate — locked/image output disqualifies a tool
  regardless of visual quality (pain 3).

## Change log

### 2026-08-16 — problems worked and projected
- **From → To:** intake only → `#problems` worked (7 candidate pains scored, top-3 carried) and projected
- **Why:** Step 1 Act pass on `segment-pains`; bridges segments → solution and seeds the desirability bets
- **Trigger:** Step 1 operating-loop pass, section `#problems`

### 2026-08-16 — created (intake)
- **From → To:** — → founder-brief facts dispatched into the intake block
- **Why:** seed the segment-pains worklog with its evidence before the Step 1 Act pass
- **Trigger:** `source-intake` at instance setup
