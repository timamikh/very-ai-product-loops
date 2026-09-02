---
node_type: card
kind: method
name: hypothesis-thresholds
steps: [4]
prerequisites: [strategy bets (H-…), the metric tree]
reads: [section:bets, section:metric-tree, register:hypotheses, register:metrics]
writes: [worklog, section:global-hypotheses, register:hypotheses]
opinionated: false
method_basis: "Pre-registered read (Bland/Osterwalder assumption mapping): success bar · failure bar · conscious inconclusive zone, each bound to an existing metric node"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.2
updated: 2026-09-02
---
# Hypothesis Thresholds

Quantify the strategy's bets: each `H-…` carried from `3-strategy.md#bets` gets a **success
threshold** and a **failure threshold**, both read against an **existing `M-…` node** from the
just-built metric tree — never a number invented for the test. The gap between the two bars is a
**conscious inconclusive zone**, stated on purpose, not discovered later. Fills
`{#global-hypotheses}`.

**Method basis.** Assumption mapping (Bland & Osterwalder, *Testing Business Ideas*): a bet only
moves belief when "true" and "false" are named in numbers *before* anyone looks. This method sets
the bars; it does not design the experiment.

> **Boundary with Step 5 (this kills a known double-write).** The thresholds set here are the
> **single source of truth**. Step 5's `hypothesis-test-design` *references* them — it sizes the
> smallest sufficient test that can reach the bar and fixes the decision rule — it **never
> re-decides the bar**. If a threshold turns out wrong, the fix happens here (a ⚙️ change to
> `{#global-hypotheses}` and the register), not inside a test design.

## When to apply
- **Step 4**, right after the metric tree exists: attach thresholds to every `H-…` the strategy
  bets on, and bind each to its `M-…` node.
- Whenever a bet is about to drive spend or build effort and its "success" is still a vibe, not a
  number.

## Prerequisites
- **Strategy bets (`H-…`)** — the falsifiable bets carried from `3-strategy.md#bets`.
  *Missing → the bet was never stated; it arrives from Step 3's `bets`, seeded there — don't invent
  one here.*
- **The metric tree** — defined `M-…` nodes to read the thresholds against.
  *Missing → run `metric-tree` first; a threshold against an undefined node is a number in the air.*

## How to do it
1. **Take each bet from `3-strategy.md#bets`.** One row per `H-…` — this method quantifies existing
   bets; it does not generate new ones.
2. **Bind it to an existing `M-…` node.** The node whose movement would prove or refute the bet.
   If no node fits, that is a gap for `metric-tree` to close — never a bespoke metric invented for
   the test (it couldn't be compared or trusted).
3. **Set the success threshold.** The bar the node must clear for the bet to count as validated.
   Anchor it in something — the economics, a benchmark, the strategy's ambition — and say which.
4. **Set the failure threshold.** The bar below which the bet is refuted. It is *not* simply
   "below success": the gap between the two bars is the **inconclusive zone**, and its width is a
   conscious choice — wide means "we tolerate ambiguity here", narrow means "this must resolve".
5. **Write why these numbers.** One line per row: where the bars come from. A threshold with no
   provenance gets re-litigated the moment the result lands near it. The bars are a choice the
   humans own: the section ends in the canonical decision line, its alternatives the bar values
   weighed and not taken.
6. **Write back to the register.** Upsert each `H-…` with its `M-…` link, both thresholds, and the
   rationale, so Step 5's test design can reference them without asking again.

## Anti-patterns
- **Threshold invented at test time.** Step 5 discovering there is no bar and making one up — the
  bar belongs here, pre-registered, before any test is designed.
- **A number with no node.** A threshold read against a metric that exists nowhere in the tree —
  bind to an `M-…` or flag the gap to `metric-tree`.
- **Success only.** No failure bar means no result can refute the bet — any outcome above zero gets
  spun as "promising".
- **Accidental inconclusive zone.** The gap between bars never stated, so a middling result triggers
  an argument instead of the pre-agreed "inconclusive → what we do then".
- **Re-deciding the bar downstream.** A test design that "adjusts" the threshold to fit the sample
  it can afford — shrink the *test*, or change the bar *here*, visibly.
- **Bars with no provenance.** "≥ 20 %" with no line on why 20 — the number survives review only
  until someone asks.

## Worklog & projection
Worklog: `4-strategic-plan/hypothesis-thresholds.md` — each bet from `3#bets`, the `M-…` it binds to or the flagged gap, both bars with the width of the inconclusive zone, the provenance of every number. Projects `{#global-hypotheses}`; face: the **Bars read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#global-hypotheses}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml). Upserts each `H-…` (metric node · success bar ·
failure bar · rationale) into the hypothesis register; Step 5's `hypothesis-test-design` reads the
bars from there and designs the smallest sufficient test — it never re-decides them.
