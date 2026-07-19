---
name: architecture-c4
kind: method
produces: architecture
reads_registers: []
writes_registers: [risks]
inputs: [interview, kb, git]
prerequisites: [product-concept]
used_by_steps: [3, 4]
opinionated: false
method_basis: "C4 model — Context level (Simon Brown)"
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Architecture (C4 Context)

Sketch the product's architecture at **C4 Context level** — the system, its users, and the
external systems it depends on. Fills `{#architecture}` (sketched at Step 3, refined at Step 4).
At the product-loops altitude we deliberately stay at Context level, not Container/Component —
enough to reason about integrations, dependencies, and cost, not to design the build.

**Method basis.** The C4 model (Simon Brown), Context diagram only.

## When to apply
- Step 3 — a context sketch informs moats (integrations are a moat), channels, and risk.
- Step 4 — refined; external systems become **infra cost lines** and **dependency risks**.

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

## Output
Fills `{#architecture}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
