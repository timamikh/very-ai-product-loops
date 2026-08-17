---
node_type: worklog
tool: goal-targets
step: 5
title: "goal targets — Period 1"
updated: 2026-08-16
version: 0.1.0
---

# goal targets — the working (Period 1)

_Source of truth for `5-tactical-plan.md#goal-targets`. Turns each period goal into a read at
period-end: go-to-market goals → an existing `M-…` node (baseline → target with the reasoning for its
size); technical & back-office goals → a **binary Definition of Done**. Every target is a step toward a
`4#strategic-targets` horizon commitment — a period moving no horizon target is drift._

## 0 · Baselines — the honest state of `metrics.csv`

**`registers/metrics.csv` is empty — the product is pre-launch, no reading exists for any node.** Per
the method a target must not be set on an invented baseline; so every baseline below is stated as
**"— (no reading; pre-launch)"** and each target is a **first rung from zero**, not a delta off a
measured value. This is the honest form of the rule when there is genuinely no history.

## 1 · Targets per goal

| Goal | Dir | Target: `M-…` or DoD | Baseline → target | Ladders to (`4#strategic-targets`) | Reasoning for the size |
|------|-----|----------------------|-------------------|-----------------------------------|------------------------|
| G-D1 engine passes eval | dev | **DoD** | — → done | (unblocks all — `H-001` is the enabler) | binary: engine emits **valid, openable** native `.pptx`/`.key` on a **≥50-brief × ≥5-vertical** eval set **and** clears `M-design-acceptance` ≥70% on that eval (the `H-001` success bar, `4#global-hypotheses`). Not "80% built" — done means the eval passes. |
| G-D2 acceptance instrumentation | dev | **DoD** | — → done | (makes `M-northstar`/`M-design-acceptance` readable → closes `R-012`) | binary: the design-acceptance / edit-behaviour proxy emits events in the build so the North Star's "kept" clause is computable. Done = the eval in G-D1 can be **read from instrumented data**, not eyeballed. |
| G-G1 recruit design partners | go-to-market | `M-activated` (proxy via partners reaching a first native value-export) | — → **≥6 activated of ≥8 recruited** | `M-northstar` ~600 WNVE/wk (the **first rung**) | size = the smallest cohort that yields a channel-CAC proxy and a usable design-acceptance read; ≥8 is realistic reach for the founder's warm audience (`resource-check`); fewer than ~6 activated wouldn't distinguish signal from noise. |
| G-G2 WTP price-talk | go-to-market | `M-paid-conv` (**proxy** — qualified price-talk acceptance, not instrumented trial→paid) | — → **≥5 of ~8 partners accept a premium price-talk** (medium+ signal) | `M-paid-conv` ≥8% at horizon | proxy denominator is partners-in-a-price-talk, not trials — flagged, because pre-launch there is no trial funnel yet; ≥5/8 is a coarse "premium is not dead on arrival" read feeding `H-010`, not the instrumented ≥8%. |
| G-B1 billing/analytics plumbing | back-office | **DoD** | — → done | (enables `M-arppu`/`M-paid-conv`/`M-contribution` later) | binary: seat/MRR/funnel events instrumented + a price page live; scoped lean (not full billing) — done = the go-to-market signals in G-G1/G-G2 have somewhere to land. |

## 2 · Drift check (the ladder rule)

Two horizon targets are moved this period: **`M-northstar`** (via G-G1's first activated cohort) and
**`M-paid-conv`** (via G-G2's WTP proxy). `M-w4-retention` and `M-contribution` are **not** moved —
correctly, because retention is unobservable pre-launch (`4#retention`) and contribution needs paying
accounts that don't exist yet. So the period is **not** drift: it moves the two horizon targets that
*can* move at concept-viability, and says plainly why the other two wait.

## Register

Reads `metrics.csv` (empty). No metric nodes minted — every target lands on an **existing** `M-…`
(`M-activated`, `M-paid-conv`) or a DoD. No writes.

## Change log

### 2026-08-16 — Period-1 targets set
- **From → To:** — → 5 goals given targets: 3 DoDs (G-D1/G-D2/G-B1) + 2 go-to-market `M-…` targets on
  `M-activated` and `M-paid-conv` (proxy), each a first rung from zero (no baseline exists — pre-launch)
  laddering to a `4#strategic-targets` commitment; drift check shows the 2 movable horizon targets move
- **Why:** a goal without a target can't be missed, so it can't teach; targets land on existing tree
  nodes so the period-end read is the register's own read
- **Trigger:** Step 5 pass, section `#goal-targets`; baselines from `metrics.csv` (empty)
