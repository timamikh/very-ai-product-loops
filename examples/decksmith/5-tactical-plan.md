---
node_type: artifact
artifact: tactical-plan
step: 5
title: "Tactical Plan — Decksmith (fictional sample) · Period 1"
status: draft
version: 0.1.0
updated: 2026-08-16
---

# Tactical Plan — Decksmith (fictional sample) · Period 1

> Status: concept-viability · Owner: acting PO (⚙️ agent) · Period: **Period 1 "Prototype-to-first-signal"** — ⚙️ ~8 weeks (no calendar dates; horizon undated, `4#open-questions`)
> Inputs: `4-strategic-plan.md` · registers. Feeds: `6-sprint-plan.md`.

> ⚠️ This artifact is the **projection** of the Step-5 worklogs in `5-tactical-plan/`. Each section's
> source of truth is its method worklog; the change-log history lives there. Metric **values** live in
> `registers/metrics.csv` (empty — pre-launch); this artifact references `M-…`/`H-…`/`R-…` ids, never
> duplicating register values. ⚙️ marks agent proposals awaiting the human — this run never
> self-issues `confirmed:`.

**Period gate (concept-viability — learning, not traction):** **(A)** a native-export engine that
clears an internal design-acceptance eval (`H-001`); **(B)** the first qualified S1 signals from the
founder-community channel (recruit design partners `H-011` + a WTP price-talk `H-010`).

## Period goals {#period-goals}
<!-- tool: prioritization-tactical-plan -->
<!-- rests-on: 4#metric-tree -->
_Measurable goals for the period, grouped by direction. N=9 candidates ranked by gate contribution;
5 musts drawn at the capacity line; cuts kept in `5-tactical-plan/prioritization-tactical-plan.md`._

| Direction <!--c:direction--> | Goal (measurable) <!--c:goal--> | Why now <!--c:why--> | Confidence <!--c:conf--> |
|-----------|-------------------|---------|------------|
| development | **G-D1** — native-export engine emits valid, on-brand `.pptx`/`.key` and passes the design-acceptance eval | gate (A); the whole how-to-win rests on `H-001` — the long pole | [assumption] |
| development | **G-D2** — instrument the design-acceptance / edit-behaviour proxy in the build | gate (A) is unreadable without it; closes `R-012` early | [assumption] |
| go-to-market | **G-G1** — recruit ≥8 S1 design partners via the founder community | gate (B); the founder-channel bet `H-011`, cheap and fast | [assumption] |
| go-to-market | **G-G2** — run a WTP price-talk with recruited partners | gate (B) monetisation `H-010`; near-zero marginal cost on G-G1 | [assumption] |
| back-office | **G-B1** — billing/analytics plumbing (seats · MRR · funnel events · price page), lean | enabler — the G-G1/G-G2 signals need somewhere to land | [assumption] |

**Backlogged (recorded, not silently dropped):** activation funnel (late-period), provider-abstraction
+ ToS, a paid-ad probe. **Cut this period:** brand-kit storage (premature before the wedge is proven).

## Goal targets {#goal-targets}
<!-- tool: goal-targets -->
<!-- rests-on: 4#metric-tree, 4#strategic-targets -->
_Go-to-market → an existing `M-…` node (baseline → target); technical & back-office → a binary DoD.
**No baseline exists — pre-launch, `metrics.csv` empty** — so each target is a first rung from zero.
Full reasoning: `5-tactical-plan/goal-targets.md`._

| Goal <!--c:goal--> | Direction <!--c:direction--> | Target: `M-…` or DoD <!--c:target--> | Baseline → target <!--c:baseline--> | Confidence <!--c:conf--> |
|------|-----------|----------------------|-------------------|------------|
| G-D1 | development | **DoD** — valid native export on ≥50 briefs × ≥5 verticals **and** `M-design-acceptance` ≥70% on that eval | — → done | [assumption] |
| G-D2 | development | **DoD** — acceptance/edit-behaviour proxy emits events; the G-D1 eval is readable from instrumented data | — → done | [assumption] |
| G-G1 | go-to-market | `M-activated` (partners reaching a first native value-export) — ladders to `M-northstar` ~600 WNVE | — → **≥6 activated of ≥8 recruited** | [assumption] |
| G-G2 | go-to-market | `M-paid-conv` (**proxy** — qualified price-talk acceptance, not instrumented trial→paid) — ladders to ≥8% | — → **≥5 of ~8 accept a premium price-talk** | [assumption] |
| G-B1 | back-office | **DoD** — seat/MRR/funnel events instrumented + a price page live (lean, not full billing) | — → done | [assumption] |

