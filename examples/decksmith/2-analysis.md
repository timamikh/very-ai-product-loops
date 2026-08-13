---
node_type: artifact
artifact: analysis
product: Decksmith (fictional sample)
step: 2
status_stage: concept-viability
owner: sample
updated: 2026-08-13
version: 0.1.0
---

# Market & Competitive Analysis — Decksmith (fictional sample)

> Status: `concept-viability` · Owner: sample · Last review: 2026-07-21
> Feeds: `3-strategy.md` · seeds the risk register (`registers/risks.md`).
> Fictional product; **the market and competitors are real, public information** (dated). Evidence
> lives in the step worklogs (`2-analysis/`), which cite the raw sources. At concept stage, sizing
> leans on a bottom-up SAM with wide error bars.

## Market sizing {#market-sizing}
<!-- tool: market-sizing -->

**Arena / segment sized:** AI-generated client-facing decks for the lead segment — salespeople &
marketers who make decks often, in English-first paying markets (job: see `1-passport.md#jtbd`).

**TAM / SAM / SOM**

| Level <!--c:layer--> | Estimate <!--c:value--> | How it was calculated <!--c:method--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|-------|----------|-----------------------|--------|------------|
| TAM (total addressable) | AI presentation-generation segment ~$2.8–4.7B (2026), inside a ~$8.6B broad presentation-software market; segment CAGR ~23–26% | top-down, published reports (range, not a point) | worked in `market-sizing` | [sourced] (reports diverge 2–3× — used as a range) |
| SAM (serviceable addressable) | **≈ $750M/yr** | **bottom-up: ~5M reachable frequent deck-making sales/marketing pros in paying English-first markets × ~$150/yr** | bottom-up (inputs illustrative) | [assumption] |
| SOM (serviceable obtainable) | **≈ $4M ARR in ~3 yr** | ~0.5% of SAM captured early, given Gamma's dominance + incumbent entry | reasoned share | [assumption] |

_SAM is the load-bearing number and is bottom-up; the divergent published TAM figures are only a
cross-check (per `market-sizing` — do not average conflicting reports)._

**Key assumptions (traced)**

| Assumption <!--c:assumption--> | Value <!--c:value--> | Source <!--c:source--> | Confidence <!--c:conf--> | → register <!--c:register--> |
|------------|-------|--------|------------|------------|
| Reachable frequent deck-makers (lead segment, paying markets) | ~5M | illustrative | [assumption] | `H-006` (viability) |
| Price per user / year | ~$150 (≈ incumbent paid tiers) | competitor pricing (below) | [sourced: market-research] → [assumption] for us | `H-006` |
| Early obtainable share (3 yr) | ~0.5% of SAM | reasoned vs leader/incumbents | [assumption] | `H-006` |

## Competitors {#competitors}
<!-- tool: competitor-analysis -->

| Competitor <!--c:name--> | Direct/Indirect <!--c:type--> | What they offer <!--c:offer--> | Confidence <!--c:conf--> |
|------------|-----------------|-----------------|------------|
| **Gamma** | direct | Web-first AI generator; fast, polished decks/sites/docs (category leader) | [sourced: market-research] |
| **Microsoft Copilot in PowerPoint** | direct (incumbent) | Agentic AI that generates and edits **native PPT** in place | [sourced: market-research] |
| **Canva (AI 2.0 / Magic Design)** | direct (incumbent) | Conversational AI building **editable design objects** in Canva | [sourced: market-research] |
| **Beautiful.ai** | direct | Rule/template-driven design automation for decks | [sourced: market-research] |
| **Pitch** | direct | Collaborative, team-oriented deck tool | [sourced: market-research] |
| General LLMs (ChatGPT / Claude) | indirect | Generate outline + copy; the user formats the slides | [sourced: market-research] |
| Tome | (exited) | Raised $81M, then **shut its Slides product (Apr 2025)** — a cautionary exit | [sourced: market-research] |

## Competitor strategy {#competitor-strategy}
<!-- tool: competitor-analysis -->

