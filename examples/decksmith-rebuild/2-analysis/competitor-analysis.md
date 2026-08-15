---
node_type: worklog
tool: competitor-analysis
step: 2
fills: [competitors, competitor-strategy, competitor-pricing, competitor-dynamics]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — competitor-analysis (fills 4 sections)

Source: `../sources/market-research.md`. One worklog, four artifact sections.

## 1 · List (≥5 named; ≥1 not named by the team first; excluded ones given a reason)

The founder brief named **no competitor**; all of these came from the desk-research sweep (so every one is
"not named first" — the two-rival trap is avoided by construction).

| Player | Direct/Indirect | Enters detailed table? |
|--------|-----------------|------------------------|
| Gamma | direct | yes — shares segment + job (generate client decks) |
| Microsoft Copilot in PowerPoint | direct | yes — and **owns the native format we target** |
| Canva (AI 2.0 / Magic Design) | direct | yes — editable design objects, same wedge |
| Beautiful.ai | direct | yes — design-automation deck tool |
| Pitch | indirect | listed — collaboration-first, weaker AI-gen overlap |
| Tome | — | **excluded — shut its Slides product Apr 2025 and pivoted away.** A signal (standalone slides is hard), not a rival. |

## 2 · Strategy — the game each plays vs our moats

| Player | Game | How | Their moat vs ours |
|--------|------|-----|--------------------|
| Gamma | share + (rare) **profit** | web-first speed, viral PLG | distribution (70M users) + brand; **weak on native-editable export** ← our wedge |
| Copilot | revenue via bundle | agentic edit-in-place inside native PPT | owns PowerPoint + M365 distribution — **the biggest threat**; we have neither |
| Canva | share / ecosystem | conversational build of editable objects | 100M+ distribution, brand; closing the "editable" wedge |
| Beautiful.ai | niche revenue | template/rule-driven design automation | design rules; less AI-native, smaller |
| Pitch | team revenue | collaboration workflow | team lock-in; not a design/fidelity play |

Our moats (execution speed on the fidelity engine + design taste) are **thin vs distribution-rich incumbents**
— this reframes H-005 into a *speed* moat (see synthesis → H-009).

## 3 · Pricing scan (input to Step-3 pricing, NOT our price; read 2026)

| Player | Plan | Price | Confidence |
|--------|------|-------|------------|
| Gamma | Pro | ~$20/mo | [sourced: deckary 2026] (secondary) |
| Canva | Pro / Business | ~$15 / ~$25 per user | [sourced: Canva 2026] |
| Beautiful.ai | Pro / Team | $12/mo annual ($45 monthly) / $40 user | [sourced: g2 2026] (secondary) |
| Pitch | entry | ~$13/mo | [sourced: nextdocs 2026] (secondary) |
| Copilot | via M365 / Copilot Pro | ~$20–30 user (bundled) | [sourced: Microsoft 2026] |

Band: **~$13–25/mo standalone**; the bundled options ($0 marginal for M365/Canva seats) are the real price
pressure, not the standalone list prices.

## 4 · Dynamics (trend, to judge whose game is working; as_of 2026)

| Player | Metric | Trend | Confidence |
|--------|--------|-------|------------|
| Gamma | ARR / users / valuation | $100M+ ARR, 70M users, profitable 2+yr, $2.1B val (Nov 2025, a16z) — **rising fast** | [sourced: BusinessWire/TechCrunch 2025-11-10] (primary) |
| Tome | product line | **shut Slides product Apr 2025** after $81M raised — exited | [sourced] (secondary) |
| Copilot / Canva | feature cadence | 2026 agentic modes shipping — **accelerating into the wedge** | [sourced: Microsoft/Canva 2026] |

Whose strategy works: Gamma's PLG + Copilot/Canva's bundle. Tome's standalone-slides exit is the cautionary
dynamic for Decksmith's own shape.

## 5 · Seeds

- Threats → risks `R-001` (Gamma dominance), `R-002` (incumbent bundling), `R-003` (self-build — see
  `substitutes.md`), `R-004` (LLM dependency), `R-005` (low entry barrier). Detailed in `synthesis.md`.
- Rival-move assumption (incumbents close the wedge) → folded into `H-009` (moat/speed, synthesis).

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → 5 players + 1 excluded (Tome); game/pricing/dynamics captured; the native-editable gap at
  Gamma identified as the wedge; incumbent bundling identified as the top threat.
- **Why:** understand who plays what game and where the leader is weak.
- **Trigger:** Step-2 analysis, rebuild.
