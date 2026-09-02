---
node_type: card
kind: method
name: ab-test
steps: [5]
prerequisites: [a hypothesis with a threshold and its metric node, enough traffic/sample to detect the effect, a way to randomize and instrument both arms]
reads: [section:guardrails, register:hypotheses, register:metrics, source:metrics]
writes: [worklog, section:hypotheses-to-test, register:hypotheses, register:metrics]
opinionated: false
method_basis: "Online controlled experiments (Kohavi/Tang/Xu) — OEC + guardrail metrics, MDE-driven sizing, pre-registered stopping rule (no peeking)"
evidence_standard: internal-data
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.4
updated: 2026-09-02
---
# A/B Test

Run a **controlled experiment** when the test picked for a hypothesis is a randomized split:
choose the single primary metric (OEC), the guardrails that must not drop, size it from the
minimum effect worth detecting, and pre-register the stopping rule. Fills `{#hypotheses-to-test}`
for the experiment case.

**Method basis.** Kohavi, Tang & Xu (*Trustworthy Online Controlled Experiments*): an experiment
reads one **OEC** against a set of **guardrail metrics**, is **sized from the MDE** so it can
actually detect the effect, and commits to a **stopping rule in advance** so significance isn't
manufactured by peeking.

**Relation to `hypothesis-test-design`.** That tool decides *whether* a bet is worth a test and
fixes the generic `metric · threshold · decision rule`. `ab-test` is the **rigor layer for the
one case where the test is a randomized online experiment** — it adds randomization, sizing, and
guardrails. If you can't randomize or lack the traffic, don't reach for this: keep the cheaper
test `hypothesis-test-design` already specified. One mechanism, one way — this doesn't replace
test selection, it executes one kind of test.

## When to apply
- **Step 5**, when a chosen `H-…` test is a split-traffic experiment and you have the volume to power it.
- Whenever a change is reversible, splittable, and its effect is small enough that eyeballing before/after would fool you.

## Prerequisites
- **A hypothesis with a threshold and its metric node** — a falsifiable `H-…`, its success/failure
  bar, and the `M-…` it reads against. *Missing → run `hypothesis-test-design` first.*
- **Enough traffic/sample to detect the effect** — the volume to reach the required n in a sane
  window. *Missing → the experiment is underpowered; pick a cheaper test instead.*
- **A way to randomize and instrument both arms** — an assignment mechanism and metrics logged per
  arm. *Missing → the instrumentation gap is `instrumentation-plan`'s (Step 4) to close — its
  per-component status says what is unmeasured; until it is closed, use an honest before/after and
  label it as such.*

## How to do it
1. **Confirm the experiment is the right instrument.** Defer test *selection* to
   `hypothesis-test-design`. Reach for A/B only when you can randomize and power it.
2. **Define the OEC.** One primary metric — an existing `M-…` — that means the bet won. Not three
   co-equal metrics; the OEC is what the decision hangs on.
3. **Pick guardrail metrics.** What must **not** degrade while chasing the OEC — latency, error
   rate, churn, revenue-per-user. Tie them to protected `M-…` / the `guardrails` section. A
   guardrail breach refutes the change regardless of the OEC.
4. **Set the randomization unit and arms.** Unit (user / account / session), control vs
   variant(s), allocation split. The unit must match the metric's grain and avoid spillover
   between arms.
5. **Size it from the MDE, and state the population.** From the minimum detectable effect, the
   baseline rate, and power/α, compute the required sample and run length. Don't start a test that
   can't reach its own bar. Write down **who is in the test** — which traffic, which segments, who is
   excluded (internal accounts, bots, an ineligible plan) and any skew you know about (time of day,
   new vs returning). The read is only reproducible if a later reader can reconstruct the denominator;
   this is the same discipline as any register reading (see
   [`../../operations/metrics-capture/SKILL.md`](../../operations/metrics-capture/SKILL.md)).
6. **Pre-register the stopping rule.** A fixed horizon, or a valid sequential method — never
   peek-and-stop when it looks significant. The verdict maps to the `hypothesis-test-design`
   validated / refuted / inconclusive bars.
7. **Check pitfalls before trusting the read.** Sample-ratio mismatch (SRM), novelty/primacy
   effects, segment interactions, cross-arm contamination. An SRM voids the read.
8. **Read and write back.** Verdict flips the `H-…` `confidence`; land the measured effect in
   `registers/metrics.csv` as a dated row; a guardrail breach → `refuted` even if the OEC moved.

## Anti-patterns
- **Peeking and stopping.** Ending the moment it looks significant — inflates false positives.
- **No guardrails.** Winning the OEC while quietly breaking latency, churn, or revenue.
- **Underpowered.** Too small or too short to detect the MDE — an inconclusive dressed up as a null.
- **Segment p-hacking.** Slicing until *something* is "significant" with no pre-registration.
- **A/B where you can't randomize.** A confounded pseudo-experiment; use a labeled before/after or holdout.
- **Ignoring SRM.** Unequal arms signal a broken assignment; the result is void, not "close enough".

## Worklog & projection
Worklog: `5-tactical-plan/ab-test.md` — the OEC and guardrails, the unit / arms / split, the MDE sizing with the stated population, the stopping rule, the pitfall checks, the verdict with the measured effect. Projects the experiment block of `{#hypotheses-to-test}` (second tool of the marker; `hypothesis-test-design` is primary); face: the **Test read** line, the same slot, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#hypotheses-to-test}` (the experiment design + read) via
[`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). It **specializes** `hypothesis-test-design` for the
online-experiment case; the result writes back to the hypotheses register (`confidence`) and the
metric register (measured effect).
