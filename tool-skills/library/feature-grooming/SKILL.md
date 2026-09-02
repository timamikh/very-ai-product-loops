---
node_type: card
kind: method
name: feature-grooming
steps: [6]
prerequisites: [featured development items exist (feature-spec rows in `{#must}` / `{#backlog}`)]
reads: [worklog:6-sprint-plan/feature-spec, section:product-surface, section:value-defensibility, register:hypotheses, register:metrics, register:features, source:kb]
writes: [worklog, section:must, section:backlog]
opinionated: true
method_basis: "Grooming to spec-readiness — every product/UX/business fork is closed by the product owner BEFORE a spec is written; technical forks are recorded for the tech lead; WHAT-not-HOW discipline"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.1
updated: 2026-09-02
---
# Feature Grooming (spec-readiness)

Take a **featured development item** (a `feature-spec` row) and close the gap between *described*
and *specifiable*: enumerate the scope one-to-one, surface every fork the description left open,
put the **product forks to the product owner**, and record the **technical forks for the tech
lead**. The output is a groomed feature that [`feature-to-spec`](../../outputs/feature-to-spec/SKILL.md)
can turn into a development instruction without inventing anything.

**Method basis.** The grooming discipline: product decisions are made by the product owner, not
defaulted by whoever writes (or reads) the spec. A gap is one of two kinds, and the whole method is
telling them apart.

**Opinionated: yes.** This card holds that an unasked product question does not disappear — it gets
answered silently by a developer at implementation time, which is the worst person and the worst
moment for it. Hence the hard rule: **no spec while a product fork is open.**

## When to apply
- Step 6, after `feature-spec` / `prioritization-sprint-plan`, for every development item that will
  be handed to the team as a written instruction.
- Skip it only for items the team grooms in its own downstream process — then the framework's
  handoff stays at feature altitude (`{#delivery}` says so).

## Prerequisites
- **Featured items** — the `feature-spec` blocks in `{#must}` / `{#backlog}` with their `H-…` /
  `M-…` links. *Missing → run `feature-spec` first.*

## The two kinds of gap — the core distinction
- **Product / UX / business** — scope boundaries (in/out), who may do what, tier/plan access,
  monetization, price or cost to the user, visible behaviour and UX forks, what counts as
  success, content policy, priorities, the fate of user data on destructive actions.
  **These are the product owner's decisions. Ask them now** — 2–4 options each, one marked as the
  recommended default, grouped so the human answers in one sitting ([`questions.yaml`](questions.yaml)).
  Never leave one as a silent assumption or an "open question" in a document.
- **Technical / implementation** — storage, delivery, contracts, formats, infrastructure,
  performance. **These are the development team's decisions.** Do not ask the product owner;
  record each as a technical fork (context · options · selection criterion · recommended default ·
  owner: tech lead) for the spec to carry.
- **Mixed** — split it: the user-visible half is a product question (ask), the internal mechanism
  is a technical fork (record). "What wins when style and user request conflict" is product; "how
  parameters merge internally" is technical.

## How to do it
1. **Enumerate the scope one-to-one.** Each scope bullet of the feature becomes one numbered groom
   item. Nothing added, nothing dropped — additions the grooming itself suggests are new *forks*,
   not new scope.
2. **Sweep for forks — the dimension list, then the text.** Walk the scope against the instance —
   the product surface (`3#product-surface`), the value definition, the registers — and list every
   open fork. Then walk the **dimension list**; the dry-run failure mode is a dimension nobody
   thought to ask, not a fork half-asked. Mark each *asked* or *n/a* — a silent skip is the defect
   the list exists for:
   - **surface** — where the user meets the feature (which UI · API · none). Any user-visible
     behaviour ("the user sees an error") implies one;
   - **told or silent** — for every ignored, blocked or overridden user action: is the user
     notified, or is it silent;
   - **media & content types** — images, files, fonts, embedded data: in or out of scope;
   - **cardinality** — "one or many" for every entity the feature touches (themes, templates,
     formats, accounts);
   - **inputs the developer can't produce** — token sets, definitions, example/test sets, copy:
     each named, with an owner and a due (one already filed in `sources/` is `source:kb`). An
     unowned input blocks readiness;
   - **check targets** — what "works in X" means concretely (which product, which version/build).
     The *target* is the PO's decision; the *verification method* is the tech lead's;
   - **trigger boundaries** — every behaviour keyed on a classification ("a styling request",
     "numeric data") needs the line drawn: what falls in, what falls out — and every threshold
     needs its counting rule (what counts toward it · measured when · are retries in). An undrawn
     line is redrawn by each implementer; a ruled number with an unruled count is still a fork;
   - **out-of-scope encounters** — input will ask for what scope excludes ("insert our logo" when
     images are out): what the user sees then — silently omitted, told, or refused — is a product
     decision, and "out of scope" alone doesn't make it.
   Classify each fork: product · technical · mixed (split). Finally, one pass per scope item:
   *could two implementers build this differently in a way that changes behaviour or cost?* An
   uncovered "yes" is a fork — the biggest unknown is usually the mechanism everyone assumed
   (record it, owner: tech lead).
3. **Close the product forks with the human.** Ask them grouped, each with 2–4 options and a
   recommended default. Record every decision as a dated decision line in the worklog. A fork the
   owner explicitly defers is recorded as **deferred** — and the feature is *not spec-ready* until
   it is closed or scoped out.
4. **Record the technical forks.** Same structure, owner "tech lead", left open on purpose — they
   travel into the spec's fork section.
5. **Pick the document type** the spec will take: **BRD/PRD** (product behaviour; the default) ·
   **tech spec** (engine-internal, audience is an engineer/AI agent) · both for a large feature.
6. **Declare readiness.** A feature is **spec-ready** when: scope enumerated 1:1 · zero open
   product forks · technical forks recorded · every named input owned · doc type picked. Mark it
   so in the worklog and
   annotate the feature's block in `{#must}` / `{#backlog}` (this card is named on those sections'
   markers after `feature-spec`).

## Anti-patterns
- **Spec ahead of questions.** A document written while a product fork was open — the fork did not
  vanish; a developer inherited it.
- **The owner interrogated about plumbing.** Asking the product owner to choose storage or
  contracts — technical forks are not their decisions; recording them is enough.
- **Scope creep in grooming.** A groom item with no parent scope bullet. Grooming clarifies scope;
  it never extends it.
- **The silent big assumption.** A consequential choice hidden as a low-risk default instead of
  asked. Small and reversible may default (marked); consequential is asked.
- **Deferred means done.** Treating a deferred fork as closed. Deferred blocks readiness.

## Worklog & projection
Worklog: `6-sprint-plan/feature-grooming.md` — one groom block per feature (the fragment is this worklog's shape): the scope 1:1, the forks by kind, the owner's decisions dated, the technical forks, the doc type, the readiness line. Projects only the **Groom** line of the feature's block in `{#must}` / `{#backlog}` (named after `feature-spec` on those markers); no card slot, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
A groomed, spec-ready feature per block. Hands off to
[`outputs/feature-to-spec`](../../outputs/feature-to-spec/SKILL.md), which authors the development
instruction; decisions closed here enter that document as **fixed requirements**, never re-asked.
