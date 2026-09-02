---
node_type: card
kind: method
name: value-definition-strategy
steps: [3]
prerequisites: [the step-1 value-defensibility section, competitor-context, strategy choices (where-to-play / how-to-win)]
reads: [section:value-defensibility, worklog:1-concept/value-definition-concept, section:competitor-strategy, section:where-to-play, section:how-to-win, register:hypotheses]
writes: [worklog, section:value-defensibility, register:hypotheses]
opinionated: true
method_basis: "7 Powers (Helmer) revisited at strategy — derivative moats once customers/scale exist, moat trajectory over time; post-AI lens (software isn't the moat, position is)"
evidence_standard: derived
volume_rule: n/a
selection_rule: "the post-AI test — a value that does not survive an LLM rebuild is a feature, not a moat"
rejects_shown: required
status: draft
version: 0.2.2
updated: 2026-09-02
---
# Value & Defensibility (strategy revisit)

**Pressure-test how the product wins, now that a strategy exists** — the Step-3 revisit of the
Step-1 `{#value-defensibility}` section. Three things become possible here that were not at
concept stage: **derivative moats** (they need a customer or scale to derive from), the **moat
trajectory** (which moats compound, which erode, and in what order they are built), and the
**contribution** of the moats to `{#how-to-win}` and `{#bets}`. Updates the Step-1 section; it does
not create a second one.

> **This is an opinionated method** (a post-AI view of defensibility — see
> `value-definition-concept` for the premise and the base taxonomy). Same lens, later vantage
> point: state the lens; don't present it as the only one.

> **Relation to neighbours (one mechanism, one way).**
> - **`value-definition-concept` (Step 1)** named the base moats and killed the feature-moats.
>   This skill *extends* that work — it never re-derives the base layer from scratch; a base moat
>   that no longer holds is updated in place, with the change logged.
> - **`where-to-play-how-to-win`** owns `{#how-to-win}`; **`bets`** owns `{#bets}`. This skill is
>   the *second* tool on both markers — its contribution is worked in its own worklog and reaches
>   those sections when their primaries re-project; it never writes another method's worklog (N6).
> - **`competitor-analysis` (Step 2)** supplies the rivals the moats are tested against.

## When to apply
- **Step 3**, after where-to-play/how-to-win choices are drafted and before the bets are fixed —
  the moats are the *because* in every bet.
- From status `pmf` onward, whenever customers or scale have materially grown: derivatives that
  were out of reach may now be real.
- Whenever a "why can't this be copied" answer still points only at base moats a year in — the
  absence of any derivative forming is itself a finding.

## Prerequisites
- **The Step-1 section** — `{#value-defensibility}` and its worklog (base moats, killed
  candidates). *Missing → run `value-definition-concept` first; there is nothing to revisit.*
- **Competitor context** — to judge whether a moat is differentiated. *Missing → offer to run
  `competitor-analysis`.*
- **Strategy choices** — the arena and winning logic the moats must serve. *Missing → run
  `where-to-play-how-to-win` (this skill contributes to it in the same pass).*

## How to do it
1. **Re-test the base moats.** A year of evidence and a chosen arena change the answers: re-run the
   post-AI rebuild test on each base moat *in the chosen arena, against the known competitors*.
   Update have/building/aspiration honestly; a moat that quietly degraded stays in the table with
   its new rating, not deleted.
2. **Counter-positioning check, per competitor in `{#competitor-strategy}`.** One worklog line each:
   *what would this incumbent have to give up to copy us?* — a revenue line, a channel, a promise
   to its customers. `nothing` is the finding: the moat is a feature. Taxonomy row:
   [`moat-taxonomy.md`](../value-definition-concept/references/moat-taxonomy.md) → counter-positioning.
3. **Derive the derivatives — now that there is something to derive from.** Given each base value
   and the customers/scale that now exist: which derivative moats (lock-in/switching costs ←
   exclusive access + an existing customer; network effects ← audience; economies of scale ←
   volume) are reachable? Name the **dependency** explicitly ("lock-in *if* integration X ships and
   a customer embeds it"). A derivative claimed with no named dependency is an aspiration —
   tag it so. Taxonomy: [`moat-taxonomy.md`](../value-definition-concept/references/moat-taxonomy.md).
4. **Draw the moat trajectory.** Moats are not static: which base moat is being converted into
   which derivative, over what horizon, and what erodes meanwhile (expertise commoditizes, access
   contracts expire)? State the order of construction — the strategy leans on the moats in the
   sequence they will actually exist, not all at once.
5. **Contribute to `{#how-to-win}` and `{#bets}`.** The winning logic names the moats it leverages;
   each bet names the moat it leans on. That working stays in **this method's worklog**; the
   primaries (`where-to-play-how-to-win`, `bets`) read the re-projected `{#value-defensibility}`
   and pick the moats up when they re-project — the first tool in a `<!-- tool: A, B -->` marker
   owns the section's thread, each named tool owns its own file
   (`process/reference/worklog-resolution.md`).
6. **Keep the kills current.** Candidates the rebuild test kills at this pass — including
   derivatives that turned out to have no dependency path — join the rejected table with reasons.
7. **Update the Step-1 section — and say what that costs.** Project the revised picture back into
   `{#value-defensibility}`. **Re-projection drops the section's `confirmed:` marker**
   (`process/CONVENTIONS.md` → *Section confirmation*): the revised moat story is a new thesis the
   human has not signed — walk it back through confirmation rather than leaving a stale sign-off.
8. **Seed hypotheses.** Each newly claimed derivative and each dependency → `H-…` (e.g. "customers
   will accept the switching cost of integration X"); reconcile with existing moat hypotheses
   rather than minting duplicates.

## Anti-patterns
- **Re-deriving the base layer.** Rebuilding the Step-1 analysis from scratch instead of updating
  it — the killed-candidates history is the part you lose.
- **Derivative without a dependency.** "We'll have network effects" with no named base moat,
  customer, or threshold it derives from.
- **A static moat story.** A table with no trajectory — moats presented as possessions rather than
  positions that compound or erode.
- **Incumbents who lose nothing.** Every counter-positioning line reads "nothing" and the moat
  story stands unchanged — that line was the verdict.
- **A second value section.** Writing a Step-3 defensibility section beside the Step-1 one. One
  moat story, one section; the revisit updates it in place.
- **Silent re-projection.** Updating the Step-1 section and leaving its old `confirmed:` marker
  standing — a signed-off thesis that no longer says what was signed.

## Worklog & projection
Worklog: `3-strategy/value-definition-strategy.md` — a **revisit** in its own step's folder: the re-tested base moats, one counter-positioning line per competitor, the derivatives with their dependencies, the trajectory, the new kills, a dated change-log entry; the Step-1 working is a declared read (`worklog:1-concept/value-definition-concept`), never written. Re-projects `{#value-defensibility}` (which drops the section's `confirmed:` marker); face: the **Moat read** line — the same slot as `value-definition-concept`, via [`template-fragment.md`](template-fragment.md). Named second on `{#how-to-win}`: that contribution is worked here and reaches the section when `where-to-play-how-to-win` re-projects. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Re-projects the Step-1 `{#value-defensibility}` via [`template-fragment.md`](template-fragment.md)
(the update drops the section's `confirmed:` marker — it awaits re-confirmation); contributes moats
to `{#how-to-win}` / `{#bets}` through their primary methods' re-projection. Inputs via
[`questions.yaml`](questions.yaml); each unproven derivative/dependency seeds `H-…`. Deeper notes:
[`moat-taxonomy.md`](../value-definition-concept/references/moat-taxonomy.md).
