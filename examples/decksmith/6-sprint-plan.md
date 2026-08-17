---
node_type: artifact
artifact: sprint-plan
step: 6
title: "Sprint Plan — Decksmith (fictional sample) · Sprint 1"
status: draft
version: 0.1.2
updated: 2026-08-17
---

# Sprint Plan — Decksmith (fictional sample) · Sprint 1 (⚙️ ~2 wk, no dates)

> Status: concept-viability · Owner: acting PO (⚙️ agent) · Capacity: ~2 features · 1 activity · 1 task (must)
> Inputs: `5-tactical-plan.md` · registers. Hands off to: the team's development process.

> ⚠️ This artifact is the **projection** of the Step-6 worklogs in `6-sprint-plan/`
> (`prioritization-sprint-plan`, `feature-spec`, `activity-spec`, `task-spec`). Each item's source of
> truth is its method worklog; the change-log history lives there. Every item links an `H-…`/`M-…`
> (and an activity names its `B-…`). Step 6 mints no register ids — it links to existing ones. ⚙️
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

**F-1 · Native-export engine — first vertical slice (`.pptx`)** — links: `H-001` / `M-design-acceptance`
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
- **Owner:** founder-engineer ⚙️ · **Estimate:** the sprint's heavy build (~1.3 dev-FTE).

**F-2 · Design-acceptance / edit-behaviour instrumentation** — links: `M-design-acceptance` / `M-northstar` / `R-012`
- **Description:** capture the proxy behind the North Star's "kept" clause (export without a full
  in-app restyle) so F-1 can be *read*, not eyeballed.
- **Scope:** instrument export + restyle-before-export events, per-vertical tagging, a minimal internal
  dashboard for the eval read.
- **Acceptance criteria:** (1) every export emits an event with vertical + a restyle flag; (2)
  `M-design-acceptance` is computable from instrumented data for the smoke set; (3) events land in the
  store the eval harness (F-3) will read.
- **Business value:** closes `R-012` early; makes `M-design-acceptance`/`M-northstar` readable. Gate
  (A) is unmeasurable without it.
- **User value:** indirect — the measurement that keeps the "designed" promise honest.
- **User stories:** *(internal)* *As the PO, I want each export's acceptance captured, so the H-001
  eval reads itself instead of being argued.*
- **Owner:** engineer ⚙️ · **Estimate:** ~0.5 dev-FTE (scoped lean).

### Go-to-market — Activities
<!-- tool: activity-spec, prioritization-sprint-plan -->

**A-1 · Founder-community design-partner recruitment** — links: `H-011` tests / `M-cac`·`M-activated` moves / **B-01·B-05** launches
- **Description:** a founder-led post + DM sequence in the warm design community inviting S1 makers
  (agencies on deadline · freelance designers) to become design partners — the `H-011` channel test.
- **Scope:** draft the founder post (the B-01/B-05 message); pick the warm-audience segment; publish +
  DM; capture qualified sign-ups via T-1; log a blended-CAC proxy (founder time + any spend).
- **Business value:** tests `H-011`; moves `M-cac` (proxy), seeds `M-activated`. Period target ≥8
  recruited / ≥6 activated (`5#goal-targets`).
- **Audience value:** early access + founder attention + influence over a tool built for their exact
  restyle-tax pain — not spam.