**Drift check:** the period moves the two horizon targets that *can* move at concept-viability
(`M-northstar` via G-G1, `M-paid-conv` via G-G2); `M-w4-retention` and `M-contribution` correctly wait
(unobservable / no payers yet). Not drift.

## Guardrails {#guardrails}
<!-- tool: guardrails -->
<!-- rests-on: 4#metric-tree -->
_What must **not** drop while hitting the goals. All 7 break-categories checked (cleared ones recorded
in `5-tactical-plan/guardrails.md`); retention/churn/support left un-guardrailed — no data pre-launch._

| Guardrail (`M-…`) <!--c:guardrail--> | Must stay <!--c:muststay--> | Red line <!--c:redline--> | Why <!--c:why--> | Confidence <!--c:conf--> |
|-------------------|-----------|----------|-----|------------|
| `M-design-acceptance` | ≥ 60% during the build (rising to the 70% `H-001` bar) | < 40% on any vertical → stop scaling the eval, fix the corpus | don't win export *volume* by shipping decks the maker restyles — that kills the wedge (ties `R-009`) | [assumption] |
| `M-cac` (proxy) | ≤ $150 blended on the founder channel | > $300 → halt the paid probe, stay founder-only | don't buy the G-G1 signal with spend that breaks payback (ties `R-008`/`R-011`) | [assumption] |

**Red lines (qualitative, no metric):** (1) never ship locked / image-only export — editability is the
`H-005` table-stakes gate; (2) no dark-pattern fences / no charge without consent (`R-005` is
conversion mechanics, not tricks); (3) corpus content licensed or original only — **mints `R-013`**
(corpus IP/licensing).

## Resources {#resources}
<!-- tool: resource-check -->
_Capacity survey — **stated, not measured**. This is a fictional run with no human to survey, so every
figure is acting-PO ⚙️ and the whole survey is `— to clarify —` for the founder. `5-tactical-plan/resource-check.md`._

| Resource <!--c:resource--> | Available this period <!--c:available--> | Constraint <!--c:constraint--> | Confidence <!--c:conf--> |
|----------|-----------------------|------------|------------|
| people | dev ~2.2 FTE (founder-eng + 1 FT + 0.5 contract) · go-to-market founder ~0.3 FTE · back-office ~0.2 FTE | **binding: dev throughput on the export engine + founder taste/curation bandwidth** (twin `R-010`) | [assumption] ⚙️ `— to clarify —` |
| budget | ~$15k (inference eval > infra > a minimal paid probe) | small; earmark is the eval, not headcount | [assumption] ⚙️ `— to clarify —` |
| time | ~8 weeks; one stage-gate at the period boundary | no fixed external dates | [assumption] ⚙️ `— to clarify —` |

## Market-entry bundles {#market-bundles}
<!-- tool: segment-cvp -->
<!-- rests-on: 1#segments, 3#uvp-cpv -->
_Candidate go-to-market entries, gated on readiness (6 filters + 1·3·5 score). 9 composed (7 S1
situations + 1 adjacent + 1 deliberate reject); top 3 staged. Scores/rejects in
`5-tactical-plan/segment-cvp.md`._

