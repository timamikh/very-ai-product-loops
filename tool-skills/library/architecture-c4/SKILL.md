---
node_type: card
kind: method
name: architecture-c4
steps: [3]
prerequisites: [product-concept]
reads: [section:idea, section:solution, register:risks, source:kb, source:git]
writes: [worklog, section:architecture, register:risks]
opinionated: false
method_basis: "C4 model — Context level (Simon Brown)"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.3.1
updated: 2026-09-02
---
# Architecture (C4 Context)

Sketch the product's architecture at **C4 Context level** — the system, its users, and the
external systems it depends on. Fills `{#architecture}` at Step 3.
At the product-loops altitude we deliberately stay at Context level, not Container/Component —
enough to reason about integrations, dependencies, and cost, not to design the build.

**Method basis.** The C4 model (Simon Brown), Context diagram only.

## When to apply
- Step 3 — a context sketch informs moats (integrations are a moat), channels, and risk.
- Step-4 refinement into the instrumentation map: see `instrumentation-plan` (Step 4).

## Prerequisites
- **Product concept.** *Missing → run `concept-formation`.*

## How to do it
1. **The system** — one box: the product.
2. **Actors** — who uses it (map to segments).
3. **External systems** — what it integrates with or depends on (auth, payments, LLM providers,
   analytics, email, data sources). Each is a potential cost, dependency, and moat/lock-in. For an
   existing system read them from architecture docs (`source:kb`) or the codebase passport
   (`source:git`).
4. **Relationships** — who talks to what, and why.
5. **Feed downstream** — external LLM/infra → Step-4 COGS; critical dependencies → `R-…` risks;
   exclusive integrations → a moat in `value-definition`.

Express as a simple list or a Mermaid diagram — keep it Context-level.

## Anti-patterns
- **Over-designing.** Dropping into Container/Component detail — that's engineering's job, later.
- **Hiding dependencies.** Omitting the external systems that carry cost and risk.

## Worklog & projection
Worklog: `3-strategy/architecture-c4.md` — the system, the actors mapped to segments, the external systems, the relationships, the downstream feeds (COGS · `R-…` · moat). Projects `{#architecture}`; face: the **Context read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#architecture}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml); critical dependencies seed `R-…` risks.