- **Owner:** founder ⚙️ · **Estimate:** ~0.3 FTE (the founder's g2m capacity).

### Back-office — Tasks
<!-- tool: task-spec, prioritization-sprint-plan -->

**T-1 · Landing + waitlist + price page + analytics events (lean)** — links: `M-activated` / `M-paid-conv`
- **Description:** the minimal go-to-market surface — landing/comparison page, waitlist/sign-up, price
  page, analytics events — so A-1's recruits are captured and the first funnel signals land somewhere.
- **Why:** enables `M-activated` and the `M-paid-conv` proxy; without it A-1's signal has nowhere to
  record (`5#goal-targets` G-B1).
- **Definition of Done:** (1) landing + waitlist live; (2) price page shows the premium tiers; (3)
  sign-up + page events fire into analytics; (4) a recruited partner can sign up and be counted.
- **Owner:** back-office contractor ⚙️ · **Estimate:** ~0.2 FTE (lean — not full billing).

## Backlog {#backlog}
<!-- tool: prioritization-sprint-plan -->
_The rest, prioritized (not flat), grouped by direction. Full specs in the `feature-spec`/
`activity-spec`/`task-spec` worklogs._

| Rank <!--c:rank--> | Direction <!--c:direction--> | Item <!--c:item--> | Format <!--c:format--> | Links (`H-…`/`M-…`/`B-…`) <!--c:links--> | Est. <!--c:est--> | Confidence <!--c:conf--> |
|------|-----------|------|--------|---------------------|------|------------|
| 1 | development | F-3 · eval harness (≥50 briefs × ≥5 verticals) | Feature | H-001 / M-design-acceptance | ~0.4 FTE | [assumption] |
| 2 | go-to-market | A-2 · WTP price-talk script + prep | Activity | H-010 / M-paid-conv / B-01 | ~0.1 FTE | [assumption] |
| 3 | development | F-4 · second export format (`.key` / Keynote) | Feature | H-001 / R-006 | ~0.6 FTE | [assumption] |
| 4 | back-office | T-2 · billing / seats integration | Task+DoD | M-arppu / M-contribution | ~0.3 FTE | [assumption] |

## Excluded {#excluded}
<!-- tool: prioritization-sprint-plan -->
_Candidates that entered the ranking (N = 10) but left it entirely — cut before backlog, with why.
Backlog is the visible reject of the must-set; this is the reject of the ranking itself._

| Item <!--c:item--> | Direction <!--c:direction--> | Why excluded <!--c:why--> |
|------|-----------|--------------|
| F-5 · brand-kit storage | development | cut at Step 5 (`5#period-goals`) — the lock-in moat is the `H-012` *trajectory*, premature before the wedge is proven; no gate contribution this period |
| A-3 · paid-ad probe | go-to-market | backlogged at Step 5, out of Sprint-1 scope — paid CAC is thin (`4#unit-economics`); don't spend into a channel modelled as secondary (`R-008`) |

_Step-5 carry-over check: the period backlog's other two items — **C3** (activation funnel; waits on
partners using the prototype, a later sprint's ranking) and **C9** (provider-abstraction/ToS risk
hygiene) — did not enter Sprint 1's candidate list at all; they stay on the period backlog, owned by
`5#prioritization`. Reconciliation table in `6-sprint-plan/prioritization-sprint-plan.md` §5._

## Delivery {#delivery}
<!-- synthesis -->
_What goes to the development process, and how (the framework ends here; work proceeds in the team's own flow)._

- **Handed off:** F-1, F-2 (dev board), A-1 (founder), T-1 (back-office) — the four musts — to the
  team's own development/execution flow; the backlog (F-3/A-2/F-4/T-2) is groomed next.
- **Acceptance / results flow back:** F-1/F-2 landing makes `H-001` measurable (eval reads out next
  sprint via F-3); A-1's recruitment + T-1's events produce the `H-011`/`M-activated` read. **A refuted
  `H-…` or a missed `M-…` bubbles up to `5-tactical-plan.md`** (and further up if a strategic bet is
  hit) — e.g. `H-001` refuted → revisit `3#how-to-win`; `H-011` refuted → `R-008` (2nd channel).

## To clarify {#to-clarify}
<!-- open -->
- **Sprint dates** — none set; the sprint is bounded by *length* (~2 wk), inheriting the undated
  horizon (`4#open-questions`). The founder must place it on a calendar to commit.
- **Owner names** — roles are ⚙️ placeholders (founder-engineer, engineer, contractor); real names are
  needed before handoff (twin of `5#resources` `— to clarify —`).
- **F-1 slice depth** — exactly which template families make the first slice is an engineering call to
  confirm at grooming; the acceptance criteria hold regardless.

## Change log

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
