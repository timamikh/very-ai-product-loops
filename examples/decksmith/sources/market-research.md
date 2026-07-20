---
node_type: source
source: market-research
product: "Decksmith (fictional sample)"
captured: 2026-07-21
updated: 2026-07-21
---

# Source — Market research digest (AI presentation tools)

> Output of the `analytics-search` tool: a triangulated desk-research pass distilled into a sourced
> digest that feeds `market-sizing`, `competitor-analysis`, `substitutes`, and the risk register.
> **Decksmith is fictional; the market and competitors below are real, public information** (dated).
> Rule: one source → `[assumption]`; ≥2 independent → `[sourced]`. Conflicts are surfaced, not averaged.

**Questions this answers:** How big is the market and how fast is it growing? Who are the main
players and how are they doing? What do they charge? What are the key trends and barriers — and
where is the leader weak?

## Size signals

| Metric | Value | Source | Date | Confidence |
|--------|-------|--------|------|------------|
| Presentation software market (broad) | ~$7.3–8.2B (2025) → ~$8.6–9.7B (2026); CAGR ~13–17% | SNS Insider; verifiedmarketreports; thebusinessresearchcompany | 2025–2026 | [sourced] (multiple reports, range) |
| AI presentation *generation* segment (2025) | **Diverges: $1.94B / $2.8B / $3.1B** depending on report | marketintelo; researchandmarkets; 2slides | 2025–2026 | [sourced] but **conflicting** |
| AI presentation *generation* segment (2026) | ~$4.7B (one report; +52% YoY) | 2slides / marketintelo | 2026 | [assumption] (single-source, high figure) |
| AI segment growth | CAGR ~23–26% → ~$18.6B by 2034 | marketintelo; 2slides | 2026 | [sourced] |
| North America share of AI segment | ~38.5% (~$1.08B, 2025) | marketintelo | 2025 | [assumption] (single-source) |

## Dynamics & trends

| Signal | So-what | Source | Date |
|--------|---------|--------|------|
| AI-slide market growing ~2–4× faster (CAGR ~23–26%) than broad presentation SW (~13–17%) | Demand for the *job* is real and accelerating — validates chasing it | market reports (above) | 2026 |
| "Editable design objects" becoming the headline feature (Canva AI 2.0, Copilot agentic) | Decksmith's "editable + designed" wedge is being actively contested by incumbents | Canva; Microsoft | 2026 |
| Agentic modes: AI edits the deck *in place* (Copilot in native PPT; Canva conversational) | The bar is moving from "generate a draft" to "edit my real file to my brand" | Microsoft; Canva | 2026 |
| Enterprise adoption of AI presentations >60%; consulting/education/SaaS >75% | Buyers with budget (incl. the lead segment) are already adopting | 2slides "State of AI Presentations 2026" | 2026 |

## Barriers · risks · drivers

| Item | Type | So-what | Seeds |
|------|------|---------|-------|
| Gamma is the dominant, *profitable* leader ($100M+ ARR, 70M users, $2.1B val) | risk (rivalry) | Displacing "the AI deck tool" head-on is very hard | `R-001` |
| Incumbents (Microsoft Copilot in PPT, Canva) bundle native-editable AI generation | risk (substitution) | They own distribution + the native formats Decksmith targets | `R-002` |
| Capable users can self-build: prompt a general LLM (ChatGPT/Claude) + hand-format | risk (self-build) | Caps willingness to pay for "just generate slides" | `R-003` |
| Engine quality depends on third-party LLMs (cost/availability) | risk (dependency) | COGS + capability outside our control | `R-004` |
| Low entry barrier for "AI slide wrapper"; hard barrier only for true native-fidelity engine | driver + risk | The moat must be the *fidelity engine*, not the app | `R-005`, `H-004` |
| **Gamma's `.pptx` export flattens 30–40% of slides into uneditable images**; web-first data model, fonts substitute, layouts break | **driver (white space)** | The leader is weak exactly on *native editable + designed* — Decksmith's thesis | `H-005` |

## Main players

