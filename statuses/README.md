---
node_type: statuses-index
title: Statuses — product-stage plane
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Statuses

A **status** is the product's current stage. It is the framework's adaptation dial: it
parameterizes the loops without changing the process core. A status decides:

- **which goals take priority** this stage,
- **which tools** from the library are most relevant,
- **the gate emphasis** — what a step's checklist should weigh most.

Whether a stage's goals lean technical or product is expressed by the `priority_goals`
themselves, not a fixed flag — it varies with the product. The process core reads whatever
status is active and applies its parameters. This is why the tactical step needs no special
case for early-stage products: at `concept-viability` the priority goals are simply about
building a prototype/MVP rather than product metrics.

## The active status

The active status is set at the instance level (referenced from the strategy artifact / a
product config). It changes as the product matures; the change is a dated entry like any other.

## Default statuses

Defaults, in maturity order. All are **configurable and extensible** — see "Add or change a
status" below.

### 1. concept-viability
Prototype or MVP to test that the product *can* be built and that there is *some* demand worth
pursuing toward PMF.
- Priority goals: build a testable prototype/MVP; get first signal of demand; frame the PMF
  hypotheses to test next.
- Typical tools: `concept-formation`, `segment-pains`, `hypothesis-test-design`, `brief`.

### 2. PMF
First clients; the product has a path to profit; validate repeatable value and monetization so
it can be scaled.
- Priority goals: retention / repeat usage; willingness to pay / monetization; unit economics
  turning viable.
- Typical tools: `metric-tree`, `unit-economics`, `ab-test`, `cjm`.

### 3. growth
A working, profitable product to develop and expand.
- Priority goals: scale acquisition and revenue within guardrails; expand; defend moats.
- Typical tools: `channels-expansion`, `metric-tree`, `financial-model`, `prioritization`.

## Anatomy of a status

Each status is a file `statuses/<name>.md`:

```yaml
---
name: <status>
order: <n>                       # maturity order
priority_goals:
  - <goal>
recommended_tools: [<tool>, ...]
gate_emphasis: <what the step checklists should weigh most at this stage>
---
```
Body: a description + a dated change log.

## Add or change a status

1. Create `statuses/<name>.md` with the anatomy above (or edit an existing one).
2. Set `priority_goals`, `recommended_tools`, `gate_emphasis`.
3. Slot it into the maturity order (`order`).
4. That's it — the process core applies it automatically. No step needs editing.

A company can have more stages (e.g. `pre-seed-validation`, `scale-up`, `mature/harvest`) or
rename these to match its own vocabulary. The framework only assumes that *a* status is active
and exposes its priority/tool hints.
