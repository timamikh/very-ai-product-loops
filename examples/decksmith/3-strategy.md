---
node_type: artifact
artifact: strategy
step: 3
title: "Strategy — Decksmith (fictional sample)"
status: draft
version: 0.1.2
updated: 2026-08-17
---

# Strategy — Decksmith (fictional sample)

> Status: concept-viability · Owner: acting PO (⚙️ agent) · Last review: 2026-08-16
> Inputs: `1-concept.md` · `2-analysis.md`. Feeds: `4-strategic-plan.md`.

> ⚠️ This artifact is the **projection** of the Step-3 worklogs in `3-strategy/`. Each section's
> source of truth is its method worklog; the change-log history lives there, not here. ⚙️ marks
> agent-proposed choices awaiting the human's confirmation — this run never self-issues `confirmed:`.

## Winning aspiration {#winning-aspiration}
<!-- tool: where-to-play-how-to-win -->
_What winning means here — who we serve, what result, by when. Not a slogan._

- **Win the "editable-AND-designed" corner for client-facing sales & marketing decks** — be the tool <!-- card -->
  S1 switches to when a deck must be *both* on-brand-beautiful *and* a real, natively-editable file,
  and prove that switch is **repeatable in the US beachhead before an incumbent closes the export
  gap**. Status is `concept-viability`, so winning = **evidence of fit** (`H-001` holds, S1 switches,
  they pay) — not market share.  [assumption] ⚙️

## Where to play {#where-to-play}
<!-- tool: where-to-play-how-to-win -->
<!-- rests-on: 1#segments, 2#opportunity -->
_Segments / markets / arena chosen — and what's explicitly excluded._

| Chosen arena <!--c:arena--> | Why <!--c:why--> | Excluded (and why) <!--c:excluded--> | Confidence <!--c:conf--> |
|--------------|-----|--------------------|------------|
| **S1 client-facing sales & marketing deck-makers, US-first** (agencies/consultancies, in-house sales/marketing, freelance designers; design-native agencies = sharpest proving ground), self-serve PLG, scope = AI generation → native fully-editable `.pptx`/`.key` | The one arena where editable **and** designed are both non-negotiable (client-facing ⇒ must look designed *and* be handed over/edited natively); our taste-corpus moat applies and incumbents are structurally conflicted | Students/education · internal-only/throwaway decks · one-off investor pitch decks · "everyone who makes slides" · non-English markets (until localisation) · enterprise top-down sales · a locked web-only editor · **real-time collaboration + non-slide formats** [sourced: founder brief out-of-scope, as_of 2026-08-16] | [assumption]; scope exclusions per cell |

_Per-dimension play-in/exclusion breakdown in `3-strategy/where-to-play-how-to-win.md` §3._