| Competitor <!--c:name--> | Game <!--c:game--> | How they play it <!--c:play--> | Their moats vs ours <!--c:moat--> | Confidence <!--c:conf--> |
|------------|------|------------------|---------------------|------------|
| Gamma | Growth + share (profitably) | Web-first speed, agentic design, own platform/format; $100M ARR | Brand + distribution + design-corpus data (strong). **Weak on native `.pptx`/`.key` fidelity** — our wedge | [sourced: market-research] |
| Microsoft Copilot | Ecosystem lock-in | Bundle Copilot into M365; agentic edits in the *native* format everyone already uses | Owns the native format + distribution (very strong). Design taste / audience narrative generic | [sourced: market-research] |
| Canva | Share + ecosystem | Freemium scale; AI across a whole design suite | Huge audience + brand. Generalist, not a deck-*narrative* specialist | [sourced: market-research] |
| Beautiful.ai | Niche profit | Design-rule automation, consistency | Design consistency; less AI-native, weaker narrative | [assumption] |
| Pitch | Team/collab niche | Collaboration-first | Collaboration; not a design/fidelity leader | [assumption] |

_Our intended moat (`passport#value-defensibility`, `H-004`) is a native-fidelity editable-and-designed
engine. Gamma is weak exactly there; Copilot is strong on native but weak on design/narrative._

## Competitor pricing {#competitor-pricing}
<!-- tool: competitor-analysis -->
_Input to our own pricing (Step 3) and the Step-4 model — not our price._

| Competitor <!--c:name--> | Plan / model <!--c:plan--> | Price <!--c:price--> | Source <!--c:source--> | Confidence <!--c:conf--> |
|------------|--------------|-------|--------|------------|
| Gamma | Pro | ~$20 / mo | worked in `competitor-analysis` | [sourced] |
| Canva | Pro / Business | ~$15 / mo · ~$25 / user | worked in `competitor-analysis` | [sourced] |
| Beautiful.ai | Pro / Team | $12/mo annual ($45 monthly) · $40/user (Team) | worked in `competitor-analysis` | [sourced] |
| Pitch | Entry | from ~$13 / mo | worked in `competitor-analysis` | [sourced] |
| Microsoft Copilot | Bundled (M365 / Copilot Pro) | ~$20–30 / user/mo | worked in `competitor-analysis` | [sourced] |

## Competitor dynamics {#competitor-dynamics}
<!-- tool: competitor-analysis -->
_Trend over time — whose strategy is working. Source: public financials / press / registries
appropriate to the company's jurisdiction._

| Competitor <!--c:name--> | Metric <!--c:metric--> | Trend + period <!--c:trend--> | Source (+ date) <!--c:source--> | Confidence <!--c:conf--> |
|------------|--------|----------------|-----------------|------------|
| Gamma | ARR / users / valuation | $0 → **$100M ARR in ~3 yr**; 70M users; **$2.1B** valuation (Series B) — profitable 2+ yrs | BusinessWire / TechCrunch, 2025-11-10 | [sourced] |
| Tome | Product line | **Shut its Slides product, Apr 2025**, after an $81M raise — pivoted away | market coverage, 2025 | [sourced] |
| Microsoft / Canva | Feature velocity | Shipping agentic / AI-2.0 deck generation through 2026 | vendor, 2026 | [sourced] |

## Substitutes {#substitutes}
<!-- tool: substitutes -->
_Competition scored against the customer's **job** (`passport#jtbd`: a credible client deck fast,
without redoing it by hand), not our category. The baseline three are always listed._

| Substitute | Whose job it does | Why the customer chooses it | When it wins against us | → Risk | Confidence |
|------------|-------------------|-----------------------------|-------------------------|--------|------------|
| Do nothing (status quo) | Present a plain/templated deck as-is | "Good enough" for low-stakes meetings | Meeting is low-stakes; look doesn't matter | — | [assumption] |
| Do it manually | Build in PowerPoint/Keynote/Canva by hand, or brief a designer | Full control, on-brand, trusted result | High-stakes flagship decks; brand-critical | `R-006` | [assumption] |
| Build / self-serve via a general LLM | Prompt ChatGPT/Claude for outline+copy, then hand-format | Already paying for the LLM; flexible | Capable user, low deck volume | `R-003` | [sourced: market-research] |
| Gamma (web-format generation) | Fast AI decks that live on the web | Speed + polish if native `.pptx`/`.key` isn't required | Native format not needed; audience views a link | `R-001` | [sourced: market-research] |
| Copilot in PowerPoint | AI edits your *real* native PPT | Native + bundled; no new tool to buy | M365 shops; native editing is the priority | `R-002` | [sourced: market-research] |

