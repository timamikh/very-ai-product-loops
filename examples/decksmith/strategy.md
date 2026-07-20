---
node_type: artifact
artifact: strategy
product: Decksmith (fictional sample)
step: 3
status_stage: concept-viability
owner: sample
updated: 2026-07-21
version: 0.1.0
---

# Strategy — Decksmith (fictional sample)

> Status: `concept-viability` · Owner: sample · Last review: 2026-07-21
> Inputs: `passport.md` · `analysis.md`. Feeds: `strategic-plan.md`.
> This step is **choices** (qualitative). At `concept-viability` the goal is to find fit: one
> beachhead, a testable positioning bet, packaging as a hypothesis — **WTP stays open, not a set price**.

## Winning aspiration {#winning-aspiration}
<!-- tool: where-to-play-how-to-win -->

- Become the default tool a client-facing deck-maker reaches for when the deck must be **edited in
  PowerPoint/Keynote *and* look designed** — winning the "actually-editable + beautiful" position
  the web-first leader (Gamma) structurally can't hold and the generalists (Copilot/Canva) only do
  generically. Concept-stage target: within ~18 months, be that default for salespeople & marketers
  who live in PowerPoint. [assumption]

## Where to play {#where-to-play}
<!-- tool: where-to-play-how-to-win -->

