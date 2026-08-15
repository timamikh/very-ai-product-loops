---
node_type: artifact
artifact: sprint-plan
step: 6
title: "Sprint Plan — Decksmith (fictional sample) · Sprint 1 (2026-08)"
status: draft
version: 0.1.0
updated: 2026-08-14
---

# Sprint Plan — Decksmith (fictional sample) · Sprint 1 (2026-08)

> Status: concept-viability · Owner: — · Capacity: ⚙️ ~1 feature + 1 activity + 1 task
> Inputs: `5-tactical-plan.md` · registers. Hands off to: the team's development process.
> Written artifact-direct (unmigrated to worklogs, as in the reference instance). No section confirmed
> (autonomous walk). This is the first ~2-week slice of period P1: get a readable **H-001** + **H-010** signal.

## Must {#must}
_Minimal mandatory items — without which the period goal is unreachable. Grouped by direction._

### Development — Features
<!-- tool: feature-spec, prioritization -->
**F-1 · Native-export prototype slice** — links: `H-001` / `M-edit-fidelity`
- **Description:** generate + export a **native .pptx** for one deck type (e.g. a sales pitch), with real
  editable shapes/text — not images.
- **Scope:** minimal generate pipeline (LLM draft → fidelity engine → .pptx); one layout family; run on 20
  diverse test decks.
- **Business value:** the feasibility gate — nothing downstream is real until the engine produces editable
  output at quality (`H-001`).
- **User value:** a deck they can actually open and edit in PowerPoint without a rebuild.
- **User stories:** "As a marketer, I generate a pitch and export it, and every object is editable in PPT."

### Go-to-market — Activities
<!-- tool: activity-spec, prioritization -->
**A-1 · Demand-probe landing + first post (bundle B-02)** — links: `H-010` / `M-activation`
- **Description:** publish a landing ("fix your Gamma export — get an editable deck") + one LinkedIn post +
  one community post; capture waitlist sign-ups.
- **Scope:** write the message from the UVP; build the landing; post to LinkedIn + one sales/design community;
  track sign-ups as the medium-tier signal.
- **Business value:** reads demand for the wedge (`H-010`) before a full product exists.
- **Audience value:** they get an editable deck instead of a broken export — a named, recognizable pain.

### Back-office — Tasks
<!-- tool: prioritization -->
**T-1 · Instrument generate/export/keep + fidelity capture** — links: `M-edit-fidelity` / `M-ns-kept-decks-wk` / `R-007`
- **Description:** fire events on generate, export, and keep-vs-redo; compute `M-edit-fidelity` (editable-object
  share) in the export pipeline.
- **Definition of Done:** events land in analytics; `M-edit-fidelity` is computed and readable on F-1's 20 test
  decks; a row can be appended to `metrics.csv`.
- **Why:** no H-001/H-010 signal is readable without it (the not-instrumented list from Step 4).

## Backlog {#backlog}
_The rest, prioritized (not a flat list), grouped by direction._

| Rank | Direction | Item | Format | Links (`H-…`/`M-…`) | Est. | Confidence |
|------|-----------|------|--------|---------------------|------|------------|
| 1 | go-to-market | A-2 · ~10 discovery interviews with the lead segment | Activity | H-010 / M-activation | ~3d | [assumption] |
| 2 | go-to-market | A-3 · B-01 private demo/diagnostic on a real deck (once F-1 lands) | Activity | H-010 | ~2d | [assumption] |
| 3 | back-office | T-2 · multi-model LLM provider abstraction + `M-cogs-per-deck` capture | Task+DoD | M-cogs-per-deck / R-004 | ~3d | [assumption] |
| 4 | development | F-2 · brand-kit support (fonts/colors) | Feature | H-012 / M-free-paid-conv | ~1wk | [assumption] |

_Cut outright (no gate contribution this sprint): Team/admin surface, SEO, paid social — recorded, not staged._

## Handoff {#handoff}
_What goes to the development process, and how (the framework ends here; work proceeds in the team's own flow)._

- **Handed off:** F-1, A-1, T-1 → the team's sprint board.
- **Acceptance / how results flow back:** `M-edit-fidelity` readable on F-1's 20 decks (→ the `H-001` read) and
  landing sign-ups tracked (→ the `H-010` read). A refuted `H-001` (fidelity < 70%) or a dead `H-010` (< 3
  signals) bubbles up to `5-tactical-plan.md#hypotheses-to-test` and, if it kills the wedge, to
  `3-strategy.md#bets` (`H-009`/`H-010`) and the risk register (`R-007`).

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → Sprint 1 must-set (F-1 prototype · A-1 demand probe B-02 · T-1 instrumentation) + ranked
  backlog; handoff with the H-001/H-010 read path back up.
- **Why:** produce the minimal work that makes the feasibility + demand bets readable.
- **Trigger:** Step-6 sprint plan, rebuild.