**Self-build threshold:** a capable individual with low deck volume who already pays for a general
LLM — at that point "just prompt it and format myself" beats paying us. [assumption]

**Switching friction:** company-standard templates and brand kits locked into incumbents (Canva/M365),
plus habit — the barrier our native-fidelity + design quality has to clearly beat. [assumption]

## Niche risks {#niche-risks}
<!-- synthesis: light Five Forces -->

| Risk <!--c:risk--> | Force <!--c:force--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | → `R-…` <!--c:register--> | Confidence <!--c:conf--> |
|------|-------|------------|--------|---------|------------|
| Gamma is a dominant, profitable leader — head-on displacement is hard | rivalry | H | H | `R-001` | [sourced: market-research] |
| Incumbents (Copilot in PPT, Canva) bundle native-editable AI generation with distribution | substitution | H | H | `R-002` | [sourced: market-research] |
| Capable buyers self-build with general LLMs → caps willingness to pay | buyer power / substitution | M | M | `R-003` | [sourced: market-research] |
| Engine quality/COGS depend on third-party LLM providers | supplier power | M | H | `R-004` | [assumption] |
| Low entry barrier for "AI slide wrappers" → crowded rivalry | entry barriers | H | M | `R-005` | [sourced: market-research] |

## Opportunity {#opportunity}
<!-- synthesis -->

- **Opportunity (the white space): native, high-fidelity editable `.pptx`/`.key` that also look
  designed.** The category leader (Gamma) is web-first and its PowerPoint export **flattens 30–40%
  of slides into uneditable images** — it is not truly native-editable. The incumbents that *are*
  native (Copilot in PPT) or claim editable objects (Canva) are generalists whose design quality and
  audience-specific *narrative* are weak. Decksmith's thesis (`passport#concept`) sits exactly in
  that gap: native fidelity **and** design quality **and** narrative structure. [sourced: market-research]
- **Threat (why the window is narrow):** the incumbents are moving into this wedge with a
  distribution advantage, and Gamma could fix its export. So this is a race — the defensible thing
  must be a genuinely hard *fidelity + design engine* (`H-004`), not the app. [sourced: market-research]
- **Why now:** AI-slide demand is growing ~23–26% CAGR; "editable design objects" is the headline
  battleground of 2026; the native-fidelity gap is currently unmet by the leader. [sourced: market-research]

## Seeded hypotheses {#hypotheses}

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | From section <!--c:from--> | Confidence <!--c:conf--> |
|----|------------|------|--------------|------------|
| H-005 | A native, high-fidelity editable-and-designed deck is a real unmet need the lead segment values over web-format generation (Gamma's export gap) | desirability/viability | opportunity/substitutes | [assumption] |
| H-006 | The obtainable market is large enough to build a business on (bottom-up SAM ~$750M; realistic SOM) | viability | market-sizing | [assumption] |

_Also pressured by this step: `H-004` (defensibility) — incumbents are entering the wedge, so the
moat must be the fidelity engine, not the app (noted in the register); `H-001` (feasibility) becomes
even more central — native fidelity is precisely where the leader fails._

## To clarify {#to-clarify}

- **Beachhead within the lead segment** and **first format** (`.pptx` vs `.key` vs both) — a Step 3 (Strategy) choice.
- **Willingness to pay vs bundled incumbents** (Copilot/Canva at ~$15–30 already bundled) — Step 3 pricing.
- **Whether to position explicitly against Gamma's export gap** ("actually-editable") — Step 3 positioning.
