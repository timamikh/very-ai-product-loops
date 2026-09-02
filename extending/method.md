---
node_type: extending
title: Add or change a method — a library card that fills a section
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Add or change a method

*Read this when a product needs a way of working the shipped library does not have, or shipped one it
does differently. The dial table is in* [`../EXTENDING.md`](../EXTENDING.md); *the card's anatomy is in*
[`../tool-skills/library/README.md`](../tool-skills/library/README.md) → *Anatomy of a tool*.

A **method** is the card that fills one **section** of a step artifact. That is the whole test of
whether this is the dial you want.

## Is this the right dial

| What you actually want | The dial |
|---|---|
| a way of working that produces content an artifact section holds | **this file** |
| something that happens between passes, tied to no step and no section | [`operation.md`](operation.md) |
| a file that leaves the framework in a human's hands | [`output.md`](output.md) |
| the same section worked differently at a different stage | [`status.md`](status.md) — a status's `per_step.tools` picks the method; two stages can call different ones for one section |
| a section the artifacts do not have at all | [`section.md`](section.md) **first**, then this file — a method with no home is the one thing the linter refuses (check B) |
| a repeatable pull or push across the instance boundary | [`../process/reference/boundary-layout.md`](../process/reference/boundary-layout.md) — an exchange card, routed by trigger |

## Where it lives — the law of two homes

| Whose method | Its folder | What happens on a framework update |
|---|---|---|
| **your product's own** | `product-loops/tool-skills/library/<name>/` | untouched — it is not part of the vendored tree |
| **the framework's** | `tool-skills/library/<name>/` | overwritten by re-vendoring |

A **local card of the same name wins**: that is how a company specializes a shipped method without
forking anything. Copy the vendored card as the starting point, keep the name, change the body.

A local card is a normal card — same frontmatter wiring, same three files, checked by the linter
exactly like a vendored one, so a local method cannot quietly produce a homeless section.

## Procedure

1. **Cut it at the right seam** before writing a line — the four gates below decide the name and the
   count of cards, and a method cut wrong has to be recut later with its worklogs already written.
2. **Create the folder** in the home the table above gives you.
3. **Write `SKILL.md`** — what · when · how · anti-patterns — plus the frontmatter wiring
   ([`../process/reference/card-schema.md`](../process/reference/card-schema.md)). A method carries
   `steps` and **no** `surfaces`: it is reached from inside a pass through its section's marker, never
   routed to (the law of ranks).
4. **Write `template-fragment.md`** — the shape of the draft the method works in. Not the clean copy's
   form: the fragment may hold a wider table or more detail, and the orchestrator adapts it into the
   section by meaning. So it carries **no column keys**
   ([`../process/reference/column-keys.md`](../process/reference/column-keys.md)) — with one named
   exception, the decision line, whose fields the framework fixes and the method copies verbatim.
5. **Write `questions.yaml`** — what the method must ask a human, and nothing it could read from an
   artifact instead. Every question carries a `type` from the closed vocabulary — `free_text` ·
   `list` · `per_item` · `single_select` · `multi_select` (the machine home is `lint.QUESTION_TYPES`,
   check Y); a select names its `options: [...]` or `from: <question-id>` on its own line, never
   inside the `type` scalar.
6. **Give its output a home.** The step template must carry `<!-- tool: <name> -->` on the section it
   fills (`section.md` if that section does not exist yet). A method that contributes to a section it
   does not own is named **second** in that section's marker (`<!-- tool: A, B -->`) and is recommended
   by no status.
7. **Add the index row** — [`../tool-skills/library/README.md`](../tool-skills/library/README.md) →
   *Index*, plus the at-a-glance row in
   [`../tool-skills/README.md`](../tool-skills/README.md). Framework cards only; a local card is
   discovered from its folder.
8. **Recommend it, if a stage should reach for it** — the status's `per_step.tools`
   ([`status.md`](status.md)). Optional: the human may call any method directly.
9. **Run the linter to zero**, then record the history where the file lives — a framework card takes a
   `version` bump and a `CHANGELOG.md` line; a local card carries its own dated change log.

## The four gates

Each was learned from a real failure, and each holds for a donated method and a local one alike.

- **One skill, one step, one operation** (check U). A method declares exactly one step. A method that
  would do *different* operations on different steps is two cards with two names
  (`hypothesis-thresholds` at 4 vs `hypothesis-test-design` at 5); the *same* operation revisited at
  another step is a per-step variant named for its step (`jtbd-concept`, `cjm-strategy`). This holds
  **within** a step too: a second pass with its own prerequisites is a second card
  (`concept-formation` states the concept; `concept-expansion` maps problems→solutions after
  `{#problems}` exists). And a card filling several sections must be doing *one* operation across them
  — `competitor-analysis` (players + the game each plays) was recut from the pricing scan
  (`competitor-pricing`) and the trend read (`competitor-dynamics`) exactly there.
- **A home for every recommendation** (check V). If a status recommends it at step *n*, the step-*n*
  template carries its marker — otherwise the agent is told to use a method with nowhere to put the
  result, and it will invent a section.
- **One owner per definition.** A scale, an enum or a gate the library already defines lives in exactly
  one card. Grep for it and point at the owner instead of restating it — drifted duplicates are how two
  "identical" 1/3/5 scales end up with different criteria.
- **Jurisdiction- and vendor-neutral** — upstream only. A region-specific registry, a data vendor or a
  legal-id scheme belongs in a local card or a company adapter, never in a base method.

## Checklist

- [ ] The section it fills exists and names it in a `<!-- tool: … -->` marker.
- [ ] It does **one** operation at **one** step — and if you hesitated, you wrote down which seam you
      cut on.
- [ ] Every scale, enum and gate it uses is either its own or pointed at by name.
- [ ] `questions.yaml` asks only what no artifact already answers.
- [ ] The card says out loud what school of thought it follows, if it follows one.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] History recorded where the file lives.

## Contributing it upstream

A method good enough to ship travels through [`../CONTRIBUTING.md`](../CONTRIBUTING.md). Two things
change: it must clear the neutrality gate above, and it must be **opinion-explicit** — if it applies a
particular school of thought (a post-AI view of defensibility, say), `SKILL.md` says so. That is exactly
why methods live in a pluggable library and not in the neutral core: another company can then supply
its own without arguing with yours.
