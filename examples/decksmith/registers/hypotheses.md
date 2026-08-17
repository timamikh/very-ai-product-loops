---
node_type: register
register: hypotheses
title: Hypothesis register — Decksmith
updated: 2026-08-16
version: 0.1.0
---

# Hypothesis register

Every bet/assumption the loops carry, born once and refined downward, results flowing back up.
Never re-authored per step; never deleted (a refuted bet stays). Schema:
[`process/REGISTERS.md`](../../../process/REGISTERS.md). One `type` per row; cross-cutting themes
go in `tags`. `signal`/`decision` fill only after a test readout.

| ID <!--c:id--> | Statement <!--c:statement--> | Type <!--c:type--> | Tags <!--c:tags--> | Status <!--c:status--> | Born <!--c:born--> | Source <!--c:source--> | Test <!--c:test--> | Confidence <!--c:confidence--> | Signal <!--c:signal--> | Decision <!--c:decision--> |
|----|-----------|------|------|--------|------|--------|------|------------|--------|----------|
| H-001 | The engine can reliably produce slide files that are **both** genuinely native-editable **and** genuinely well-designed **at scale**, across arbitrary user content (not just demos). | feasibility | engine, quality | testing | 1 | founder brief; `1-concept/concept-formation.md`, `1-concept/concept-expansion.md` | `M-design-acceptance` ≥70% / <40% (thresholds); P1: ≥50-brief×5-vertical eval (`5-tactical-plan/hypothesis-test-design.md`) | [assumption] | | |
| H-002 | The engine can reliably produce **audience-appropriate narrative structure** (the right story for the audience), not only visual polish. | feasibility | engine, narrative | open | 1 | `1-concept/concept-expansion.md` (agent-derived split of the wrong-story pain the founder brief observed) | — | [assumption] | | |
| H-003 | Client-facing deck makers experience AI output as "templated" and **restyle it by hand**, so the promised time-saving does not materialise. | desirability | pain | open | 1 | founder brief; `1-concept/segment-pains.md` | `M-w4-retention` ≥30% (flattening) / <10% (`4-strategic-plan/hypothesis-thresholds.md`) | [assumption] | | |
| H-004 | The **wrong-structure/story** pain is significant and **distinct** from the visual pain (not merely cosmetic). | desirability | pain, narrative | open | 1 | founder brief; `1-concept/segment-pains.md` | — | [assumption] | | |
| H-005 | **Editability is a hard gate** — locked/image output disqualifies a tool regardless of its visual quality. | desirability | pain, table-stakes | open | 1 | founder brief; `1-concept/segment-pains.md`, `1-concept/jtbd-concept.md` | — | [assumption] | | |
| H-006 | **Sales & marketing client-facing deck makers (S1)** are a reachable beachhead with a recurring, company-budgeted need. | viability | segment | open | 1 | founder brief; `1-concept/segmentation.md` | `M-activated` ≥ base ramp / < conservative ramp (`4-strategic-plan/hypothesis-thresholds.md`) | [assumption] | | |
| H-007 | The **curated design corpus + founder taste/credibility** is a real, compounding moat — the editable-and-designed quality edge is hard to replicate cheaply. | viability | moat | open | 1 | `1-concept/value-definition-concept.md` | trajectory bet: `M-design-acceptance` edge holds/widens vs a matching rival (proxy) (`4-strategic-plan/hypothesis-thresholds.md`) | [assumption] | | |
| H-008 | The reachable **US beachhead** is ~3–4M sales & marketing client-facing deck-makers at ~$180/yr → SAM ~$0.3–1.5B/yr — big enough to build a venture on. | viability | sizing | open | 2 | `2-analysis/market-sizing.md` (BLS OEWS + competitor price anchor) | — | [assumption] | | |
| H-009 | The **editable-AND-designed corner is genuinely unoccupied** (design-led tools export lossily; native tools sacrifice design) — the white space is real and defensible long enough to enter. | viability | white-space | open | 2 | `2-analysis/synthesis.md`, `2-analysis/competitor-analysis.md` | — | [assumption] | | |
| H-010 | **S1 will pay a premium (~$40/seat/mo blended)** for editable-AND-designed — above the $8–20 prosumer cluster — rather than discounting to bundle/free levels. | viability | pricing | testing | 3 | `3-strategy/pricing-strategy.md`, `3-strategy/bets.md` | `M-paid-conv` ≥8% / <3% (thresholds); P1: partner price-talk **proxy** (`5-tactical-plan/hypothesis-test-design.md`) | [assumption] | | |
| H-011 | **Founder-led design-community distribution reaches S1 at a PLG-viable CAC** (near-zero on the founder's warm audience). | desirability | channel, gtm | testing | 3 | `3-strategy/channels-expansion.md`, `3-strategy/bets.md` | `M-cac` ≤$150 / >$300 (thresholds, provisional `— to clarify —`); P1: 2-wk founder recruit push, ≥8 partners (`5-tactical-plan/hypothesis-test-design.md`) | [assumption] | | |
| H-012 | The native-export **wedge converts to a durable moat** (edit-behaviour data loop + brand-kit lock-in) **before** Gamma/Canva ship real native export or Microsoft bundles it away. | viability | moat, timing | open | 3 | `3-strategy/bets.md`, `1-concept/value-definition-concept.md` (Step-3 revisit) | trajectory/timing bet: `M-w4-retention` + brand-kit adoption rise before incumbent native-export parity ships (`4-strategic-plan/hypothesis-thresholds.md`) | [assumption] | | |
| H-013 | A **named consulting community** reaches S1 consultants (recurring-QBR-deck situation) at a qualified-action signal — a distinct go-to-market channel from the founder's design community. | desirability | channel, gtm | open | 5 | `5-tactical-plan/segment-cvp.md` (bundle B-02) | staged bundle B-02 — test deferred past Period 1 (founder capacity, `5-tactical-plan/prioritization-tactical-plan.md`) | [assumption] | | |

## Change log

### 2026-08-16 — Step 5 (Period 1): `H-013` seeded; `H-001`/`H-010`/`H-011` → testing
- **From → To:** H-012 → added `H-013` (desirability: a named consulting community reaches S1, from
  staged bundle B-02); `H-001`/`H-010`/`H-011` moved `open → testing` with a Period-1 test design
  appended to `test` (50-brief eval · 2-wk recruit push · partner price-talk proxy)
- **Why:** Step 5 stages the go-to-market bundles and picks which bets to test this period.
  `segment-cvp` seeded only the genuinely-new channel claim (B-02 → `H-013`); B-01/B-05 are **instances
  of `H-011`/`H-003`**, not re-minted (one claim, one id). Thresholds are the Step-4 bars, **referenced
  not re-decided** (`hypothesis-test-design` boundary).
- **Trigger:** Step 5 pass (`#market-bundles` → `segment-cvp`; `#hypotheses-to-test` →
  `hypothesis-test-design`); status writes are the orchestrator's (acting PO)

### 2026-08-16 — Step 4: bets quantified — `test` bars upserted (hypothesis-thresholds)
- **From → To:** the 7 strategy bets (`test` empty) → each bound to an existing `M-…` node with a
  success/failure bar: `H-001`→`M-design-acceptance` (≥70%/<40%), `H-003`→`M-w4-retention`
  (≥30%/<10%), `H-006`→`M-activated` (base/conservative ramp), `H-010`→`M-paid-conv` (≥8%/<3%),
  `H-011`→`M-cac` (≤$150/>$300, bars provisional — to clarify — own-funnel), and two **trajectory
  bets** with proxy slopes not single-shot bars: `H-007`→`M-design-acceptance` edge-holds,
  `H-012`→`M-w4-retention`+brand-kit vs incumbent-parity timing
- **Why:** Step 4 pre-registers each bet's "true/false" in numbers before any spend/build so no
  result gets spun; these bars are the single source of truth Step-5 `hypothesis-test-design` reads
  and never re-decides. No new ids — existing bets quantified, not re-minted.
- **Trigger:** Step 4 pass, `#global-hypotheses` (`hypothesis-thresholds`); worklog is source of truth

### 2026-08-16 — H-010, H-011, H-012 born (Step 3 strategy); H-003 sharpened as the switching bet
- **From → To:** H-009 → added `H-010` (viability: S1 pays the premium — the monetisation bet),
  `H-011` (desirability: founder-community reaches S1 at PLG-viable CAC), `H-012` (viability: the
  export wedge converts to a durable moat before the gap closes — the timing bet)
- **Why:** Step 3 restates the strategy choices as falsifiable, moat-backed wagers. `H-001`/`H-006`/
  `H-007` were **reused** as bets (not re-minted); the desirability *switch* (S1 abandons "Gamma +
  rebuild") was folded onto existing `H-003` rather than duplicated — one claim, one id, one evidence
  trail. Only pricing/channel/moat-trajectory were genuinely new claims → three new ids.
- **Trigger:** Step 3 operating-loop pass (`#pricing`, `#channels-expansion`, `#bets`, `#how-to-win`);
  evidence is the orchestrator's own strategy reasoning (acting PO), not external research

### 2026-08-16 — H-008, H-009 born (Step 2 analysis)
- **From → To:** H-007 → added `H-008` (viability: SAM ~$0.3–1.5B US beachhead) and `H-009`
  (viability: the editable-and-designed white space is real) from the market sizing and competitive
  synthesis
- **Why:** Step 2 turns the load-bearing sizing assumption and the white-space claim into testable
  viability bets; both are `[assumption]` (bottom-up has wide bars; the white space rests on a scan,
  not a hands-on export test — see `2-analysis/synthesis.md` open items)
- **Trigger:** Step 2 operating-loop pass (`#market-sizing`, `#opportunity`); evidence from `loops-research`

### 2026-08-16 — H-001…H-007 born (Step 1 concept)
- **From → To:** empty → `H-001` (feasibility: editable+designed at scale), `H-002` (feasibility:
  narrative structure), `H-003`/`H-004`/`H-005` (desirability: restyle-tax / wrong-story /
  editability-gate pains), `H-006` (viability: S1 beachhead), `H-007` (viability: corpus+taste moat)
- **Why:** the Step 1 concept turns every segment, pain, solution mechanism and moat claim into a
  falsifiable bet; `H-001` is the riskiest assumption and the concept-viability centre of gravity
- **Trigger:** Step 1 operating-loop pass (sections `#idea`, `#jtbd`, `#segments`, `#problems`,
  `#solution`, `#value-defensibility`)

### 2026-08-16 — created
- **From → To:** — → empty register scaffolded
- **Why:** instance setup; hypotheses are born in the Step 1 pass, not at scaffold time
- **Trigger:** `product-setup` scaffolding of the Decksmith sample instance
