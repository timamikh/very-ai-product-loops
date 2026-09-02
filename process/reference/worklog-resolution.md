---
node_type: reference
title: Worklog resolution — how a section finds its worklog
status: draft
version: 0.2.0
updated: 2026-08-20
---

# Worklog resolution

*Read this when a section's marker names more than one tool, when creating a worklog, or when a
reader/tool must resolve which file backs a section. The one-line contract stays in*
[`CONVENTIONS.md`](../CONVENTIONS.md) → *Artifacts, step folders & worklogs* — *the worklog path form, the
first-tool-owns rule, and check P; the resolution detail is here. When **creating** a worklog,
copy the skeleton from* [`worklog-skeleton.md`](worklog-skeleton.md) *verbatim — don't retype
the shape from this prose.*

## The folder and the stem

The artifact `<step-number>-<slug>.md` is a **projection**; the working documents it is assembled
from live in a sibling folder of the same stem — `2-analysis/` beside `2-analysis.md` (file and
folder coexist; the artifact is **not** moved inside). The stem is the **artifact's**
(`<step-number>-<slug>`), which matches the step directory `steps/<step-number>-<slug>/` for every
step — the console and check P both resolve the worklog folder from the artifact stem.

The folder holds one **worklog** per method that fills a section: `<step-folder>/<tool>.md`, where
`<tool>` is the id in the section's `<!-- tool: <tool> -->` marker. `<!-- synthesis -->` sections —
no method, the orchestrator's own reasoning — share the reserved `<step-folder>/synthesis.md`.

A worklog carries `node_type: worklog` frontmatter (`tool`, `step`, `title`, `updated`, `version`).
Its change log is the home of that method's history — the artifact section carries none of its own,
because the section is a projection and its past belongs to the source of truth.

## One id threads the chain

The same `<tool>` names the section's marker, the skill folder (`tool-skills/.../<tool>/`), and the
worklog file — so a reader resolves a section's worklog with no guessing and no per-instance link.
The flow runs along it: subagents gather into `<tool>.md`, then the skill `<tool>` **projects** the
artifact section from it (the writing move itself — the
[`projection`](../../tool-skills/operations/projection/SKILL.md) operations skill). The **worklog is
the source of truth; the artifact section is its projection.** Every section that a method fills has
a worklog; this is not optional — a projected section with no worklog behind it is the source of
truth gone missing (the linter's check P holds it).

## One method → several sections: one worklog

A method that fills several sections keeps **one** worklog; every one of its markers points at it
(e.g. `competitor-analysis` fills `{#competitors}` and `{#competitor-strategy}`, both projected from
`2-analysis/competitor-analysis.md`).

## Several methods → one section: the first is primary

When a section's marker lists more than one tool
(`<!-- tool: where-to-play-how-to-win, value-definition-strategy -->`), the **first** tool is the
section's **primary**: its worklog `<step-folder>/<first-tool>.md` backs the section, carries the
id-thread, and is what the section projects from. Every other tool named is a **contributing
method**. It works in **its own worklog** — `<its-step-folder>/<tool>.md`, the same file it keeps
wherever it is primary — never in the primary's: no method writes another method's worklog (the
write rule, OPERATING-LOOP → Delegation). Its contribution reaches the section when the section is
re-projected; the marker names every writer, so a reader resolves the section to the primary's
worklog for its thread and to each named worklog for its history.

## A revisit from a later step: its own worklog, in its own step folder

A **revisit** is a later step's method named on an earlier step's marker
(`1#cjm` → `cjm-concept, cjm-strategy` · `1#value-defensibility` → `value-definition-concept,
value-definition-strategy` · `3#pricing` → `pricing-strategy, pricing-strategic-plan`). It is the
one sanctioned way a later step rewrites an earlier section: it builds on the earlier working and
refines it, it does not redo it. Its worklog lives in **its own step's folder**
(`3-strategy/cjm-strategy.md`); the earlier method's worklog is a **declared read**
(`worklog:1-concept/cjm-concept` in `reads`); the section is re-projected from the revisit's
worklog, which drops the section's `confirmed:` marker (CONVENTIONS → Section confirmation). A
revisit exists only where the template marker names it (linter check B2); any other return to an
earlier section comes through a register revision — a hypothesis refuted, a risk fired, a metric
moved — and is worked by the section's primary.

So every section resolves to exactly one **primary** worklog, and to every worklog its marker
names — the rule a reader and the linter both apply is *the first tool in the marker owns the
section's thread; each named tool owns its own file, in its own step's folder*.

## Raw inputs are not worked here

Raw external inputs are **not** worked in worklogs directly: they live in `sources/` and are
dispatched into these worklogs by the
[`source-intake`](../../tool-skills/operations/source-intake/SKILL.md) operations skill
(CONVENTIONS → *Raw data & access*). A worklog cites `../sources/<file>`; an artifact links only the
worklog.
