---
node_type: reference
title: process/reference — canon read on demand, not every pass
status: draft
version: 0.4.0
updated: 2026-09-02
---

# process/reference

These files are **canon**, but they are **not** part of the always-loaded reading order in
[`AGENTS.md`](../../AGENTS.md). Each is read at a **named moment** — when you are about to do the
one thing it governs — so the per-pass `process/` files stay lean. `REGISTERS.md` follows the same
pattern from the core: read at loop moves 2 (register rows as inputs) and 5 (before writing rows).

The split follows [`CONVENTIONS.md`](../CONVENTIONS.md) → *One mechanism, one way* (the full test in
[`extending/rules.md`](../../extending/rules.md)): a contract two readers must agree on lives in `process/`; a
lookup or an authoring rule that only one task ever needs lives here and is pointed at from the
stub that stays in the core.

| File | Read it when |
|------|--------------|
| [`GLOSSARY.md`](GLOSSARY.md) | a term is unclear, or onboarding — the entity **vocabulary** (a map of names to where each is actually defined; not a second definition home) |
| [`card-schema.md`](card-schema.md) | writing or validating a **card** — a step README, a library method, an operations/outputs skill, an instance exchange skill: the one frontmatter schema all five kinds fill |
| [`column-keys.md`](column-keys.md) | authoring or editing a **step template** or a **register** — deciding whether a table column carries a `<!--c:key-->` and where its key lives |
| [`config-schema.md`](config-schema.md) | writing or validating an instance's **`config.yaml`** (setup, or adding a key) |
| [`state-schema.md`](state-schema.md) | writing or reconstructing an instance's **`state.yaml`** — the position keys, the gate-tick map and the tick values |
| [`node-type-matrix.md`](node-type-matrix.md) | in doubt **which conventions apply** to a file — the by-`node_type` lookup |
| [`worklog-resolution.md`](worklog-resolution.md) | a section's marker names **more than one tool**, a worklog is being created, or a reader must resolve which worklog backs a section |
| [`worklog-skeleton.md`](worklog-skeleton.md) | **creating a worklog** — the copyable shape (frontmatter, the typed inputs line, the intake table) |
| [`register-skeletons/`](register-skeletons/README.md) | **creating the register files** at setup or after a loss — copy each verbatim, never retype a header |
| `scales.md` | **Scales** — the shared scoring scales used by the hypothesis and prioritization methods (read when a method's `§Scales` points here) |
| [`boundary-layout.md`](boundary-layout.md) | adding a `sources/` subfolder, writing an instance's own **exchange skill** (pull/push), or resolving where a piece of external data belongs |
| [`late-hypothesis.md`](late-hypothesis.md) | a hypothesis surfaces **after** the step where it belongs and you must place it without forking the process |
| [`worked-example.md`](worked-example.md) | you want the operating loop shown end-to-end on one concrete pass |

A pointer in the core file names the moment; follow it here only then.
