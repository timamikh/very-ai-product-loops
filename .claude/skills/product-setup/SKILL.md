---
name: product-setup
description: >
  Set up a PRODUCT on the very-ai-product-loops framework. Runs AFTER the framework is installed
  (this skill does not vendor the framework). Use when the framework is present but there is no
  product/ working area yet, or the user asks to set up / onboard a product. Asks the documentation
  language and for all existing materials, links and accesses; converts and files them; distributes
  their content across the steps (human confirms, agent never invents); then PROPOSES a product
  status with descriptions for the human to pick. Ends by summarizing what's filled vs blank and
  proposing a gap-closing plan in step order — the point where the working loops begin.
status: draft
version: 0.2.0
updated: 2026-07-19
---

# Product Setup (onboarding)

The first-run experience. Its job: get from "framework installed + a pile of existing materials" to
"a scaffolded `product/` working area, pre-populated from those materials with gaps clearly marked,
a chosen status, and a plan for what to work on first." Good onboarding is the difference between
the framework feeling alive on day one and feeling like blank templates.

**Install ≠ setup.** Installing the framework (vendoring `process/ steps/ statuses/ tool-skills/
.claude/`, pinned to a version) is a separate, earlier step — see [`install/`](../../../install/README.md).
This skill assumes the framework is already present and sets up the **product**; it does not vendor
the framework.

Golden rule holds: **the agent prepares, the human decides.** Everything ingested is tagged with
its source and confidence; nothing is invented; gaps are `— to clarify —`.

## Phase 1 — Setup

### 1. Ask the documentation language
Ask which language to keep the **product's documentation** in (the instance artifacts — passport,
analysis, plans). Default to the user's preference; offer their language and English. Record it in
`product/config.yaml` as `language:`.

> The **framework core** (steps, tools, statuses) stays English; only the **instance's product
> artifacts** are authored in the chosen language. Templates are translated on fill, not forked.

### 2. Ask for all existing materials, links and accesses
Ask the user to provide everything that could help the product work — in any form: docs, decks,
spreadsheets, metrics exports, PRDs, research, **links**, notes, and **accesses** (connectors or
credentials to metrics / analytics / knowledge base, so later steps can pull data). "Whatever
exists, however messy." If nothing exists, that's fine — skip to scaffolding with empty templates.
Accesses are recorded per `CONVENTIONS.md` "Raw data & access" (secret *values* never stored — only
where they live and how to check/recover them).

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

### 5. Propose the status (agent proposes, human picks)
Do **not** ask "what status?" cold — the human may not know the options. **Present the choice:**
read [`statuses/README.md`](../../../statuses/README.md) → "Choosing a status" and surface each
available status with its short description (you're here when · what it optimizes for · main
evidence), then **recommend one** (⚙️) inferred from the materials, with a one-line reason. The
human confirms or overrides. Record the choice in `product/config.yaml` as `active_status`.

> **Directions are not asked in v1.** Default them to `development · go-to-market · back-office` in
> `config.yaml` and move on. They are an instance config power users edit later when they tailor the
> framework — keep first-run setup to as few forks as possible.

### 6. Scaffold the working area
Create `product/` from templates (see layout below), in the chosen language, pre-filled per
step 4. Produce the **placement report**: what went where, what conflicts were found, what's still
open. This closes Phase 1 — the product is set up.

## Phase 2 — Orient and hand into the loops

### 7. Summarize the product and propose where to start
Now that everything is filled and a status is set, give the human a **product summary**, then a plan:
- **State of the artifact set:** step by step (1→6), what is populated (from which sources) and where
  the **white spots** are (`— to clarify —` sections, open forks, unseeded registers, conflicts).
- **Proposed plan:** in step order, propose closing the biggest/earliest gaps first — the shortest
  path to a coherent line from concept to sprint, weighted by the active status's `per_step` goals.
- The human **agrees or proposes their own plan.** Either way, acting on it **is** the operating
  loop (OPERATING-LOOP.md) — Phase 2 is simply the first Orient/Focus. Setup does not "end" so much
  as become the loop.

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
repo's source. The framework itself (`steps/`, `statuses/`, `process/`, `tool-skills/`) is vendored
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
- **Asking status cold.** Presenting `concept-viability / pmf / growth` as a bare question — propose
  with descriptions and a recommendation instead (the human may not know the options).
- **Forking on directions in v1.** Don't ask about work directions at first-run — default them and
  let power users edit `config.yaml` later.

## Change log

### 2026-07-19 — corrected onboarding flow (install≠setup · propose status · Phase 2)
- **From → To:** (1) framed the skill as the PRODUCT-setup phase that runs *after* install (it does
  not vendor the framework); (2) step 2 now also asks for links & accesses; (3) step 5 changed from
  "ask status + directions" to **propose the status with descriptions + a recommendation** — and
  **directions are no longer asked** (defaulted; power users edit later); (4) added **Phase 2** — a
  product summary (filled vs white spots) + a gap-closing plan in step order that becomes the first
  turn of the operating loop.
- **Why:** the old "what status? what directions?" was a cold question a context-less human can't
  answer — it violated "agent prepares, human decides"; and setup had no explicit hand-off into the
  loops. Fewer first-run forks (directions defaulted) per the v1 simplicity goal.
- **Trigger:** onboarding-flow review, 2026-07-19.