| Player | Position / notable | Source | Date |
|--------|--------------------|--------|------|
| **Gamma** | Category leader; web-first generator. Founded 2020, launched 2022; Nov 2025 raised $68M Series B at **$2.1B valuation** (a16z); **70M users, 600k+ paying, $100M+ ARR, profitable 2+ yrs, ~50 staff**; 400M+ assets created. **But** its PPTX export breaks (flatten-to-image). | businesswire; techcrunch; siliconangle; slidegmm/wps (export) | 2025-11-10 / 2026 |
| **Microsoft Copilot in PowerPoint** | Incumbent; 2026 **Agentic Mode** edits native PPT in place (adapt deck to corporate brand, executes). Bundled with M365 / Copilot Pro. | Microsoft; deckary | 2026 |
| **Canva (AI 2.0 / Magic Design)** | Incumbent giant; conversational AI builds **fully editable design objects** ("10-slide pitch deck in brand colors in 22s"). Pro tier + AI credit pool. | Canva; eesel | 2026 |
| **Beautiful.ai** | Design-automation deck tool; template/rule-driven. | g2; scribe | 2026 |
| **Pitch** | Collaborative deck tool, startup/team-oriented. | nextdocs | 2026 |
| **Tome** | Raised $81M then **shut its Slides/presentation product (Apr 2025)** and pivoted away. | (AI-presentation market coverage) | 2025-04 |

## Pricing scan (input to Step 3 pricing / Step 4 model — not our price)

| Player | Plan / model | Price | Source | Date |
|--------|--------------|-------|--------|------|
| Gamma | Pro (paid tier) | ~$20 / mo | deckary | 2026 |
| Canva | Pro / Business | ~$15 / mo (Pro); ~$25 / user (Business) | Canva; aiproductivity | 2026 |
| Beautiful.ai | Pro / Team | $12/mo annual ($45 monthly); Team $40/user/mo | g2; scribe; costbench | 2026 |
| Pitch | entry | from ~$13 / mo | nextdocs | 2026 |
| Microsoft Copilot | via M365 / Copilot Pro | ~$20–30 / user/mo (bundled) | Microsoft; prezent | 2026 |

## Conflicts noted
- **AI-segment market size diverges 2–3×** across reports ($1.94B vs $2.8B vs $3.1B for 2025; $4.7B for 2026). Do **not** average — use as a wide-error-bar range and lean on bottom-up SAM instead (per `market-sizing`).
- Broad "presentation software" market and "AI presentation generation" segment are **different scopes** — don't mix the two headline numbers.

## Reliability note
Vendor/comparison-site and SEO-blog sources (pricing, Gamma-export behavior) are **secondary**; funding/valuation facts are from primary press (BusinessWire) + major outlets (TechCrunch, SiliconANGLE) and are stronger. Tagged accordingly.

**Feeds:** `market-sizing` (size) · `competitor-analysis` (players/pricing/dynamics) · `substitutes` · `risk-mitigation`.
**Seeded registers:** `H-005` (native-fidelity white space) · `H-006` (market big/growing enough) → hypotheses; `R-001…R-005` → risks.

## Sources (URLs)
- https://www.businesswire.com/news/home/20251110805751/en/ — Gamma $100M ARR / $2.1B valuation (2025-11-10)
- https://techcrunch.com/2025/11/10/ai-powerpoint-killer-gamma-hits-2-1b-valuation-100m-arr-founder-says/
- https://siliconangle.com/2025/11/10/ai-powered-visual-presentation-platform-gamma-raises-68m-2-1b-valuation/
- https://www.slidegmm.ai/en/blog/gamma-export-powerpoint-quality-guide — Gamma PPTX export flatten-to-image
- https://www.wps.com/blog/gamma-ai-export-to-powerpoint-how-to-convert-ai-presentations-into-editable-pptx-slides/
- https://www.snsinsider.com/reports/presentation-software-market-8545 — broad market size
- https://marketintelo.com/report/ai-presentation-generation-market — AI-segment size/CAGR
- https://2slides.com/blog/state-of-ai-presentations-2026-trends-stats-predictions — AI trends/stats
- https://powerpoint.cloud.microsoft/create/en/copilot-in-powerpoint/ — Copilot agentic in PPT
- https://www.buildfastwithai.com/ai-tools/canva-magic-design — Canva AI 2.0 editable objects
- https://www.g2.com/products/beautiful-ai-beautiful-ai/pricing ; https://www.nextdocs.io/compare/beautiful-ai-vs-pitch — pricing
