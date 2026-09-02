---
node_type: card
kind: method
name: hypothesis-test-design
steps: [5]
prerequisites: [a hypothesis with a threshold, its metric node]
reads: [section:global-hypotheses, section:market-bundles, register:hypotheses, register:metrics]
writes: [worklog, section:hypotheses-to-test, register:hypotheses]
opinionated: false
method_basis: "Assumption mapping (Bland/Osterwalder) + smallest viable test: metric · threshold · sample/duration · decision rule"
evidence_standard: derived
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.3.2
updated: 2026-09-02
---
# Hypothesis Test Design

Turn a hypothesis into a **test you can act on**: pick the metric that reflects it, set the
**threshold** that means success or failure, size the **smallest sufficient test** (sample /
duration), and fix the **decision rule** *before* running it. Fills `{#hypotheses-to-test}`.

**Method basis.** Assumption mapping (Bland & Osterwalder, *Testing Business Ideas*): surface the
riskiest assumption behind a bet, then run the *smallest* experiment that can move belief on it.
Paired with a pre-registered read: a test is `metric · threshold · sample/duration · decision
rule`, all named in advance so the result reads itself.

**Boundary.** Thresholds come from `hypothesis-thresholds` at Step 4 and are **referenced, never
re-decided here** — this method designs the smallest test that can reach that bar this period.

## When to apply
- **Step 5**, choosing which `H-…` to test this period: attach the smallest sufficient test design.
- Whenever a bet is about to drive spend or build effort and its truth is still an assumption.

## Prerequisites
- **A hypothesis with a threshold** — a falsifiable `H-…` and the quantified bar that means success.
  *Missing threshold → quantify it at Step 4 via `hypothesis-thresholds`; missing hypothesis → seed
  it via the tool that surfaced the bet (e.g. `channels-expansion`, `value-definition`).*
- **Its metric node** — the `M-…` in the metric tree that the threshold is read against.
  *Missing → run `metric-tree` so the test reads against a defined, instrumented node.*

## How to do it
1. **Name the hypothesis and its riskiest assumption.** Which `H-…`, and what has to be true for the
   bet to pay off. Test the assumption that would kill the bet, not the comfortable one.
2. **Pick the metric node that reflects it.** Bind the test to an existing `M-…` — not a bespoke
   number invented for the test. If no node fits, that's a gap for `metric-tree`, not a new metric here.
3. **Reference the threshold: success and failure.** The bars come from Step 4
   (`hypothesis-thresholds`) — cite both; the gap between them is the inconclusive zone. A missing
   bar is a Step 4 gap to close there, never a number decided here.
4. **Size the smallest sufficient test.** The sample size or duration that can distinguish success
   from failure at that threshold — no larger. If the test costs more than the answer is worth, shrink
   the question or drop it.
5. **Fix the decision rule in advance.** Before running: "at ≥ threshold → `validated`; at < failure
   bar → `refuted`; in between → `inconclusive`, and what we do then." No post-hoc goalposts.
6. **Write it back to the register.** Set the `H-…` `status` to `testing`, link the `test` field to
   this design, and record the metric node, threshold, and rule so the result later flips
   `confidence` to `validated` / `refuted` on its own.

## Scales
The four gradations a hypothesis travels with — the **readiness gate** (6 filters), the **priority
score** (1/3/5 on five criteria), **signal strength** (`weak` / `medium` / `strong`) and the
**decision** (`scale` / `iterate` / `reject` / `research`) — are defined once, in
[`process/reference/scales.md`](../../../process/reference/scales.md). This method applies the readiness gate and reads against
the bars; `segment-cvp` operates the gate and the score over bundles, `experiment-readout` grades
the signal and records the decision. Nothing here redefines a scale; a hypothesis missing a channel,
a priced pain, a current alternative or a target action is **not ready to test** — fix it before
designing the test, don't run it.

## Anti-patterns
- **No threshold set in advance.** Running a test with no pre-declared bar — any result can be
  spun as a win.
- **A test that skips the readiness gate.** Designing a test for a bet with no channel, no priced
  pain, or no target action — the gate is what makes the test answerable at all.
- **"Let's look at the data."** A test with no decision rule; the verdict gets negotiated after the
  numbers land, so belief never actually moves.
- **Test costs more than the answer.** Elaborate experiment to settle a cheap or reversible bet —
  the smallest sufficient test is the point.
- **Sample / duration unspecified.** No sample size or run length, so the test stops when someone
  likes the number, not when it's conclusive.
- **Metric invented for the test.** Reading against a one-off number instead of a defined `M-…` node,
  so the result can't be compared or trusted.

## Worklog & projection
Worklog: `5-tactical-plan/hypothesis-test-design.md` — the `H-…` and its riskiest assumption, the bound `M-…`, the referenced bars, the smallest-sufficient sizing, the pre-registered decision rule. Projects `{#hypotheses-to-test}`; face: the **Test read** line, via [`template-fragment.md`](template-fragment.md). Primary of the marker; `ab-test` fills the same section for the experiment case with the same slot. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#hypotheses-to-test}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml). The threshold and `M-…` binding it references are set
at Step 4 by `hypothesis-thresholds`; the readout at the period boundary is `experiment-readout`.
