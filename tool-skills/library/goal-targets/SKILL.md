---
node_type: card
kind: method
name: goal-targets
steps: [5]
prerequisites: [period goals, the metric tree, baselines in metrics.csv]
reads: [section:period-goals, section:metric-tree, section:strategic-targets, register:metrics]
writes: [worklog, section:goal-targets]
opinionated: false
method_basis: "Per-goal target setting: go-to-market goals steer an existing metric node (baseline from metrics.csv → target with reasoned size); technical & back-office goals get a binary DoD; every target traces to the period gate"
evidence_standard: derived
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.1
updated: 2026-09-02
---
# Goal Targets

Turn each period goal into a **target you can read at the end of the period**: select the
metric-tree nodes to steer by this period, and for each go-to-market goal state **baseline →
target** on an existing `M-…` node with the reasoning for the target's size; for technical and
back-office goals state a **binary Definition of Done**. Fills `{#goal-targets}` (Step 5).

**Method basis.** A goal without a target cannot be missed, so it cannot teach anything. The target
lives on the **metric tree** — an existing, defined `M-…` node — so the end-of-period read is the
same read the register already makes. The baseline comes from `registers/metrics.csv` (captured via
`metrics-capture`), **never invented**: a target set against a guessed baseline is a guess squared.
Goals that no metric can honestly measure this period (a build, a compliance task) get a **binary
DoD** instead — done or not, no percentages of done.

## When to apply
- Step 5, right after `{#period-goals}` — every goal that made the period gets its target here.
- Whenever a period goal is about to be tracked and its "what does hitting it look like" is still
  prose.

## Prerequisites
- **Period goals** — the ranked goal set for the period. *Missing → run
  `prioritization-tactical-plan`.*
- **The metric tree** — defined `M-…` nodes to steer by. *Missing → run `metric-tree` (Step 4); a
  goal with no node to land on is a gap for the tree, not a new metric here.*
- **Baselines in `metrics.csv`** — a dated reading for each node about to get a target. *Missing →
  capture it via `metrics-capture` first; never set a target on an invented baseline.*

## How to do it
1. **Take the period goals as given.** One row per goal from `{#period-goals}` — this method sets
   targets, it does not re-rank or re-scope the goals.
2. **Select the node to steer by.** For each go-to-market goal, pick the **existing** `M-…` node
   that the goal moves. If no node fits, that's a gap for `metric-tree` — do not mint a bespoke
   number here.
3. **Read the baseline from the register.** The current value comes from `registers/metrics.csv`
   (captured via `metrics-capture`), cited as `[sourced: …]`. A baseline that isn't in the csv is
   not a baseline — capture it first.
4. **Set the target, and reason about its size.** Baseline → target, with *why this size*: what the
   period gate needs, what the historical trend supports, what capacity allows. A target with no
   reasoning is a wish; record the reasoning so a miss can be diagnosed (wrong size vs wrong work).
5. **Give technical & back-office goals a binary DoD.** Done / not done, checkable at period end —
   no "80% migrated" unless the percentage itself is the defined outcome.
6. **Trace every target to the period gate — and up the ladder.** Each target states how hitting
   it moves the gate, and which `4#strategic-targets` commitment it is a step toward. A target that
   doesn't serve the gate belongs to another period; a period in which no horizon target moves is
   drift — flag it, don't pad a target to hide it.

## Anti-patterns
- **Invented baseline.** A "current value" that exists nowhere in `metrics.csv` — the target's size
  is fiction and the end-of-period read has nothing to compare against.
- **A metric minted for the goal.** Steering by a number that is not a defined `M-…` node — it can't
  be compared, trended, or trusted.
- **Target with no reasoning.** "`M-… 3% → 5%`" with no why — when it misses, nobody can tell an
  overambitious size from underdelivered work.
- **A DoD you can't answer yes/no to.** "Improve the pipeline" is not done or not-done; it's a
  direction, not a DoD.
- **Orphan target.** A target that doesn't trace to the period gate — effort spent moving a number
  the period doesn't need.

## Worklog & projection
Worklog: `5-tactical-plan/goal-targets.md` — per goal the `M-…` selected or the binary DoD, the baseline with its `metrics.csv` citation, the target with the reasoning for its size, the trace to the gate and up the ladder. Projects `{#goal-targets}`; face: the **Trace to the gate** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#goal-targets}` (Step 5) via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml). The targets are what `experiment-readout`
and the next period's gate read against; guardrails (what must *not* drop meanwhile) are the
separate `guardrails` method.
