---
node_type: worklog
tool: task-spec
step: 6
title: "task specs — Sprint 1"
updated: 2026-08-16
version: 0.1.0
---

# task specs — the working (Sprint 1)

_Source of truth for the **Back-office → Tasks** blocks of `6-sprint-plan.md#must` / `#backlog`. Each
task: Description · Why (the `M-…`/`R-…`/`H-…` it serves, as a link) · binary Definition of Done ·
Owner · Estimate. Ranking/line from `prioritization-sprint-plan`._

## Must

### T-1 · Landing + waitlist + price page + analytics events (lean) — links `M-activated`/`M-paid-conv`
- **Description:** stand up the minimal go-to-market surface — a landing/comparison page, a
  waitlist/sign-up, a price page, and the analytics events — so A-1's recruits are captured and the
  first funnel signals land somewhere.
- **Why:** enables `M-activated` (signup→first-export) and the `M-paid-conv` proxy; without it the
  Sprint-1 channel test (A-1) produces a signal with nowhere to record it (`5#goal-targets` G-B1).
- **Definition of Done (binary):** (1) landing + waitlist live and reachable; (2) a price page shows
  the premium tiers; (3) sign-up and page events fire into analytics; (4) a recruited partner can
  sign up and be counted.
- **Owner:** back-office contractor ⚙️.
- **Estimate:** ~0.2 FTE (lean — not full billing).

## Backlog

### T-2 · Billing / seats integration — links `M-arppu`/`M-contribution`
- **Description:** integrate billing (seats, plans, MRR) beyond the static price page.
- **Why:** enables `M-arppu` / `M-contribution` once there are payers; serves the eventual instrumented
  `H-010` trial→paid test (next period, `5#hypotheses-to-test`).
- **Definition of Done (binary):** (1) a seat can be purchased on a paid plan; (2) MRR + seat counts
  are recorded; (3) `M-arppu` is computable from billing data.
- **Owner:** back-office contractor / eng ⚙️.
- **Estimate:** ~0.3 FTE — deferred: no payers to bill in Sprint 1.

## Change log

### 2026-08-16 — Sprint-1 task specs written
- **From → To:** — → T-1 (must, the lean go-to-market surface, serves `M-activated`/`M-paid-conv`) +
  T-2 (backlog, fuller billing, serves `M-arppu`/`M-contribution`), each with a binary DoD and a link
- **Why:** Step 6 specs back-office items at handover altitude; a task with no link or an
  un-answerable DoD is a candidate to cut
- **Trigger:** Step 6 pass, Back-office subsections of `#must`/`#backlog`
