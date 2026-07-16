---
node_type: step
step: 2
name: analysis
title: "Step 2 — Analysis"
output: analysis.md
cadence: "~6–12 mo view; revisit ~quarterly or on a market shift"
method_basis: "TAM/SAM/SOM (bottom-up preferred) · competitor 'what game are they playing' · substitutes incl. do-nothing · light Five Forces for niche risk"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Step 2 — Analysis

**Goal.** Understand the market and the competition well enough to conclude **where the
opportunity (or threat) is**. Analysis without a "so what" is inert — the conclusion is the point.

## Inputs (source slots)
`analytics-search` · `kb` · `interview` · the passport (`[[passport]]`).

## Output
`analysis.md`. Recommended tools are soft; the active [status](../../statuses/README.md) sets
which to lean on.

## Artifact skeleton
| Section (ID) | What | Recommended tool |
|--------------|------|------------------|
| `market-sizing` | TAM / SAM / SOM with method + source | `market-sizing` |
| `competitors` | Direct & indirect competitors | `competitor-analysis` |
| `competitor-strategy` | What game each plays (revenue/profit/share/social capital — how), vs our moats | `competitor-analysis` |
| `substitutes` | Non-obvious competition incl. "do nothing / do it manually" | `substitutes` |
| `niche-risks` | Structural risks of the niche (light Five Forces) | `analytics-search` |
| `opportunity` | The "so what" — where the white space / the threat is | — (synthesis) |

## Register touchpoints
- **Risks** — seeds the risk register from `niche-risks` (`R-…`).
- **Hypotheses** — market/sizing assumptions become `H-…` (`type: viability`).

## Gate checklist (soft) — each item ↔ artifact section
- [ ] sizing has an explicit method and source → `analysis#market-sizing`
- [ ] direct & indirect competitors named → `analysis#competitors`
- [ ] each competitor's game identified, compared to our moats → `analysis#competitor-strategy`
- [ ] substitutes incl. "do nothing" covered → `analysis#substitutes`
- [ ] niche risks logged → `analysis#niche-risks` → risk register
- [ ] an explicit opportunity/threat conclusion is stated → `analysis#opportunity`

## Cadence & invalidation
- **Cadence:** ~quarterly or on a market shift.
- **Invalidates downward:** a changed `opportunity` flags Strategy (3) for review.
- **From below:** strategy/tactics learning about a competitor can trigger a revisit.

## The human's role
Decide the opportunity call at the forks the agent surfaces; the agent gathers and compares the facts.
