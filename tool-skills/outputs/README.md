---
node_type: outputs-index
title: Outputs — produce the files that leave the framework
status: draft
version: 0.5.0
updated: 2026-08-21
---

# Outputs

The framework's **output layer**. The four planes (process · registers · library · statuses)
produce a structured **instance** — markdown artifacts with stable section IDs, three registers,
and `sources/`. An **outputs skill** produces a file a human uses **outside the framework** —
an export file. In an instance every such file lives in **`product-loops/export-files/`**, the
mirror of `sources/`: sources are what comes **in** from outside; export-files are what goes
**out**. No outputs skill fills an artifact section, and none writes a register.

## Two kinds, one plane

Both are `kind: output` cards in one `SKILL.md`; `output_kind:` is what tells them apart — two
filenames for one entity was the same defect as two schemas.

| `output_kind` | Mechanic | Source of truth |
|---------------|----------|-----------------|
| **`rendered`** (a renderer) | **reads** the structured instance, renders a view — never authors content | the instance; the rendered file is **regeneratable**, re-run to refresh |
| **`authored`** (a deliverable) | **authors** a document from the instance's state | the document itself (`node_type: deliverable`) — it is signed and versioned, not regenerated |

- **Renderers**: [`to-table`](to-table/SKILL.md) · [`to-document`](to-document/SKILL.md) ·
  [`to-deck`](to-deck/SKILL.md).
- **Authored**: [`brief`](brief/SKILL.md) (one-page framing of an initiative) ·
  [`interview`](interview/SKILL.md) (an interview guide the product person runs outside;
  the notes come **back** as a source — see the skill) ·
  [`feature-to-spec`](feature-to-spec/SKILL.md) (the development instruction — BRD/PRD or tech
  spec — per groomed Step-6 feature; product decisions arrive fixed from `feature-grooming`, only
  technical forks stay open).

A renderer's whole job is the **last hop**: from what's structured for an *agent* to read
(stable IDs, typed links, register codes) into what's convenient for a *human* to consume. Its
output must be the **finished deliverable**, not another intermediate form — a deck is a
presentable file you can open and present, not a markdown outline.

> **Source of truth stays in the instance — for renderers.** A rendered table/doc/deck is a *view*
> of the instance at a moment — never edited in place as if it were the source. Change the
> artifact/register, re-run the renderer. An **authored** deliverable is the opposite: the file
> *is* the source (a brief is what the human signed), and a renderer may re-format it
> (`to-document` → `.docx`) without ever becoming its home.

## The renderer set

| Renderer | Mode | Renders | Typical deliverables |
|----------|------|---------|----------------------|
| [`to-table`](to-table/SKILL.md) | table | a register or artifact section → a flat table | hypothesis scoreboard · metric series · market-bundle registry · sprint backlog |
| [`to-document`](to-document/SKILL.md) | document | selected sections → one compiled document | full strategy doc · weekly test report · status update · a brief re-formatted to `.docx` |
| [`to-deck`](to-deck/SKILL.md) | deck | the instance → a self-contained, presentable HTML deck (one idea per slide), plus a PDF companion once approved | strategy-defense · analysis readout · sprint-review · concept-pitch |

## Base vs. company (the boundary)

- **Base outputs** (this folder) are **neutral and open**: generic renderers and authored-document
  skills that ship with the framework. They assume nothing about a company's house style,
  templates, or internal forms.
- **Company outputs** live **outside** the base, in a private/plugin repo, and **specialize** a
  base one into a specific format — a branded deck, an internal steering-committee card, a
  downstream dev-framework hand-in. They may import a base renderer's structure and re-skin it.

Keeping the base neutral is what lets the framework stay open while each company layers its own
formats on top without forking. (See `process/OVERVIEW.md` §10.)

## Anatomy

A **renderer** is a folder `outputs/<name>/`:

```
outputs/<name>/
  SKILL.md     # what it renders · what it reads · how to render · output shape · anti-patterns
  render.py    # a generic, instance-agnostic renderer — shipped where the deliverable format needs a library/engine
```

`SKILL.md` is an **instruction skill** (the agent selects, orders, and decodes — no build step for
the *reasoning*). **Where the final format needs a library or engine, the renderer also ships a
generic `render.py`** that reads *any* instance and holds **no product data** — so the render logic
travels with the framework and the base stays instance-agnostic. All three base renderers carry
one, which is the canon:

- `to-table` → `.xlsx` needs **openpyxl**;
- `to-document` → `.docx` needs **python-docx**;
- `to-deck` → the emailable **PDF** needs a **browser engine** (uses the installed system browser).

The *content* is still authored per instance by the agent (a deck's HTML, a doc's markdown); the
renderer only applies the format. Formats the agent can emit directly with no library (CSV, markdown,
the deck's HTML) need no code. Its frontmatter is a card header like any other:

```yaml
---
node_type: card
kind: output
name: <renderer>
output_kind: rendered                 # rendered (regeneratable view) | authored (signed document)
prerequisites: []
reads: [section:*, register:hypotheses, register:metric-tree]   # what instance data it reads
writes: [file:export-files/*]         # everything leaving the framework lands there
surfaces: [file:export-files/*]       # what move 5 owes
formats: [csv, markdown, ...]         # output formats it can emit
opinionated: false
status: draft
version: <x.y.z>
updated: <date>
---
```

An **authored deliverable** is a folder with the library anatomy (`SKILL.md` ·
`template-fragment.md` · `questions.yaml`), except its `produces` is a **file in
`product-loops/export-files/`**, never an artifact section, and it writes no register —
registers are written by the orchestrator through the methods that work the evidence.

## How to add one

The procedure and its checklist: [`extending/output.md`](../../extending/output.md). This file holds the
anatomy and the two kinds; that one holds the change.
