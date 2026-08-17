---
node_type: worklog
tool: market-sizing
step: 2
title: "market-sizing — the working"
updated: 2026-08-16
version: 0.1.0
---

# market-sizing — the working

_Source of truth for `2-analysis.md#market-sizing`; that section is the projection of this file._
Evidence gathered by a `loops-research` brief (web, `as_of 2026-08-16`), integrated and reasoned
here. Bottom-up is the headline; the top-down band is a directional sanity check only.

## Arena sized

The **beachhead**: US sales & marketing professionals who make **client-facing** decks (S1 from
`1-concept.md#segments`). Sizing the US first because that is the reachable serviceable market at
concept stage; global is the TAM direction.

## Bottom-up SAM (units × price) — US beachhead, annual

**Population — reachable client-facing deck-makers (US):**

| Component | Count | Source | Conf |
|-----------|-------|--------|------|
| Market research analysts & marketing specialists (SOC 13-1161) | 899,580 | BLS OEWS May 2025 (via BLS-derived tables + press summary; bls.gov 403'd direct fetch), `as_of 2026-08-16` | [sourced: BLS OEWS, fact] |
| Marketing managers (SOC 11-2021) | 395,240 | BLS OEWS May 2025 (press→BLS), `as_of 2026-08-16` | [sourced: BLS OEWS, fact — single-surfaced] |
| B2B / professional salespeople who regularly build decks | ~2–3M ⚙️ | derived: a fraction (~15–25%) of "Sales & Related" 13.4M (BLS OEWS May 2025, cross-checked vs FRED CPS LNU02032206) — excludes retail/cashier roles that don't make decks | [assumption] (the fraction is an estimate) |
| **Reachable US client-facing deck-makers** | **~3–4M** (mid ~3.5M) | sum, wide bars | [assumption] |

**Price input (annual, per seat):** competitor scan (`competitor-pricing.md`) clusters the
prosumer/business AI-deck tier at **~$10–20/mo/seat**. Take a blended **$15/mo = $180/yr** ⚙️ as the
first-pass anchor. Willingness-to-pay for Decksmith specifically is an open hypothesis (deferred to
Step 3 per the founder brief) — this is the *market* anchor, not our price.

**SAM = units × price:**
- Mid: 3.5M × $180 = **~$630M / yr**
- Band: 2M × $120 = ~$240M … 5M × $300 = ~$1.5B
- **SAM ≈ $0.3–1.5B / yr (US beachhead), midpoint ~$630M.** [assumption] — wide bars are expected and
  acceptable at concept-viability (the status asks "just enough to know it's worth chasing").

**TAM (global, directional):** all professionals who make presentations, worldwide. Global knowledge
workers ≈ 1B (Gartner, via aggregators — primary not reached, `as_of 2026-08-16`, [estimate, low]);
the deck-making, client-facing subset is far smaller. Order-of-magnitude TAM: **low single-digit $B
to ~$10B/yr**, consistent with the report-mill "presentation software" band below. Precise TAM is
`— to clarify —` (no reachable primary/analyst sizing exists).

**SOM (obtainable, ~3-yr horizon, unproven entrant):** an early share of the US beachhead SAM. At
0.5–2% capture → **~$3–12M ARR**, take **~$5M ARR** ⚙️ as a concept-stage 3-yr target. Rationale:
the category can grow fast (Gamma reached ~$100M ARR in ~2 yr — `competitor-dynamics.md`), but an
unproven entrant betting on a hard feasibility problem (`H-001`) should not assume hypergrowth.

## Top-down cross-check (soft — all report-mill, not anchor-grade)

Every reachable "presentation software / AI presentation" market figure is a **report-mill forecast**
with paywalled method → **forbidden zone for the number** (evidence-standards §2). Reported only as a
directional band, never as the headline:

| Figure | Publisher (class) | `as_of` |
|--------|-------------------|---------|
| Presentation software ~$8–9B today → ~$16–22B by 2030–33, ~11–15% CAGR | SNS Insider / Cognitive Market Research et al. (report-mill, forbidden zone) | 2026-08-16 |
| "AI presentation generation" $2.8B (2025) → $18.6B (2034), 23% CAGR | MarketIntelo (report-mill, single-sourced) | 2026-08-16 |

These diverge >20% on base/end-year and none exposes its method → **`[CONFLICT]`, not resolved.**
Bottom-up SAM ~$630M US is a plausible ~7–8% of a global ~$8–9B presentation market (US ≈ 40% of
software spend × an AI-deck slice) — **within an order of magnitude**, which is all the top-down band
can honestly support. **Bottom-up stays the headline.**

## Seeded hypotheses (→ register, `type: viability`)

- **H-008:** the reachable US beachhead is ~3–4M client-facing deck-makers at ~$180/yr → SAM
  ~$0.3–1.5B/yr — big enough to build a venture on. `tags: sizing`.

## Open items

- The B2B-sales fraction (~15–25%) is a ⚙️ estimate; a cleaner cut (deck-making B2B roles) would
  tighten SAM. `— to clarify —`.
- Revisit the price anchor once Step-3 pricing sets Decksmith's actual model.

## Change log

### 2026-08-16 — market sizing worked and projected
- **From → To:** empty → bottom-up SAM ~$0.3–1.5B (US beachhead), TAM directional, SOM ~$5M/3yr; H-008 seeded
- **Why:** Step 2 Act pass; size the prize roughly to confirm it's worth chasing (concept-viability)
- **Trigger:** Step 2 operating-loop pass, section `#market-sizing`; evidence from `loops-research`
