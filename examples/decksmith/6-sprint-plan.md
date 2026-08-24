---
node_type: artifact
artifact: sprint-plan
step: 6
title: "Sprint Plan — Decksmith (fictional sample) · Sprint 1"
status: draft
version: 0.2.0
updated: 2026-08-23
---

# Sprint Plan — Decksmith (fictional sample) · Sprint 1 (⚙️ ~2 wk, no dates)

> Status: concept-viability · Owner: acting PO (⚙️ agent) · Capacity: ~2 features · 1 activity · 1 task (must)
> Inputs: `5-tactical-plan.md` · registers. Hands off to: the team's development process.

> ⚠️ This artifact is the **projection** of the Step-6 worklogs in `6-sprint-plan/`
> (`prioritization-sprint-plan`, `feature-spec`, `activity-spec`, `task-spec`). Each item's source of
> truth is its method worklog; the change-log history lives there. Every item links an `H-…`/`M-…`
> (and an activity names its `B-…`), and names the feature-register row it advances (`F-…`,
> `registers/features.md`) — new candidates were minted there as `planned` by the item specs. ⚙️
> marks agent proposals; this run never self-issues `confirmed:`.

## Sprint goal {#sprint-goal}
<!-- synthesis -->
<!-- rests-on: 5#period-goals -->

- **Stand up the first shippable slice of the native-export engine and its acceptance <!-- card -->
  instrumentation, and launch founder-community partner recruitment** — i.e. *start* period gate (A)
  (`H-001` becomes measurable) and *start* (B) (`H-011` clock running). At `concept-viability` the
  sprint's job is to make the bet **testable**, not to hit traction.

## Must {#must}
<!-- rests-on: 5#period-goals, 5#hypotheses-to-test -->
_Minimal mandatory items — without which the period goal is unreachable. Grouped by direction.
Ranking/line: `6-sprint-plan/prioritization-sprint-plan.md`._

### Development — Features
<!-- tool: feature-spec, prioritization-sprint-plan -->

**1 · Native-export engine — first vertical slice (`.pptx`)** — links: `H-001` / `M-design-acceptance`
- **Feature:** `F-001` (native export engine — this item builds its first slice)
- **Description:** the core generator → valid, natively-editable `.pptx` on the primary template
  families (title · agenda · content · chart · closing) — the "editable" half of the wedge, first slice.
- **Scope:** brief→outline→layout mapping; native `.pptx` shape/text/theme emission; theme-token
  application; a ~10-brief smoke set across the primary verticals.
- **Acceptance criteria:** (1) `.pptx` opens clean in PowerPoint **and** Google Slides, no repair
  prompt; (2) every text box/shape natively editable (no flattened images); (3) every slide renders the
  single applied theme's tokens — no off-theme colour; (4) the ~10-brief smoke set exports with no hard
  failure.
- **Business value:** the enabler bet `H-001`; moves `M-design-acceptance` and unblocks the metric
  tree. Gate (A) is unreachable without this slice starting now.
- **User value:** a client-ready deck the maker edits in their own tool — zero rebuild.
- **User stories:** *As an agency deck-maker, I want the AI's deck as a real editable `.pptx`, so I can
  tweak a slide without rebuilding it from a screenshot.*
