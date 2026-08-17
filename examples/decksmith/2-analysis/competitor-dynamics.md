---
node_type: worklog
tool: competitor-dynamics
step: 2
title: "competitor-dynamics — the working"
updated: 2026-08-17
version: 0.1.1
---

# competitor-dynamics — the working

_Source of truth for `2-analysis.md#competitor-dynamics`. Trend per player from public sources,
per-fact-type, `as_of` on every number. Evidence from a `loops-research` brief, all read
`as_of 2026-08-16`._

## Trend per detailed-table player

| Player | Metric | Value + period | Trend | Source (class) | Conf |
|--------|--------|----------------|-------|----------------|------|
| **Gamma** | valuation / ARR / users | $2.1B val (Nov 2025 Series B, a16z); ARR ~$100M (Oct 2025) up from ~$30M end-2024; ~70M users, 600k+ paying, ~50 staff | ▲▲ accelerating hard | TechCrunch + SiliconANGLE (press) + Sacra (database), cross-checked | [sourced, fact — high] |
| **Canva** | valuation / ARR / users | ~$42B val (Aug 2025) up from $32B; ~$3.5B rev 2025, ~$4B ARR run-rate, B2B ~$500M ARR (~2× YoY); 265M MAU | ▲ accelerating | Sacra (database) + TechCrunch (press), cross-checked | [sourced, fact — high] |
| **Microsoft (Copilot)** | paid seats | M365 Copilot 15M paid seats +160% YoY (FY26 Q2, Jan 2026) → 20M+ (FY26 Q3, Apr 2026); PowerPoint-specific usage not disclosed | ▲ accelerating (bundled) | Microsoft earnings via press, two quarters (a time series, not a conflict) | [sourced, fact — high] |
| **Beautiful.ai** | funding / revenue | ~$13.5M revenue (Oct 2025); funding **CONFLICT $16M vs $61M** (aggregators disagree) | → stable niche | getlatka / tracxn (database/estimate) | [sourced, estimate — low; funding CONFLICT unresolved] |
| **Plus AI** | funding / ARR | `— to clarify —` — bootstrapped, no disclosed round; one aggregator estimates ~$47.5M ARR (unverified) | growing, undisclosed | getlatka (aggregator) only | [assumption — low] |
| **Tome** *(exited)* | status | shut down Mar 2025, most of ~70 staff laid off (exact sunset date `— to clarify —`); 20% layoff Apr 2024; <$4M ARR on 20M users; pivoted to sales AI | ◼ retreated/pivoted | Forbes (press, Mar 2025 shutdown) + Semafor (press, Apr 2024 layoffs); tome.com unreachable (domain sold) | [sourced, fact — high] |
| **Pitch** *(exited)* | status / ARR | Jan 2024 reset: ~78% layoffs (180→40), returned most VC, employees own ~80%; ARR ~$10M (Feb 2025, Sacra estimate) up from ~$5M; repositioned to sales enablement | ◼ retreated/reset | Sacra (database; single source on the ARR estimate) | [sourced, estimate — med-high] |

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

## Sources — openable URLs (each fetched and confirmed to contain the figure, read 2026-08-17)

- **Gamma** $2.1B / $100M ARR: <https://techcrunch.com/2025/11/10/ai-powerpoint-killer-gamma-hits-2-1b-valuation-100m-arr-founder-says/>
  (TechCrunch, 2025-11-10); cross-checks <https://siliconangle.com/2025/11/10/ai-powered-visual-presentation-platform-gamma-raises-68m-2-1b-valuation/>
  and <https://sacra.com/c/gamma/> ($102M est., Oct 2025). Both press pieces trace to Gamma's own
  announcement — the valuation is a company *statement*, not a measured fact.
- **Canva** $42B / ~$4B ARR / B2B $500M: <https://sacra.com/c/canva/>; 265M MAU (COO-stated):
  <https://techcrunch.com/2026/02/18/canva-gets-to-4b-in-revenue-as-llm-referral-traffic-rises/>.
- **Microsoft 365 Copilot** seats: 15M +160% YoY (FY26 Q2) <https://office365itpros.com/2026/01/30/microsoft-fy26-q2-results/>;
  20M (FY26 Q3) <https://www.nojitter.com/ai-automation/microsoft-365-copilot-hits-20-million-paid-seats>
  — both citing Microsoft earnings calls.
- **Tome** Mar 2025 shutdown + pivot: <https://www.forbes.com/sites/rashishrivastava/2026/07/20/ai-startups-are-pivoting-from-flashy-demos-to-tech-that-pays-the-bills/>;
  Apr 2024 layoffs: <https://www.semafor.com/article/04/16/2024/ai-startup-tome-lays-off-staff-to-focus-on-revenue>.
- **Pitch** reset + ~$10M ARR (estimate): <https://sacra.com/c/pitch/> — single source, no independent second read.
- **Beautiful.ai** ~$13.5M rev: <https://getlatka.com/companies/beautiful.ai> — Latka's own estimate,
  no method shown; kept `[sourced, estimate — low]`.

## Change log

### 2026-08-17 — human review pass: openable URLs attached, three sub-facts corrected
- **From → To:** publisher-level citations → per-player openable URLs (each fetched 2026-08-17);
  Tome's shutdown re-sourced Semafor→Forbes (the Semafor piece covers only the Apr-2024 layoffs;
  the ~Apr-2025 sunset date demoted to `— to clarify —`); Pitch layoffs ~2/3 → ~78% (180→40) and its
  ARR marked single-source estimate; Copilot 15M-vs-20M "CONFLICT" resolved into a two-quarter time
  series (15M +160% FY26 Q2 → 20M+ FY26 Q3)
- **Why:** the evidence standard wants citations a stranger can open; the re-verification pass also
  surfaced that two original attributions didn't hold
- **Trigger:** human review pass on the finished run (evidence lens); re-verified via fresh research
  briefs

### 2026-08-16 — competitor dynamics worked and projected
- **From → To:** empty → trend per player; Gamma/Canva/MS accelerating, Tome/Pitch exited
- **Why:** Step 2 Act pass; compare whose strategy works, feed the niche-risk read
- **Trigger:** Step 2 pass, section `#competitor-dynamics`; evidence from `loops-research`
