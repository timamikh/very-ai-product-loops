---
node_type: card
kind: output
name: feature-to-spec
output_kind: authored
prerequisites: [a spec-ready groomed feature (its feature-grooming block, zero open product forks), the feature's register row (`F-…`) and links (`H-…` / `M-…`)]
reads: [worklog:6-sprint-plan/feature-grooming, worklog:6-sprint-plan/feature-spec, register:features, register:hypotheses, register:metrics, source:kb]
writes: [file:export-files/<feature>-spec.md]
surfaces: [file:export-files/*]
formats: [md]
opinionated: true
method_basis: "Development instruction from a groomed feature — scope-faithful, WHAT-not-HOW, product decisions arrive fixed, only technical forks stay open; BRD/PRD by default, tech spec for engine-internal features"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.0
updated: 2026-08-21
---
# Feature → Spec (development instruction)

Author the **`.md` instruction a development team implements from** — one file per groomed
feature, at `product-loops/export-files/<feature>-spec.md` (`node_type: deliverable`). This is the
step past the framework's feature altitude: [`feature-spec`](../../library/feature-spec/SKILL.md)
describes the item, [`feature-grooming`](../../library/feature-grooming/SKILL.md) closes its
product forks, **this card writes what the developer opens**. The document must be **faithful to
the groomed scope, compact, and hand no product decision to the developer**.

**Authored, not rendered.** An edit to a spec is an edit — the file is the source of truth once it
leaves, signed and carrying its own dated change log. `to-document` may re-format it without
becoming its home.

## Principles (each is a line in the quality checklist below)
1. **Product decisions are the product owner's — and they are already made.** The groom closed
   them; they enter this document as **fixed requirements** (mark them "agreed with the product
   owner"), never as options. Meeting an *open* product fork while writing is a **stop**: return it
   to `feature-grooming`, do not write around it. Only **technical forks** stay open in the
   document, addressed to the tech lead.
2. **Scope fidelity.** Every in-scope line maps to a groom scope item, one-to-one. Nothing "from
   yourself" — an idea the writing surfaced is a product question or out of scope, never a quiet
   requirement.
3. **WHAT, not HOW.** A requirement states behaviour and result ("works without an app release"),
   not mechanism ("via server + API"). A mechanism the groom never set, if it matters, is a
   technical fork — not a requirement.
4. **No hard names.** Event, field, status, endpoint and interface names are *recommendations with
   examples*, under a standing disclaimer that the codebase's existing entities win. Acceptance
   criteria test for the **presence of data by meaning**, never for a specific name.
5. **Compact.** Business context is 2–4 lines, not a strategy retelling. The weight sits on scope,
   requirements and acceptance criteria. A spec noticeably longer than its groom is carrying
   something it shouldn't.
6. **Instance facts, not invented facts.** Product context comes from the instance — the product
   surface (`3#product-surface`), the value definition, plans/pricing where the artifacts hold
   them, `sources/`. It is read for *compatibility* (don't contradict the product), never as
   licence to add features.

## How to author it
1. **Pick the shape from the groom's doc type.** **BRD/PRD** (default — product behaviour;
   audience: product + development) or **tech spec** (engine-internal; audience: engineer/AI
   agent) — both skeletons are in [`template-fragment.md`](template-fragment.md). Both for a large
   feature: BRD first, tech spec follows it.
2. **Verify readiness.** The groom block says *spec-ready*. If it doesn't — stop; the missing
   product fork goes back to `feature-grooming`. This card never asks the product owner directly:
   the interview lives in the groom.
3. **Write from the groom, block by block.** Scope in/out from the groom's 1:1 items (out-of-scope
   names why); one FR block per scope item, each with Given/When/Then acceptance criteria covering
   happy path, boundaries, errors, empty states and irreversible actions; the owner's decisions as
   fixed requirements; the groom's technical forks verbatim in the forks section (context ·
   options · criterion · default · owner: tech lead).
4. **Analytics by meaning** (only if it was in scope): what is tracked and for which metric/decision
   (`M-…`), proposed names in parentheses under the naming disclaimer.
5. **Run the quality checklist** (below), then the **developer pass**: re-read the finished
   document as its implementer, with no context beyond the file. Every question that surfaces is
   either already a fork with an owner — or a defect: a product-shaped one goes back to
   `feature-grooming`, a technical one becomes a fork. The classic failures the checklist exists
   to catch: a product decision left to the developer · a spec written past an open product fork ·
   a requirement not traceable to the groom · a prescribed mechanism · a hard name · a requirement
   with no acceptance criterion · a criterion with nothing to check it against.
6. **Deliver and log.** Save to `product-loops/export-files/`, add the deliverable's own dated
   change-log entry, and note the handoff in `{#delivery}` (file name per feature). Tell the human
   which product decisions the document fixes and which technical forks remain for the tech lead.

## The technical fork, in the document
```
### Fork: <name>
- Context: what the groom left unset, and what it affects.
- Option A / Option B: pros / cons.
- Selection criterion: what decides it.
- Recommended default: A/B — why.
- Owner: tech lead.
```

## Quality checklist — run before delivering
- [ ] No product/UX/business decision is left to the developer — in a fork, an assumption or an
      open question. Open items are technical only, owner: tech lead.
- [ ] Every in-scope line traces to a groom scope item; nothing added "from yourself".
- [ ] Requirements state behaviour/result, not mechanism; a mechanism the groom never set is a
      fork, not a requirement.
- [ ] Every concrete name (event, field, status, endpoint) is a recommendation with the
      codebase-wins disclaimer; analytics acceptance tests data-by-meaning, not names.
- [ ] Every functional requirement carries Given/When/Then criteria; they cover happy path,
      boundaries, errors, empty states, irreversible actions.
- [ ] Consequential unset choices are forks (options · criterion · default · owner), not silent
      `[assumption]` marks; only small, reversible defaults may be assumptions — and are marked.
- [ ] No invented product facts: everything traces to the groom, the instance's artifacts, or
      `sources/` — or is explicitly marked.
- [ ] Every criterion has something to check it against: the inputs it needs (token sets,
      definitions, example sets) exist or carry the groom's owner + due; every check target is
      concrete (which product, which version/build), never "current".
- [ ] Every normative clause of an FR is exercised by at least one criterion — a "colour, type
      and spacing" requirement with colour-and-type criteria silently drops a clause.
- [ ] No two fixed decisions collide: walk every pair that constrains the same behaviour (a size
      cap vs "nothing is dropped") and state which wins on collision — or return the pair to the
      groom.
- [ ] No criterion presupposes behaviour a requirement only permits ("may map to a chart" + a
      criterion that assumes the chart exists): make the requirement mandatory or fix the
      criterion.
- [ ] Every criterion is decidable: two honest testers reach the same verdict. "Represented",
      "appropriate", "reasonable" without a stated rule is water — replace with the rule
      (what is counted, measured when, retries in or out).
- [ ] The developer pass ran clean: read as the implementer with nothing but the file, no
      surfaced question is product-shaped and every technical one is a fork with an owner.
- [ ] The business context is 2–4 lines; no section the feature doesn't touch.

## Anti-patterns
- **The spec as a strategy essay.** Long value sections a developer doesn't need — the links
  (`H-…` / `M-…`) carry the why.
- **Water instead of a requirement.** "Fast/convenient" → a checkable value, or a technical fork
  with an owner.
- **Irreversibility ignored.** Deletion or overwrite with no safe default and no confirmation
  named in the criteria.
- **The regenerated deliverable.** Re-authoring the file from the instance after the team edited
  it — it is `authored`: the file is the source; changes go through its change log.
