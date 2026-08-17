---
node_type: worklog
tool: competitor-dynamics
step: 2
title: "competitor-dynamics — the working"
updated: 2026-08-16
version: 0.1.0
---

# competitor-dynamics — the working

_Source of truth for `2-analysis.md#competitor-dynamics`. Trend per player from public sources,
per-fact-type, `as_of` on every number. Evidence from a `loops-research` brief, all read
`as_of 2026-08-16`._

## Trend per detailed-table player

| Player | Metric | Value + period | Trend | Source (class) | Conf |
|--------|--------|----------------|-------|----------------|------|
| **Gamma** | valuation / ARR / users | $2.1B val (Nov 2025 Series B, a16z); ARR ~$100M (Oct 2025) up from ~$30M end-2024; ~70M users, 600k+ paying, ~50 staff | ▲▲ accelerating hard | BusinessWire (primary) + TechCrunch (press) + Sacra (database), cross-checked | [sourced, fact — high] |
| **Canva** | valuation / ARR / users | ~$42B val (Aug 2025) up from $32B; ~$3.5B rev 2025, ~$4B ARR run-rate, B2B ~$500M ARR (~2× YoY); 265M MAU | ▲ accelerating | Sacra (database) + TechCrunch (press), cross-checked | [sourced, fact — high] |
| **Microsoft (Copilot)** | paid seats | M365 Copilot 20M+ paid seats (2025/26), +160% YoY; PowerPoint-specific usage not disclosed | ▲ accelerating (bundled) | Microsoft-reported (primary) + press (CONFLICT 15M vs 20M, different dates → range) | [sourced, fact — med-high] |
| **Beautiful.ai** | funding / revenue | ~$13.5M revenue (Oct 2025); funding **CONFLICT $16M vs $61M** (aggregators disagree) | → stable niche | getlatka / tracxn (database/estimate) | [sourced, estimate — low; funding CONFLICT unresolved] |
| **Plus AI** | funding / ARR | `— to clarify —` — bootstrapped, no disclosed round; one aggregator estimates ~$47.5M ARR (unverified) | growing, undisclosed | getlatka (aggregator) only | [assumption — low] |
| **Tome** *(exited)* | status | killed Tome Slides ~Apr 2025 (announced Mar 2025); 20% layoff Apr 2024; <$4M ARR on 20M users; pivoted to sales AI | ◼ retreated/pivoted | Semafor (press) + Tome.com (primary) | [sourced, fact — high] |
| **Pitch** *(exited)* | status / ARR | Jan 2024 reset: ~2/3 layoffs, returned most VC, employees own ~80%; ARR ~$10M (Feb 2025) up from ~$5M; repositioned to sales enablement | ◼ retreated/reset | Sacra (database) + TechCrunch (press) | [sourced, fact — high] |

## Read (whose strategy is working)

- **Accelerating into our space:** **Gamma** (the clearest threat — ~$100M ARR in ~2 yr on 50
  people, explicitly replacing PowerPoint), **Canva** (biggest in absolute terms, owns distribution),
  **Microsoft** (bundling Copilot into seats everyone already has).
- **Retreated (space vacated, but contested):** **Tome** and **Pitch** both exited consumer AI decks
  — validating that **free-user virality without monetization is the category trap**. Crucially, both
  retreated *toward* sales/marketing (Tome "make deals not decks"; Pitch → sales enablement) — so the
  client-deck niche is **contested, not empty**.
- **Beautiful.ai** is a stable lateral, not a leading threat.

Seeds `synthesis.md` niche-risks: rival acceleration (Gamma/Canva) and Microsoft bundling.

## Change log

### 2026-08-16 — competitor dynamics worked and projected
- **From → To:** empty → trend per player; Gamma/Canva/MS accelerating, Tome/Pitch exited
- **Why:** Step 2 Act pass; compare whose strategy works, feed the niche-risk read
- **Trigger:** Step 2 pass, section `#competitor-dynamics`; evidence from `loops-research`
