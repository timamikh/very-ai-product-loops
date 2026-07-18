---
name: product-setup
description: >
  Onboard the very-ai-product-loops framework into a product's repository. Use when a user
  points an agent at this framework and asks to add/install/set it up, or when a repo has the
  framework but no product/ working area yet. Asks for the documentation language and all
  existing product materials, converts them to a convenient format, files them, and distributes
  their content across the process steps so the product starts with as much pre-filled as the
  materials allow — human confirms, agent never invents.
status: draft
version: 0.1.0
updated: 2026-07-16
---

# Product Setup (onboarding)

The first-run experience. Its job: get from "empty repo + a pile of existing materials" to "a
scaffolded `product/` working area with each step pre-populated from those materials, gaps
clearly marked." Good onboarding is the difference between the framework feeling alive on day one
and feeling like blank templates.

Golden rule holds: **the agent prepares, the human decides.** Everything ingested is tagged with
its source and confidence; nothing is invented; gaps are `— to clarify —`.

## Flow

### 1. Ask the documentation language
Ask which language to keep the **product's documentation** in (the instance artifacts — passport,
analysis, plans). Default to the user's preference; offer their language and English. Record it in
`product/config.yaml` as `language:`.

> The **framework core** (steps, tools, statuses) stays English; only the **instance's product
> artifacts** are authored in the chosen language. Templates are translated on fill, not forked.

### 2. Ask for all existing materials
Ask the user to provide everything they already have about the product — in any form: docs,
decks, spreadsheets, metrics exports, PRDs, research, links, notes. "Whatever exists, however
messy." If nothing exists, that's fine — skip to scaffolding with empty templates.

### 3. Convert and file them
For each material: convert to a convenient, diff-able format (markdown; tabular data → csv),
preserving the original reference. Put the converted copies in **`product/sources/`**, one file
per original, with a short header noting the original filename/date. Do not edit the originals.

### 3b. Write the sources index (navigation file)
Create **`product/sources/INDEX.md`** — a navigation map the agent reads *first* on every future
task, so it opens only the files relevant to the task at hand instead of re-reading everything
(saves context and prevents lost nuance). For each converted source, the agent **proposes** a row
and the human corrects it:

| Column | What it captures |
|--------|------------------|
| File | `sources/<name>.md` |
| What it contains | 1–2 lines: the document's actual content |
| In scope | Which parts apply to **this** product/instance |
| Out of scope | Which parts explicitly do **not** apply (e.g. "only the SaaS part; the infrastructure/GPU section is a different product") |
| Feeds steps | Which process steps draw on it (1–6) |
| Confidence / freshness | source date, staleness, `[assumption]` where the split is inferred |

The out-of-scope column is the point: it durably records boundary decisions (like "take only the
service part of the strategy, not the infrastructure part") so they are never silently lost when a
later agent re-reads the raw source. Present the proposed index to the user; they edit before it's
saved. Re-run this step whenever a source is added or a scope boundary changes.

> INDEX.md is the **entry point for knowledge**, not a step artifact. Agents consult it to decide
> what to read; it is not itself distributed across steps.

### 4. Distribute across the steps
Read the converted materials and map their content onto the step artifacts:
- Draft each artifact section from the materials as **⚙️ proposals**, tagging every value
  `[sourced: <original material>]`.
- Where materials conflict, mark the field `[assumption]` and surface the conflict.
- Where a section has no supporting material, leave `— to clarify —`.
- Seed the registers (hypotheses/risks/metrics) from anything the materials imply.

Produce a **placement report**: what went where, what conflicts were found, what's still open.

### 5. Set status and directions
Ask (or infer + confirm) the product's current [status](../../../statuses/README.md)
(`concept-viability` / `pmf` / `growth` / custom) and its work directions (default
`development · go-to-market · back-office`). Record in `product/config.yaml`.

### 6. Scaffold the working area
Create `product/` from templates (see layout below), in the chosen language, pre-filled per
step 4. Hand back the placement report and the first suggested step to work on.

## Instance layout (created in the product's repo)

```
product/
  config.yaml            # language · active status · directions · metric source slots
  sources/               # converted copies of the user's existing materials (source of record)
    INDEX.md             # navigation map: per-source what/in-scope/out-of-scope/feeds-steps
  passport.md            # Step 1 artifact
  analysis.md            # Step 2
  strategy.md            # Step 3
  strategic-plan.md      # Step 4
  tactical-plan.md       # Step 5
  sprint-plan.md         # Step 6
  registers/
    hypotheses.md        # H-… (typed)
    risks.md             # R-…
    metric-tree.md       # M-… node definitions (id/unit/kind/parent/instrumentation/target)
    metrics.csv          # append-only dated readings (id,period_start,period_end,measured_at,value,basis,source,note)
```

Kept **separate from code** (its own top-level `product/`), so it never interferes with the
repo's source. The framework itself (`steps/`, `library/`, `statuses/`, `process/`) is vendored
read-only into the repo at install and pinned to a version tag.

## Anti-patterns

- **Inventing to fill.** Populating a section with plausible content the materials don't support.
- **Silent conflicts.** Merging contradictory materials without flagging.
- **Editing originals.** Converted copies live in `product/sources/`; originals are untouched.
- **Framework in the code tree.** Product docs must sit in `product/`, away from `src/`.
- **Reading everything, every time.** With `sources/INDEX.md` present, consult it first and open
  only the files a task needs — don't re-ingest the whole `sources/` folder each turn.
- **Losing scope boundaries.** A source that only partly applies (e.g. a deck covering two products)
  must have its out-of-scope part recorded in INDEX.md, or a later agent will silently re-import it.