| Dimension | We play in | We deliberately exclude | Confidence |
|-----------|------------|-------------------------|------------|
| Segments | **Beachhead:** salespeople & marketers who make client-facing decks often and live in PowerPoint | Founders (occasional use), designers (resist AI design), enterprise procurement — for now | [assumption] |
| Geographies / markets | English-first paying markets | Non-English localization (until a channel proves out) | [assumption] |
| Channels | Sales/marketing communities + product-led (shareable output) | Enterprise direct sales / RFPs — premature at concept stage | [assumption] |
| Product scope / value-chain stage | **Native `.pptx` first** (largest install base); the generation+fidelity engine | Web-first decks (Gamma's game), real-time co-editing (out of concept), `.key` until later | [assumption] |

_ONE beachhead (per `concept-viability`): salespeople & marketers who need on-brand client decks fast
**and** need to edit them in PowerPoint. First format = `.pptx`._

## How to win {#how-to-win}
<!-- tool: where-to-play-how-to-win, value-definition -->

| Winning move | Moat it leverages | Why a rival can't cheaply copy it | Confidence |
|--------------|-------------------|-----------------------------------|------------|
| Output decks that are **both** truly editable in native PPT/Keynote **and** genuinely designed | Unique IP — the native-fidelity + design engine (`H-004`) | The leader (Gamma) is web-first and its PPT export flattens 30–40% of slides; sustained native-fidelity+design quality is hard | [assumption] |
| Structure the **narrative** for the audience, not just style slides | Unique data — a designed-deck corpus + design taste | Generalists (Copilot/Canva) optimize general design, not deck-narrative fit | [assumption] |

**Cascade check:** ⚙️ Does this win in the beachhead, given the aspiration? **Yes — but only if
`H-001` (the engine reliably hits native-fidelity + design at scale) holds.** The whole strategy
rests on that one feasibility bet; that is the honest fragility (→ `R-007`). [assumption]

**Moats revisited (value-definition):** base moats unchanged from `passport#value-defensibility`
(engine IP + design corpus + brand). **Derivative moats (lock-in, network effects) remain deferred
— no customers/scale yet, even at Strategy (`concept-viability`); revisit at `pmf`.**

**Seeded hypotheses:** the cascade rests on `H-001` (feasibility), `H-004` (moat), `H-005` (the wedge is valued).

## UVP & CPV {#uvp-cpv}
<!-- tool: uvp-cpv -->

**Best-fit customer:** a salesperson/marketer who must send an on-brand client deck they can still
edit in PowerPoint. [assumption]

**Alternative they use today:** Gamma (web-first; PPT export breaks), or manual build in
PowerPoint/Canva, or Copilot in PPT (native but generic design). [sourced: analysis#substitutes]

**Value (not features)**

| Top job / pain | Outcome we create | Why it beats the alternative | Confidence |
|----------------|-------------------|------------------------------|------------|
| Deck looks templated → I redo it (P1) | A deck that reads as designed, out of the box | Gamma/Copilot output still needs a design pass | [assumption] |
| Can't truly edit AI output (baseline) | A native `.pptx` with real, editable objects | Gamma's export flattens 30–40% of slides to images | [sourced: analysis#opportunity] |
| Wrong structure/story (P2) | Narrative sequenced for the audience | Generalists style slides, don't structure the argument | [assumption] |

**Customer-perceived value:** "I get a deck I don't have to redo." [assumption] — signal `— to clarify —` (interview/WTP, Step 5).

**One-liner:** ⚙️ _For salespeople & marketers who need a client deck that looks designed and stays
editable in PowerPoint, Decksmith generates a native, on-brand, well-structured `.pptx` you can
actually edit — unlike Gamma (whose PPT export flattens slides) or Copilot/Canva (native but
generic) — because our engine is built for native-fidelity + design, not web-first._

**Seeded hypotheses:** `H-005` (the editable+designed wedge is valued) → register.

## Pricing & Packaging {#pricing}
<!-- tool: pricing -->
_At `concept-viability`: packaging is a hypothesis and **WTP stays open** — no committed price. Quantified at Step 4._

**Value metric:** ⚙️ per active deck-maker (seat), with a possible usage overlay (decks/month) —
scales with the value a frequent deck-maker gets. [assumption]

**Packaging (tiers & fences)**

| Tier | For which segment | What's included | Fence | Price point | Model | Confidence |
|------|-------------------|-----------------|-------|-------------|-------|------------|
| Free | trial users | limited exports / watermark | try before paying | $0 | freemium | [assumption] |
| Pro | individual salesperson/marketer | unlimited native exports, design engine | needs real editable output | ⚙️ ~$15–25/mo (open) | subscription | [assumption] |
| Team | a sales/marketing team | brand kit, shared templates, seats | on-brand at team scale | ⚙️ ~$30–40/user (open) | subscription | [assumption] |

**Anchor to the alternative**

| Segment | Next-best alternative (what they'd pay/do) | Our price | Value gap that justifies the delta | Confidence |
|---------|--------------------------------------------|-----------|------------------------------------|------------|
| Salespeople & marketers | Gamma ~$20/mo; Copilot/Canva ~$15–30 **bundled** | standalone ~$15–25 (open) | must be justified purely by the fidelity+design gap — the hard part | [assumption] |

**Willingness-to-pay evidence:** none yet — WTP is an explicit hypothesis (`H-009`), tested at Step 5
(price talk / pilot), not set here. **Trial → first exported editable deck** as the first paid-conversion moment. [assumption]

**Seeded hypotheses:** `H-009` (beachhead pays a standalone subscription despite bundled incumbents, `type: viability`).

## Channels & expansion {#channels-expansion}
<!-- tool: channels-expansion -->

**Channel ranking (Bullseye rings)**

| Channel | Ring | Segment reached | Metric | Cost | Success threshold | Confidence |
|---------|------|-----------------|--------|------|-------------------|------------|
| Sales/marketing communities (revenue-ops, sales-enablement Slacks/forums) | inner | beachhead directly | signups → activated | low | CAC < 1 mo of Pro | [assumption] |
| Content/SEO on "actually-editable AI decks / fix Gamma PPT export" | inner | intent-driven searchers | organic signups | low | rank + signups/mo | [assumption] |
| Product-led virality (shared, editable decks carry a mark) | middle | recipients of decks | viral coefficient | low | k > 0.3 | [assumption] |
| Sales-enablement platform partnerships | middle | teams | referred accounts | med | — | [assumption] |
| Paid ads | outer | broad | CAC | high | — | [assumption] |

_Message (what we say) stays in `#uvp-cpv`; this is where we reach them._

**Expansion path**

| Order | Next segment / market / geography | Trigger that unlocks it | Confidence |
|-------|-----------------------------------|-------------------------|------------|
| 1 | Consultants / agencies (frequent client decks) | beachhead channel hits viable CAC | [assumption] |
| 2 | `.key` / Keynote users | `.pptx` fidelity proven | [assumption] |
| 3 | Non-English markets | a channel proves out in English first | [assumption] |

**Seeded registers:** `H-010` (community + PLG acquire the beachhead at viable CAC); `R-009` (channel/CAC risk).

## Product surface {#product-surface}
<!-- tool: product-surface -->
_Sketched here, refined at Step 4 (instrumentation defines where the metric tree's data comes from)._

| Surface | Type | Purpose | Instrumentation (what we measure + how) | Gap? | Confidence |
|---------|------|---------|-----------------------------------------|------|------------|
| Landing page | landing | acquisition | visits, signups (analytics) | — | [assumption] |
| Generator app | in-product | the core job | generate → export funnel, events | — | [assumption] |
| **Export flow** | in-product | the moment of truth | export success + **edit-fidelity** (% objects editable, edits made post-export) | **— to clarify —** (the key signal, not instrumented yet) | [assumption] |
| Account / billing | admin | monetization | trial→paid conversion | — | [assumption] |
| Reactivation email | mailing | retention | opens, return | — to clarify — | [assumption] |

**Behavior-study tools:** product analytics + funnels; user interviews (Step 5). 
**Infra implications (→ Step 4 costs):** LLM provider(s), the rendering/fidelity engine, analytics, email, payments.

## Architecture {#architecture}
<!-- tool: architecture-c4 -->
_C4 Context level — refined at Step 4 (external systems become cost lines + dependency risks)._

**System:** Decksmith — generates native, editable, designed `.pptx`/`.key`.

**Actors:** salespeople & marketers (beachhead); their deck recipients (viral surface).

**External systems / dependencies:**

| External system | Role | Cost driver? | Dependency risk? | Moat? |
|-----------------|------|--------------|------------------|-------|
| LLM provider(s) | content + structure generation | yes (COGS) | yes → `R-004` | — |
| Native-format render engine (`.pptx`/`.key` writer) | **the core IP** — in-house, not external | build cost | low | **yes (`H-004`)** |
| Design-corpus store | design patterns the engine learns from | small | low | supports moat |
| Auth · Payments (e.g. Stripe) · Analytics · Email | table-stakes infra | small | low | — |

_The native-format writer is the moat and is deliberately **in-house**, not a dependency; the LLM is
the dependency and cost driver (→ `R-004`, quantified at Step 4)._

## Bets {#bets}
<!-- tool: jtbd, value-definition · segment-cvp lens sharpens each into a testable entry -->
_The strategic hypotheses we're wagering on, framed on the customer's job + forces (`passport#jtbd`)._

| ID | Bet | Type | Rests on (job / force / moat) | Confidence |
|----|-----|------|-------------------------------|------------|
| H-007 | For the beachhead job, "actually-editable + designed native decks" is a strong enough wedge that salespeople & marketers switch (pull beats the "I'll still have to fix it" anxiety + PowerPoint habit) | desirability | job + forces (`#jtbd`); `H-005` | [assumption] |
| H-008 | A standalone native-fidelity+design engine can stay ahead of incumbents (Copilot/Canva) closing the wedge long enough to build lock-in | viability/moat | `H-004` + `H-001`; `analysis#opportunity` | [assumption] |
| H-009 | The beachhead will pay a standalone subscription (~$15–25) despite incumbents bundling | viability | pricing; the value gap | [assumption] |
| H-010 | Sales/marketing communities + product-led virality acquire the beachhead at viable CAC | viability | channels | [assumption] |

_Each bet is a candidate market-entry entry; the full `segment-cvp` bundle set + readiness gate is
composed and staged for test at Step 5._

## Product risks {#product-risks}
<!-- tool: risk-mitigation -->
_Pre-mortem ("it's 12 months out and the strategy failed — why?"). Existing R- risks pulled from the
register; mitigations + owners + triggers are added at Step 4._

| ID | Risk (concrete failure story) | Category | Likelihood | Impact | Confidence |
|----|-------------------------------|----------|------------|--------|------------|
| R-007 | The engine never reliably hits native-fidelity + design at scale — the whole strategy rests on this one feasibility bet (`H-001`) | product/execution | M | H | [assumption] |
| R-008 | The beachhead won't pay standalone vs bundled incumbents (Copilot/Canva at $15–30 already bundled) → no viable revenue | financial | M | H | [assumption] |
| R-009 | Community + PLG virality doesn't materialize → CAC too high to grow | market/execution | M | M | [assumption] |
| R-002 (pulled) | Incumbents close the editable+designed wedge with distribution before we build lock-in | market | H | H | [sourced: analysis] |
| R-001 (pulled) | Gamma's dominance makes head-on positioning hard | market | H | H | [sourced: analysis] |

_New this step: `R-007`, `R-008`, `R-009` → risk register. `R-001`/`R-002` pulled (already logged at Step 2)._

## To clarify {#to-clarify}

- **First format confirmed as `.pptx`** (vs `.key` or both) — assumed `.pptx`; validate against beachhead reality.
- **WTP vs bundled incumbents** — open hypothesis `H-009`; test at Step 5 (price talk / pilot), do not set now.
- **Edit-fidelity metric definition** — the key product signal (% objects editable / edits post-export) is not yet instrumented (`#product-surface`).
