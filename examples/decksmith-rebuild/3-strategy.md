---
node_type: artifact
artifact: strategy
step: 3
title: "Strategy — Decksmith (fictional sample)"
status: draft
version: 0.1.0
updated: 2026-08-14
---

# Strategy — Decksmith (fictional sample)

> Status: concept-viability · Owner: — · Last review: 2026-08-14
> Inputs: `1-passport.md` · `2-analysis.md`. Feeds: `4-strategic-plan.md`.
> Projection of `3-strategy/` worklogs (heavy working) + method output. No section confirmed (autonomous walk).

## Winning aspiration {#winning-aspiration}
<!-- tool: where-to-play-how-to-win -->
_What winning looks like this horizon._

- Own **"the AI deck you don't have to rebuild"** for salespeople & marketers — their default for client-facing
  decks that are *both* editable and designed — and reach a defensible position in the lead segment before
  incumbents close the native-fidelity gap (⚙️ horizon ~18–24 mo). [assumption]

## Where to play {#where-to-play}
<!-- tool: where-to-play-how-to-win -->
<!-- rests-on: 1#segments, 2#opportunity -->
_Arena chosen, exclusions explicit. (4 candidate cascades considered; B/C/D rejected — see worklog.)_

| Chosen arena | Why | Excluded (and why) | Confidence |
|--------------|-----|--------------------|------------|
| Sales/marketing client-deck makers, NA+EU, standalone web app → native .pptx/.key | the native-fidelity wedge (Gamma's export gap) with money + frequency behind it | enterprise brand-compliance (Copilot's turf, slow — expansion); co-editing (out of concept); non-slide formats; education/personal (low WTP); API/embed (later); non-NA/EU geos (focus) | [assumption] |

## How to win {#how-to-win}
<!-- tool: where-to-play-how-to-win, value-definition -->
_Winning logic + named moats. (value-definition revisited for the moat.)_

- **Winning logic:** be the only tool whose output is *actually editable AND designed*, and out-run incumbents
  closing the gap by focusing on the **fidelity+design engine, not the app**; wedge on Gamma's export weakness. [assumption]
- **Moats leveraged:** execution speed on the fidelity engine (`H-009`) + design taste/corpus (`H-005`).
  **Not distribution** (we lack it) — speed + focus substitute. The moat is honestly thin/temporal → win fast,
  then build derivative lock-in (brand kits) once customers exist. [assumption]

## UVP & CPV {#uvp-cpv}
<!-- tool: uvp-cpv -->
_For [best-fit customer] who [job/pain], we [value] — unlike [alternative], because [why us]._

| Best-fit customer | Job / pain | Value (outcome) | vs alternative | Customer-perceived value | Confidence |
|-------------------|------------|-----------------|----------------|--------------------------|------------|
| Salespeople & marketers making client decks | produce a client-ready deck fast without rebuilding it | a native, fully-editable, designed deck you finish in your own tool | Gamma (export flattens 30–40% to images); Copilot/Canva (editable but generic); do-it-manually | "a first draft I actually keep, not one I rebuild" | [assumption] |

**One-liner.** For salespeople & marketers who must produce client-ready decks fast, Decksmith generates a
native, fully-editable, well-designed deck you finish in your own tool — unlike web-first generators whose export
breaks, because our engine is built for native fidelity + design. [assumption]

## Pricing & Packaging {#pricing}
<!-- tool: pricing -->
_Decided here (value-based), quantified + margin-checked at Step 4. WTP unevidenced → `[assumption]`._

- **Value metric:** per active deck-maker (seat) — scales with the person getting value; decks as a secondary
  fair-use meter. [assumption]

| Tier | For which segment | Included | Fence (why they pick it) | Price point | Model | Confidence |
|------|-------------------|----------|--------------------------|-------------|-------|------------|
| good (Free/trial) | trialists | a few decks/mo, export cap or watermark | try before paying; converts on first full export | $0 | freemium | [assumption] |
| better (Pro) | lead segment | unlimited decks, full native export, brand kit | the individual deck-maker's tier | ~$18/mo | subscription (seat) | [assumption] |
| best (Team) | orgs (Seg 3 expansion) | shared brand kits, team templates, admin | teams standardizing on-brand decks | ~$30/user/mo | subscription (seat) | [assumption] |

**Anchor:** vs Gamma $20 (but its export breaks — we charge for the part that works); vs bundled Copilot/Canva
($0 marginal) — the standalone price is justified only by the native-fidelity gap they don't close. → `H-008`
(will pay standalone), `H-012` (packaging converts free→Pro at ~$18).

