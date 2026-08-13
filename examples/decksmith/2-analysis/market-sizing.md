---
node_type: worklog
tool: market-sizing
step: 2
title: "Market sizing — the working"
updated: 2026-08-13
version: 0.1.0
---

# Market sizing — the working

_Source of truth for `2-analysis.md#market-sizing`; that section is the projection of this file._
_Method: `tool-skills/library/market-sizing`. External inputs are dispatched here from
`../sources/market-research.md` (see CONVENTIONS → Raw data & access), never linked from the artifact._

## Arena sized

AI-generated **client-facing decks** for the lead segment — salespeople & marketers who make decks
often, in English-first paying markets (job: `../1-passport.md#jtbd`). The arena is the *paying*
generation segment, not the whole presentation-software market. [assumption]

## Method — bottom-up SAM is the load-bearing number

Per `market-sizing`, a bottom-up SAM is trusted over the published top-down figures (which diverge
2–3× and are used only as a cross-check — never averaged).

**SAM (serviceable addressable) ≈ $750M / yr** — bottom-up:

| Input | Value | Basis | Confidence |
|-------|-------|-------|------------|
| Reachable frequent deck-makers (sales/marketing, paying English-first markets) | ~5,000,000 | illustrative population estimate | [assumption] |
| Price per user / year | ~$150 | ≈ incumbent paid tiers (`competitor-analysis.md`) | [sourced: market-research] → [assumption] for us |
| **SAM = users × price** | **≈ $750M / yr** | 5.0M × $150 | [assumption] |

→ seeds `H-006` (viability) in `registers/hypotheses.md`.

## TAM cross-check (top-down, range only)

Published reports put AI presentation-generation at **~$2.8–4.7B (2026)** inside a ~$8.6B broad
presentation-software market, segment CAGR **~23–26%**. Used as a sanity band around the bottom-up
SAM, not as the estimate. [sourced: market-research] — reports diverge 2–3×, kept as a range. See
`../sources/market-research.md`.

## SOM (serviceable obtainable, ~3 yr)

**≈ $4M ARR** — ~0.5% of SAM captured early, given Gamma's dominance and incumbent entry
(`competitor-analysis.md`). Reasoned share, not a booked plan. [assumption]

## Open

- The 5M reachable-population figure is illustrative — a real bottom-up needs a named source per
  market. `— to clarify —`
- Price anchor leans on competitor pricing; revisit once our own pricing (Step 3) exists.

## Change log

### 2026-08-13 — created
- **From → To:** — → first market-sizing working, reconstructed from `2-analysis.md#market-sizing`.
- **Why:** stand up the worklog layer so the analysis board can drill into where sizing was worked out.
- **Trigger:** console drill-through slice (see `DESIGN-console-rework.md` → Transition A).