<!-- card -->
**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** horizontal
"AI PowerPoint for everyone" (no moat we hold applies), enterprise brand-compliance (reachable, not
winnable now), investor pitch-deck niche (Tome/Pitch's grave) — full cascades + why each loses in
`3-strategy/where-to-play-how-to-win.md`.

## How to win {#how-to-win}
<!-- tool: where-to-play-how-to-win, value-definition-strategy -->
<!-- rests-on: 1#value-defensibility, 2#competitor-strategy, 2#competitor-dynamics -->
_The winning logic + which moats we leverage._

- **Winning logic:** own the corner where editable **and** designed are both mandatory; beat the <!-- card -->
  native-export tools on **taste**, beat the design-led tools on a **real native file** — the axis
  each is structurally unable to prioritise.  [assumption]

| Winning move | Moat it leverages | Why a rival can't cheaply copy it | Confidence |
|--------------|-------------------|-----------------------------------|------------|
| Out-design the native-export tools (Plus AI/Copilot/MagicSlides) | Curated design corpus + founder taste/credibility (`H-007`) | Taste = curated labelled corpus + reputation; a rival gets the model, not the curation | [assumption] |
| Out-export the design-led tools (Gamma/Canva/Beautiful.ai) | Native-editable-and-designed engine (`H-001`) | Their core business is the *locked editor*; real native export cannibalises their lock-in (incumbent's dilemma) | [assumption] |
| Convert the head-start before the wedge erodes | Edit-behaviour data loop + brand-kit lock-in (derivatives) | Proprietary keep-vs-restyle data + embedded brand system; both scale-gated | [assumption] |

- **Cascade check (⚙️):** wins **iff** `H-001` holds **and** the wedge converts to the data/lock-in
  moat before Gamma/Canva ship real native export or Microsoft bundles it away — the load-bearing
  fragility is **timing** (`H-012`/`R-007`).

## UVP & CPV {#uvp-cpv}
<!-- tool: uvp-cpv -->
<!-- rests-on: 1#segments, 1#problems, 2#substitutes -->
_For [best-fit customer] who [job/pain], we [value] — unlike [alternative], because [why us]._

| Best-fit customer <!--c:customer--> | Job / pain <!--c:job--> | Value (outcome) <!--c:value--> | vs alternative <!--c:alt--> | Customer-perceived value <!--c:cpv--> | Confidence <!--c:conf--> |
|-------------------|------------|-----------------|----------------|--------------------------|------------|
| Client-facing deck-maker (agency/consultant/in-house S1) who must look designed *and* hand over an editable file | New pitch / recurring report / client handoff — the restyle tax + export breakage | Client-ready, on-brand, **fully-editable** deck in minutes; no rebuild; no breakage | Gamma/Canva + manual rebuild (polished but locked) | *"A deck that already looks designed — and a real PowerPoint I can edit and send, so I'm not rebuilding it at midnight"* | [assumption] |

- **One-liner:** *For sales & marketing teams who must send client-ready decks, Decksmith generates a <!-- card -->
  fully-editable, on-brand PowerPoint or Keynote in minutes — unlike Gamma or Canva, whose polished
  decks lock you into their editor and break on export, because our curated design engine writes
  native files, not screenshots.*  [assumption]
- CPV signal: **none yet** (fictional sample, no pilot) — the *pains* are `[sourced: founder brief;
  1-concept/segment-pains.md]`; the *value delivered* is `[assumption]`. Per-situation working in
  `3-strategy/uvp-cpv.md`.

## Pricing & Packaging {#pricing}
<!-- tool: pricing-strategy -->
<!-- rests-on: 2#competitor-pricing -->
_What we charge and how we package it — anchored to value vs the alternative. Quantified at Step 4._

- **Value metric:** per active seat (per deck-maker) — value scales per deck-maker and the market
  prices per-seat; a fair-use generation cap fences the entry tier only. (Per-deck/usage rejected as
  primary — it punishes the power users who are the best-fit customer.)  [assumption]

| Tier <!--c:tier--> | For which segment <!--c:segment--> | Included <!--c:included--> | Fence (why they pick it) <!--c:fence--> | Price point <!--c:price--> | Model <!--c:model--> | Confidence <!--c:conf--> |
|------|-------------------|----------|--------------------------|-------------|-------|------------|
| good (Solo) | Freelance / individual | Generation, native `.pptx`/`.key` export, core styles, 1 brand kit, fair-use cap | Single seat; feel the editable-AND-designed value | ~$24/mo ⚙️ | subscription | [assumption] |
| better (Team) | Agency / sales team | Multi-seat, shared brand kits, brand-lock, priority generation | Teams that must stay on-brand across people | ~$45/seat/mo ⚙️ | subscription/seat | [assumption] |
| best (Studio) | Agencies at volume | Unlimited brand kits, client workspaces, white-label, bulk/API | Volume + client management | ~$90/seat/mo or custom ⚙️ | subscription/hybrid | [assumption] |

- **Anchoring:** premium *above* the $8–20 prosumer cluster (dated Step-2 scan) — we are not the <!-- card -->
  cheapest; we are the one that removes the rebuild. We do **not** win on price vs the Copilot bundle
  ($18–30 by tier on M365); we win on taste.  [sourced: 2-analysis.md#competitor-pricing, as_of
  2026-08-17]
- **Monetisation discipline (guards `R-005`):** tight time-boxed free trial, **not** free-first-
  unlimited; native export + brand kits are paid fences from day one. Numbers at Step 4
  (`pricing-strategic-plan` → `unit-economics`).

**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** per-deck/usage
as the primary value metric (punishes the power users who are the best-fit customer) · price at
parity with the $8–20 cluster (surrenders the premium the removed rebuild justifies; kept as an open
question in `#to-clarify`) · free-first-unlimited (the Tome/Pitch trap, `R-005`).

## Channels & expansion {#channels-expansion}
<!-- tool: channels-expansion -->
<!-- rests-on: 1#segments -->
_Acquisition/comms channels (Bullseye) + the GTM motion + expansion paths._

- **GTM motion:** **product-led (self-serve)** — Solo ~$24 / Team ~$45 can't fund a sales call; S1 <!-- card -->
  buys self-serve; try→buy. Studio tier layers light sales-assist *later*. Inner ring all start the
  PLG first step (coherence check passes).  [assumption]

| Channel <!--c:channel--> | Stage (traction / scale) <!--c:stage--> | Why it fits the segment <!--c:fit--> | Confidence <!--c:conf--> |
|---------|--------------------------|-------------------------|------------|
| Founder-led design community | traction (inner ring, test now) | Founder taste/credibility reaches S1; CAC ≈ $0 on the warm audience | [assumption] |
| Paid search (intent/competitor kw) | traction (inner ring, test now) | Fast, readable CAC signal on high-intent demand | [assumption] |
| Content/SEO comparison + intent pages | traction (inner ring, test now) | "Gamma alternative" / "editable export" intent demand (unverified — needs a keyword-demand check) | [assumption] |

- Brainstorm was 11 candidates × 7 categories, scored 1·3·5 (reach × cost × testability); middle/outer
  rings (Product Hunt, communities, referral [gated vs `R-005`], paid social, influencer, outbound,
  marketplace, partnerships) kept with reasons in `3-strategy/channels-expansion.md`.
- **Expansion path:** S1 US → adjacent US segments *(trigger: PLG CAC < LTV **and** brand-kit
  retention proven)* → non-English geos *(trigger: localisation ships)* → enterprise top-down
  *(trigger: SSO/governance shipped **and** ≥N agency case studies)*.  [assumption]

## Product surface {#product-surface}
<!-- tool: product-surface -->
_Every user-interaction surface + instrumentation (sketched here, refined at Step 4)._

| Surface <!--c:surface--> | Purpose <!--c:purpose--> | Instrumentation (what/where data comes from) <!--c:instrumentation--> | Confidence <!--c:conf--> |
|---------|---------|----------------------------------------------|------------|
| Landing + comparison pages | acquisition | visits, source, signup CVR (analytics) | [assumption] |
| Signup / onboarding | activation | signup→first-deck time, drop-off (funnel) | [assumption] |
| Generation UI | core value | generations, time-to-first-deck, regenerations (events) | [assumption] |
| Native export action | the promise | export rate/format; **— to clarify —** open-success off our surface | [assumption] |
| Edit-behaviour capture | moat + `H-001` proof | keep-vs-restyle events; **— to clarify —** post-export edits leave our surface | [assumption] |
| Brand-kit manager | retention / lock-in | kits created, reuse rate (events) | [assumption] |
| Admin / billing | ops + revenue | seats, MRR, churn (billing + analytics) | [assumption] |
| Lifecycle emails | activation/retention | opens, clicks, return-to-paid-action | [assumption] |

- **Behaviour-study tools:** analytics/funnels, session capture on onboarding+export, in-app + email <!-- card -->
  surveys. **Load-bearing gap:** export-open fidelity + post-export edits leave our surface (the cost
  of the differentiation) — proxies needed; feeds Step-4 `instrumentation-plan`.
- **Infra implications (→ Step 4 costs):** analytics, email, session capture, **LLM inference
  (COGS — the big one)**, file-render/export service.

**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** none recorded
as competing surface sets — the map follows from the chosen PLG motion (`#channels-expansion`); the
honest fork is instrumentation of the promise (export-open fidelity / post-export edits leave our
surface), flagged in `#to-clarify` rather than resolved here.

## Architecture {#architecture}
<!-- tool: architecture-c4 -->
_System architecture at C4 **Context** level (product, its users, external systems). Refined at Step 4._

- **Context sketch:** **Decksmith** (system) · **actors:** deck-maker (S1, primary), client/recipient <!-- card -->
  who edits natively (secondary) · **external systems:** LLM provider(s), curated design corpus,
  native export engine (`.pptx`/`.key`/Slides), auth, payments, analytics/email.  [assumption]

| External system | Role | Cost driver? | Dependency risk? | Moat? |
|-----------------|------|--------------|------------------|-------|
| LLM provider(s) | generation | yes — COGS (the big line) | yes (`R-004`) | — (commodity) |
| Curated design corpus | design from | small | internal | **yes** (`H-007`) |
| Native export engine | the promise | build/maintain | yes (`R-006`) | wedge, not durable |
| Auth · Payments · Analytics · Email | ops/instrumentation | small | low | — |

- **Downstream feeds:** LLM + export infra → Step-4 COGS; `R-004`/`R-006` already in register (not
  duplicated); **no exclusive integration moat yet** — the corpus is the moat, the export engine a
  proprietary wedge. Mermaid context diagram in `3-strategy/architecture-c4.md`.

**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** none recorded
as competing contexts — a C4-Context read of the already-chosen scope; build-vs-buy on the export
engine is not an open fork (the proprietary engine *is* the `H-001` bet), and multi-LLM abstraction
is deferred as risk hygiene (`R-004`, backlogged at Step 5).

## Bets {#bets}
<!-- tool: bets, value-definition-strategy -->
<!-- rests-on: 1#jtbd, 2#opportunity -->
_The strategic hypotheses we're wagering on (framed on the customer's job + forces)._

| ID <!--c:id--> | Bet <!--c:bet--> | Type <!--c:type--> | Job / circumstance <!--c:job--> | Why it wins (pull > anxiety + habit) <!--c:whywins--> | Outcome it moves <!--c:outcome--> | Confidence <!--c:conf--> |
|----|-----|------|--------------------|--------------------------------------|------------------|------------|
| H-001 | The engine does editable-AND-designed at scale (the enabler) | feasibility | Any client deck from a brief | Pull: no rebuild; the whole how-to-win rests here | Activation / retention | [assumption] |
| H-003 | S1 switches from "Gamma/Canva + manual rebuild" (sharpened, reused) | desirability | Making a client-ready deck | Pull (restyle tax removed) > anxiety (trust AI taste) + habit (owns PowerPoint) | Switching / activation | [assumption] |
| H-006 | S1 US is a reachable, budgeted beachhead | viability | The where-to-play bet | Recurring, company-budgeted need | Acquisition | [assumption] |
| H-007 | Taste corpus + founder credibility is a compounding moat | viability | Defensibility of the win | A clone gets the model, not the curation/reputation | Defensibility | [assumption] |
| H-010 | S1 pays a premium (~$40/seat/mo) for editable-AND-designed | viability | Monetisation | Value gap (hours saved) justifies premium vs $8–20 cluster | Revenue / margin | [assumption] |
| H-011 | Founder-led community reaches S1 at PLG-viable CAC | desirability | Distribution | Warm audience, credibility as channel; CAC ≈ $0 | CAC / acquisition | [assumption] |
| H-012 | The wedge converts to a durable moat before the export gap closes | viability | Moat trajectory / timing | Data loop + brand-kit lock-in outrun incumbents' export | Defensibility over time | [assumption] |

Reconciled against the register — `H-001`/`H-003`/`H-006`/`H-007` reused (not re-minted);
`H-010`/`H-011`/`H-012` newly minted. Cuts (feature bets) in `3-strategy/bets.md`.

**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** two candidate
bets cut — "users will love the generation UI" (a feature bet, no segment/forces; belongs in a spec)
and "we win because we use a frontier LLM" (commodity input, already killed as a moat at Step 1) —
kept visible in `3-strategy/bets.md`.

## Product risks {#product-risks}
<!-- tool: pre-mortem -->
_Risks specific to this strategy (mitigations owned at Step 4)._

| ID <!--c:id--> | Risk <!--c:risk--> | Category <!--c:category--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | Confidence <!--c:conf--> |
|----|------|----------|------------|--------|------------|
| R-007 | Incumbent closes the export gap before the wedge converts to a durable moat (timing) | market | H | H | [assumption] |
| R-009 | Taste doesn't travel — corpus feels samey/off-brand across diverse content; "designed" fails at scale | product | M | H | [assumption] |
| R-011 | WTP overestimated — S1 won't pay the premium; forced discounting breaks the model | financial | M | H | [assumption] |
| R-008 | Founder-community channel doesn't scale past the founder's audience → CAC explodes | execution | M | H | [assumption] |
| R-010 | Key-person dependency on the founder's taste/credibility (moat = bottleneck; bus factor) | execution | M | M | [assumption] |

- Ranked by likelihood × impact (top first). Carried **open and unmanaged** — mitigation/owner/
  trigger are Step-4 `risk-mitigation`. Pre-mortem surfaced 11 failure modes; 5 folded onto existing
  entries — `H-001` (f1, the core feasibility bet — a hypothesis, not a risk), `R-002`, `R-004`,
  `R-005`, `R-006` (re-confirmed, not duplicated) — and 1 parked (inverse of `H-005`). Full triage in
  `3-strategy/pre-mortem.md`.

**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** the full
11-mode triage — 5 carried as new `R-007`…`R-011`, 5 folded onto existing register entries, 1 parked
— each with its disposition recorded in `3-strategy/pre-mortem.md`.

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced for the human to resolve._

- **All price points are ⚙️ `[assumption]`.** ~$24 / ~$45 / ~$90 per seat need WTP evidence — Step-4
  `pricing-strategic-plan` + a pilot/survey. Does the human accept the premium-above-cluster stance,
  or price at parity to fight the bundle?
- **Design-native agencies as the sharpest proving ground** (carried from Step-1 `#to-clarify`): S1 is
  the scale bet, but should the *first* wedge be design-native agencies specifically? A go-to-market
  sequencing call.
- **Studio tier = a second motion.** The best tier implies light sales-assist; is that in scope this
  horizon, or defer to keep a pure PLG motion?
- **Instrumentation of the promise.** Export-open fidelity + post-export edits leave our surface;
  which proxy does the human accept (pre-export lint / opt-in ping / agency panel)?
- **No customer evidence yet** (carried): every desirability bet rests on the founder's observation.
  Discovery interviews are the first thing the tactical loop should buy.

## Change log

### 2026-08-17 — card lines marked for the console board
- **From → To:** no section carried a `<!-- card -->` mark → 8 section(s) with a natural headline
  line now mark it; table-only sections stay unmarked (title and status only, the body one expand away)
- **Why:** the console no longer composes a card face of its own — a board card shows the author's
  marked line verbatim or nothing (CONVENTIONS → *Card line*)
- **Trigger:** console rework — a card is a collapsed section, not a third text

### 2026-08-17 — human review pass: canonical Decided lines added
- **From → To:** the six decision-class sections (`#where-to-play` — carrying the cascade choice —
  `#pricing`, `#product-surface`, `#architecture`, `#bets`, `#product-risks`) had no canonical
  `**Decided:**` line → each now ends with one (dated, attributed ⚙️, alternatives shown); where a
  worklog recorded no competing alternatives, the line says so instead of inventing them; the Copilot
  bundle reference updated to $18–30 by tier (per the Step-2 pricing fix)
- **Why:** the library convention makes the decision line the section's one canonical, checkable
  record of a choice — the run's decisions were real but carried only in prose; review returned the
  omission
- **Trigger:** human review of the finished run (strategy lens)

### 2026-08-16 — created (Step 3 strategy)
- **From → To:** — → strategy projected from the 8 `3-strategy/` worklogs: winning aspiration,
  where-to-play (with exclusions), how-to-win (moats named), UVP/CPV (per-situation), pricing (value
  metric + good/better/best), channels + PLG motion + gated expansion, product surface, C4-context
  architecture, 7 bets, 5 new product risks
- **Why:** Step 3 = the qualitative choices (where to play / how to win / the bets); numbers, models,
  mitigations deferred to Step 4
- **Trigger:** Step 3 operating-loop pass. Registers updated by the orchestrator: `H-010`/`H-011`/
  `H-012` minted, `R-007`…`R-011` seeded open/unmanaged; Step-1 `#value-defensibility` re-projected
  with the derived derivatives + trajectory.
