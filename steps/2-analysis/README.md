---
node_type: card
kind: step
name: analysis
step: 2
title: "Step 2 — Analysis"
output: 2-analysis.md
prerequisites: [the concept artifact `1-concept.md` exists]
reads: [file:1-concept.md, source:research, source:kb, source:interview]
writes: [section:*]
surfaces: [ticks, register:hypotheses, register:risks, sign-off, change-log]
cadence: "~6–12 mo view; revisit ~quarterly or on a market shift"
method_basis: "TAM/SAM/SOM (bottom-up preferred) · competitor 'what game are they playing' · substitutes incl. do-nothing · light Five Forces for niche risk"
status: draft
version: 0.2.1
updated: 2026-08-22
---
# Step 2 — Analysis

**Goal.** Understand the market and the competition well enough to conclude **where the
opportunity (or threat) is**. Analysis without a "so what" is inert — the conclusion is the point.

## Inputs (source slots)
`research` (scoped desk research the methods run themselves) · `kb` · `interview` · the concept (`1-concept.md`).

## Output
`2-analysis.md` — assembled from the section skeleton below. Template: [`template.md`](template.md).
Recommended tools are soft; the active [status](../../statuses/README.md) sets which to lean on.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `market-sizing` | TAM / SAM / SOM with method + source | `market-sizing` |
| `competitors` | Direct & indirect competitors | `competitor-analysis` |
| `competitor-strategy` | What game each plays (revenue/profit/share/social capital — how), vs our moats | `competitor-analysis` |
| `competitor-pricing` | Dated competitor pricing — input to our pricing (Step 3), sizing's price anchor & the financial model | `competitor-pricing` |
| `competitor-dynamics` | How each competitor develops over time (revenue/headcount trend) — compares strategy effectiveness | `competitor-dynamics` |
| `substitutes` | Non-obvious competition incl. "do nothing / do it manually" | `substitutes` |
| `niche-risks` | Structural risks of the niche (light Five Forces — checklist: [`five-forces-light.md`](../../tool-skills/library/references/five-forces-light.md)) | synthesis — no library method; its worklog is `2-analysis/synthesis.md` (check P requires it) |
| `opportunity` | The "so what" — where the white space / the threat is | synthesis — projects from the same `2-analysis/synthesis.md` |

## Register touchpoints
- **Risks** — seeds the risk register from `niche-risks` (`R-…`).
- **Hypotheses** — market/sizing assumptions become `H-…` (`type: viability`).

## Gate checklist (soft) — each item ↔ artifact section
- [ ] sizing has an explicit method and source → `analysis#market-sizing`
- [ ] direct & indirect competitors named → `analysis#competitors`
- [ ] each competitor's game identified, compared to our moats → `analysis#competitor-strategy`
- [ ] competitor pricing captured where findable → `analysis#competitor-pricing`
- [ ] competitor development dynamics captured where findable → `analysis#competitor-dynamics`
- [ ] substitutes incl. "do nothing" covered → `analysis#substitutes`
- [ ] niche risks logged → `analysis#niche-risks` → risk register
- [ ] an explicit opportunity/threat conclusion is stated → `analysis#opportunity`
- [ ] seeded hypotheses typed and carried to the register → `analysis#hypotheses` → hypothesis register
- [ ] open questions logged for the human to resolve → `analysis#to-clarify`

## Cadence & invalidation
- **Cadence:** ~quarterly or on a market shift.
- **Invalidates downward:** a changed `opportunity` flags Strategy (3) for review.
- **From below:** strategy/tactics learning about a competitor can trigger a revisit.

## The human's role
Decide the opportunity call at the forks the agent surfaces; the agent gathers and compares the facts.
