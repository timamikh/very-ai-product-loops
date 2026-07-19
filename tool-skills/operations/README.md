---
node_type: operations-index
title: Operations — runtime skills for how the agent works
status: draft
version: 0.1.0
updated: 2026-07-19
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

The list is a starting set. Candidate future operations skills (not yet authored): a metrics
**collection schedule** (when to pull which metric), and **automation** wiring for aggregators.

## Anatomy

An operations skill follows the same folder anatomy as a library tool — `SKILL.md`
(what · when · how · anti-patterns + frontmatter wiring), and any `template-fragment.md` /
`questions.yaml` it needs. The difference is classification, not packaging: its `used_by_steps` is
typically `any`, and it reads/writes the instance's operational state rather than a step section.

**Rules stay in the core.** Where an operations skill has normative behavior (e.g. the handoff
reading order, the "state not rules" guarantee), the authority is `process/` — the skill file
carries the *form* and points to the core for the *rule*, so there is one source of truth.

## Change log

### 2026-07-19 — created
- **From → To:** — → `operations/` plane; `handoff` moved here from `library/handoff/`.
- **Why:** `handoff` is a runtime capability, not a product method; the library is now product
  methods only. Room to grow (scheduling, automation) without bloating the library or the core.
- **Trigger:** restructure discussion, 2026-07-19.
