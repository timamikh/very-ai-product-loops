---
name: product-setup
description: >
  Set up a PRODUCT on the very-ai-product-loops framework. Runs AFTER the framework is installed
  (this skill does not vendor the framework). Use when the framework is present but there is no
  product-loops/ working area yet, or the user asks to set up / onboard a product. Asks the documentation
  language and for all existing materials, links and accesses; converts and files them; routes their
  content to the steps via the sources index (human confirms, agent never invents); then PROPOSES a
  product status with descriptions for the human to pick. Ends by summarizing what the sources cover
  vs what's blank and proposing a gap-closing plan in step order — the point where the working loops
  begin. Step artifacts are NOT created here — each is born by its step's first pass.
status: draft
version: 0.9.0
updated: 2026-08-23
---

# Product Setup (onboarding)

The first-run experience. Its job: get from "framework installed + a pile of existing materials" to
"a scaffolded `product-loops/` working area — sources filed and indexed, registers seeded, gaps
clearly marked, a chosen status, and a plan for what to work on first." Good onboarding is the
difference between the framework feeling alive on day one and feeling like blank templates.

**Install ≠ setup.** Installing the framework (vendoring `process/ steps/ statuses/ tool-skills/
.claude/`, pinned to a version) is a separate, earlier step — see [`install/`](../../../install/README.md).
This skill assumes the framework is already present and sets up the **product**; it does not vendor
the framework.

Golden rule holds: **the agent prepares, the human decides.** Everything ingested is tagged with
its source and confidence; nothing is invented; gaps are `— to clarify —`.

## Step 0 — bootstrap the rules (before anything)

**Do not trust auto-load.** This skill is usually invoked right after install or from another repo's
session, when the framework's root `AGENTS.md` was never auto-loaded as the boot entry. So load the
rules yourself, in order, before any setup work:
`process/OVERVIEW.md` → `OPERATING-LOOP.md` → `goal-map.md` → `CONVENTIONS.md` (plus `REGISTERS.md`
before any register work). They define the
disciplined loop and the "prepare, don't invent" rule the rest of this skill depends on. Skipping
them is exactly how a first run turns into an invented bulk-fill.

**Onboarding is not a work cycle.** Setup only *places* existing material and *marks* gaps. It does
**not** produce method-derived content (metric thresholds, test designs, pricing, hypotheses beyond
what a source states) and does **not** bulk-fill the downstream steps. That work happens later, one
section at a time, each through its library method, per the operating loop. Blurring the two is the
single most common failure — see anti-patterns.

## Phase 1 — Setup

