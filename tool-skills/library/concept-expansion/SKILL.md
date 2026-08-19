---
node_type: card
kind: method
name: concept-expansion
steps: [1]
prerequisites: [concept, ranked-problems]
reads: [source:interview, source:kb, worklog:1-concept/concept-formation]
writes: [worklog, section:solution, register:hypotheses]
opinionated: false
method_basis: "problem→solution mapping — every ranked pain gets its mechanism; no orphan features"
evidence_standard: decision
volume_rule: "one row per ranked problem carried from {#problems} — every tier-1 pain covered"
selection_rule: "a feature that answers no ranked problem is an orphan — dropped to the reject table, not kept"
rejects_shown: required
status: draft
version: 0.2.0
updated: 2026-08-19
---
# Concept Expansion

Expand the concept into a **problem→solution mapping**: for each ranked problem, *how* the product
solves it. Fills `{#solution}`. This is the second pass over the concept — [`concept-formation`](../concept-formation/SKILL.md)
states *what* the product is and the shift it makes; this method states *how* it delivers, problem
by problem, once `{#problems}` exist. No orphan features: a capability that answers no ranked pain
does not belong in the concept.

**Method basis.** Explicit problem→solution articulation: the mapping runs **from the pains, not
from the feature list** — each tier-1 pain gets a named mechanism, and each proposed capability
must point back at a pain or be rejected as an orphan.

## When to apply

- Step 1, after `{#problems}` — the mapping needs ranked pains to map against.
- Whenever the problem ranking changes (a new tier-1 pain, a demoted one) — the mapping is re-read
  against the new ranking, and mechanisms that lost their pain become orphans.

## Prerequisites

- **The concept** — the one-liner, the shift, and the solution stub from `concept-formation`'s
  worklog — a **declared** worklog input (`worklog:1-concept/concept-formation` in this card's
  `reads`; OPERATING-LOOP move 2). *Missing → run `concept-formation`.*
- **Ranked problems** — `{#problems}` with tiers, from `segment-pains`. *Missing → run
  `segment-pains`; mapping against unranked pains produces feature soup.*

## How to do it

1. **Carry the ranked problems over.** One row per problem from `{#problems}`, tier-1 first, in
   ranking order. A tier-1 pain with no row is a hole, not an editorial choice.
2. **Name the mechanism, not the feature.** For each problem: *how* the product removes it — the
   mechanism a stranger could paraphrase ("matches X against Y so Z never happens"), not a feature
   label ("smart matching"). The solution stub from `concept-formation` seeds this; the pains
   discipline it.
3. **Run the orphan check.** Any capability in the stub / backlog / founder's head that maps to no
   ranked problem goes to the reject table with the reason (`no ranked pain`, `tier-3 only`,
   `duplicate mechanism`). Orphans are dropped from the concept, not silently kept.
4. **Surface the feasibility bets.** A mechanism the team has not built before, or one that leans
   on unproven tech, is an `[assumption]` — seed it as `H-…` (`type: feasibility`) so the build
   risk is testable, not asserted.
5. **Tag confidence.** Each mapping row is a design decision (`[sourced: PO decision]`) or an
   `[assumption]`; nothing in this section is evidence about the market.

## Anti-patterns

- **Feature soup.** Mapping features to features — rows that name capabilities on both sides, with
  no pain anywhere.
- **Orphan features kept "for later".** If it answers no ranked pain, it leaves the concept; "later"
  is a re-run of this method after the ranking changes.
- **One mechanism, every pain.** The same mechanism pasted against each problem — that's a slogan,
  not a mapping; say what specifically removes *this* pain.
- **Silent feasibility.** A hard mechanism presented with the same confidence as a trivial one — the
  build bet stays hidden and never gets tested.

## Worklog & projection

The working is done in the step's **worklog** `<step-folder>/concept-expansion.md`
(`node_type: worklog`, e.g. `1-concept/concept-expansion.md`): the carried problem ranking, the
mechanism per pain with its feasibility read, the orphan table with reasons, and the seeded `H-…`.
That worklog is the **source of truth**; the artifact section `{#solution}` is its **projection**
into the fixed shape of [`template-fragment.md`](template-fragment.md), holding nothing the worklog
does not, and the step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External inputs arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output

Projects `{#solution}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml).
