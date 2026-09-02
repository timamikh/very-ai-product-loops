---
node_type: card
kind: method
name: concept-formation
steps: [1]
prerequisites: [raw-idea]
reads: [register:hypotheses, source:interview, source:kb]
writes: [worklog, section:idea, register:hypotheses]
opinionated: false
method_basis: "April Dunford positioning ('the shift') + problem→solution articulation"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.4.2
updated: 2026-09-02
---
# Concept Formation

Turn a raw idea into a crisp product **concept** and the **shift** it makes. Fills `{#idea}`.
A good concept is a sentence a stranger repeats correctly — not a feature list. The
problem-by-problem solution mapping is a separate pass with its own prerequisites —
[`concept-expansion`](../concept-expansion/SKILL.md), after `{#problems}` exist.

**Method basis.** April Dunford-style positioning (define the product by the *shift* it creates
versus the current alternative, not by its features) + explicit problem→solution articulation.

## When to apply

- Step 1, first thing — everything downstream leans on a clear concept.
- Whenever the concept has drifted or a pivot is on the table.

## Prerequisites

- **Raw idea** — the founder's/PO's description, however rough: a filed pitch or notes (`source:kb`),
  a founder conversation returned as notes (`source:interview`). *Missing → interview to elicit it.*

## How to do it

1. **One-line concept.** "<Product> is a <category> that <does the core thing> for <who>." Keep
   it to a sentence; if it needs a paragraph, it isn't sharp yet.
2. **Name the shift.** What does the world do *today* (the current alternative, incl. "do
   nothing / do it manually"), and what does this product make possible instead? The shift is
   the concept's spine.
3. **Riskiest assumption.** State the single belief the concept most depends on — the thing
   that, if false, sinks it. Seed it as a hypothesis (`H-…`). Beside it, pre-register one **kill
   sentence** in the worklog: `we drop/pivot the concept if we observe …` — an observation, not a
   feeling. At `concept-viability` this is the center of gravity.
4. **Sketch the solution stub** — 2–4 lines on *how* it delivers the shift, kept in the worklog;
   `concept-expansion` reads it there as its **declared** worklog input
   (`worklog:1-concept/concept-formation` in that card's `reads`). Do not design features here; the
   problem→solution mapping runs downstream of `{#problems}`.
5. **Tag confidence.** The concept is usually a `[sourced: PO decision]`; the shift and the
   assumption are `[assumption]` until evidenced.

## Anti-patterns

- **Feature soup.** A list of capabilities instead of one repeatable sentence.
- **No alternative.** Describing the product without naming what it replaces — no shift, no edge.
- **Hiding the bet.** Not stating the riskiest assumption, so it never gets tested.
- **Unobservable kill sentence.** "…if it doesn't work out" — nothing anyone could see and act on.

## Worklog & projection
Worklog: `1-concept/concept-formation.md` — the one-line concept, the shift versus the current alternative, the riskiest assumption with its kill sentence, the solution stub (`concept-expansion` reads it as a declared worklog input). Projects `{#idea}`; face: the concept sentence, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output

Projects `{#idea}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml).
