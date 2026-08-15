---
node_type: reference
title: Glossary — the entities of very-ai-product-loops
status: draft
version: 0.1.0
updated: 2026-08-15
---

# Glossary

One shared vocabulary for the framework, so a person and an agent name the same thing the same way.
A desynced name is a latent bug — the console, the linter, and the step templates all key off these
names, so this file is the reference they are held against. Where a name was recently changed, the
old one is listed too, under **Renames** at the end.

The framework separates **mechanism** (a thin, fixed core) from **content** (pluggable methods and
product stages). Most entities below belong to one side or the other; a few are the seams between them.

---

## The four planes (the architecture)

| Entity | Where | What it is |
|--------|-------|------------|
| **Process core** / **steps** | `steps/` | The thin, fixed skeleton: six gated steps. Each owns an artifact's structure and its gate — **no methods inside**. |
| **Registers** | an instance's `registers/` | The vertical, living, shared state: the **metric**, **hypothesis**, and **risk** registers. Born once, refined down, results flow back up. |
| **Library** | `tool-skills/library/` | Product **methods** as skills (segmentation, pricing, jtbd, …). The plane meant to grow and be adapted per company. |
| **Statuses** | `statuses/` | Product **stages** as config: `concept-viability` · `pmf` · `growth` (extensible). Each re-prioritises goals and tool emphasis per step. |

Alongside the library sit two more `tool-skills/` planes:

| Entity | Where | What it is |
|--------|-------|------------|
| **Operations** | `tool-skills/operations/` | Runtime skills, not product methods: `handoff`, `metrics-capture`, `orchestration`, `source-intake`, `theses`. |
| **Adapters** | `tool-skills/adapters/` | The **output layer**: read the structured instance and render deliverables (`to-table`, `to-document`, `to-deck`). |

---

## The six steps