## Channels & expansion {#channels-expansion}
<!-- tool: channels-expansion -->
_Bullseye — inner ring tested now (10 candidates scored in worklog). Message (UVP) kept separate from channel._

| Channel | Stage (traction / scale) | Why it fits the segment | Confidence |
|---------|--------------------------|-------------------------|------------|
| LinkedIn content / thought-leadership | traction (inner) | the lead segment lives there; cheap to test | [assumption] |
| Sales/design communities | traction (inner) | high-intent, cheap, fast read | [assumption] |
| PLG virality ("made with Decksmith") | traction (inner) | shared client decks carry the product | [assumption] |
| SEO, paid social, creator partnerships | middle (revisit) | promising but slower/pricier to read | [assumption] |

- **Expansion path:** lead segment → founders/consultants (once PLG k-factor > 0.3 & Pro retention holds) →
  teams/orgs (once the brand-kit "Team" tier shows repeat use) → later API/embed or enterprise. [assumption]

## Product surface {#product-surface}
<!-- tool: product-surface -->
_Every user-interaction surface + instrumentation (sketched here, refined at Step 4)._

| Surface | Purpose | Instrumentation (what/where data comes from) | Confidence |
|---------|---------|----------------------------------------------|------------|
| Web app (generate / edit / export) | the core job | product events: generate, export, keep-vs-redo | [assumption] |
| Export pipeline (native .pptx/.key) | the fidelity-critical surface | `M-edit-fidelity` (share of natively-editable objects) | [assumption] |
| Landing pages (per channel) | acquisition | funnel analytics per channel | [assumption] |
| Onboarding emails / notifications | activation | open/click, time-to-first-export | [assumption] |
| Brand-kit setup | retention/expansion | brand-kit created/used | [assumption] |
| Admin panel (Team) | org management | seats, usage | — to clarify — |

_Infra implied (Step-4 cost lines): analytics stack, email provider, LLM inference (COGS)._

## Architecture {#architecture}
<!-- tool: architecture-c4 -->
_C4 Context level (product · users · external systems). Refined at Step 4._

- **Context sketch:** **System** = Decksmith. **Actors** = deck-maker (lead segment), team admin.
  **External systems:** LLM provider(s) — content/layout reasoning (dependency + COGS → `R-004`); **in-house
  native-fidelity render/export engine** — the moat (not external); auth; payments (e.g. Stripe); analytics;
  email; design-corpus/asset + font/brand store. **Flow:** user → app → LLM (draft) → fidelity engine (native
  render) → export .pptx/.key. Multi-model abstraction mitigates `R-004`. [assumption]

## Bets {#bets}
<!-- tool: jtbd, value-definition -->
_Strategic hypotheses, framed on the job + forces (pull > anxiety + habit)._

| ID | Bet | Type | Job / circumstance | Why it wins (pull > anxiety + habit) | Outcome it moves | Confidence |
|----|-----|------|--------------------|--------------------------------------|------------------|------------|
| H-010 | The lead segment prefers native-fidelity editable+designed decks over web-first generators enough to switch | desirability | client deck under time pressure | pull (keep the draft, no rebuild) beats the "I'll still have to fix it" anxiety + PowerPoint habit | activation / retention | [assumption] |
| H-009 | A standalone native-fidelity engine stays ahead of incumbents closing the wedge | viability (moat) | — | speed + focus on the engine vs their distribution | retention / defensibility | [assumption] |
| H-011 | Sales/marketing communities + PLG acquire the beachhead at viable CAC | viability | — | high-intent, low-cost channels fit the segment | acquisition / CAC | [assumption] |

## Product risks {#product-risks}
<!-- tool: risk-mitigation -->
_Risks specific to this strategy (mitigations owned at Step 4). Extend the risk register._

| ID | Risk | Category | Likelihood | Impact | Confidence |
|----|------|----------|------------|--------|------------|
| R-006 | PLG virality doesn't fire → CAC too high without distribution | execution | M | H | [assumption] |
| R-007 | The fidelity engine can't hold design quality across arbitrary content at scale → the wedge collapses | product | M | H | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
- **WTP / price points** are `[assumption]` — need a price-talk pilot before Step-4 unit-economics can validate.
- **Enterprise vs beachhead sequencing** — cascade C (enterprise) is deferred; confirm the trigger to revisit it.

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → strategy cascade (beachhead wedge), UVP, value-based pricing, Bullseye channels, product
  surface + C4 context, 3 bets (`H-010/H-011` new, `H-009` carried), 2 product risks (`R-006/R-007`).
- **Why:** decide where to play / how to win on the native-fidelity wedge under closing-incumbent pressure.
- **Trigger:** Step-3 strategy, rebuild.