| ID <!--c:id--> | Segment <!--c:segment--> | Situation <!--c:situation--> | Pain <!--c:pain--> | CVP <!--c:cvp--> | Offer <!--c:offer--> | Channel <!--c:channel--> | Signal · tier <!--c:signal--> | Readiness <!--c:readiness--> | `H-…` <!--c:register--> | Confidence <!--c:conf--> |
|----|---------|-----------|------|-----|-------|---------|---------------|-----------|-------|------------|
| B-05 | S1 freelance designer | multi-SMB-client deck work | deck volume caps billable clients | "10× your output, keep your taste" | trial | founder design community | paid sub · **strong** | ready · **23** (staged) | H-011 | [assumption] |
| B-01 | S1 agency | client pitch on deadline | night-before rebuild by hand | "client-ready native deck, zero rebuild" | design-partner trial | founder design community | pilot + price-talk · **strong** | ready · **21** (staged) | H-011 / H-003 | [assumption] |
| B-02 | S1 consultant | recurring monthly QBR deck | re-skinning the report monthly | "productise your report deck, on-brand monthly" | diagnostic + trial | named consulting community | trial + repeat · **strong** | ready · **19** (staged) | H-013 | [assumption] |
| B-07 | S1 agency | RFP response deck overnight | brief → deck under time pressure | "RFP brief → editable deck by morning" | trial | agency-owner Slack | pilot · **strong** | ready · 17 (next) | H-011 | [assumption] |
| B-04 | S1 sales rep | per-prospect customisation | rebuild per prospect | "personalise every pitch, no rebuild" | trial | sales-enablement community | seat expansion · **strong** | ready · 15 | H-011 | [assumption] |
| B-06 | S2 (adjacent) founder | investor deck | locked image or ugly editable | "investor-ready, editable" | template + trial | IndieHackers / accelerator | trial · medium | ready · 13 (off-beachhead) | — | [assumption] |
| B-03 | S1 in-house marketer | rebrand rollout | re-skin the deck library by hand | "re-skin the library, still editable" | brand-kit demo | LinkedIn content + SEO | demo → meeting · medium | ready · 11 (needs brand-kit) | — | [assumption] |
| B-09 | S1 marketer | conference/speaker deck | one-off on-brand deck | "on-brand speaker deck in an afternoon" | template + trial | event/community | trial · medium | ready · 11 (low pain) | — | [assumption] |
| B-08 | "SMB owners" (mass) | — | "would be nice" | "better decks with AI" | trial | "online" | interest · weak | **not-ready** (fails 6/6 — reference reject) | — | [assumption] |

**Staged (top 3 by readiness):** B-05, B-01, B-02. **Tested this period:** B-01/B-05 via the `H-011`
recruit push (G-G1); **B-02's bet `H-013` is deferred** to a later period on founder capacity
(`#hypotheses-to-test`). Seeding: B-01/B-05 are instances of `H-011`/`H-003` — **not** re-minted; B-02
mints **`H-013`**.

## Hypotheses to test {#hypotheses-to-test}
<!-- tool: hypothesis-test-design, ab-test -->
<!-- rests-on: 4#global-hypotheses -->
_One row per `H-…` tested this period — a pre-registered read; thresholds referenced from Step 4, never
re-decided. Bets waiting (H-003 needs usage history; H-012 is a trajectory bet; H-013 deferred on
capacity) are recorded in `5-tactical-plan/hypothesis-test-design.md`._

| `H-…` <!--c:register--> | Metric node (`M-…`) <!--c:node--> | Success <!--c:success--> | Failure <!--c:failure--> | Sample / duration <!--c:sample--> | Decision rule <!--c:decision--> | Confidence <!--c:conf--> |
|-------|---------------------|---------|---------|-------------------|---------------|------------|
| H-001 | `M-design-acceptance` | ≥ 70% kept | < 40% | ≥50 briefs × ≥5 verticals / within the build | ≥70% → validated; <40% → refuted (corpus rework); 40–70% → iterate worst verticals, re-eval | [assumption] |
| H-011 | `M-cac` (proxy) / `M-activated` | ≤ $150 (≥8 recruited) | > $300 (or <3 recruited) | 1 founder recruit push / ~2 wk | ≥8 at ≤$150 → validated; <3 or >$300 → refuted (`R-008`); between → one more push | [assumption] |
| H-010 | `M-paid-conv` (**proxy**: price-talk) | ≥5 of ~8 accept premium | ≤1 of 8 | ~8 partner price-talks / rides on H-011 | ≥5 → validated(proxy) → design instrumented test next period; ≤1 → refuted (`R-011`); between → price follow-up | [assumption] |

