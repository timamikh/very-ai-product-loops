---
name: hypothesis-test-design
kind: method
produces: hypotheses-to-test
prerequisites: [a hypothesis with a threshold, its metric node]
reads_registers: [hypotheses, metrics]
writes_registers: [hypotheses]
inputs: [metrics]
used_by_steps: [5]
opinionated: false
method_basis: "Assumption mapping (Bland/Osterwalder) + smallest viable test: metric · threshold · sample/duration · decision rule"
evidence_standard: derived
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.3.0
updated: 2026-08-16
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

## Scales — the shared gradations

Four ordinal scales travel with a hypothesis. They are **gradations**, orthogonal to the confirmation
marker a human signs (see `process/CONVENTIONS.md` → *Gradation vs confirmation*). This method is
their canonical home; the deferred `hypothesis-scoring` / `experiment-readout` skills (Steps 5–6) will
*operate* them at sprint scale, but the definitions live here so there is one of each.

- **Readiness gate (before a test) — 6 filters, pass/fail.** A hypothesis is test-ready only if each
  filter has a concrete answer, not a hand-wave:

  | Filter | Question it must answer | Fails on |
  |--------|-------------------------|----------|
  | Find | Where exactly do we reach this segment? | "somewhere in small business" |
  | Recognize | Would the person recognize themselves in it? | "everyone who wants AI" |
  | Pain | Is there a cost of inaction? | "would be nice" |
  | Alternative | How do they solve it today? | "no idea / they don't" |
  | CVP | Do we promise a concrete result? | "gets more efficient" |
  | Action | What signal will we get? | "interest / reactions" |

  A hypothesis missing a channel, a priced pain, a current alternative, or a target action is **not
  ready to test** — fix it before designing the test, don't run it.

- **Priority score (selecting what to test) — 1 / 3 / 5 on five criteria:** pain acuteness
  (`interesting` / `blocks work` / `already costs money`) · segment reach (`unclear where` / `channels
  exist` / `bases, communities, partners`) · product fit (`needs work` / `partial` / `sellable now`) ·
  pay potential (`likes` / `leads` / `willing to pay, pilot`) · test speed (`>2 weeks` / `1 week` /
  `1–2 days`). Rank by the sum; the top few enter the test.

- **Signal strength (the result) — `weak` / `medium` / `strong`.** `weak` (click · like · page-view) is
  **channel diagnostics, not a result**; `medium` (lead · sign-up · reply · details request); `strong`
  (meeting with a real DM · trial access · price talk · pilot · pre-pay · sale). Success means a
  qualified action, so the decision rule reads against the signal grade, not raw clicks.

- **Decision (after the readout) — `scale` / `iterate` / `reject` / `research`.** The call the result
  drives, written back to the hypothesis register's `decision`. A test with no decision recorded is not
  finished.

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
The working is done in the step's **worklog** `<step-folder>/hypothesis-test-design.md` (`node_type:
worklog`, e.g. `5-tactical-plan/hypothesis-test-design.md`): the named `H-…` and its riskiest
assumption, the bound `M-…` metric node, the success and failure thresholds, the smallest-sufficient
test sizing (sample / duration), and the pre-registered decision rule. That worklog is the **source of
truth**; the artifact section `{#hypotheses-to-test}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the step's
change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#hypotheses-to-test}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml). The threshold and `M-…` binding it references are set
at Step 4 by `hypothesis-thresholds`; the readout at the period boundary is `experiment-readout`.
