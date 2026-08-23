---
node_type: artifact
artifact: analysis
step: 2
title: "Market & Competitive Analysis — Decksmith (fictional sample)"
status: draft
version: 0.1.1
updated: 2026-08-23
---

<!--
  Analysis artifact. Each section projects from its worklog in 2-analysis/. Section IDs, rests-on
  markers and column keys are stable. The point of this step is the CONCLUSION (#opportunity).
  Evidence is real: gathered by loops-research (web, as_of 2026-08-16), tagged and dated in the
  worklogs. Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting human approval.
-->

# Market & Competitive Analysis — Decksmith (fictional sample)

> Status: concept-viability · Owner: acting PO (agent) · Last review: 2026-08-16
> Feeds: `3-strategy.md` · seeds the risk register.

## Market sizing {#market-sizing}
<!-- tool: market-sizing -->
<!-- rests-on: 1#segments -->
_Bottom-up is the headline; the top-down band is a directional sanity check only (all top-down
figures are report-mill → not anchor-grade). Wide error bars are acceptable at concept-viability.
Price anchor from `#competitor-pricing`._

| Layer <!--c:layer--> | Value <!--c:value--> | Method <!--c:method--> | Key assumptions <!--c:assumptions--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|-------|-------|--------|-----------------|--------|------------|
| TAM | order of ~$ several billion–$10B/yr (directional) | top-down band, soft | all professionals who make presentations globally; no reachable primary sizing | report-mill band ($8–9B presentation sw); `— to clarify —` on the precise figure | [assumption] |
| SAM | **~$0.3–1.5B/yr** (mid ~$630M), US beachhead | bottom-up: units × price | ~3–4M US sales & marketing client-facing deck-makers × ~$180/yr blended anchor | BLS OEWS May 2025 (13-1161 900k, 11-2021 395k, a fraction of Sales 13.4M) — reached via BLS-derived tables + FRED (bls.gov 403'd direct fetch); `competitor-pricing` | [assumption] |
| SOM | **~$3–12M ARR** (take ~$5M), ~3-yr | bottom-up: 0.5–2% capture of SAM | unproven entrant on a hard feasibility bet; category can grow fast (Gamma $0→$100M in ~2 yr) | derived | [assumption] |

_Bottom-up SAM ~$630M is a plausible ~7–8% of a global ~$8–9B presentation market — within an order
of magnitude, all the report-mill top-down can honestly support. `[CONFLICT]` among top-down sources
left unresolved (see worklog)._

## Competitors {#competitors}
<!-- tool: competitor-analysis -->
<!-- rests-on: 1#segments, 1#jtbd -->
_Direct & indirect (substitutes are separate, below). 8-player sweep incl. a registry pick
(MagicSlides); the 5 sharing our segment AND job enter the detailed scans. Full sweep + exclusions in
the worklog._

| Competitor <!--c:name--> | Direct/Indirect <!--c:type--> | What they offer <!--c:offer--> | Confidence <!--c:conf--> |
|------------|-----------------|-----------------|------------|
| Gamma | direct | AI deck generator, card-based web canvas; designed look, lossy pptx export (class b, contested) | [sourced: help.gamma.app, as_of 2026-08-16] |
| Canva | direct | broad design suite + AI decks; pptx export partly rasterized (class b) | [sourced: canva help + press, as_of 2026-08-16] |
| Microsoft Copilot in PowerPoint | direct | prompt-to-deck inside PowerPoint; native/editable but generic design (class a) | [sourced: support.microsoft.com, as_of 2026-08-16] |
| Beautiful.ai | direct | smart-template web builder + AI; export "editable" vs reviews (class b, CONFLICT) | [sourced: beautiful.ai + press, as_of 2026-08-16] |
| Plus AI | direct | AI generator inside PPT/Google Slides; native but template-bound (class a) | [sourced: plusai.com, as_of 2026-08-16] |
| Presentations.ai | indirect | own format, one-way pptx export | [sourced: presentations.ai, as_of 2026-08-16] |
| Decktopus | indirect | quick pro decks; export exists, editability unverified | [assumption] |
| MagicSlides (registry pick) | indirect | Google Slides add-on, text→slides; speed/volume, not design | [sourced: Google Workspace Marketplace, as_of 2026-08-16] |

## Competitor strategy {#competitor-strategy}
<!-- tool: competitor-analysis -->
<!-- rests-on: 1#value-defensibility -->
_What game each plays vs our moats (`H-007`: corpus + taste)._

| Competitor <!--c:name--> | Game <!--c:game--> | How they play it <!--c:play--> | Their moats vs ours <!--c:moat--> | Confidence <!--c:conf--> |
|------------|------|------------------|---------------------|------------|
| Gamma | share / hypergrowth | freemium virality (70M users) → "replace PowerPoint"; a16z-backed | distribution + brand + data — strong; sacrifices native export fidelity (our axis) | [sourced: competitor-dynamics, as_of 2026-08-16] |
| Canva | share / ecosystem | bundle AI into a design empire; own distribution (265M MAU) | distribution + brand — dominant; general tool, deck export lossy | [sourced: competitor-dynamics, as_of 2026-08-16] |
| Microsoft Copilot | bundling / lock-in | ride 20M+ M365 Copilot seats into enterprise | distribution + lock-in — dominant; design generic, no taste/corpus edge | [sourced: competitor-dynamics, as_of 2026-08-16] |
| Beautiful.ai | niche / profit | smart templates; stable ~$13.5M rev | template IP + brand — modest; value trapped in its editor | [sourced: competitor-dynamics, as_of 2026-08-16] |
| Plus AI | wedge | add-in *inside* PPT/Slides → native by construction | integration/distribution; template-bound, not design-led | [sourced: competitor-dynamics, as_of 2026-08-16] |

_The field competes on **distribution** (Gamma/Canva/MS) and **integration** (Plus AI). None competes
on **native-and-designed quality** — where `H-007` bets our moat lives. The risk: distribution can
beat a quality edge if the gap is small or slow to show (`R-003`)._

## Competitor pricing {#competitor-pricing}
<!-- tool: competitor-pricing -->
_Input to Step-3 pricing, sizing's price anchor, and the financial model — not our price. Every price
read `as_of 2026-08-16`. Non-comparable tiers (enterprise "contact us", Canva Pro unreachable) in the
worklog reject table._

| Competitor <!--c:name--> | Plan / model <!--c:plan--> | Price (+ read date) <!--c:price--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|------------|--------------|-------|--------|------------|
| Gamma | per-seat + credits | Free · Plus $8/mo · Pro $18/mo · Ultra $100/mo (2026-08-16) | gamma.app/pricing | [sourced: med] |
| Beautiful.ai | flat / per-seat | Pro $12/mo · Team $40/user/mo · deck $45 (2026-08-16) | beautiful.ai/pricing | [sourced: high] |
| Microsoft Copilot | per-seat add-on | enterprise $30/user/mo · SMB "Copilot Business" $21 list / $18 promo (2026-08-17) + M365 base | microsoft.com pricing pages | [sourced: high] |
| Plus AI | per-seat + credits | Basic $10 · Pro $20 · Team $30 · Max $200 /mo (2026-08-16) | plusai.com/pricing | [sourced: high] |
| Presentations.ai | flat + credits | Free · Pro $20 · Gold $100 /mo (2026-08-16) | presentations.ai/pricing | [sourced: med] |
| Pitch | per-seat + credits | Free · Plus €10 · Team €15 · Business €20 /mo (2026-08-16) | pitch.com/pricing | [sourced: high] |

_Blended market anchor ⚙️ ≈ **$15/mo = $180/yr/seat**. The bundle (Copilot $18–30 by tier on top of
an existing M365 seat) and freemium tiers are the real WTP pressure — a paid standalone must beat
"already in PowerPoint." No >20% CONFLICT on entered figures._

## Competitor dynamics {#competitor-dynamics}
<!-- tool: competitor-dynamics -->
_Trend over time — whose strategy is working. Per-fact-type sourcing, `as_of` on every number._

| Competitor <!--c:name--> | Metric (revenue / headcount / …) <!--c:metric--> | Trend + period <!--c:trend--> | Source (+ date) <!--c:source--> | Confidence <!--c:conf--> |
|------------|----------------------------------|----------------|-----------------|------------|
| Gamma | valuation / ARR / users | $2.1B val (Nov 2025); ARR ~$100M up from ~$30M (2024); ~70M users | TechCrunch + SiliconANGLE + Sacra, cross-checked (as_of 2026-08-16; URLs in worklog) | [sourced: TechCrunch + SiliconANGLE + Sacra] fact — high |
| Canva | valuation / ARR / users | ~$42B val (Aug 2025); ~$4B ARR run-rate, B2B ~2× YoY; 265M MAU | Sacra + TechCrunch (as_of 2026-08-16) | [sourced: Sacra + TechCrunch] fact — high |
| Microsoft Copilot | paid seats | M365 Copilot 15M seats +160% YoY (FY26 Q2) → 20M+ (FY26 Q3); PPT-specific not disclosed | Microsoft earnings via press, two quarters (URLs in worklog) | [sourced: Microsoft earnings via press] fact — high |
| Beautiful.ai | revenue / funding | ~$13.5M rev (2025); funding CONFLICT $16M vs $61M | getlatka / tracxn (as_of 2026-08-16) | [sourced: getlatka / tracxn] estimate — low |
| Plus AI | funding / ARR | — to clarify — (bootstrapped, no disclosed round; one aggregator ~$47.5M ARR, unverified) | getlatka only (as_of 2026-08-16) | [assumption] low — single aggregator, unverified |
| Tome (exited) | status | shut down Mar 2025 (sunset date — to clarify —); pivoted to sales AI | Forbes (shutdown) + Semafor (2024 layoffs) | [sourced: Forbes + Semafor] fact — high |
| Pitch (exited) | status / ARR | Jan 2024 reset (~78% layoffs); ~$10M ARR (est.); → sales enablement | Sacra (single-source estimate) | [sourced: Sacra] estimate — med-high; single source |

_Accelerating into our space: Gamma (clearest threat), Canva, Microsoft (bundle). Retreated: Tome,
Pitch — validating the free-virality monetization trap (`R-005`), but retreating *toward* the
sales/marketing niche, so it is contested, not empty._

## Substitutes {#substitutes}
<!-- tool: substitutes -->
<!-- rests-on: 1#jtbd -->
_Non-obvious competition incl. do-nothing / do-it-manually / self-build. Full map (6 substitutes +
self-build threshold) in the worklog._

| Substitute <!--c:substitute--> | How it does the job today <!--c:job--> | Why a customer would stay with it <!--c:why--> | Confidence <!--c:conf--> |
|------------|---------------------------|-----------------------------------|------------|
| do-nothing | reuse last quarter's deck, swap numbers | zero cost/risk; wins when low-stakes or brutal deadline | [assumption] |
| do-it-manually (status quo) | build in PowerPoint/Slides/Keynote by hand | habit + control — the dominant substitute and the real competitor | [assumption] |
| self-build (internal template / python-pptx) | ops team maintains a locked corporate template | wins above the volume + design-team + brand-governance threshold | [assumption] |
| hire a designer / agency | outsource to a human | highest-stakes one-shots where quality > speed | [assumption] |
| general AI chat (ChatGPT/Claude) → paste in | LLM writes content, human formats | does the words, not the designed editable file — leaves the restyle tax | [assumption] |
| bundled incumbent (Copilot/Gemini in-suite) | deck-gen inside the paid suite | "free, already-here, native" — a real threat (`R-002`) | [sourced: competitor-dynamics, as_of 2026-08-16] |

## Niche risks {#niche-risks}
<!-- synthesis: light Five Forces -->
_Structural risks of the niche (light Five Forces). Seeded to the risk register R-001…R-006._

| Risk <!--c:risk--> | Force <!--c:force--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | → `R-…` <!--c:register--> | Confidence <!--c:conf--> |
|------|-------|------------|--------|---------|------------|
| Funded incumbents accelerating (Gamma, Canva) | rivalry | H | H | R-001 | [sourced: competitor-dynamics, as_of 2026-08-16] |
| Bundled substitutes (Copilot/Gemini in-suite) | substitution | H | H | R-002 | [sourced: substitutes, as_of 2026-08-16] |
| Low entry barriers / thin moat unless corpus+taste holds | entry barriers | H | H | R-003 | [assumption] |
| Foundation-model supplier power (price/access) | supplier power | M | M | R-004 | [assumption] |
| Monetization trap (free virality kills — Tome/Pitch) | buyer power | M | H | R-005 | [sourced: competitor-dynamics, as_of 2026-08-16] |
| Platform/format dependency (.pptx/.key owned by others) | substitution/dependency | L | M | R-006 | [assumption] |

## Opportunity {#opportunity}
<!-- synthesis -->
_The "so what" — the point of the step._

- **Opportunity / threat:** the **editable-AND-designed corner is genuinely unoccupied** and is
  Decksmith's wedge. The field splits exactly along the thesis — **design-led tools (Gamma, Canva,
  Beautiful.ai) trap value in their web editor with lossy pptx export ("pretty-but-locked")**, while
  **native-export tools (Plus AI, Copilot, MagicSlides) sacrifice design ("editable-but-ugly")**. The
  field split is observed [sourced: competitor-analysis, as_of 2026-08-16]; that **no** opened tool
  does both is an **inference** [assumption] — it supports (does not prove) `H-001`, and it rests on a
  scan, not a hands-on export test (see `#to-clarify`). The corner is **contested, not safe**:
  Gamma/Canva/Microsoft are racing and Tome/Pitch retreated toward the same niche.
- **The sharpest conclusion (⚙️):** win the editable-and-designed corner for client-facing
  sales/marketing decks by **proving `H-001` faster than Gamma/Canva can make their export truly
  native**, and monetize deliberately to dodge the Tome/Pitch free-virality trap (`R-005`).
- **Why now:** AI generation quality crossed the threshold where editable-and-designed is buildable
  [assumption] (this *is* `H-001`, not an evidenced fact); the category is exploding (Gamma $0→$100M
  ARR in ~2 yr) [sourced: competitor-dynamics, as_of 2026-08-16] yet nobody has solved it
  [assumption] (the scan-based inference above) — a real but narrow window before an incumbent closes
  the export gap [assumption].

## Seeded hypotheses {#hypotheses}
_Market/sizing/white-space assumptions carried into the hypothesis register._

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | From section <!--c:from--> | Confidence <!--c:conf--> |
|----|------------|------|--------------|------------|
| H-008 | US beachhead ~3–4M deck-makers × ~$180/yr → SAM ~$0.3–1.5B — worth chasing | viability | market-sizing | [assumption] |
| H-009 | The editable-AND-designed corner is genuinely unoccupied — the white space is real | viability | opportunity | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced by the agent for the human to resolve._

- **The white space rests on a scan, not a file test.** No competitor's exported `.pptx` was opened
  and inspected for real-shape editability — Gamma's class (a vs b) and Decktopus's editability are
  `contested`/`[assumption]`. A hands-on export inspection of 2–3 rivals is the cheapest way to harden
  `H-009` (and it doubles as an `H-001` design-bar reference). ⚙️ recommend running it in Step 5–6.
- **Top-down market size is `— to clarify —`.** All reachable figures are report-mill; treat only the
  bottom-up SAM as anchor-grade.
- **Bottom-up SAM's B2B-sales fraction (~15–25%) is a ⚙️ estimate** — a cleaner "deck-making B2B
  roles" cut would tighten it.
- **Plus AI's traction is `— to clarify —`** (bootstrapped, no disclosed funding) — sizing it as a
  threat needs a primary source.

## Change log

### 2026-08-23 — confidence-tag grammar normalized
- **From → To:** compound tags (`[sourced, fact — high]`, `[assumption: …]`, bare `[sourced]`) →
  canon grammar (`[sourced: <where>]` / `[assumption]`), qualifiers moved into notes
- **Why:** the tag vocabulary check (lint D2) is promoted to ERROR; the shipped example must model
  the grammar it teaches
- **Trigger:** run-2 hardening — the local model copied the example's compound-tag style

### 2026-08-17 — human review pass: evidence findings returned and fixed
- **From → To:** (1) the general-AI-chat substitute row `[sourced: competitor-dynamics]` →
  `[assumption]` — the cited worklog says nothing about AI chat (citation laundering caught in
  review); (2) `#opportunity` "why now" — untagged load-bearing clauses now carry per-clause tags
  (the buildability claim is `H-001` itself, not evidence); (3) Copilot pricing row gains the $30
  enterprise tier next to the SMB $18/$21; (4) dynamics source cells corrected (Tome:
  Semafor→Forbes; Pitch: single-source Sacra estimate, ~78% layoffs; Copilot seats: two-quarter
  series, not a CONFLICT) — openable URLs now in `2-analysis/competitor-dynamics.md`
- **Why:** the run was committed raw as the honest demonstration; this pass is the human review the
  loop prescribes — findings sent back, fixed at the worklog first, re-projected here
- **Trigger:** human review of the finished run (three review lenses); re-verification via fresh
  `loops-research` briefs, read 2026-08-17

### 2026-08-16 — Step 2 analysis worked and projected
- **From → To:** — → all sections filled from real web research (`loops-research`, `as_of
  2026-08-16`): bottom-up SAM ~$0.3–1.5B, 8-player competitor sweep, dated pricing, dynamics
  (Gamma/Canva/MS up; Tome/Pitch out), substitutes, 6 niche risks (R-001…R-006), and the white-space
  opportunity call; H-008/H-009 seeded
- **Why:** Step 2's job is an explicit opportunity/threat conclusion — the editable-and-designed
  corner is unoccupied but contested; every external claim is dated and cross-checked, report-mill
  numbers refused as anchors
- **Trigger:** Step 2 operating-loop pass; four parallel `loops-research` briefs, integrated and
  synthesised by the orchestrator