### 1. Ask the documentation language
Ask which language to keep the **product's documentation** in (the instance artifacts — concept,
analysis, plans). Default to the user's preference; offer their language and English. Record it in
`product-loops/config.yaml` as `language:`.

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
Scaffold the three source subfolders first: `product-loops/sources/{originals,snapshots,access}/`.
For each material: convert to a convenient, diff-able format (markdown; tabular data → csv),
preserving the original reference. Put the converted copies in **`product-loops/sources/originals/`**
(the human's brought material — a format conversion, never a reinterpretation), one file per original,
with a short header noting the original filename/date. Do not edit the originals. Access facts the
human gives (where a tool lives, how to reach it) go to `sources/access/<slug>.md` as a **passport**,
recorded from their answers — never invented (see [`boundary-layout`](../../process/reference/boundary-layout.md)).

### 3b. Write the sources index (navigation file)
Create **`product-loops/sources/INDEX.md`** — a navigation map the agent reads *first* on every future
task, so it opens only the files relevant to the task at hand instead of re-reading everything
(saves context and prevents lost nuance). For each converted source, the agent **proposes** a row
and the human corrects it:

| Column | What it captures |
|--------|------------------|
| File | `sources/originals/<name>.md` (or `snapshots/`, `access/`) |
| Role | `access` · `evidence` — the trust class (see boundary-layout) |
| Type | the slot this source serves for a method's `reads:` — one of `kb` · `interview` · `research` · `metrics` · `git` (closed list; lint check S2 holds rows to it) |
| What it contains | 1–2 lines: the document's actual content |
| In scope | Which parts apply to **this** product-loops/instance |
| Out of scope | Which parts explicitly do **not** apply (e.g. "only the SaaS part; the infrastructure/GPU section is a different product") |
| Feeds steps | Which process steps draw on it (1–6) |
| Confidence / freshness | source date, staleness, `[assumption]` where the split is inferred |

The header is **copied verbatim** — every column carries its `<!--c:key-->` mark (prose is not a
carrier; the console and the linter read the keys, never the header words):

```markdown
| File <!--c:file--> | Role <!--c:role--> | Type <!--c:type--> | What it contains <!--c:what--> | In scope <!--c:in-scope--> | Out of scope <!--c:out-of-scope--> | Feeds steps <!--c:feeds--> | Dispatched into <!--c:dispatched--> | Confidence / freshness <!--c:conf--> |
```

(`Dispatched into` stays empty at setup — `source-intake` fills it as it routes each source into
step worklogs.)

The out-of-scope column is the point: it durably records boundary decisions (like "take only the
service part of the strategy, not the infrastructure part") so they are never silently lost when a
later agent re-reads the raw source. Present the proposed index to the user; they edit before it's
saved. Re-run this step whenever a source is added or a scope boundary changes.

> INDEX.md is the **entry point for knowledge**, not a step artifact. Agents consult it to decide
> what to read; it is not itself distributed across steps.

### 4. Distribute across the steps — a map, not a fill
Read the converted materials and map their content onto the **steps** — as routing, not as drafts.
**No step artifact is written here**: the artifact of a step is born by that step's *first pass* and
grows section-by-section (see [`projection`](../../../tool-skills/operations/projection/SKILL.md) —
every `<!-- tool -->` marker in an artifact is a worklog obligation, check P, so a pre-filled or
empty-template artifact fails the linter before the loop has run once). What setup does instead:
- Route each source to its steps in `INDEX.md` (**Feeds steps** column) — precise enough that the
  step's first pass finds its material without re-reading everything.
- Where materials conflict, record the conflict in INDEX.md and the placement report.
- Create the **registers** (hypotheses/risks/metrics/features/surfaces) by **copying the six skeleton files from
  `process/reference/register-skeletons/` verbatim** into `registers/` — they carry the keyed table
  headers (`<!--c:key-->`) check D and the console read; substitute only `<product>`/`<date>` in
  the frontmatter, never retype a header. No rows invented; registers carry no worklog obligation.
  Seed a row only for something a source *states outright* and no
  method will produce (a metric already being measured, a risk the founder names). **Anything a step's
  method owns is that method's to seed**, on its pass: a concept bet becomes `H-…` in `concept-formation`,
  not here. Both sides seeding is how one id gets issued twice.
- **Only place what the sources say.** Do NOT derive numbers, thresholds, hypotheses, test designs,
  or pricing here — those are method work for the loop. A section that will need a library method is
  simply a gap the plan (step 7) names, not an invented draft.

Produce a **placement report**: which sources feed which steps, what conflicts were found, what's
still open.

### 5. Propose the status (agent proposes, human picks)
Do **not** ask "what status?" cold — the human may not know the options. **Present the choice:**
read [`statuses/README.md`](../../../statuses/README.md) → "Choosing a status" and surface each
available status with its short description (you're here when · what it optimizes for · main
evidence), then **recommend one** (⚙️) inferred from the materials, with a one-line reason. The
human confirms or overrides. Record the choice in `product-loops/config.yaml` as `active_status`.

> **Directions are not asked in v1.** Default them to `development · go-to-market · back-office` in
> `config.yaml` and move on. They are an instance config power users edit later when they tailor the
> framework — keep first-run setup to as few forks as possible.

### 5b. Ask the delegation toggle
The loop can fan a heavy pass out to **subagents** (a `draft` subagent writes its method's worklog;
`gather`/`research`/`verify` return text) — but only where the environment allows spawning them, and
only if the human wants it. Ask one question: *may this instance use subagents?* Recommend `allowed`
(⚙️) — it is the framework's normal mode and the orchestrator still falls back to running a pass
itself whenever a pass fits one context. Choose `off` when spawning agents is restricted here, or the
human prefers no fan-out; then the orchestrator runs every pass itself and writes every worklog
directly. Record the answer in `product-loops/config.yaml` as `delegation:` (`allowed` · `off`) —
CONVENTIONS → *Instance config*. This is separate from the session-restart caveat in Phase 2 step 7:
that is about the agent definitions being *available*; this is about whether they are *permitted* at
all.

### 6. Scaffold the working area
Create `product-loops/` (see layout below), in the chosen language: `config.yaml`, `state.yaml`,
`HANDOFF.md`, `sources/` (already filed in step 3), `registers/` (seeded per step 4),
`export-files/`. **Do not create the step artifacts** (`1-concept.md` … `6-sprint-plan.md`) — not
even as empty templates: each is born by its step's first pass and grows section-by-section; a step
the instance has not reached has no artifact file, and that is the linter's expected state. Write an
initial **`state.yaml`** (`current_step: 1`, gate ticks empty) — the cycle's position home, distinct
from the human-authored `config.yaml`.

**Then verify before closing Phase 1 — two checks, both mandatory:**
1. **`config.yaml` against the pinned schema** (`process/reference/config-schema.md`): all four
   required keys present — `product` (the product's name as the human says it — a key setups have
   silently dropped) · `language` · `active_status` · `directions` — spelled exactly as the schema
   spells them, no aliases.
2. **The linter**: run `python3 tools/lint.py <instance>`, confirm `instances checked:` names the
   instance, and fix every error it reports *now* — an error left here is debt the first working
   session inherits silently.

This closes Phase 1 — the product is set up.

## Phase 2 — Orient and hand into the loops

### 7. Summarize the product and propose where to start
Now that the sources are filed and a status is set, give the human a **product summary**, then a plan:
- **Coverage by step:** step by step (1→6), what the sources cover (per `INDEX.md` → *Feeds steps*)
  and where the **white spots** are (steps with no material, open conflicts, unseeded registers).
- **Proposed plan:** in step order, propose closing the biggest/earliest gaps first — the shortest
  path to a coherent line from concept to sprint, weighted by the active status's `per_step` goals.
- The human **agrees or proposes their own plan** — then **stop. Setup ends here.** Acting on the
  plan is the operating loop (OPERATING-LOOP.md): it runs **one section at a time, each produced
  through its library method** — open the method's `SKILL.md`, check prerequisites, clarify real
  forks as 2–4 options + ⚙️ and wait, then fill. That is **never** another bulk fill. Do not slide
  from setup straight into that work; hand the plan over and begin the loop only on the human's go.
From the next session on, that loop is entered via the **`start-work`** skill (which self-bootstraps
the rules and runs one pass at a time).

**Before handing over, check delegation.** Only if `config.yaml` set `delegation: allowed` in step 5b
— if it is `off`, the loop runs without subagents and there is nothing to check here. When allowed: the
loop runs on subagents (`loops-gather` · `loops-research` · `loops-draft` · `loops-verify`), and their
definitions — vendored at install — are picked up only at **session start**. Tell the human plainly:
restart the session once before the first `start-work`, or the agent types will not be found. If
spawning agents is restricted in this environment, say that too — the owner's standing approval line
lives in the host repo's root `AGENTS.md` (written at install).

## Instance layout (created in the product's repo)

```
product-loops/
  config.yaml            # HUMAN-authored: language · active status · directions · delegation · metric source slots
  state.yaml             # AGENT-written each pass: current_step · last_pass · gate ticks (cycle position)
  HANDOFF.md             # session-to-session: environment/access checks + open forks (see operations/handoff)
  sources/               # what comes from OUTSIDE — never agent reasoning (see reference/boundary-layout)
    INDEX.md             # navigation map: per-source what/in-scope/out-of-scope/feeds-steps
    originals/           # the user's existing materials (source of record)
    snapshots/           # dated, immutable captures (URL extracts, pulled exports)
    access/              # one passport per external point, recorded from the human
  skills/                # (optional) the product's own exchange skills: <pull|push>-<endpoint>-<what>/
  # step artifacts (1-concept.md … 6-sprint-plan.md) are NOT created at setup — each is born
  # by its step's first pass and grows section-by-section (projection; linter check P)
  registers/
    hypotheses.md        # H-… (single-value type + optional tags)
    risks.md             # R-… (single-value category + optional tags)
    metric-tree.md       # M-… node definitions (id/unit/kind/parent/instrumentation/target)
    metrics.csv          # append-only dated readings (id,period_start,period_end,measured_at,value,basis,source,note)
  export-files/          # what goes OUTSIDE — rendered views (decks/docs/tables, regeneratable) + authored deliverables (briefs, interview guides — signed source)
```

Kept **separate from code** (its own top-level `product-loops/`), so it never interferes with the
repo's source. The framework itself (`steps/`, `statuses/`, `process/`, `tool-skills/`) is vendored
read-only into the repo at install and pinned to a version tag.

## Anti-patterns

- **Inventing to fill.** Populating a section with plausible content the materials don't support.
- **Silent conflicts.** Merging contradictory materials without flagging.
- **Editing originals.** Converted copies live in `product-loops/sources/originals/`; the human's originals are untouched.
- **Framework in the code tree.** Product docs must sit in `product-loops/`, away from `src/`.
- **Reading everything, every time.** With `sources/INDEX.md` present, consult it first and open
  only the files a task needs — don't re-ingest the whole `sources/` folder each turn.
- **Losing scope boundaries.** A source that only partly applies (e.g. a deck covering two products)
  must have its out-of-scope part recorded in INDEX.md, or a later agent will silently re-import it.
- **Asking status cold.** Presenting `concept-viability / pmf / growth` as a bare question — propose
  with descriptions and a recommendation instead (the human may not know the options).
- **Forking on directions in v1.** Don't ask about work directions at first-run — default them and
  let power users edit `config.yaml` later.
- **Skipping the rules.** Running setup without first reading `process/` in order (Step 0). Auto-load
  of the root `AGENTS.md` does not fire when this skill runs from install or another session — load
  the rules yourself.
- **Onboarding as a work cycle.** Bulk-filling downstream artifacts or running a "first cycle" during
  setup. Setup places sourced material and stops; method work is the loop's job, one section at a time.
- **Scaffolding step artifacts.** Creating `1-concept.md` … `6-sprint-plan.md` at setup — filled *or*
  empty. Every `<!-- tool -->` marker in an artifact is a worklog debt (check P), so an unrolled
  template fails the linter before any pass has run. Artifacts are born by passes.
- **Deriving content during onboarding.** Producing thresholds, test designs, pricing, or hypotheses
  beyond what the sources state — that is method work (e.g. `hypothesis-test-design`), not onboarding.
