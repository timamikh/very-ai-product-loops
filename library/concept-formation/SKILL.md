---
name: concept-formation
kind: method
produces: concept
reads_registers: []
writes_registers: [hypotheses]
inputs: [interview, kb]
prerequisites: [raw-idea]
used_by_steps: [1]
opinionated: false
method_basis: "April Dunford positioning ('the shift') + problem→solution articulation"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Concept Formation

Turn a raw idea into a crisp product **concept** and the **shift** it makes. Fills `{#concept}`
(and seeds `{#solution}`). A good concept is a sentence a stranger repeats correctly — not a
feature list.

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
4. **Sketch the solution stub** — 2–4 lines on *how* it delivers the shift, to seed `{#solution}`.
   Do not design features here; that's later and downstream of problems.
5. **Tag confidence.** The concept is usually a `[sourced: PO decision]`; the shift and the
   assumption are `[assumption]` until evidenced.

## Anti-patterns

- **Feature soup.** A list of capabilities instead of one repeatable sentence.
- **No alternative.** Describing the product without naming what it replaces — no shift, no edge.
- **Hiding the bet.** Not stating the riskiest assumption, so it never gets tested.

## Output

Fills `{#concept}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
