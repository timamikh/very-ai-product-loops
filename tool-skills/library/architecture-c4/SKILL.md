---
node_type: card
kind: method
name: architecture-c4
steps: [3]
prerequisites: [product-concept]
reads: [source:interview, source:kb, source:git]
writes: [worklog, section:architecture, register:risks]
opinionated: false
method_basis: "C4 model — Context level (Simon Brown)"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.0
updated: 2026-08-16
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
   analytics, email, data sources). Each is a potential cost, dependency, and moat/lock-in.
4. **Relationships** — who talks to what, and why.
5. **Feed downstream** — external LLM/infra → Step-4 COGS; critical dependencies → `R-…` risks;
   exclusive integrations → a moat in `value-definition`.

Express as a simple list or a Mermaid diagram — keep it Context-level.

## Anti-patterns
- **Over-designing.** Dropping into Container/Component detail — that's engineering's job, later.
- **Hiding dependencies.** Omitting the external systems that carry cost and risk.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/architecture-c4.md`
(`node_type: worklog`): the C4 Context sketch — the system box, the actors mapped to segments, the
external systems it integrates with or depends on, the relationships between them, and the downstream
feeds (external LLM/infra → Step-4 COGS, critical dependencies → `R-…` risks, exclusive integrations
→ a moat). That worklog is the **source of truth**; the artifact section `{#architecture}` is its
**projection** into the fixed shape of [`template-fragment.md`](template-fragment.md) — it holds
nothing the worklog does not, and the step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#architecture}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml); critical dependencies seed `R-…` risks.
