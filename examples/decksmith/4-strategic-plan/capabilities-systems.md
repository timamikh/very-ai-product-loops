---
node_type: worklog
tool: capabilities-systems
step: 4
title: "capabilities & management systems — the working"
updated: 2026-08-16
version: 0.1.0
---

# capabilities & management systems — the working

_Source of truth for `4-strategic-plan.md#capabilities`. Playing-to-Win choices 4 & 5: what we must
be reliably great at for the `3#how-to-win` logic to hold, and the system that builds/maintains/
measures each. A capability is an **ability**, not an asset. The test runs both ways — every
winning-logic element needs a capability; every capability must serve the winning logic. Gaps seed
execution `R-…`._

## Walk of the winning logic, element by element

| # | Winning-logic element (`3#how-to-win`) | Capability (an ability) | Rating ⚙️ | Gap & close | Management system (build · cadence · slip signal) |
|---|----------------------------------------|-------------------------|-----------|-------------|---------------------------------------------------|
| 1 | Out-design the native-export tools (taste corpus + founder taste, `H-007`) | **Curate + label a design corpus and encode taste into the generator, refreshed on a cadence** | partial | build the corpus pipeline + labelling by launch → ties `R-009` | design-review cadence; slip signal `M-design-acceptance` |
| 2 | Out-export the design-led tools (native engine, `H-001`) | **Reliably emit valid, on-brand native `.pptx`/`.key` at scale on arbitrary content** | missing/unproven | the core feasibility build → *is* `H-001`; gap closes only by proving it | export-fidelity test suite; slip signal `M-design-acceptance` + export-success |
| 3 | Convert the wedge → durable moat (data loop + brand-kit lock-in) | **Instrument edit-behaviour + ship brand-kit storage** | missing | build the instrumentation + brand-kit store → **seeds new `R-012`** | the instrumentation plan; slip signal = the gap itself (`M-w4-retention` unobservable) |
| — | (motion, from `3#channels-expansion`) PLG self-serve + founder-led distribution | **Run a self-serve funnel and a founder-led community engine** | partial | activation + community ops → ties `R-008` | funnel review; slip signal `M-activated`, `M-cac` |

## Gap → risk seeding (reconciled — no duplicates)

- Element 1 gap (corpus/taste travel) → **existing `R-009`** (taste doesn't travel). Not re-minted.
- Element 2 gap (native engine) → **is `H-001`** (a hypothesis we test), and its "even if built,
  users reject" failure → **existing `R-009`**. No new risk.
- Element 3 gap (edit-behaviour instrumentation + brand-kit store) → **new `R-012`** (execution: the
  instrumentation gap blocks both the North-Star measurement *and* the data-loop moat `H-012`). This
  is genuinely uncovered by any existing risk → minted.
- Motion gap (community/funnel) → **existing `R-008`** (channel doesn't scale) + `R-010` (key-person).
  Not re-minted.

## Rejected nice-to-haves (kept — the org's wish list, named so it can't creep back)

| Proposed capability | Why rejected |
|---------------------|--------------|
| "World-class real-time collaboration" | serves no winning-logic element; real-time collab is explicitly out of scope (`3#where-to-play`) |
| "Best-in-class mobile app" | S1 makes client decks on desktop; no element needs it this horizon |
| "Enterprise SSO/DLP now" | serves the *expansion* arena (C), not the launch arena — deferred, not built |

## Change log

### 2026-08-16 — capabilities & systems worked and projected
- **From → To:** — → element-by-element capability walk (4 elements → 4 capabilities, honest
  have/partial/missing), gap-and-close each with the `R-…` it ties to, management system + slip
  signal per capability, 3 nice-to-haves rejected; **minted `R-012`** for the instrumentation gap
- **Why:** Step 4 lands PTW choices 4–5 — a how-to-win no capability supports is a hope; capability
  gaps become tracked execution risks
- **Trigger:** Step 4 pass, section `#capabilities`; `R-012` seeded to `registers/risks.md`
