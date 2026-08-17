---
node_type: worklog
tool: prioritization-sprint-plan
step: 6
title: "prioritization (sprint) — Sprint 1"
updated: 2026-08-17
version: 0.1.1
---

# prioritization — the working (Sprint 1)

_Source of truth for `6-sprint-plan.md#must` / `#backlog` / `#excluded`. Ranks the sprint's candidate
items by **contribution to the period gate** (not an abstract score), draws the **must/backlog line by
capacity**, and keeps every excluded item with its reason. RICE/ICE is a ranking aid. **N recorded.**
This method decides *order + line*; what each item **is** comes from `feature-spec` / `activity-spec` /
`task-spec` (one mechanism, one way)._

## 0 · The gate + this sprint's contribution

**Period-1 gate:** (A) an export engine that passes the design-acceptance eval (`H-001`); (B) the
first S1 signals (recruit partners `H-011` + WTP price-talk `H-010`). **Sprint 1 (~2 wk of the ~8-wk
period) must:** stand up the first shippable slice of the engine + its acceptance instrumentation
(start A), and **launch** the founder-community recruitment (start B). It cannot *finish* the engine or
read a result in one sprint — the smallest set that makes the period gate *reachable* is what "must"
means here.

## 1 · Candidates — all of them (N = 10), scored (ICE, 1–5) and re-ranked by gate contribution

| # | Dir | Candidate item | Format | Links | ICE (I·C·E) | Gate contribution |
|---|-----|----------------|--------|-------|-------------|-------------------|
| F-1 | dev | Native-export engine — first vertical slice (`.pptx`, core template families) emitting valid editable files | Feature | `H-001` · `M-design-acceptance` | 5·2·2 | **(A) — the long pole; the period is unreachable without it starting now** |
| F-2 | dev | Design-acceptance / edit-behaviour instrumentation (the proxy events) | Feature | `M-design-acceptance`/`M-northstar` · `R-012` | 4·4·3 | **(A) — F-1 can't be read without it; closes `R-012` early** |
| A-1 | g2m | Launch founder-community design-partner recruitment (runs bundles B-01/B-05) | Activity | `H-011` · `M-cac`/`M-activated` · `B-01`/`B-05` | 5·3·4 | **(B) — the first channel signal; cheap, starts now** |
| T-1 | back | Landing + waitlist + price page + analytics events (lean) | Task | `M-activated`/`M-paid-conv` | 3·4·3 | **(B) enabler — A-1's signals need somewhere to land** |
| F-3 | dev | Eval harness — the ≥50-brief × ≥5-vertical test set | Feature | `H-001` · `M-design-acceptance` | 4·3·3 | (A) later — reads F-1, but only once F-1 emits |
| A-2 | g2m | WTP price-talk script + prep (`G-G2`) | Activity | `H-010` · `B-01` | 3·3·4 | (B) later — rides on A-1's recruited partners |
| T-2 | back | Billing / seats integration (fuller than the price page) | Task | `M-arppu`/`M-contribution` | 2·3·2 | (B) enabler, later — no payers to bill in Sprint 1 |
| F-4 | dev | Second export format (`.key` / Keynote) | Feature | `H-001` · `R-006` | 3·3·2 | (A) breadth — after the `.pptx` slice proves out |
| F-5 | dev | Brand-kit storage (lock-in derivative) | Feature | `H-012` (trajectory) | 2·3·3 | **none this period** — cut at Step 5 (`5#period-goals`) |
| A-3 | g2m | Paid-ad probe (secondary channel) | Activity | `R-008` · `M-cac` | 2·2·4 | **weak/none** — backlogged at Step 5; paid CAC thin |

## 2 · Must-set (minimum for the period gate to be reachable) drawn at the capacity line

