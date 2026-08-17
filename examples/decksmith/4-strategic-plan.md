---
node_type: artifact
artifact: strategic-plan
step: 4
title: "Strategic Plan — Decksmith (fictional sample)"
status: draft
version: 0.1.2
updated: 2026-08-17
---

# Strategic Plan — Decksmith (fictional sample)

> Status: concept-viability · Owner: acting PO (⚙️ agent) · Last review: 2026-08-16
> Inputs: `3-strategy.md` · registers. Feeds: `5-tactical-plan.md`.

> ⚠️ This artifact is the **projection** of the Step-4 worklogs in `4-strategic-plan/`. Each section's
> source of truth is its method worklog; the change-log history lives there, not here. Metric **node
> definitions** live in `registers/metric-tree.md` and **values** in `registers/metrics.csv` (empty —
> pre-launch, no readings) — this artifact references ids, never duplicates values. ⚙️ marks
> agent-proposed defaults awaiting the human's confirmation — this run never self-issues `confirmed:`.

## Architecture & instrumentation {#architecture-instrumentation}
<!-- tool: instrumentation-plan -->
<!-- rests-on: 3#architecture, 3#product-surface -->
_Where each metric's data comes from, and what drives infra cost. Full map + COGS reconciliation:
`4-strategic-plan/instrumentation-plan.md`._

| Surface / component <!--c:surface--> | Instrumentation (instrumented / proxy / not) <!--c:instrumentation--> | Data it produces <!--c:data--> | Infra cost driver <!--c:cost--> | Confidence <!--c:conf--> |
|---------------------|----------------------------------------------|------------------|-------------------|------------|
| Signup / onboarding | instrumented | signup→first-export funnel, drop-off (→ `M-activated`) | analytics (small) | [assumption] |
| Generation UI + LLM provider | instrumented | generations, tokens/deck, time-to-deck (→ `M-cogs-per-export`) | **LLM inference — the COGS line** | [assumption] |
| Native export action | instrumented | export count, format (→ `M-northstar`, count half) | export/render service | [assumption] |
| Design-acceptance / edit-behaviour | **proxy** | in-app restyle-before-export as stand-in for "off-brand" (→ `M-design-acceptance`, `M-northstar` "kept" half) | analytics | [assumption] |
| Post-export fidelity (client opens file) | **not-instrumented** | whether the file opens clean / stays edited — off our surface | — | [assumption] |
| Billing / admin | instrumented | seats, plan, MRR, churn (→ `M-arppu`, `M-paid-conv`, `M-contribution`) | — | [assumption] |
| Cohort store | not-instrumented | value-export recurrence by cohort (→ `M-w4-retention`; no data pre-launch) | analytics | [assumption] |
| Paid / community attribution | instrumented / **proxy** | CAC by paid channel (instrumented); community/organic (proxy) → `M-cac` | ad spend | [assumption] |

<!-- card -->
**Two load-bearing gaps** (→ Steps 5–6; carried as `R-012`): the design-acceptance / edit-behaviour
proxy behind the North Star, and post-export fidelity (not-instrumented — the native file leaves our
surface, which is the differentiation *and* what makes it unmeasurable).

## Metric tree {#metric-tree}
<!-- tool: metric-tree -->
<!-- rests-on: 3#how-to-win -->
_North Star → drivers → input metrics. Node **definitions** live in `registers/metric-tree.md`,
**values** in `registers/metrics.csv` (empty, pre-launch) — this section is the shape + rationale.
Candidate North Stars and the filter each loser failed: `4-strategic-plan/metric-tree.md`._

