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
[`CONVENTIONS.md`](../CONVENTIONS.md) → *Step folders & worklogs* — *the worklog path form, the
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
id-thread, and is what the section projects from. The others are **contributing methods** — their
working for *this* section lands in the primary's worklog, not a file of their own (a contributing
method still owns its own worklog for any section where *it* is primary).

So every section resolves to exactly one worklog, whether its marker names one method or several —
the rule a reader and the linter both apply is *the first tool in the marker owns the section's
worklog*.

## Raw inputs are not worked here

Raw external inputs are **not** worked in worklogs directly: they live in `sources/` and are
dispatched into these worklogs by the
[`source-intake`](../../tool-skills/operations/source-intake/SKILL.md) operations skill
(CONVENTIONS → *Raw data & access*). A worklog cites `../sources/<file>`; an artifact links only the
worklog.
