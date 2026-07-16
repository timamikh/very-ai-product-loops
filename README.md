# very-ai-product-loops

A product-agnostic workflow that takes a product from **idea → sprint plan** through
**nested, gated loops**.

> The agent prepares every artifact from real sources; the human decides at the forks;
> the loops refresh at their own pace and feed each other in both directions.

The framework separates **mechanism from content**: a thin, stable process skeleton, plus
pluggable methods (a **library**) and pluggable product stages (**statuses**). The rules of
the game stay fixed; *how* you define value, segment users, or test a hypothesis is swappable
and grows per company — without forking the framework.

## Architecture — four planes

- **Process core** (`steps/`) — thin skeleton per step: goal, gate checklist, movement rules, register touchpoints, artifact structure. No methods inside.
- **Registers** — three living, vertical objects: metrics · hypotheses · risks.
- **Library** (`library/`) — product methods as skills: what / when / how / template. See [`library/README.md`](library/README.md).
- **Statuses** (`statuses/`) — product stages as config (concept-viability · PMF · growth, extensible). See [`statuses/README.md`](statuses/README.md).

## The six steps

| # | Step | Horizon (~) | Output |
|---|------|-------------|--------|
| 1 | Idea / Concept | product lifetime | `passport.md` |
| 2 | Analysis | ~6–12 mo | `analysis.md` |
| 3 | Strategy | ~3–12 mo | `strategy.md` |
| 4 | Strategic Plan | ~3–12 mo | `strategic-plan.md` |
| 5 | Tactical Plan | ~1–3 mo | `tactical-plan.md` |
| 6 | Sprint Plan | ~1–2 wk | `sprint-plan.md` |

Timeframes are indicative — each team moves at its own pace. See
[`process/OVERVIEW.md`](process/OVERVIEW.md) for the full model.

## Status

Early draft, building in phases:

- **Phase 0 — Process foundation** → [`process/OVERVIEW.md`](process/OVERVIEW.md) · library + statuses models _(merged)_
- **Phase 1 — Step/tool/status anatomy + golden exemplar (Step 1)** _(in review)_
- **Phase 2 — Remaining steps + register schemas + library growth**
- **Phase 3 — Agent rules, install skill, examples, contribution + branching**
- **Phase 4 — Adapters, aggregators, automation** _(later)_
