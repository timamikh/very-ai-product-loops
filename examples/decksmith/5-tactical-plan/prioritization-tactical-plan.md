---
node_type: worklog
tool: prioritization-tactical-plan
step: 5
title: "prioritization (tactical) — Period 1"
updated: 2026-08-16
version: 0.1.0
---

# prioritization — the working (Period 1)

_Source of truth for `5-tactical-plan.md#period-goals`. Ranks the period's candidate goals by
**contribution to the period gate** (not an abstract score) and keeps only what fits the capacity from
`resource-check`. RICE/ICE is a ranking aid, not the verdict. Every candidate that was current for the
period enters the ranking — **N recorded** — and every cut is kept with its reason._

## 0 · The period gate (stated first — everything is ranked against this)

**Period-1 gate (concept-viability, learning not traction):**
**(A)** a working native-export engine that emits valid, on-brand native `.pptx`/`.key` and clears an
internal **design-acceptance eval** — enough to keep betting on `H-001`; **and (B)** the first
**qualified S1 signals** from the founder-community channel (design-partner recruitment + a WTP
price-talk). A candidate earns a slot only by moving (A) or (B).

## 1 · Candidates — all of them, per direction (N = 9 entered the ranking)

Generated from the metric tree (`M-…` to move), the capability gaps (`4#capabilities`), and the bets
(`H-…`). None pre-cut before scoring.

| # | Dir | Candidate goal | Moves node / tests bet | ICE (I·C·E, 1–5) | Gate contribution |
|---|-----|----------------|------------------------|------------------|-------------------|
| C1 | dev | Native-export engine emits valid on-brand `.pptx`/`.key` at eval-scale | `H-001` · `M-design-acceptance` | 5·2·2 | **(A) — the long pole; nothing reads without it** |
| C2 | dev | Instrument the design-acceptance / edit-behaviour proxy in the first build | `M-northstar`/`M-design-acceptance`; closes `R-012` | 4·4·3 | **(A) — without it the eval can't be read** |
| C3 | dev | Signup→first-export activation funnel + instrumentation | `M-activated` | 3·4·3 | (B) partial — needed once partners use it |
| C4 | dev | Brand-kit storage (lock-in derivative) | `H-012` trajectory | 2·3·3 | neither gate this period (moat is later) |
| C5 | g2m | Founder-community landing → recruit ≥8 design partners | `H-011` · `M-cac`(proxy)/`M-activated` | 5·3·4 | **(B) — the first channel signal** |
| C6 | g2m | WTP price-talk with recruited partners | `H-010` · `M-paid-conv`(proxy) | 4·3·4 | (B) — the monetisation signal, rides on C5 |
| C7 | g2m | Minimal paid-ad probe (secondary channel) | `R-008` 2nd-channel · `M-cac` | 2·2·4 | weak (B) — paid is thin (`unit-economics` §4) |
| C8 | back | Billing + analytics plumbing (seats, MRR, funnel events) | `M-arppu`/`M-paid-conv`/`M-contribution` | 3·4·3 | (B) enabler — DoD, not a metric move yet |
| C9 | back | Provider-abstraction groundwork + ToS/legal | `R-004` · `R-006` | 2·3·2 | neither gate — risk hygiene, deferrable |

## 2 · Re-rank by gate contribution, then bound at the capacity line

Capacity (`resource-check`): ~2.2 dev-FTE (binding), founder ~0.3 FTE g2m, ~0.2 FTE back-office, ~8 wk.

| Rank | Candidate | In the period? | Reason |
|------|-----------|----------------|--------|
| 1 | C1 engine | **must** | gate (A); the whole how-to-win rests here (`H-001`) |
| 2 | C2 acceptance instrumentation | **must** | gate (A) unreadable without it; closes `R-012` early (the mission's own risk) |
| 3 | C5 recruit design partners | **must** | gate (B); the founder-channel bet `H-011`, cheap and fast |
| 4 | C6 WTP price-talk | **must** (rides on C5) | gate (B) monetisation `H-010`; near-zero marginal cost on C5's partners |
| 5 | C8 billing/analytics plumbing | **must (lean)** | enabler for C3/C6 signals; scoped to events + a price page, not full billing |
| 6 | C3 activation funnel | **partial / backlog** | needed only once partners have the prototype; lands late in the period, minimal build |
| 7 | C9 provider-abstraction + ToS | **backlog** | risk hygiene (`R-004`/`R-006`); no gate contribution this period |
| 8 | C7 paid-ad probe | **backlog** | paid CAC thin; don't spend into a channel we already model as secondary |
| 9 | C4 brand-kit storage | **cut (this period)** | moat/lock-in is the `H-012` *trajectory* — premature before the wedge is proven |

**Capacity check:** the five musts fit ~2.2 dev-FTE only because C2/C8 are scoped lean and C1 is the
sole heavy build. If C1 slips, C2/C5/C6 still yield a channel + WTP read — the period degrades
gracefully rather than producing nothing. The minimum set is **not** inflated: C3/C7/C9/C4 are
explicitly out, each with a reason, so the next pass doesn't silently re-propose them.

## 3 · The period goal set (→ `#period-goals`, grouped by direction)

- **development:** G-D1 = C1 (engine passes eval) · G-D2 = C2 (acceptance instrumentation).
- **go-to-market:** G-G1 = C5 (recruit ≥8 design partners) · G-G2 = C6 (WTP price-talk).
- **back-office:** G-B1 = C8 (billing/analytics plumbing — lean DoD).

Five goals, three directions. Targets set in `goal-targets`; what must not drop in `guardrails`.

## Change log

### 2026-08-16 — Period-1 goals ranked and bounded
- **From → To:** — → gate stated; **N=9** candidates ranked by gate contribution (ICE as aid);
  5 musts drawn inside capacity (G-D1/G-D2/G-G1/G-G2/G-B1); C3/C7/C9 backlogged and C4 cut, each with
  a recorded reason
- **Why:** Step 5 turns the strategy into a capacity-bounded period; the gate — not a RICE number —
  is the ordering key at concept-viability
- **Trigger:** Step 5 pass, section `#period-goals`; capacity from `resource-check`
