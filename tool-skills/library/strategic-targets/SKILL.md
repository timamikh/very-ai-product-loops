---
node_type: card
kind: method
name: strategic-targets
steps: [4]
prerequisites: [horizon, metric-tree, financial-model]
reads: [register:metrics, register:features, register:risks, source:interview, source:kb]
writes: [worklog, section:strategic-targets, register:features]
opinionated: false
method_basis: "Horizon commitments read off the driver-based projection: 3–5 key metric nodes × value at the strategy horizon, scenario named, decision-attributed; Step-5 period targets ladder up to these"
evidence_standard: decision
volume_rule: n/a
selection_rule: "3–5 nodes carry a horizon target; nodes considered and left untargeted are kept with why"
rejects_shown: required
status: draft
version: 0.2.0
updated: 2026-08-24
---
# Strategic Targets

Commit **what the key metric nodes must reach by the strategy horizon**. Fills
`{#strategic-targets}`. This is the third target object in the framework, distinct from the other
two: `metric-tree` **defines** a node, this method commits its **horizon value**, and Step-5
`goal-targets` sets the **period value** — three values, three owners, no double-write. Without
this layer the ladder has no top: period targets are set "up from baseline" with nothing to check
that the periods sum to the strategy.

**Method basis.** The financial model *contains* the horizon values — but as a computation, not a
commitment. A projection nobody signed is re-forecast without ceremony; a target someone committed
to is missed *visibly*, which is the point. This method reads the numbers off the projection and
turns 3–5 of them into dated, attributed commitments.

## When to apply
- Step 4, once the metric tree and the financial model exist — before Step 5 sets period targets.
- When the winning aspiration changes its horizon or its definition of the result, or a
  re-forecast diverges from the committed targets (re-confirm or re-commit — never silently update).

## Prerequisites
- **Horizon** — the "by when" from `3#winning-aspiration`. *Missing a date → that is a gap in the
  aspiration; ask, don't invent one here.*
- **Metric tree** — defined `M-…` nodes to commit on. *Missing → run `metric-tree`.*
- **Financial model** — the projection the values are read off. *Missing → run `financial-model`.*

## How to do it
1. **Take the horizon from the aspiration.** `3#winning-aspiration` states who we serve, what
   result, by when — the "by when" is this section's horizon date. If the aspiration has no date,
   send the gap upstream rather than picking one here.
2. **Pick 3–5 nodes.** The North Star plus the drivers the winning logic actually leans on. More
   than 5 is a dashboard, not a set of commitments — nobody can miss seven promises visibly.
   Nodes considered and left untargeted go to the reject table with why (deliberately not steered
   at the horizon ≠ forgotten).
3. **Read each value off the projection — name the scenario.** Base / conservative / optimistic,
   from `{#financial-model}`. A target no scenario produces is a wish: either the model is missing
   a driver (fix the model) or the target is bravado (lower it). Cite the model, not the air.
4. **Commit, don't compute.** Each target ends in the canonical decision line — dated, attributed,
   with the alternatives considered (the scenario values not chosen, and why this one). ⚙️ while
   the agent's proposal is unconfirmed.
5. **State the ladder rule downward.** Step-5 `goal-targets` sets each period target as a step
   toward these values; a period in which no horizon target moves is drift, visible at the Step-5
   gate — that check lives there, the commitment lives here.
6. **Seed the priority cascade.** With the targets committed, sweep `registers/features.md` by each
   row's `serves`: a feature moving a node that now carries a horizon target — or closing a
   top-ranked risk — is a `priority: now`/`next` candidate; one moving a peripheral node is
   `later`. This is the **structural** weight only (what the model needs, regardless of timing);
   Step-5 `prioritization-tactical-plan` re-weighs it by period fit, Step 6 only adds cost. The
   method declares the write, the orchestrator writes the cells.

## Anti-patterns
- **A target no scenario produces.** Committed bravado — the model says it cannot happen and the
  section pretends otherwise.
- **Seven commitments.** A dashboard in disguise; when everything is promised, no miss is visible.
- **Silently re-forecast targets.** The model changed, the table quietly followed — a commitment
  that tracks the forecast commits nothing.
- **A horizon minted here.** The "by when" belongs to the aspiration; a date invented at Step 4
  hides a strategy gap.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/strategic-targets.md`
(`node_type: worklog`, e.g. `4-strategic-plan/strategic-targets.md`): the horizon taken from the
aspiration, the 3–5 nodes chosen with why each carries a commitment, the scenario each value is
read off with the model citation, the nodes considered and left untargeted with why, and the
decision line per target. That worklog is the **source of truth**; the artifact section
`{#strategic-targets}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the
step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*).

## Output
Projects `{#strategic-targets}` via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml). Step-5 `goal-targets` reads this section
as the top of the ladder; the values themselves are commitments, not `metrics.csv` readings — the
register keeps what *is*, this section keeps what we *promised*.
