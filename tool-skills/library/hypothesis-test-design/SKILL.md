---
name: hypothesis-test-design
kind: method
produces: hypotheses-to-test
prerequisites: [a hypothesis with a threshold, its metric node]
reads_registers: [hypotheses, metrics]
writes_registers: [hypotheses]
inputs: [metrics]
used_by_steps: [4, 5]
opinionated: false
method_basis: "Assumption mapping (Bland/Osterwalder) + smallest viable test: metric · threshold · sample/duration · decision rule"
status: draft
version: 0.1.0
updated: 2026-07-18
---

# Hypothesis Test Design

Turn a hypothesis into a **test you can act on**: pick the metric that reflects it, set the
**threshold** that means success or failure, size the **smallest sufficient test** (sample /
duration), and fix the **decision rule** *before* running it. Fills `{#hypotheses-to-test}`.

**Method basis.** Assumption mapping (Bland & Osterwalder, *Testing Business Ideas*): surface the
riskiest assumption behind a bet, then run the *smallest* experiment that can move belief on it.
Paired with a pre-registered read: a test is `metric · threshold · sample/duration · decision
rule`, all named in advance so the result reads itself.

**Two-step use.** On **Step 4** a hypothesis gets its **threshold** — the quantified bar, tied to a
metric node (`M-…`) in the metric tree. On **Step 5** that same `H-…` gets its **test design** — the
smallest test that can reach the bar this period. Step 4 says *what "true" means in numbers*; Step 5
says *how we'll find out cheaply, and what verdict each outcome triggers*.

## When to apply
- **Step 4**, quantifying a strategy bet: attach a threshold to an `H-…` and bind it to an `M-…`.
- **Step 5**, choosing which `H-…` to test this period: attach the smallest sufficient test design.
- Whenever a bet is about to drive spend or build effort and its truth is still an assumption.

## Prerequisites
- **A hypothesis with a threshold** — a falsifiable `H-…` and the quantified bar that means success.
  *Missing threshold → quantify it first (Step 4 use of this tool); missing hypothesis → seed it via
  the tool that surfaced the bet (e.g. `channels-expansion`, `value-definition`).*
- **Its metric node** — the `M-…` in the metric tree that the threshold is read against.
  *Missing → run `metric-tree` so the test reads against a defined, instrumented node.*

## How to do it
1. **Name the hypothesis and its riskiest assumption.** Which `H-…`, and what has to be true for the
   bet to pay off. Test the assumption that would kill the bet, not the comfortable one.
2. **Pick the metric node that reflects it.** Bind the test to an existing `M-…` — not a bespoke
   number invented for the test. If no node fits, that's a gap for `metric-tree`, not a new metric here.
3. **Set the threshold: success and failure.** The bar the metric must clear to count as validated,
   and the bar below which it's refuted. State both — the gap between them is the inconclusive zone.
4. **Size the smallest sufficient test.** The sample size or duration that can distinguish success
   from failure at that threshold — no larger. If the test costs more than the answer is worth, shrink
   the question or drop it.
5. **Fix the decision rule in advance.** Before running: "at ≥ threshold → `validated`; at < failure
   bar → `refuted`; in between → `inconclusive`, and what we do then." No post-hoc goalposts.
6. **Write it back to the register.** Set the `H-…` `status` to `testing`, link the `test` field to
   this design, and record the metric node, threshold, and rule so the result later flips
   `confidence` to `validated` / `refuted` on its own.

## Anti-patterns
- **No threshold set in advance.** Running a test with no pre-declared bar — any result can be
  spun as a win.
- **"Let's look at the data."** A test with no decision rule; the verdict gets negotiated after the
  numbers land, so belief never actually moves.
- **Test costs more than the answer.** Elaborate experiment to settle a cheap or reversible bet —
  the smallest sufficient test is the point.
- **Sample / duration unspecified.** No sample size or run length, so the test stops when someone
  likes the number, not when it's conclusive.
- **Metric invented for the test.** Reading against a one-off number instead of a defined `M-…` node,
  so the result can't be compared or trusted.

## Output
Fills `{#hypotheses-to-test}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml). On Step 4 the same method quantifies `{#global-hypotheses}`
(threshold + `M-…` link) before the Step 5 test design.
