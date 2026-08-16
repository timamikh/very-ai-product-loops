---
name: jtbd-concept
kind: method
produces: jtbd
prerequisites: [a segment/customer]
reads_registers: [hypotheses]
writes_registers: [hypotheses]
inputs: [interview, kb]
used_by_steps: [1]
opinionated: false
method_basis: "Jobs-to-be-Done — Christensen 'progress' + Ulwick ODI: job statement · forces (push/pull/anxiety/habit) · desired outcomes"
evidence_standard: primary-research
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.0
updated: 2026-08-16
---

# Jobs-to-be-Done (concept)

Frame the **job** a customer hires the product to do — the *progress they want in a
circumstance* — and the **forces** that move them toward or away from it. Fills `{#jtbd}` at
Step 1 (the job, four forces, and desired outcomes): this anchors `{#segments}` and `{#problems}`
and **feeds Step 2 `substitutes`**, where the job is the frame for finding indirect competition.

**Method basis.** JTBD in two lenses: Christensen's *progress in a circumstance* (a job is
"when… I want… so that…") and Ulwick's ODI (a job resolves into measurable **desired outcomes**).
Movement between the old way and the new is read through the **four forces** — push, pull, anxiety,
habit.

> **Relation to neighbours (one mechanism, one way).**
> - **`segment-pains`** takes the job as given and scores the *pains inside it* (severity ×
>   frequency, differentiator vs table-stakes). `jtbd-concept` sits one level up: it **states the
>   job itself and the forces** around switching. Don't re-score pains here.
> - **`substitutes` (Step 2)** uses the job statement as its frame — "what else gets this job
>   done" is only answerable once the job is stated.
> - **`bets` (Step 3)** re-uses the job and forces to frame the strategic wagers — "hired over the
>   status quo for this job because pull beats anxiety + habit". This skill states the job once;
>   `bets` wagers on it. Don't write bets here.

## When to apply

- **Step 1 — fills `{#jtbd}`, upstream of segments and pains.** JTBD frames *who* (segments) and
  *where it hurts* (problems), so run it before/alongside `segmentation` and `segment-pains` — its
  job statement and forces anchor both, and the job is what `substitutes` (Step 2) uses to find
  indirect competition. Reach for it especially when segments read as demographics or pains read as
  a feature wish-list — the job re-anchors both on progress.
- Any time a segment or pain drifts toward a solution and away from the underlying progress.

## Prerequisites

- **A segment / customer** — whose job we're framing. Circumstance and forces are read *for a
  specific customer in a specific situation*, not in the abstract. *Missing → run `segmentation`,
  or name the customer the concept targets.*

## How to do it

1. **Write the job statement.** `When <circumstance/trigger>, I want to <make this progress>, so
   that <outcome/motivation>.` The middle clause is *progress*, never a product or feature. If you
   can't state the circumstance, you don't yet have a job — you have a persona.
2. **Read the four forces.** For the switch from the current way to the new one:
   - **Push** — what about the current situation makes it unacceptable (drives away from status quo).
   - **Pull** — what attracts them to the new solution.
   - **Anxiety** — fears/uncertainty about the new solution.
   - **Habit / inertia** — attachment to the existing way (allegiance to the status quo).
   Progress happens only when **push + pull > anxiety + habit**. Name all four; a missing force is
   usually the one that kills adoption.
3. **Name the desired outcomes (ODI).** How does the customer *measure* success at this job?
   State outcomes as measurable directions (minimize / increase the time/likelihood/effort of …),
   not features. These are what `segment-pains` later scores and what metrics later track.
4. **Tag confidence & source.** `[sourced: interview …]` / `[sourced: kb …]` / `[assumption]` per
   `process/CONVENTIONS.md`. Early on the job and forces are largely `[assumption]`. Where a force is
   sourced from interviews, name the sample (how many, who) — the four forces are the part of this
   method most often filled in from the team's own intuition and then quoted back as customer
   evidence.
5. **Seed hypotheses.** Each unproven claim about the job or a force → `H-…` (`type: desirability`
   — is this the job, is this force real and this strong). Often jtbd **sharpens** existing
   segment/pain hypotheses rather than adding new ones — reconcile against the register before
   minting a new id.

## Anti-patterns

- **Job as a feature / solution.** "They want our button / our dashboard" is a solution, not a
  job. The job is the progress they'd make with *or without* us.
- **Job without a circumstance.** A job with no *when* is a persona statement — it can't be tested
  and the forces can't be read.
- **Ignoring habit / anxiety.** Listing only push+pull and assuming the switch happens. Inertia and
  fear of the status quo are usually why a "great" solution doesn't get hired.
- **Segment as demographics.** Cutting the customer by age/role/industry instead of by the job and
  circumstance. Same demographic, different job → different product.
- **Writing the strategy's bets here.** Wagers framed on the job belong to `bets` at Step 3 — this
  skill supplies the job and forces they are framed on, nothing more.

## Worklog & projection

The working is done in the step's **worklog** `1-concept/jtbd-concept.md` (`node_type: worklog`):
the job statement (`when… I want… so that…`), the four forces (push · pull · anxiety · habit) with
their sources, and the measurable desired outcomes. That worklog is the **source of truth**; the
artifact section `{#jtbd}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the
step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External inputs arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output

Projects `{#jtbd}` via [`template-fragment.md`](template-fragment.md) from the step's worklog;
inputs via [`questions.yaml`](questions.yaml). The job statement anchors `{#segments}`/`{#problems}`,
is the input `substitutes` (Step 2) frames indirect competition against, and is what `bets` (Step 3)
wagers on.
