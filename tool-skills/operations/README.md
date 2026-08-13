---
node_type: operations-index
title: Operations — runtime skills for how the agent works
status: draft
version: 0.3.3
updated: 2026-08-13
---

# Operations

Operations are **runtime skills**: they are about *how the agent runs the process*, not about the
product's content. Unlike `library/` tools (which fill a section of a step artifact) or `adapters/`
(which render deliverables), an operations skill acts on the **session and the instance's
operational state** — continuity across restarts, cadence, automation.

They are not tied to a step. They are triggered by **events** (a session boundary, an environment
change, a schedule) — the OPERATING-LOOP and each skill's own file define those triggers.

## Skills

| Skill | What it does | Triggered by | Authority for the mechanism |
|-------|--------------|--------------|-----------------------------|
| [`handoff`](handoff/SKILL.md) | Write/update the instance's `HANDOFF.md` so a fresh agent resumes without re-asking the human | session boundary · environment change needing restart · imminent compaction · on request | [`process/OPERATING-LOOP.md`](../../process/OPERATING-LOOP.md) → "Session handoff" |
| [`metrics-capture`](metrics-capture/SKILL.md) | Turn a source into dated rows in `metrics.csv` plus the living method file that makes them reproducible | a step/gate needs a value the register lacks · a hypothesis enters `testing` · a reading went stale · the source changed · on request | [`process/REGISTERS.md`](../../process/REGISTERS.md) → "Metric register" + [`process/CONVENTIONS.md`](../../process/CONVENTIONS.md) → "Raw data & access" |
| [`orchestration`](orchestration/SKILL.md) | Run one pass with subagents: cut the work, write the brief, score the return against its passport, integrate it | the pass is wider than one context (many sources, many directions) · an artifact needs checking by someone who did not write it · on request | [`process/OPERATING-LOOP.md`](../../process/OPERATING-LOOP.md) → "Delegation" |
| [`source-intake`](source-intake/SKILL.md) | Dispatch a raw `sources/` file into the step worklog(s) it informs and cite it there, so no artifact ever links a source directly | product setup (legacy sources) · a new file lands in `sources/` · a source changed · on request | [`process/CONVENTIONS.md`](../../process/CONVENTIONS.md) → "Raw data & access" + "Step folders & worklogs" |
| [`theses`](theses/SKILL.md) | Walk the human through a step's section results (its theses) for sign-off and stamp `<!-- confirmed: date -->` — the semantic half of the two-layer check | operating-loop step 7 (results just worked) · a section was re-projected · on request | [`process/OPERATING-LOOP.md`](../../process/OPERATING-LOOP.md) → step 7 + [`process/CONVENTIONS.md`](../../process/CONVENTIONS.md) → "Section confirmation" |

The list is a starting set. Candidate future operations skills (not yet authored): a metrics
**collection schedule** (when to pull which metric — `metrics-capture` runs one pass, it does not
decide the cadence), and **automation** wiring for aggregators.

## Anatomy

An operations skill follows the same folder anatomy as a library tool — `SKILL.md`
(what · when · how · anti-patterns + frontmatter wiring), and any `template-fragment.md` /
`questions.yaml` it needs. The difference is classification, not packaging: its `used_by_steps` is
typically `any`, and it reads/writes the instance's operational state rather than a step section.

**Rules stay in the core.** Where an operations skill has normative behavior (e.g. the handoff
reading order, the "state not rules" guarantee), the authority is `process/` — the skill file
carries the *form* and points to the core for the *rule*, so there is one source of truth.