- **Expected impact:** makes `H-001` measurable — `M-design-acceptance` readable on the ~10-brief
  smoke set (no eval verdict yet; that is F-005's read) · check-by Sprint-2 gate [assumption]
- **Owner:** founder-engineer ⚙️
- **Estimate:** L (~1.3 dev-FTE, the sprint's heavy build) — [assumption] until the readout reads the actual

**2 · Design-acceptance / edit-behaviour instrumentation** — links: `M-design-acceptance` / `M-northstar` / `R-012`
- **Feature:** `F-002`
- **Description:** capture the proxy behind the North Star's "kept" clause (export without a full
  in-app restyle) so item 1 can be *read*, not eyeballed.
- **Scope:** instrument export + restyle-before-export events, per-vertical tagging, a minimal internal
  dashboard for the eval read.
- **Acceptance criteria:** (1) every export emits an event with vertical + a restyle flag; (2)
  `M-design-acceptance` is computable from instrumented data for the smoke set; (3) events land in the
  store the eval harness (`F-005`) will read.
- **Business value:** closes `R-012` early; makes `M-design-acceptance`/`M-northstar` readable. Gate
  (A) is unmeasurable without it.
- **User value:** indirect — the measurement that keeps the "designed" promise honest.
- **User stories:** *(internal)* *As the PO, I want each export's acceptance captured, so the H-001
  eval reads itself instead of being argued.*
- **Expected impact:** closes `R-012` (measurement gap) — `M-design-acceptance` computable from
  instrumented data · check-by Sprint-2 gate [assumption]
- **Owner:** engineer ⚙️
- **Estimate:** M (~0.5 dev-FTE, scoped lean) — [assumption] until the readout reads the actual

### Go-to-market — Activities
<!-- tool: activity-spec, prioritization-sprint-plan -->

**1 · Founder-community design-partner recruitment** — links: `H-011` tests / `M-cac`·`M-activated` moves / **B-01·B-05** launches
- **Feature:** `F-003` (the campaign line; the shipped post's external id lands on the row after the run)
- **Description:** a founder-led post + DM sequence in the warm design community inviting S1 makers
  (agencies on deadline · freelance designers) to become design partners — the `H-011` channel test.
- **Scope:** draft the founder post (the B-01/B-05 message); pick the warm-audience segment; publish +
  DM; capture qualified sign-ups via the back-office landing item; log a blended-CAC proxy (founder
  time + any spend).
- **Business value:** tests `H-011`; moves `M-cac` (proxy), seeds `M-activated`. Period target ≥8
  recruited / ≥6 activated (`5#goal-targets`).
- **Audience value:** early access + founder attention + influence over a tool built for their exact
  restyle-tax pain — not spam.
- **Surface:** `S-09` (the warm founder design community)
- **Expected impact:** tests `H-011` — `M-activated` 0 → ≥6 activated partners (≥8 recruited) ·
  check-by end of period (`5#goal-targets`) [assumption]
- **Owner:** founder ⚙️
- **Estimate:** M (~0.3 FTE, the founder's g2m capacity) — [assumption] until the readout reads the actual

### Back-office — Tasks
<!-- tool: task-spec, prioritization-sprint-plan -->

**1 · Landing + waitlist + price page + analytics events (lean)** — links: `M-activated` / `M-paid-conv`
- **Feature:** `F-004`
- **Description:** the minimal go-to-market surface — landing/comparison page, waitlist/sign-up, price
  page, analytics events — so the recruitment activity's sign-ups are captured and the first funnel
  signals land somewhere.
- **Why:** enables `M-activated` and the `M-paid-conv` proxy; without it the `H-011` signal has
  nowhere to record (`5#goal-targets` G-B1).
- **Definition of Done:** (1) landing + waitlist live; (2) price page shows the premium tiers; (3)
  sign-up + page events fire into analytics; (4) a recruited partner can sign up and be counted.
- **Expected impact:** `M-activated` capture enabled — sign-up events fire and a recruit is countable ·
  check-by Sprint-2 gate [assumption]
- **Owner:** back-office contractor ⚙️
- **Estimate:** S (~0.2 FTE, lean — not full billing) — [assumption] until the readout reads the actual

## Backlog {#backlog}
<!-- tool: prioritization-sprint-plan -->
_The rest, prioritized (not flat), grouped by direction. Full specs in the `feature-spec`/
`activity-spec`/`task-spec` worklogs._

| Rank <!--c:rank--> | Direction <!--c:direction--> | Item <!--c:item--> | Format <!--c:format--> | Feature <!--c:feature--> | Links (`H-…`/`M-…`/`B-…`) <!--c:links--> | Est. <!--c:est--> | Confidence <!--c:conf--> |
|------|-----------|------|--------|---------|---------------------|------|------------|
| 1 | development | eval harness (≥50 briefs × ≥5 verticals) | Feature | F-005 | H-001 / M-design-acceptance | M (~0.4 FTE) | [assumption] |
| 2 | go-to-market | WTP price-talk script + prep | Activity | F-006 | H-010 / M-paid-conv / B-01 | S (~0.1 FTE) | [assumption] |
| 3 | development | second export format (`.key` / Keynote) | Feature | F-001 | H-001 / R-006 | L (~0.6 FTE) | [assumption] |
| 4 | back-office | billing / seats integration | Task+DoD | F-007 | M-arppu / M-contribution | M (~0.3 FTE) | [assumption] |

_The second export format advances the same `F-001` as must-item 1 — an item is sprint-local, the
feature row is the cross-sprint identity several items may serve._

## Excluded {#excluded}
<!-- tool: prioritization-sprint-plan -->
_Candidates that entered the ranking (N = 10) but left it entirely — cut before backlog, with why.
Backlog is the visible reject of the must-set; this is the reject of the ranking itself._

| Item <!--c:item--> | Direction <!--c:direction--> | Why excluded <!--c:why--> |
|------|-----------|--------------|
| brand-kit storage (`F-008`) | development | cut at Step 5 (`5#period-goals`) — the lock-in moat is the `H-012` *trajectory*, premature before the wedge is proven; no gate contribution this period. Its register row stays `planned` — a cut is not a delete |
| paid-ad probe | go-to-market | backlogged at Step 5, out of Sprint-1 scope — paid CAC is thin (`4#unit-economics`); don't spend into a channel modelled as secondary (`R-008`) |

_Step-5 carry-over check: the period backlog's other two items — **C3** (activation funnel; waits on
partners using the prototype, a later sprint's ranking) and **C9** (provider-abstraction/ToS risk
hygiene) — did not enter Sprint 1's candidate list at all; they stay on the period backlog, owned by
`5#prioritization`. Reconciliation table in `6-sprint-plan/prioritization-sprint-plan.md` §5._

## Delivery {#delivery}
<!-- synthesis -->
_What goes to the development process, and how (the framework ends here; work proceeds in the team's own flow)._

- **Handed off:** the four musts — dev items 1–2 (dev board), the recruitment activity (founder),
  the landing task (back-office) — to the team's own development/execution flow; the backlog
  (F-005/F-006/F-001-second-format/F-007) is groomed next.
- **Acceptance / results flow back:** shipped items are read at the next Step-5 gate by
  `impact-readout` against their pre-registered Expected impact — their `F-…` rows flip
  `planned → live`. Dev items 1–2 landing makes `H-001` measurable (eval reads out next sprint via
  `F-005`); the recruitment + landing events produce the `H-011`/`M-activated` read. **A refuted
  `H-…` or a missed expectation bubbles up to `5-tactical-plan.md`** (and further up if a strategic
  bet is hit) — e.g. `H-001` refuted → revisit `3#how-to-win`; `H-011` refuted → `R-008` (2nd channel).

## To clarify {#to-clarify}
<!-- open -->
- **Sprint dates** — none set; the sprint is bounded by *length* (~2 wk), inheriting the undated
  horizon (`4#open-questions`). The founder must place it on a calendar to commit.
- **Owner names** — roles are ⚙️ placeholders (founder-engineer, engineer, contractor); real names are
  needed before handoff (twin of `5#resources` `— to clarify —`).
- **Item-1 slice depth** (`F-001`) — exactly which template families make the first slice is an
  engineering call to confirm at grooming; the acceptance criteria hold regardless.

## Change log

### 2026-08-23 — migrated to the product axis (framework v0.12)
- **From → To:** items carried register-style positional ids (`F-1`/`A-1`/`T-1`) → items are
  numbered 1, 2, … within their direction subsection; each names its feature-register row
  (`- **Feature:** F-…`) and pre-registers an **Expected impact** with a check-by and an
  **Estimate** class (S/M/L); backlog gains the `feature` column
- **Why:** the positional id died with the sprint while looking like a register id; the `F-…` row
  in `registers/features.md` is the durable identity `impact-readout` reads at the next Step-5 gate
- **Trigger:** framework product-axis rework; rows F-001…F-008 / S-01…S-09 minted from these specs
  and `3#product-surface`

### 2026-08-17 — card lines marked for the console board
- **From → To:** no section carried a `<!-- card -->` mark → 1 section(s) with a natural headline
  line now mark it; table-only sections stay unmarked (title and status only, the body one expand away)
- **Why:** the console no longer composes a card face of its own — a board card shows the author's
  marked line verbatim or nothing (CONVENTIONS → *Card line*)
- **Trigger:** console rework — a card is a collapsed section, not a third text

### 2026-08-17 — human review pass: Step-5 carry-over made visible
- **From → To:** `#excluded` gains the carry-over check — the period backlog's C3/C9 did not enter
  Sprint 1's ranking and now say so explicitly, with the re-entry condition; reconciliation table in
  the worklog §5
- **Why:** two period-plan items vanishing between Step 5 and Step 6 files is the silent-drop the
  prioritization pair exists to prevent; review returned it
- **Trigger:** human review of the finished run (tactics lens)

### 2026-08-16 — created (Step 6, Sprint 1 projection)
- **From → To:** — → Sprint-1 plan projected from the four `6-sprint-plan/` worklogs: sprint goal;
  must-set F-1/F-2 (Features) · A-1 (Activity, runs B-01/B-05) · T-1 (Task+DoD); ordered backlog
  (F-3/A-2/F-4/T-2); excluded F-5/A-3 with reasons; delivery + results-flow-back. Every item links an
  existing `H-…`/`M-…` (and A-1 its `B-…`); **no register ids minted** at Step 6.
- **Why:** Step 6 turns the period goals into a minimal, capacity-bounded sprint and hands off to the
  team's flow — the bottom of the cascade
- **Trigger:** Step 6 operating-loop pass; worklogs are source of truth, this artifact their projection
