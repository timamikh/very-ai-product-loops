---
node_type: reference
title: process/reference — canon read on demand, not every pass
status: draft
version: 0.2.0
updated: 2026-08-18
---

# process/reference

These files are **canon**, but they are **not** part of the always-loaded reading order in
[`AGENTS.md`](../../AGENTS.md). Each is read at a **named moment** — when you are about to do the
one thing it governs — so the per-pass `process/` files stay lean. `REGISTERS.md` follows the same
pattern from the core: read at loop steps 3 (register rows as inputs) and 7 (before writing rows).

The split follows [`CONVENTIONS.md`](../CONVENTIONS.md) → *Where a new rule goes* (now in
[`EXTENDING.md`](../../EXTENDING.md)): a contract two readers must agree on lives in `process/`; a
lookup or an authoring rule that only one task ever needs lives here and is pointed at from the
stub that stays in the core.

| File | Read it when |
|------|--------------|
| [`GLOSSARY.md`](GLOSSARY.md) | a term is unclear, or onboarding — the entity **vocabulary** (a map of names to where each is actually defined; not a second definition home) |
| [`column-keys.md`](column-keys.md) | authoring or editing a **step template** or a **register** — deciding whether a table column carries a `<!--c:key-->` and where its key lives |
| [`config-schema.md`](config-schema.md) | writing or validating an instance's **`config.yaml`** (setup, or adding a key) |
| [`node-type-matrix.md`](node-type-matrix.md) | in doubt **which conventions apply** to a file — the by-`node_type` lookup |
| [`worked-example.md`](worked-example.md) | you want the operating loop shown end-to-end on one concrete pass |
| [`worklog-resolution.md`](worklog-resolution.md) | a section's marker names **more than one tool**, a worklog is being created, or a reader must resolve which worklog backs a section |
| [`late-hypothesis.md`](late-hypothesis.md) | a hypothesis surfaces **after** the step where it belongs and you must place it without forking the process |

A pointer in the core file names the moment; follow it here only then.
