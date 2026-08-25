---
node_type: card
kind: method
name: concept-formation
steps: [1]
prerequisites: [raw-idea]
reads: [register:hypotheses, register:metrics, source:interview, source:kb]
writes: [worklog, section:idea, register:hypotheses]
opinionated: false
method_basis: "April Dunford positioning ('the shift') + problem→solution articulation"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.4.0
updated: 2026-08-25
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

- **Raw idea** — the founder's/PO's description, however rough. *Missing → interview to elicit it.*

## How to do it

1. **One-line concept.** "<Product> is a <category> that <does the core thing> for <who>." Keep
   it to a sentence; if it needs a paragraph, it isn't sharp yet.
2. **Name the shift.** What does the world do *today* (the current alternative, incl. "do
   nothing / do it manually"), and what does this product make possible instead? The shift is
   the concept's spine.
3. **Riskiest assumption.** State the single belief the concept most depends on — the thing
   that, if false, sinks it. Seed it as a hypothesis (`H-…`). At `concept-viability` this is the
   center of gravity.
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

## Worklog & projection

The working is done in the step's **worklog** `<step-folder>/concept-formation.md`
(`node_type: worklog`, e.g. `1-concept/concept-formation.md`): the one-line concept sentence, the
**shift** it names versus the current alternative, the riskiest assumption the concept depends on,
and the solution stub. That worklog is the **source of truth**; the artifact section `{#idea}` is its
**projection** into the fixed shape of [`template-fragment.md`](template-fragment.md), holding nothing
the worklog does not, and the step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External inputs arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output

Projects `{#idea}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml).