## Readouts {#readouts}
<!-- tool: experiment-readout -->
_Verdicts of tests that finished this period. **Period 1 finishes none** — it launches the three above;
reading now would be peeking. Stated, not skipped. `5-tactical-plan/experiment-readout.md`._

| `H-…` <!--c:register--> | Test <!--c:test--> | Result vs rule <!--c:result--> | Signal <!--c:signal--> | Decision <!--c:decision--> | Follow-up <!--c:followup--> | Confidence <!--c:conf--> |
|-------|------|----------------|--------|----------|-----------|------------|
| — | no test finished this period (P1 launches H-001 / H-011 / H-010) | n/a — reading before the pre-registered sample = peeking | — | — | the three readouts land at the Period-1 boundary → next period | n/a |

## Blockers {#blockers}
<!-- open -->
_Dependencies / blockers with an owner (link back to `R-…`)._

| Blocker <!--c:blocker--> | Owner <!--c:owner--> | Links (`R-…`) <!--c:links--> | Status <!--c:status--> | Confidence <!--c:conf--> |
|---------|-------|---------------|--------|------------|
| Native-export fidelity across PPT/Keynote versions must hold before G-D1 sign-off | eng ⚙️ | R-006 | open | [assumption] |
| Design-acceptance instrumentation (G-D2) gates whether the G-D1 eval can be read | eng ⚙️ | R-012 | open | [assumption] |
| Model-provider access / cost / rate for the eval batch | eng ⚙️ | R-004 | open | [assumption] |
| Founder bandwidth is shared across curation (dev) and recruitment (g2m) — the binding constraint | founder ⚙️ | R-010 | open | [assumption] |
| Corpus licensing/provenance unresolved could block using real design references | acting PO / legal ⚙️ | R-013 | open | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
- **Horizon date** — still an upstream gap (`4#open-questions`); Period 1 is bounded by *length* (~8
  wk) not dates, and the horizon targets it ladders to stay ⚙️ provisional.
- **Capacity is un-attributed** — no real human confirmed the people/budget/time; the founder must
  confirm before Period 1 is committed (`resource-check` `— to clarify —`).
- **H-010 reads a proxy**, not the instrumented trial→paid rate (no funnel pre-launch); the Step-4 bar
  is not moved to fit the proxy — the instrumented test is next period.
- **H-003 / H-012 not testable this period** — retention needs usage history; the moat/timing bet is a
  trajectory, not a one-period read.

**Checked, not confirmed.** A check that came back neither validated nor refuted is a result — written
down so the next cycle doesn't re-run it.

| What we checked <!--c:checked--> | What the data said <!--c:said--> | Why it is not a verdict <!--c:why--> | Moved <!--c:moved--> |
|-----------------|--------------------|-------------------------|-------|
| Do 8+ go-to-market bundles survive the readiness gate? | 8 of 9 ready; the mass-audience bundle (B-08) failed all six filters | a readiness gate result, not a market test — readiness ≠ desirability | staged B-05/B-01/B-02; B-08 kept as the guard |
| Can the founder channel be tested cheaply now? | yes — a 2-wk recruit push needs no product | it designs the test; the *result* is `H-011`, still testing | `H-011` → testing (no verdict yet) |

## Change log

### 2026-08-16 — created (Step 5, Period 1 projection)
- **From → To:** — → full Period-1 tactical plan projected from the seven `5-tactical-plan/` worklogs
  (prioritization, goal-targets, guardrails, resource-check, segment-cvp, hypothesis-test-design,
  experiment-readout); references `M-activated`/`M-paid-conv`/`M-design-acceptance`/`M-cac`, the bets
  `H-001`/`H-010`/`H-011` (→ testing) + new `H-013`, and risks incl. new `R-013` — never duplicating
  register values
- **Why:** Step 5 turns the strategy into a capacity-bounded period of focused work: goals per
  direction, targets that ladder to the horizon, guardrails, staged bundles, and pre-registered tests
- **Trigger:** Step 5 operating-loop pass; worklogs are source of truth, this artifact their projection
