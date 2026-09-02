---
node_type: card
kind: method
name: bets
steps: [3]
prerequisites: [the job and forces (jtbd), strategy choices (where-to-play / how-to-win), value & defensibility]
reads: [section:jtbd, section:where-to-play, section:how-to-win, section:value-defensibility, register:hypotheses]
writes: [worklog, section:bets, register:hypotheses]
opinionated: false
method_basis: "Strategic bets framed on the JTBD forces — '<segment> will hire us over <status quo> for <job> because pull > anxiety + habit' — each tied to a named moat; one bet = one typed hypothesis"
evidence_standard: decision
volume_rule: "3–7 bets; each names the segment, the job/circumstance, the status quo it displaces, and the moat it leans on"
selection_rule: "a bet must beat the status quo on the forces (pull > anxiety + habit) and lean on a named moat; candidates that can't say why they win are recorded, not carried"
rejects_shown: required
status: draft
version: 0.2.1
updated: 2026-09-02
---
# Strategic Bets

State the **3–7 wagers the strategy stands on** — each framed on the customer's job, not on our
features: *we bet that `<segment>` will hire us over `<status quo>` for `<job>`, because the pull
beats the anxiety + habit*. Each bet names the **moat** it leans on and is seeded as a typed
hypothesis (`H-…`). Fills `{#bets}`.

**Method basis.** The JTBD switching model applied to strategy: a strategy choice becomes real only
as a falsifiable claim about who switches, from what, and why the forces favour us. A bet worded as
"customers will hire us over the status quo *for this job* because the pull beats the anxiety+habit"
is testable; "we will win on quality" is not. The moat (from `value-definition-strategy`) is the
*because* — why the win, once earned, holds.

> **Relation to neighbours (one mechanism, one way).**
> - **`jtbd-concept` (Step 1)** states the job and the four forces — this skill *wagers on* that
>   job, it does not restate it. If the job or forces are missing or stale, fix them there first.
> - **`value-definition-strategy`** contributes the moats: it is the second tool on the `{#bets}`
>   marker, works in its own worklog, and its moats reach this skill through the re-projected
>   `{#value-defensibility}` and `{#how-to-win}` — no method writes another's worklog (N6).
> - **`where-to-play-how-to-win`** seeds the cascade's load-bearing assumptions as `H-…` when the
>   arena is chosen. A bet here often *is* one of those assumptions made concrete — **reconcile
>   before minting** (see step 4 below); a duplicate `H-` for the same claim splits its evidence.
> - **Downstream:** `segment-cvp` (Step 5) sharpens a staged bet into a testable market-entry
>   bundle; `hypothesis-test-design` designs the actual test. This skill produces the *wager*, not
>   the experiment.

## When to apply
- **Step 3, last** — after where-to-play / how-to-win, the UVP, and the moats are chosen. The bets
  are those choices restated as falsifiable claims; writing them first is writing them from hope.
- Whenever a strategy review asks "what exactly are we assuming" and the answer is prose, not a
  list of typed hypotheses with ids.

## Prerequisites
- **The job and forces** — from Step 1 `{#jtbd}` (`jtbd-concept`). *Missing → run it; a bet without
  a job is a feature roadmap item.*
- **Strategy choices** — the chosen where-to-play / how-to-win. *Missing → run
  `where-to-play-how-to-win`.*
- **Value & defensibility** — the moats a bet can lean on. *Missing → run
  `value-definition-strategy` (or Step 1's `value-definition-concept` if nothing exists at all).*

## How to do it
1. **Draft the candidate bets.** For each chosen arena/segment: *we bet that `<segment>` will hire
   us over `<status quo>` for `<the job>`, because `<pull>` beats `<anxiety + habit>`*. Name the
   circumstance (from the job statement) and the concrete status quo being displaced (a rival, a
   substitute, do-nothing) — a bet against "the market" displaces nothing.
2. **Tie each bet to a named moat.** From `{#value-defensibility}` / `{#how-to-win}`: which moat
   makes this win durable once it happens? A bet with no moat behind it is a promotion, not a
   strategy — record it, but say so.
3. **Type each bet.** `desirability` / `viability` / `feasibility` / `usability` — mixed types are
   normal (a pricing bet is viability; a switching bet is desirability). The type decides what
   evidence can settle it.
4. **Reconcile against the register — no duplicate `H-` for the same claim.** Read the hypothesis
   register first: `where-to-play-how-to-win` has already seeded the cascade's load-bearing
   assumptions as `H-…`, and Step 1 tools seeded segment/job claims. If a bet restates an existing
   hypothesis, **sharpen that entry** (tighten its statement, raise its stakes) and reuse its id —
   do not mint a second one. Two ids for one claim means each accumulates half the evidence and
   neither ever settles.
5. **Cut to 3–7 and record what you cut.** Fewer than 3 usually means the strategy's assumptions
   haven't been examined; more than 7 is a backlog, not a strategy — nobody can hold ten wagers
   accountable. Every candidate not carried stays in the worklog with the reason (no moat, no
   testable status quo, duplicate of `H-…`, out-scoped by where-to-play).
6. **Seed the register and tag confidence.** Each carried bet → `H-…` in the hypothesis register
   (new id or the reconciled existing one), statement carrying segment · status quo · job · forces ·
   moat; confidence per `process/CONVENTIONS.md` — at this point almost everything is
   `[assumption]`, and that is the point.

## Anti-patterns
- **Feature bets.** "We bet users will love feature X" — no segment, no status quo, no forces.
  Frame it on the job or drop it.
- **No status quo.** A bet that displaces nothing can't lose, so it can't be a bet.
- **Pull-only reasoning.** Claiming the win on pull alone while anxiety and habit go unnamed — the
  forces that kill adoption are exactly the ones left off the slide.
- **Moatless bets carried silently.** A bet with no defensibility behind it may still be worth
  making — but the table must say so, or the strategy looks more durable than it is.
- **Duplicate `H-` ids.** Minting a fresh hypothesis for a claim `where-to-play-how-to-win` (or a
  Step-1 tool) already seeded — the evidence splits and neither entry settles.
- **Ten bets.** A wager list nobody can be held to. Cut to 3–7; the cuts stay visible.

## Worklog & projection
Worklog: `3-strategy/bets.md` — every candidate with segment · status quo · job · forces · moat, the register reconciliation (which `H-…` each reuses or mints), the carried 3–7, every cut with its reason. Projects `{#bets}`; face: the **Lead bet** line, via [`template-fragment.md`](template-fragment.md). Primary of the `{#bets}` marker; `value-definition-strategy`'s moats reach it through the re-projected `{#value-defensibility}` and `{#how-to-win}`, never through this worklog. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#bets}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml). Each carried bet is an `H-…` in the hypothesis register; Step 5
`segment-cvp` sharpens staged bets into market-entry bundles, and `hypothesis-test-design` turns a
chosen bet into an experiment.
