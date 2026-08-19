---
node_type: card
kind: method
name: experiment-readout
steps: [5]
prerequisites: [a finished test, its pre-registered decision rule, the measured result]
reads: [register:hypotheses, register:metrics, source:metrics]
writes: [worklog, section:readouts, register:hypotheses]
opinionated: false
method_basis: "Pre-registered read: result vs the decision rule fixed at design time — signal grade + decision (scale · iterate · reject · research) written back to the hypothesis register; no post-hoc re-thresholding"
evidence_standard: internal-data
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.0
updated: 2026-08-16
---
# Experiment Readout

Read a **finished test strictly against its pre-registered decision rule** from
`{#hypotheses-to-test}`: record the result, grade the **signal**, make the **decision**
(`scale` · `iterate` · `reject` · `research`), and write both back to the hypothesis register.
Fills `{#readouts}` (Step 5). The whole value of pre-registering a rule at design time is that the
result **reads itself** — this method is where that promise is kept or broken.

**Method basis.** The rule was fixed before the test ran (`hypothesis-test-design` / `ab-test`):
metric node · success and failure thresholds · sample/duration · the verdict each zone triggers.
The readout applies that rule and nothing else — **no post-hoc re-thresholding**: a bar moved after
the numbers land is not a read, it's a negotiation. The scales it operates — signal grade and
decision — are defined once, in [`hypothesis-test-design`](../hypothesis-test-design/SKILL.md)
§Scales and `process/REGISTERS.md`; this method applies them, it does not redefine them.

## When to apply
- Step 5, at the period boundary: every test that finished this period gets a readout — none
  skipped, none carried silently.
- Whenever a test reaches its pre-registered sample/duration — not before (reading early is
  peeking).

## Prerequisites
- **A finished test** — the `H-…` reached its pre-registered sample or duration. *Not finished →
  wait; a mid-test read is peeking, not a readout.*
- **Its pre-registered decision rule** — the metric node, thresholds, and verdict map from
  `{#hypotheses-to-test}`. *Missing → the test was never properly designed; record that as the
  finding and route the bet back through `hypothesis-test-design`.*
- **The measured result** — the metric value(s), landed in `registers/metrics.csv` as dated rows
  (via `metrics-capture`). *Missing → capture first; a readout against a remembered number is not
  reproducible.*

## How to do it
1. **List the tests that finished this period.** From `{#hypotheses-to-test}` and the hypothesis
   register (`status: testing`). Every finished test gets a row — an unread finished test is a paid
   answer left unopened.
2. **Restate the pre-registered rule verbatim.** Metric node, success threshold, failure threshold,
   sample/duration, and the verdict each zone triggers — copied from the design, not reconstructed
   from memory.
3. **Read the result against the rule — and only the rule.** ≥ success bar → `validated`; below the
   failure bar → `refuted`; between → `inconclusive`, and the *pre-declared* next action for that
   zone. The inconclusive zone is exactly as wide as the design said; widening it after the fact is
   re-thresholding in disguise.
4. **Grade the signal.** `weak` / `medium` / `strong` per the register's scale — a weak signal
   (clicks, likes) diagnoses the channel, not the fit, whatever the raw count says.
5. **Make the decision.** `scale` · `iterate` · `reject` · `research` (the register enums). A
   readout without a decision is not finished. `research` is not a shrug — it must produce a
   **named learning item** (what exactly we now need to find out) that enters the next period's
   goals as a candidate.
6. **Write back to the register.** On the `H-…` row: `status` → `validated` / `refuted`, `signal`,
   `decision`; `confidence` flips accordingly. The register is the home of the verdict; the
   artifact section only projects it.
7. **Bubble a refuted bet upward.** A refuted `H-…` **names the section whose confirmation it
   invalidates** (a strategy bet, a metric-tree assumption, a staged bundle) — the upward revisit
   is triggered by name, not by vibes.

## Anti-patterns
- **Peeking mid-test.** Reading before the pre-registered sample/duration is reached — inflates
  false positives; the read is void, not "early signal".
- **Post-hoc re-thresholding.** Moving the success or failure bar after seeing the numbers — any
  result can be spun as a win.
- **Silently widening the inconclusive zone.** Calling a failed test "inconclusive" by stretching
  the middle — a refutation dodged is a lesson unlearned and a budget re-spent.
- **Averaging two conflicting reads.** Two tests (or two segments) disagree and the readout blends
  them into one mushy number — record both, name the conflict, and decide which read the rule
  actually covers.
- **A readout with no decision.** Result recorded, verdict pending forever — the test isn't
  finished until `scale` / `iterate` / `reject` / `research` is on the register row.
- **`research` as a shrug.** A research decision with no named learning item — nothing enters the
  next period, and the same bet returns unimproved.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/experiment-readout.md` (`node_type:
worklog`, e.g. `5-tactical-plan/experiment-readout.md`): each finished test, its pre-registered
rule restated verbatim, the measured result with its `metrics.csv` citation, the verdict zone it
landed in, the signal grade, the decision with the named learning item for any `research`, and the
section a refuted `H-…` invalidates. That worklog is the **source of truth**; the artifact section
`{#readouts}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the
step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*).

## Output
Projects `{#readouts}` (Step 5) via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml). Writes `signal` / `decision` / `status` back to the
hypothesis register; a `research` decision feeds a named learning item into the next period's
goals; a refuted `H-…` triggers the upward revisit of the section it names.
