---
node_type: card
kind: step
name: strategy
step: 3
title: "Step 3 — Strategy"
output: 3-strategy.md
prerequisites: [the concept and the analysis exist]
reads: [file:1-concept.md, file:2-analysis.md, source:interview, source:kb]
writes: [section:*]
surfaces: [ticks, register:hypotheses, register:risks, sign-off, change-log]
cadence: "~3–12 mo; reviewed ~quarterly"
method_basis: "Playing to Win (where-to-play / how-to-win) · Dunford positioning · UVP/CPV · value-based pricing & packaging · channels (Bullseye) · moats revisited (7 Powers) · product surface & instrumentation · C4-context architecture"
status: draft
version: 0.3.0
updated: 2026-08-16
---
# Step 3 — Strategy

**Goal (qualitative choices).** Decide **where to play** and **how to win**, and state the
**bets** we're making. This step is choices and direction — not numbers (those are Step 4).

> **Boundary 3 ↔ 4:** if it's a *choice* → here; if it's a *number, model, or mitigation* → Step 4.

## Inputs (source slots)
The passport (`1-concept.md`), the analysis (`2-analysis.md`), `interview`, `kb`.

## Output
`3-strategy.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).
The [status](../../statuses/README.md) sets goal shape: `concept-viability`
strategy = find fit; `pmf` = prove repeatable value; `growth` = scale + defend.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `winning-aspiration` | What winning looks like this horizon | `where-to-play-how-to-win` |
| `where-to-play` | Segments / markets / arena chosen | `where-to-play-how-to-win` |
| `how-to-win` | The winning logic + which moats we leverage | `where-to-play-how-to-win`, `value-definition-strategy` |
| `uvp-cpv` | Unique value proposition / customer-perceived value (per situation for the lead segment) | `uvp-cpv` |
| `pricing` | Pricing model & packaging (value metric, tiers/fences, price vs the alternative) | `pricing-strategy` |
| `channels-expansion` | Acquisition/comms channels + expansion paths | `channels-expansion` |
| `product-surface` | Every user-interaction surface + instrumentation: channels, landings, mailings, admin, metric collection, behavior-study tools | `product-surface` |
| `architecture` | System architecture at **C4 Context** level (product, its users, external systems) | `architecture-c4` |
| `bets` | The strategic hypotheses we're wagering on | `bets`, `value-definition-strategy` |
| `product-risks` | Risks specific to this strategy | `pre-mortem` |

## Register touchpoints
- **Hypotheses** — `bets` become `H-…` (mixed types) in the register; unproven pricing/packaging
  choices become `H-…` (`type: viability`).
- **Risks** — `product-risks` extend the risk register (`R-…`).
- **Value** — `value-definition-strategy` revisits the Step-1 moats here; **derivative moats** appear now (customers/scale exist from `pmf`).

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
- [ ] open questions logged for the human to resolve → `strategy#to-clarify`

> `product-surface` and `architecture` are **sketched here and refined at Step 4** — the
> instrumentation defines where metric-tree data comes from, and the architecture feeds infra
> cost lines in the financial model. Pricing is likewise **decided here (`pricing-strategy`) and
> quantified at Step 4**: the price points feed `unit-economics` (margin check) and
> `financial-model` (projection). `uvp-cpv` formulates the CVP **per situation** for the lead
> segment; market-entry bundles are composed at Step 5 (`segment-cvp`), not here.

## Cadence & invalidation
- **Cadence:** ~quarterly, or when a bet is validated/refuted, or the opportunity shifts.
- **Invalidates downward:** a changed choice flags the Strategic Plan (4).
- **From below:** a refuted bet (from tactics/sprint) triggers a revisit here.

## The human's role
Make the strategic choices; the agent frames the options, the trade-offs, and the moats in play.