A **step** is a folder `steps/<n>-<slug>/` holding a thin `README.md` (goal · gate · touchpoints ·
skeleton · cadence) and a `template.md` (the artifact's shape). The `<slug>` matches the artifact's
stem for **every** step.

| # | Step (`slug`) | Artifact |
|---|---------------|----------|
| 1 | **concept** | `1-concept.md` |
| 2 | **analysis** | `2-analysis.md` |
| 3 | **strategy** | `3-strategy.md` |
| 4 | **strategic-plan** | `4-strategic-plan.md` |
| 5 | **tactical-plan** | `5-tactical-plan.md` |
| 6 | **sprint-plan** | `6-sprint-plan.md` |

---

## Inside a step

| Entity | Notation | What it is |
|--------|----------|------------|
| **Artifact** (clean copy) | `<n>-<slug>.md` | The step's output: a **projection** of the worklogs into the template's fixed shape — the form a human reviews and signs. Its template is `steps/<n>-<slug>/template.md` (`node_type: artifact-template`). |
| **Section** | `## Title {#anchor}` | One unit of an artifact. The `{#anchor}` is its **stable identity** — rename the heading text freely, keep the anchor. |
| **Gate item** | `artifact#section` | A soft checklist entry that validates one section, e.g. `concept#idea`. Gates report what's open; they never block descent. |
| **Tool marker** | `<!-- tool: X -->` | Names the library method that fills a section (and the drill-through target: skill folder + worklog). Multi-tool form `<!-- tool: A, B -->`, first is primary. |
| **Column key** | `<!--c:key-->` | A table column's **stable key**, read instead of its header prose — so the column is found in any language. A table is all-keyed or none (linter check O). |
| **Synthesis section** | `<!-- synthesis -->` | A section with no method — the orchestrator's own reasoning; its worklog is the reserved `<step-folder>/synthesis.md`. |

**The three homes of a column key:** the **step template**, the **instance section** that carries it,
and the **registers**. Never a method's `template-fragment.md` (no consumer, no key). See
`process/CONVENTIONS.md` → *Column keys*.

---

## A tool (library method)

A **tool** is one skill folder `tool-skills/library/<tool>/`. One id threads the section marker, the
folder, and the worklog file.

| File | What it is |
|------|------------|
| `SKILL.md` | what it is · when to apply · **prerequisites** · how · anti-patterns; frontmatter declares `produces` (section id(s) or a file). |
| `template-fragment.md` | the section the method produces, with source + confidence markers (the *draft's* shape — carries **no** column keys). |
| `questions.yaml` | the interview that gathers the method's inputs. |
| `references/` | deeper method notes (optional). |

---

## An instance (one product's working area)

| Entity | Where | What it is |
|--------|-------|------------|
| **Instance** | `product-loops/` (a host repo), `instances/<name>/` (a dev repo, gitignored), or `examples/<name>/` | One product's folder: config, state, artifacts, worklogs, registers, sources. Discovered by **marker** (`config.yaml`/`state.yaml`/`registers/`), never by folder name. |
| **`config.yaml`** | instance root | Human-authored, rarely changes: `product` (the product's **name**), `language`, `active_status`, `directions`, `delegation`, metric source slots. |
| **`state.yaml`** | instance root | Agent-written each pass: `current_step`, `last_pass`, and the **gate ticks** (`artifact#section: done`). The single home of cycle position. |
| **Worklog** | `<step-folder>/<tool>.md` | The **source of truth** for a method: inputs, reasoning, numbers, open items. Free-form (`node_type: worklog`); the artifact section is its projection. One per method that fills a section. |
| **`sources/`** | instance | Converted copies of the product's materials + `INDEX.md`; access notes and dated evidence. Raw captures and secrets never go under version control. |
| **`HANDOFF.md`** | instance | Session-to-session state transfer, written by the `handoff` operations skill. |
| **`deliverables/`** / **`outputs/`** | instance | Adapter render outputs — regeneratable views, not source. |

**The three document layers** (do not confuse them): the **worklog** is where the work is done; the
**registers** are the canon for the `H-`/`R-`/`M-` ids; the **artifact** is the projection
a human signs. A value lives in exactly one home.

---

## Roles & delegation

| Entity | What it is |
|--------|------------|
| **Orchestrator** | The agent holding the human's session. It owns every **shared** write — the projection (artifact sections), the registers, `state.yaml`, the gate ticks, and the change log. The only subagent that writes at all is `loops-draft`, and only its own worklog. |
| **Subagent** | A spawned worker with a narrow write rule. `loops-draft` **writes exactly one file** — its method's worklog (the draft) — and nothing else; `loops-gather` / `loops-research` / `loops-verify` **write nothing** and return text. Enforced on Claude Code: only `loops-draft` carries a `Write` tool (linter check N). |
| **Acceptance passport** (a.k.a. *return passport*) | The numbered checklist a subagent's return is scored against **before** its content is used. A return that fails its passport is not integrated. (This is the **only** meaning of "passport" in the framework — see Renames.) |
| **Direction** | An execution stream in Steps 5–6 (default `development` · `go-to-market` · `back-office`), editable per instance. Named `go-to-market`, not `growth`, to avoid colliding with the `growth` **status**. |

---

## Renames (2026-08-15)

Names changed to remove desyncs. Old names still appear in git history and in the not-yet-rebuilt
`examples/`.

| Old | New | Why |
|-----|-----|-----|
| Step 1 directory `steps/1-idea/` | `steps/1-concept/` | Match the artifact stem, like every other step; "concept" says what the step is. |
| Step-1 artifact `1-passport.md` (slug `passport`) | `1-concept.md` (slug `concept`) | Same stem as the step directory — removes the `1-passport/`-vs-`1-idea/` worklog-folder trap. |
| Section `{#concept}` (Step 1's first section) | `{#idea}` | Frees the artifact-level `concept` name; avoids the `concept#concept` gate-key clash. Still filled by `concept-formation`. |
| Instance folder `product/` | `product-loops/` | `product/` collides with a folder many product repos already have. Legacy `product/` is still recognised. |
| "passport" = **two** things (Step-1 artifact **and** the delegation acceptance spec) | "passport" = **one** thing (the acceptance spec) | The artifact is now `concept`, so the word is unambiguous. |
