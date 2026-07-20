---
name: jtbd
kind: method
produces: [jtbd, bets]
prerequisites: [a segment/customer]
reads_registers: [hypotheses]
writes_registers: [hypotheses]
inputs: [interview, kb]
used_by_steps: [1, 3]
opinionated: false
method_basis: "Jobs-to-be-Done — Christensen 'progress' + Ulwick ODI: job statement · forces (push/pull/anxiety/habit) · desired outcomes"
status: draft
version: 0.2.0
updated: 2026-07-21
---

# Jobs-to-be-Done

Frame the **job** a customer hires the product to do — the *progress they want in a
circumstance* — and the **forces** that move them toward or away from it. At Step 1 it fills
`{#jtbd}` (the job, four forces, and desired outcomes) — this anchors `{#segments}` and
`{#problems}` and **feeds Step 2 `substitutes`**, where the job is the frame for finding indirect
competition. At Step 3 it sharpens `{#bets}`: strategic wagers framed around the customer's job,
not around our features.

**Method basis.** JTBD in two lenses: Christensen's *progress in a circumstance* (a job is
"when… I want… so that…") and Ulwick's ODI (a job resolves into measurable **desired outcomes**).
Movement between the old way and the new is read through the **four forces** — push, pull, anxiety,
habit.

> **Boundary with `segment-pains`.** `segment-pains` takes the job as given and scores the *pains
> inside it* (severity × frequency, differentiator vs table-stakes). `jtbd` sits one level up: it
> **states the job itself and the forces** around switching. Use `jtbd` to define/validate the job
> and its dynamics; use `segment-pains` to rank the pains within it. Don't re-score pains here.

## When to apply

- **Step 1 — fills `{#jtbd}`, upstream of segments and pains.** JTBD frames *who* (segments) and
  *where it hurts* (problems), so run it before/alongside `segmentation` and `segment-pains` — its
  job statement and forces anchor both, and the job is what `substitutes` (Step 2) uses to find
  indirect competition. Reach for it especially when segments read as demographics or pains read as
  a feature wish-list — the job re-anchors both on progress.
- **Step 3 — to sharpen `bets`.** Alongside `value-definition`, frame the strategic wagers around
  the customer's job and the forces that gate switching. A bet worded as "customers will hire us
  over the status quo *for this job* because the pull beats the anxiety+habit" is testable.
- Any time a segment, pain, or bet drifts toward a solution and away from the underlying progress.

## Prerequisites

- **A segment / customer** — whose job we're framing. Circumstance and forces are read *for a
  specific customer in a specific situation*, not in the abstract. *Missing → run `segmentation`
  (Step 1) or name the customer the bet targets (Step 3).*

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
   `process/CONVENTIONS.md`. Early on the job and forces are largely `[assumption]`.
5. **Seed hypotheses.** Each unproven claim about the job or a force → `H-…` (`type: desirability`
   — is this the job, is this force real and this strong). At Step 3, each bet framed on the job →
   `H-…` (mixed types) in the register.

## Anti-patterns

- **Job as a feature / solution.** "They want our button / our dashboard" is a solution, not a
  job. The job is the progress they'd make with *or without* us.
- **Job without a circumstance.** A job with no *when* is a persona statement — it can't be tested
  and the forces can't be read.
- **Ignoring habit / anxiety.** Listing only push+pull and assuming the switch happens. Inertia and
  fear of the status quo are usually why a "great" solution doesn't get hired.
- **Segment as demographics.** Cutting the customer by age/role/industry instead of by the job and
  circumstance. Same demographic, different job → different product.

## Output

At Step 1, fills `{#jtbd}`; at Step 3, fills `{#bets}` — both via
[`template-fragment.md`](template-fragment.md); inputs via [`questions.yaml`](questions.yaml). The
Step-1 job statement anchors `{#segments}`/`{#problems}` and is the input `substitutes` (Step 2)
frames indirect competition against.
