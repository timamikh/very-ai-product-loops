---
node_type: adapters-index
title: Adapters — render instance data into deliverables
status: draft
version: 0.1.0
updated: 2026-07-18
---

# Adapters

The framework's **output layer**. The four planes (process · registers · library · statuses)
produce a structured **instance** — markdown artifacts with stable section IDs, three registers,
and `sources/`. An **adapter** reads that structured instance and renders it into a **deliverable**
a human actually shares: a table, a document, or a presentation.

An adapter's whole job is that **last hop**: from what's structured for an *agent* to read
(stable IDs, typed links, register codes) into what's convenient for a *human* to consume. Its
output must therefore be the **finished deliverable**, not another intermediate form — a deck is a
presentable file you can open and present, not a markdown outline.

Adapters are why the base artifacts are kept structured (stable `{#ids}`, typed links, register
IDs): the structure is the contract an adapter renders against, so deliverables can be regenerated
from source instead of hand-maintained in parallel.

> **Source of truth stays in the instance.** An adapter **reads**, it does not author. A rendered
> table/doc/deck is a *view* of the instance at a moment — never edited in place as if it were the
> source. Change the artifact/register, re-run the adapter. (One mechanism, one way: values live in
> the registers and artifacts; a deliverable is a projection, not a second home.)

## Base adapters vs. company adapters (the boundary)

- **Base adapters** (this folder) are **neutral and open**: generic table / document / deck
  renderers that ship with the framework. They assume nothing about a company's house style,
  templates, or internal forms.
- **Company adapters** live **outside** the base, in a private/plugin repo, and **specialize** a
  base adapter into a specific format — a branded deck, an internal steering-committee card, a
  downstream dev-framework hand-in. They may import a base adapter's structure and re-skin it.

Keeping the base neutral is what lets the framework stay open while each company layers its own
formats on top without forking. (See `process/OVERVIEW.md` §10.)

## The base set

| Adapter | Mode | Renders | Typical deliverables |
|---------|------|---------|----------------------|
| [`to-table`](to-table/ADAPTER.md) | table | a register or artifact section → a flat table | hypothesis scoreboard · metric series · market-bundle registry · sprint backlog |
| [`to-document`](to-document/ADAPTER.md) | document | selected sections → one compiled document | one-pager brief · full strategy doc · weekly test report · status update |
| [`to-deck`](to-deck/ADAPTER.md) | deck | the instance → a self-contained, presentable HTML deck (one idea per slide) | strategy-defense · analysis readout · sprint-review · concept-pitch |

## Anatomy of an adapter

Each adapter is a folder `adapters/<name>/`:

```
adapters/<name>/
  ADAPTER.md   # what it renders · what it consumes (by stable id) · how to render · output shape · anti-patterns
```

`ADAPTER.md` is an **instruction skill** (the agent renders — no build step; the framework stays
plain markdown until pain justifies code). Its frontmatter declares the wiring:

```yaml
---
name: <adapter>
kind: adapter
mode: table | document | deck
consumes: [registers, artifacts]     # what instance data it reads
reads_ids: [<stable section/register ids it targets>]  # the contract it renders against
produces: <deliverable description>
formats: [csv, markdown, ...]         # output formats it can emit
opinionated: false
status: draft
version: <x.y.z>
updated: <date>
---
```

## How to add an adapter

1. Create `adapters/<name>/ADAPTER.md` with the anatomy above.
2. State exactly which instance IDs it consumes and the output shape it emits.
3. Register it in the table above.
4. If it encodes a company-specific format, put it in the company/plugin repo instead — this folder
   is for neutral base adapters only.

## Change log

### 2026-07-21 — sharpened the "finished deliverable" purpose; `to-deck` now emits HTML
- **From → To:** stated the adapter's purpose as the agent-readable → human-consumable last hop
  (output must be the finished deliverable, not an intermediate form); updated the `to-deck` row —
  it renders a self-contained **HTML deck** (not a markdown outline) and gained a `concept-pitch`
  profile. See `to-deck/ADAPTER.md`.
- **Why:** a markdown slide list isn't something a human presents; the base adapter was stopping
  halfway. Surfaced by the decksmith live run.
- **Trigger:** example run, Step-6 wrap.

### 2026-07-18 — created
- **From → To:** — → base adapters plane (`to-table`, `to-document`, `to-deck`) + anatomy + the
  base-vs-company boundary.
- **Why:** the framework produced a well-structured instance but had no neutral, open way to turn it
  into the everyday deliverables (tables/docs/decks). Base renderers belong in the open framework;
  company-specific formats stay external. Realizes the "adapters" concept OVERVIEW §10 had deferred.
- **Trigger:** base-converters pass, 2026-07-18.
