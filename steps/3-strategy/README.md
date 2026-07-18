---
node_type: step
step: 3
name: strategy
title: "Step 3 — Strategy"
output: strategy.md
cadence: "~3–12 mo; reviewed ~quarterly"
method_basis: "Playing to Win (where-to-play / how-to-win) · Dunford positioning · UVP/CPV · value-based pricing & packaging · channels (Bullseye) · moats revisited (7 Powers) · product surface & instrumentation · C4-context architecture"
status: draft
version: 0.2.0
updated: 2026-07-18
---

# Step 3 — Strategy

**Goal (qualitative choices).** Decide **where to play** and **how to win**, and state the
**bets** we're making. This step is choices and direction — not numbers (those are Step 4).

> **Boundary 3 ↔ 4:** if it's a *choice* → here; if it's a *number, model, or mitigation* → Step 4.

## Inputs (source slots)
The passport (`[[passport]]`), the analysis (`[[analysis]]`), `interview`, `kb`.

## Output
`strategy.md`. The [status](../../statuses/README.md) sets goal shape: `concept-viability`
strategy = find fit; `pmf` = prove repeatable value; `growth` = scale + defend.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `winning-aspiration` | What winning looks like this horizon | `where-to-play-how-to-win` |
| `where-to-play` | Segments / markets / arena chosen | `where-to-play-how-to-win` |
| `how-to-win` | The winning logic + which moats we leverage | `where-to-play-how-to-win`, `value-definition` |
| `uvp-cpv` | Unique value proposition / customer-perceived value | `uvp-cpv` |
| `pricing` | Pricing model & packaging (value metric, tiers/fences, price vs the alternative) | `pricing` |
| `channels-expansion` | Acquisition/comms channels + expansion paths | `channels-expansion` |
| `product-surface` | Every user-interaction surface + instrumentation: channels, landings, mailings, admin, metric collection, behavior-study tools | `product-surface` |
| `architecture` | System architecture at **C4 Context** level (product, its users, external systems) | `architecture-c4` |
| `bets` | The strategic hypotheses we're wagering on | `jtbd`, `value-definition` |
| `product-risks` | Risks specific to this strategy | `risk-mitigation` |

## Register touchpoints
- **Hypotheses** — `bets` become `H-…` (mixed types) in the register; unproven pricing/packaging
  choices become `H-…` (`type: viability`).
- **Risks** — `product-risks` extend the risk register (`R-…`).
- **Value** — `value-definition` is revisited here; **derivative moats** appear now (customers/scale exist from `pmf`).

## Gate checklist (soft) — each item ↔ artifact section
- [ ] winning aspiration stated → `strategy#winning-aspiration`
- [ ] where-to-play chosen (and what's excluded) → `strategy#where-to-play`
- [ ] how-to-win names the moat(s) it leverages → `strategy#how-to-win`
- [ ] UVP/CPV articulated → `strategy#uvp-cpv`
- [ ] pricing model & packaging chosen, anchored to the alternative → `strategy#pricing`
- [ ] channels & expansion path named → `strategy#channels-expansion`
- [ ] product surface & instrumentation mapped → `strategy#product-surface`
- [ ] C4-context architecture sketched → `strategy#architecture`
- [ ] bets captured as typed hypotheses → `strategy#bets` → hypothesis register
- [ ] product risks logged → `strategy#product-risks` → risk register

> `product-surface` and `architecture` are **sketched here and refined at Step 4** — the
> instrumentation defines where metric-tree data comes from, and the architecture feeds infra
> cost lines in the financial model. `pricing` is likewise **decided here and quantified at Step 4**:
> the price points feed `unit-economics` (margin check) and `financial-model` (projection).

## Cadence & invalidation
- **Cadence:** ~quarterly, or when a bet is validated/refuted, or the opportunity shifts.
- **Invalidates downward:** a changed choice flags the Strategic Plan (4).
- **From below:** a refuted bet (from tactics/sprint) triggers a revisit here.

## The human's role
Make the strategic choices; the agent frames the options, the trade-offs, and the moats in play.

## Change log

### 2026-07-18 — added `pricing` section
- **From → To:** skeleton gained `pricing` (value metric · packaging/fences · price vs the
  alternative), filled by the new `pricing` tool; gate + register touchpoints updated.
- **Why:** pricing was the one strategic choice with no home — competitor pricing (Step 2) is an
  input and `unit-economics` (Step 4) only validates the margin; nowhere *set* the price. Pricing
  is a choice, so it lives at Step 3 and is quantified at Step 4.
- **Trigger:** missing-tools pass, 2026-07-18.

### 2026-07-16 — created
- **From → To:** — → Step 3 skeleton (thin, grounded in Playing to Win + Dunford)
- **Trigger:** Phase 1 / PR #5.
