---
node_type: card
kind: method
name: impact-readout
steps: [5]
prerequisites: [shipped sprint items carrying a Feature link and a pre-registered Expected impact with a check-by, the measured fact landed (metrics.csv / register statuses)]
reads: [section:must, section:readouts, register:features, register:metrics, register:risks, register:hypotheses]
writes: [worklog, section:item-readouts, register:features]
opinionated: false
method_basis: "Pre-registered read of shipped items: expected impact vs the fact (metrics.csv / register state) and estimate vs actual cost — verdict flips the feature's state, no post-hoc re-goaling; a check-by not reached is `pending`, never skipped"
evidence_standard: internal-data
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.1
updated: 2026-09-02
---
# Impact Readout (items)

Read the **shipped sprint items strictly against the expectations pre-registered on them** in
`6#must`: did the impact land as claimed (`M-…` moved / `R-…` closed / `H-…` verdict) and did the
item cost what its Estimate said. Fills `{#item-readouts}` (Step 5) and flips the feature register.
This is the right side of the V for **work items** — the sibling of
[`experiment-readout`](../experiment-readout/SKILL.md), which owns **hypothesis tests**: an `H-…`
with a designed test reads there, never here (one read per verdict, no double-reading).

**Method basis.** Every must item shipped with three pre-registered things: a `Feature: F-…` link,
an `Expected impact` (which id, which direction/size, `check-by` when it becomes readable), and an
`Estimate` (class S/M/L + range). The readout applies exactly those and nothing else — **no
post-hoc re-goaling**: an expectation softened after the numbers land is not a read, it's a
negotiation. The fact comes from `metrics.csv` rows, register statuses, and `experiment-readout`
verdicts — never from memory.

> **A declared forward edge.** `reads` names `section:must` of Step 6 — the one place a Step-5
> method reads a later step's section. It is deliberate, not an accident of wiring: the sprint plan
> pre-registers what this gate reads, so the edge runs from the *previous* period's sprint plan
> into *this* period's gate — backward in time, forward in step number. It is legal only because
> the card declares it; no other method may read ahead.

## When to apply
- Step 5, at the period gate: every item shipped last period gets a row — read, `pending`
  (check-by not reached), or `inconclusive`; none skipped silently.
- Whenever an item's `check-by` arrives — not before (reading a retention claim a week after
  launch is peeking).

## Prerequisites
- **Shipped items with pre-registered expectations** — Feature link, Expected impact, check-by,
  Estimate, from `6#must`. *An item shipped without them → record that as the finding; its impact
  cannot be read, only narrated.*
- **The measured fact** — `metrics.csv` rows for an `M-…` claim (via `metrics-capture`), the
  register status for an `R-…` claim, the `experiment-readout` verdict for an `H-…` claim.
  *Missing → capture first.*

## How to do it
1. **List last period's shipped items** from `6#must` (and any backlog item that shipped). Every
   one gets a row. An item not shipped is not read — it returns to ranking, and its feature stays
   `planned`.
2. **Restate each expectation verbatim** — the id, the expected direction/size, the check-by, the
   estimate — copied from the sprint plan, not reconstructed.
3. **Sort by check-by.** Not reached → verdict `pending`, listed, re-read next gate. Reached →
   read now.
4. **Read impact against the fact — and only the fact.** `M-…`: the `metrics.csv` reading vs the
   expected direction/size → `confirmed` / `missed` / `inconclusive` (a directional claim reads
   directionally — that is exactly as much as was pre-registered). `R-…`: did the register status
   move as claimed. `H-…`: cite the `experiment-readout` verdict — do not re-run it.
5. **Read the estimate.** Actual cost vs the estimated class/range. A miss is calibration data,
   not blame: note it on the row; repeated misses in one class are the trigger to recalibrate how
   the specs size that class.
6. **Flip the feature register.** A shipped item's `F-…`: `planned → live` (shipped is shipped —
   state and verdict are orthogonal). The verdict lands on the row's `serves` confidence:
   `[validated: sprint-N, …]` / `[refuted: sprint-N, …]`. A `retired`-type item retires its row.
7. **Bubble a miss upward by name.** A `missed` impact names the section or register row whose
   assumption it breaks (a period goal, a `serves` claim, a strategy bet) — the upward revisit is
   triggered by name, not by vibes, exactly like a refuted `H-…`.

## Anti-patterns
- **Post-hoc re-goaling.** Softening the expected size or swapping the metric after the numbers
  land — any item can be spun as a win.
- **Reading before check-by.** A retention claim read at launch week is peeking; the verdict is
  void, not "early signal".
- **Skipping the unreadable.** An item with no pre-registered expectation quietly omitted — the
  row exists and says so; that gap is this method's most valuable output early on.
- **Verdict without a citation.** `confirmed` with no `metrics.csv` row / register state named —
  not reproducible, not a read.
- **Double-reading a hypothesis.** An `H-…` with a designed test gets its verdict from
  `experiment-readout`; this method cites it, never re-judges it.
- **Estimate miss as blame.** The point is a self-calibrating sizing table, not a performance
  review; hide the misses and the estimates stay fiction.

## Worklog & projection
Worklog: `5-tactical-plan/impact-readout.md` — each shipped item, its expectation verbatim, the fact with its citation, the verdict, the estimate-vs-actual note, the register flips, the section a miss invalidates. Projects `{#item-readouts}`; face: the **Impact read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#item-readouts}` (Step 5) via [`template-fragment.md`](template-fragment.md) from the
worklog; inputs via [`questions.yaml`](questions.yaml). Writes `state` flips and `serves`
confidence onto `registers/features.md`; a `missed` verdict triggers the upward revisit of the
section it names; estimate misses feed the sizing calibration the specs use next sprint.