Capacity (from `5#resources`, this sprint's slice): ~2.2 dev-FTE, founder ~0.3 FTE g2m, ~0.2 FTE
back-office, ~2 wk. The binding constraint is dev throughput on F-1.

| Item | Verdict | Reason |
|------|---------|--------|
| **F-1** | **must** | gate (A); nothing reads without the engine slice |
| **F-2** | **must** | gate (A); F-1 is unmeasurable without it, and it closes `R-012` early |
| **A-1** | **must** | gate (B); founder-led, near-zero cost, starts the `H-011` clock |
| **T-1** | **must (lean)** | gate (B) enabler; scoped to landing + events + price page, not full billing |

Four musts. The must-set fits **only** because F-1 is the sole heavy build and F-2/T-1 are scoped
lean; if F-1 slips, F-2/A-1/T-1 still yield instrumentation + a channel read — graceful degradation,
not a dead sprint.

## 3 · Backlog (ordered — the rest that has an `M-…`/`H-…` link)

1. **F-3** eval harness — the moment F-1 emits, this reads it (`H-001`).
2. **A-2** WTP price-talk prep — fires once A-1 has recruited partners (`H-010`).
3. **F-4** second export format `.key` (`H-001`/`R-006`).
4. **T-2** fuller billing/seats (`M-arppu`/`M-contribution`) — no payers to bill yet.

## 4 · Excluded — entered the ranking (N=10), left it entirely (not backlog, not must)

| Item | Dir | Why excluded |
|------|-----|--------------|
| **F-5** brand-kit storage | dev | cut at Step 5 (`5#period-goals`) — the lock-in moat is the `H-012` *trajectory*, premature before the wedge is proven; no gate contribution this period |
| **A-3** paid-ad probe | g2m | backlogged at Step 5 and out of Sprint-1 scope — paid CAC is thin (`4#unit-economics`); don't spend into a channel modelled as secondary |

Backlog is the visible reject of the must-set; these two are the reject of the **ranking itself** —
kept here so the next sprint doesn't silently re-propose them.

## 5 · Step-5 carry-over reconciliation (nothing vanishes between the period plan and the sprint)

Of the period plan's non-musts (`5#prioritization`: backlog C3 · C7 · C9, cut C4):

| Period item | In Sprint 1's ranking? | Where it went |
|-------------|------------------------|---------------|
| C7 paid-ad probe | yes → **A-3** | entered, excluded again (§4) |
| C4 brand-kit storage | yes → **F-5** | entered, excluded again (§4) |
| **C3** activation funnel | **no** | waits on recruited partners *using* the prototype — mid-period work for a later sprint's ranking; T-1's lean landing+events is the Sprint-1 slice of that instrumentation, not the funnel itself |
| **C9** provider-abstraction + ToS | **no** | period-backlog risk hygiene (`R-004`/`R-006`), no gate contribution — not sprint-sized until a sprint has slack |

C3 and C9 stay on the **period** backlog, owned by `5#prioritization`; recorded here so the
carry-over is visible, not silent.

## Change log

### 2026-08-17 — human review pass: Step-5 carry-over reconciled
- **From → To:** the period plan's backlog items C3 (activation funnel) and C9 (provider-abstraction/
  ToS) silently absent from the sprint ranking → §5 reconciliation table added: C7/C4 re-entered as
  A-3/F-5 and were excluded again; C3/C9 deliberately not sprint-sized, staying on the period backlog
  with the reason and the re-entry condition stated
- **Why:** the worklog promised "the next sprint doesn't silently re-propose" its own rejects but let
  two period items vanish without a trace — the same discipline applied one level up
- **Trigger:** human review of the finished run (tactics lens)

### 2026-08-16 — Sprint-1 items ranked; must/backlog/excluded drawn
- **From → To:** — → gate stated; **N=10** candidates ranked by gate contribution (ICE as aid); 4
  musts (F-1/F-2/A-1/T-1) drawn at the capacity line; 4 backlog (F-3/A-2/F-4/T-2) ordered; F-5/A-3
  excluded with reasons
- **Why:** Step 6 turns the period goals into a minimal, capacity-bounded sprint; the gate — not a
  RICE number — is the ordering key at concept-viability
- **Trigger:** Step 6 pass, `#must`/`#backlog`/`#excluded`; item descriptions from the specs