<!-- card -->
**North Star:** `M-northstar` — Weekly Native Value-Exports (on-brand decks natively exported and
*kept*, no full restyle before export) · [decision: ⚙️ awaiting human]
_Why this one: **leading** (moves before revenue) · **value-repeating** (each kept native export is
the value, and it recurs per client deck) · **strategy-encoding** (it *is* the editable-AND-designed
promise; a design-led rival's tree would top out at "decks generated" — the metric this one rejects)._

| Driver <!--c:driver--> | Node <!--c:node--> | Inputs (nodes) <!--c:inputs--> | Instrumentation <!--c:instrumentation--> |
|--------|------|----------------|-----------------|
| acquisition / activation | `M-activated` | signup→first-export funnel | instrumented |
| conversion | `M-paid-conv` | trial starts, paid starts | instrumented |
| deepening (engagement) | `M-exports-per-acct` | export events × design-acceptance | proxy |
| retention | `M-w4-retention` | cohort export recurrence | not-instrumented |

Guardrails: `M-design-acceptance` (quality — proxy), `M-contribution` (finance — instrumented),
`M-cogs-per-export` (cost — instrumented). Unit-econ inputs: `M-arppu`, `M-cac`.

**Not instrumented (→ Steps 5–6):** the design-acceptance / post-export-fidelity signal behind
`M-northstar` / `M-exports-per-acct` / `M-design-acceptance` (measures the promise itself → `R-012`);
and `M-w4-retention`, unobservable until usage history exists.

## Retention {#retention}
<!-- tool: retention-analysis -->
_Cohort retention curve + engagement loop. **concept-viability, pre-launch → no usage history; no
cohort can be formed** — every cell is censored (`—`), nothing written to `metrics.csv`. The
"why-value-repeats" signal comes from Step-1 evidence, not data. Full working:
`4-strategic-plan/retention-analysis.md`._

| Cohort (join period) <!--c:cohort--> | P1 <!--c:p1--> | P3 <!--c:p3--> | P6 <!--c:p6--> | P12 <!--c:p12--> | Flattens at <!--c:flattens--> | Shape read <!--c:shape--> | Confidence <!--c:conf--> |
|----------------------|----|----|----|-----|-------------|------------|------------|
| — (none — pre-launch) | — | — | — | — | ~mo 3–4 (benchmark) | expected flattening core | [assumption] |

- **Retained action:** a native value-export (the North Star action), **not** a login. Natural <!-- card -->
  frequency **weekly** for S1 (agencies ship client decks continuously); `M-w4-retention` read at week 4.
- Engagement loop: **trigger** (a client deck is due) → **action** (generate → native value-export) →
  **reward** (client-ready, no rebuild — restyle tax removed) → **investment** (brand kit saved,
  reused — the lock-in derivative). Whether value *does* repeat is `H-003`, untested until launch.
- Churn handed to economics as a **scenario axis** (base 5%/mo, band 3–7%) `[sourced: Recurly ~3.2%
  SaaS floor + ChartMogul ~2.3% net MRR, as_of 2026-08-16]`, adjusted up for monthly self-serve — not
  a measured curve.

## Unit economics {#unit-economics}
<!-- tool: unit-economics -->
<!-- rests-on: 3#pricing -->
_Contribution margin with LLM inference as an explicit COGS line. **Single basis** — Decksmith runs on
third-party API compute (no own GPUs), so operational and honest collapse to one. Pre-launch → every
figure modelled. Full working incl. the `pricing-strategic-plan` verdict:
`4-strategic-plan/unit-economics.md`._

| Metric <!--c:metric--> | Operational <!--c:operational--> | Honest (+depreciation / market compute) — own-compute only <!--c:honest--> | Assumptions <!--c:assumptions--> |
|--------|-------------|------------------------------------------------------------|-------------|
| Revenue per payer ($/mo) | ~$33 (→ `M-arppu`) | n/a (single basis — API compute) | [assumption: 60/35/5 Solo/Team/Studio mix] |
| COGS per payer ($/mo) | ~$3–4 (inference ~$1.70 + infra ~$1.50; tail ~$13) | n/a | [assumption: ~10 decks/payer, power-law tail; inference $0.17/deck sourced as_of 2026-08-16] |
| Contribution ($/mo · %) | ~$29.5 · ~89% (→ `M-contribution`) | n/a | inference dwarfed by a $33 subscription |
| CAC (by channel) | community ~$150 · paid ~$400 (→ `M-cac`) | n/a | [assumption: directional — report-mill only; — to clarify — own-funnel read] |
| Payback | community ~5 mo · paid ~14 mo | n/a | ceiling ≤12 mo [sourced: Skok/Bessemer, as_of 2026-08-16] |
| LTV | — churn 3/5/7% ⚙️ → ~$975 / ~$590 / ~$415 — | n/a | uses the `#retention` axis; LTV/CAC community 6.5×/3.9×/2.8× |

<!-- card -->
**Finding:** at these prices inference is **not** the margin threat; the binding viability constraints
are **WTP (`H-010`)** and **CAC/payback (`H-011`)** — paid-search is thin-to-underwater, community is
the inner ring. `pricing-strategic-plan` verdict: **HOLDS** (no ⚙️ change to `3#pricing`).

## Financial model {#financial-model}
<!-- tool: financial-model -->
<!-- rests-on: 2#market-sizing, 3#pricing -->
_A simple driver-based projection; churn as a scenario axis; the capacity ceiling first-class.
**Pre-launch, no run-rate → an illustrative shape, not a forecast.** Full working:
`4-strategic-plan/financial-model.md`._

| Driver <!--c:driver--> | Base <!--c:base--> | Assumption <!--c:assumption--> | Confidence <!--c:conf--> |
|--------|------|------------|------------|
| New paying accounts / mo (`M-activated`→`M-paid-conv`) | ramp 20 → 120 over 12 mo | founder-community + content inner ring | [assumption] |
| Churn / mo (scenario axis) | 5% base (3% / 7%) | from `#retention` benchmark | [assumption] |
| ARPPU (`M-arppu`) | ~$33/mo | mix assumption | [assumption] |
| COGS / payer (`M-cogs-per-export` +infra) | ~$3.5/mo | inference trivial | [assumption] |
| CAC blended (`M-cac`) | ~$150 community → ~$400 if paid leans in | directional | [assumption] |
| Fixed costs / mo | ~$40–80k ⚙️ | small team + founder | [assumption] |

- **Capacity ceiling: the founder, not the servers.** Compute scales elastically; the binding caps are <!-- card -->
  human — founder-community channel saturation (`R-008`, ~mo 6–9 ⚙️) and founder-as-corpus/taste
  bottleneck (`R-010`). Saying *when* the human cap binds is the model's main output, not the MRR line.
- **Scenarios @ mo-12** (illustrative — the point is the ~2× spread, not the decimals): conservative
  7%/mo ~400 accts/~$13k · **base 5%/mo ~600 accts/~$20k** · stretch 3%/mo ~850 accts/~$28k.
- Breakeven ≈ **~2,000 paying accounts** ⚙️ — beyond the 12-mo base ramp: a **fund-and-prove-fit**
  phase, not self-funding. Honest and expected at `concept-viability`.

## Strategic targets {#strategic-targets}
<!-- tool: strategic-targets -->
<!-- rests-on: 3#winning-aspiration -->
_Horizon commitments anchored to the base scenario — read off it where it outputs the number,
derived or committed as a driver bar where it doesn't (per-node provenance in the worklog).
`metric-tree` defines the node, this commits its horizon value, Step-5 `goal-targets` sets the
period value. Full working + nodes left untargeted: `4-strategic-plan/strategic-targets.md`._

<!-- card -->
**Horizon:** ⚙️ **+12 months from launch** — provisional. `3#winning-aspiration` names "this horizon"
with **no explicit date**; per the method a missing horizon is an upstream gap (→ `#open-questions`),
flagged not invented. Targets rest on a model with no actuals — doubly ⚙️.

| Node (`M-…`) <!--c:node--> | Target at horizon <!--c:target--> | From scenario <!--c:scenario--> | Why this node <!--c:why--> | Confidence <!--c:conf--> |
|--------------|-------------------|---------------|---------------|------------|
| `M-northstar` | ~600 WNVE/wk | base, derived (~600 accts × ~1 export/acct/wk ⚙️) | the value delivered — the whole strategy in one number | [assumption] |
| `M-paid-conv` | ≥ 8% | driver bar (`H-010`), not a scenario output | the WTP/monetisation bet `H-010` made visible | [assumption] |
| `M-w4-retention` | ≥ 30% floor | driver bar (`H-003`), not a scenario output | the switch *sticking* (`H-003`); a flattening core is the fit signal | [assumption] |
| `M-contribution` | ≥ $25/mo (~80%) | base §5 (read off: ~$29.5/payer) | the margin guardrail — stay economic while chasing volume | [assumption] |

**Decided:** 2026-08-16 · **by:** acting PO ⚙️ (awaiting human) · **alternatives considered:** the
conservative/stretch scenario values (e.g. WNVE ~400 / ~850) — base chosen as the honest middle. ⚙️
while unconfirmed. **Ladder rule:** Step-5 period targets each step toward these; a period moving no
horizon target is drift, visible at the Step-5 gate.

## Capabilities & systems {#capabilities}
<!-- tool: capabilities-systems -->
<!-- rests-on: 3#how-to-win, 3#where-to-play -->
_What we must be reliably great at for the winning logic to hold, and the system that builds and
measures each (Playing to Win, choices 4–5). Gaps seed `R-…`. Rejected nice-to-haves + gap
reconciliation: `4-strategic-plan/capabilities-systems.md`._

| Capability <!--c:capability--> | Serves (element / moat) <!--c:serves--> | Level <!--c:level--> | Gap & close <!--c:gap--> | Management system <!--c:system--> | Owner <!--c:owner--> | Confidence <!--c:conf--> |
|------------|--------------------------|-------|--------------|--------------------|-------|------------|
| Curate + label a design corpus and encode taste into the generator | out-design the native-export tools (`H-007`) | partial | build corpus pipeline + labelling by launch → `R-009` | design-review cadence; slip signal `M-design-acceptance` | founder / design ⚙️ | [assumption] |
| Reliably emit valid, on-brand native `.pptx`/`.key` at scale on arbitrary content | out-export the design-led tools (`H-001`) | missing/unproven | the core feasibility build — *is* `H-001`; closes only by proving it | export-fidelity test suite; slip signal `M-design-acceptance` + export-success | eng ⚙️ | [assumption] |
| Instrument edit-behaviour + ship brand-kit storage | convert wedge → durable moat (data loop + lock-in, `H-012`) | missing | build instrumentation + brand-kit store → **seeds `R-012`** | the instrumentation plan; slip signal = the gap itself | eng ⚙️ | [assumption] |
| Run a self-serve funnel + a founder-led community engine | PLG + founder-led distribution (`3#channels-expansion`) | partial | activation + community ops → `R-008` | funnel review; slip signal `M-activated`, `M-cac` | acting PO ⚙️ | [assumption] |

## Risk mitigation {#risk-mitigation}
<!-- tool: risk-mitigation -->
<!-- rests-on: 3#product-risks -->
_Each carried `R-…` made **managed**: an action, an owner, an observable trigger, a review date, a
lifecycle status. Upserted into `registers/risks.md` — this is a projection of those rows. Scores
travel from the pre-mortem/niche triage. Full working: `4-strategic-plan/risk-mitigation.md`._

| `R-…` <!--c:register--> | Risk <!--c:risk--> | Likelihood <!--c:likelihood--> | Impact <!--c:impact--> | Mitigation <!--c:mitigation--> | Owner <!--c:owner--> | Trigger <!--c:trigger--> | Due <!--c:due--> | Status <!--c:status--> |
|-------|------|------------|--------|------------|-------|---------|-----|--------|
| R-001 | funded incumbents accelerating | H | H | ship the wedge in the narrow S1 niche; don't fight broad | founder ⚙️ | an incumbent announces native-export parity | quarterly | mitigating |
| R-002 | bundled substitutes (Copilot/Gemini) | H | H | position on taste, not price; target S1 the bundle won't satisfy | acting PO ⚙️ | Copilot ships on-brand designed decks | quarterly | mitigating |
| R-003 | low entry barriers / thin moat | H | H | convert wedge → data + lock-in on the `H-012` trajectory; instrument early | founder ⚙️ | a clone reaches design-acceptance parity | quarterly | mitigating |
| R-004 | model-supplier power | M | M | provider-abstraction + multi-provider fallback; monitor COGS | eng ⚙️ | provider price/rate/access change >20% | on provider change | mitigating |
| R-005 | monetization trap | M | H | paid fences + tight trial from day one; measure `M-paid-conv` | acting PO ⚙️ | `M-paid-conv` below the `H-010` band | monthly (post-launch) | mitigating |
| R-006 | platform / format dependency | L | M | export-fidelity suite across PPT/Keynote; watch format/API changes | eng ⚙️ | a format/API change breaks native export | on Office/macOS release | open |
| R-007 | timing / moat-erosion (twin of `H-012`) | H | H | race the data-loop + brand-kit lock-in before the gap closes; close `R-012` first | founder ⚙️ | Gamma/Canva ship native `.pptx` parity | quarterly | mitigating |
| R-008 | GTM channel doesn't scale (twin of `H-011`) | M | H | validate a 2nd inner-ring channel early; watch `M-cac` | acting PO ⚙️ | community new-payers plateau / `M-cac` > ~$300 | monthly | mitigating |
| R-009 | taste doesn't travel | M | H | corpus breadth + per-vertical style tests; a design-acceptance gate before scaling | founder / design ⚙️ | `M-design-acceptance` below floor across verticals | design gate + monthly | mitigating |
| R-010 | key-person dependency | M | M | codify taste into rubrics; document the system; train a 2nd curator | founder ⚙️ | founder review queue > threshold | +6 mo | mitigating |
| R-011 | WTP overestimated (twin of `H-010`) | M | H | WTP survey + price test in pilot; hold premium, measure `M-arppu`/`M-paid-conv` | acting PO ⚙️ | `M-paid-conv` below the `H-010` failure bar | pilot readout | mitigating |
| R-012 | instrumentation gap behind the North Star + data-loop moat | M | H | build design-acceptance proxy + edit-behaviour capture in first release; prioritise NS instrumentation | eng ⚙️ | North Star still proxy-only at launch + 1 mo | launch gate | mitigating |

## Global hypotheses {#global-hypotheses}
<!-- tool: hypothesis-thresholds -->
<!-- rests-on: 3#bets -->
_Strategy bets, now quantified & tied to metric nodes (threshold set here; test design at Step 5).
Bars are the single source of truth — Step 5 references, never re-decides. Provenance per bar:
`4-strategic-plan/hypothesis-thresholds.md`._

| `H-…` <!--c:register--> | Bet <!--c:bet--> | Metric node (`M-…`) <!--c:node--> | Success threshold <!--c:success--> | Failure threshold <!--c:failure--> | Confidence <!--c:conf--> |
|-------|-----|---------------------|-------------------|-------------------|------------|
| H-001 | engine does editable-AND-designed at scale (the enabler) | `M-design-acceptance` | ≥ 70% kept without a full restyle | < 40% | [assumption] |
| H-003 | S1 switches from "Gamma/Canva + manual rebuild" | `M-w4-retention` | ≥ 30% wk-4, curve flattening | < 10% | [assumption] |
| H-006 | S1 US is a reachable, budgeted beachhead | `M-activated` | meets the base activation ramp | below the conservative ramp | [assumption] |
| H-007 | taste corpus + founder credibility is a compounding moat | `M-design-acceptance` (trajectory proxy) | acceptance edge holds/widens vs a matching rival | edge flat/declining as rivals match | [assumption] |
| H-010 | S1 pays a premium (~$40/seat/mo) | `M-paid-conv` | ≥ 8% trial→paid at premium | < 3% | [assumption] |
| H-011 | founder-community reaches S1 at PLG-viable CAC | `M-cac` | ≤ $150 (payback ≤ ~5 mo) | > $300 (payback > ~14 mo) — bars provisional, `— to clarify —` | [assumption] |
| H-012 | wedge → durable moat before the export gap closes | `M-w4-retention` (trajectory proxy) + brand-kit adoption | retention + lock-in rise before incumbent native-export parity | incumbent parity ships first / lock-in flat | [assumption] |

`H-007` and `H-012` are **trajectory bets** — resolved as a slope against a moving competitor, not one
readout; each bound to a proxy node with an external-event failure condition, both dependent on the
`R-012` instrumentation being built to be observable at all.

## Open questions {#open-questions}
<!-- open -->
_What's still unknown, explicitly — not hidden._

- **Horizon date is an upstream gap.** `3#winning-aspiration` names "this horizon" with no date;
  `#strategic-targets` runs on a ⚙️ provisional +12mo. **Needs the human to fix the aspiration's date**
  before the targets are more than illustrative.
- **CAC has no primary source.** `#unit-economics` CAC (~$150 community / ~$400 paid) is directional,
  report-mill-anchored only — `— to clarify —` an OpenView/KeyBanc primary or an own-funnel read
  before any CAC target is committed (why `M-cac` is left untargeted in `#strategic-targets`).
- **The North Star's "kept/accepted" clause is proxy-only** (`R-012`). Post-export fidelity is
  not-instrumented — the native file leaves our surface. Closing this is Steps 5–6 work and the
  gating capability for the data-loop moat (`H-012`).
- **Fixed costs (~$40–80k/mo) and the deck-per-payer mix** are ⚙️ assumptions with wide bars; they
  swing breakeven and the tail-COGS risk.

**Checked, not confirmed.** A check that came back neither validated nor refuted is a result: written
down it stops the next cycle from re-running it.

| What we checked <!--c:checked--> | What the data said <!--c:said--> | Why it is not a verdict <!--c:why--> | Moved <!--c:moved--> |
|-----------------|--------------------|-------------------------|-------|
| Is LLM inference the margin threat? | ~$0.17/deck vs a ~$33 subscription → ~89% contribution; even the power-user tail ~61% | not a *bet* — a modelled finding on ⚙️ deck-mix assumptions, no actuals; but firm enough to redirect discipline | `R-005` (mitigation re-aimed at conversion/fences, not cost); no `H-` |
| Does the Step-3 price survive the margin? | all three tiers clear ~85–90% contribution; no tier underwater | a `pricing-strategic-plan` verdict on modelled costs, not a market WTP test — WTP is still `H-010` | pricing HOLDS (logged, not re-decided); `H-010` still open |
| Can week-4 retention be measured now? | no — pre-launch, every cohort censored | absence of data, not a refutation | `M-w4-retention` marked not-instrumented; `H-003` untested until launch |

## Change log

### 2026-08-17 — card lines marked for the console board
- **From → To:** no section carried a `<!-- card -->` mark → 6 section(s) with a natural headline
  line now mark it; table-only sections stay unmarked (title and status only, the body one expand away)
- **Why:** the console no longer composes a card face of its own — a board card shows the author's
  marked line verbatim or nothing (CONVENTIONS → *Card line*)
- **Trigger:** console rework — a card is a collapsed section, not a third text

### 2026-08-17 — human review pass: target provenance made honest
- **From → To:** `#strategic-targets` claimed all four horizon values were "read off the base
  scenario" → the scenario column now states each value's real provenance: `M-contribution` read off
  the model, `M-northstar` derived via an assumed exports-per-account multiplier,
  `M-paid-conv`/`M-w4-retention` committed as the driver bars the scenario assumes
- **Why:** the financial model outputs accounts and MRR — the old wording laundered hypothesis bars
  into scenario outputs; fixed at the worklog first, re-projected here
- **Trigger:** human review of the finished run (strategy lens)

### 2026-08-16 — created (Step 4 projection)
- **From → To:** — → full Step-4 strategic plan projected from the nine `4-strategic-plan/` worklogs
  (instrumentation, metric-tree, retention, unit-economics, financial-model, strategic-targets,
  capabilities-systems, risk-mitigation, hypothesis-thresholds); references the 10 `M-…` nodes, 12
  `R-…`, and the 7 quantified `H-…` bets in the registers — never duplicating their values
- **Why:** Step 4 is instruments & resources — the North-Star tree, the economics, the horizon
  targets, the capability system, and the pre-registered bet thresholds the lower ladder references
- **Trigger:** Step 4 operating-loop pass; worklogs are the source of truth, this artifact their
  keyed projection
