---
node_type: operating-loop
title: Operating Loop — how the agent runs one pass of a step
status: draft
version: 0.12.0
updated: 2026-08-18
---

# Operating Loop

The **runtime** that ties the four planes together; everything else (steps, statuses, library,
registers, conventions) is data this loop consumes. One pass produces or updates one part of one
step's artifact; the agent repeats the loop, item by item, step by step.

> The golden rule holds throughout: **the agent prepares, the human decides.** The loop never
> silently invents — it drafts (⚙️), asks, or marks `— to clarify —`.

## The loop, step by step

**0 · Orient.**
Read the **active status** from `product-loops/config.yaml` and the **current step** + **gate
ticks** from `product-loops/state.yaml` — both **read, not guessed**. If `state.yaml` is missing,
reconstruct it from the artifacts and confirm with the human. The two files split by who writes
them: **`config.yaml`** is the human's decisions (rarely changes); **`state.yaml`** is agent-written
every pass — the single home of cycle **position** (`current_step`, `last_pass`, ticks), never rules
or product truth. A gate item's stable id is its **`artifact#section`** target (an explicit
`tick-id` where an item spans or repeats sections); tick values: `done` · `open` · `n/a` ·
`deferred`.

**1 · Focus.**
Read the step's **gate checklist** and the **active status's goals for this step**
(status › per_step › goals). Propose which checklist item / artifact section to work next; the human
can redirect. **Empty `per_step` for this step?** Do not block: work by the step defaults, and at
step 7 **propose filling that status's `per_step`** from what the pass just learned.

**2 · Recommend tools.**
Offer the tools tied to that item: the **step** gives the section's default (step › skeleton), the
**status** refines it for the stage (status › per_step › tools). **Prefer the status's per-step
tools when present**; the human may pick any. A status's `tools:` list holds **library methods
only** — how data is gathered lives in the goals prose, not the list (check V).

**3 · Check the tool's prerequisites — and size the pass.**
Check the tool's **prerequisites checklist** against the source slots (git · metrics · kb · prior
artifacts). **Pull the register rows this pass needs as inputs** — open `H-` items on the section's
theme, live `R-` items, the metric nodes it touches; when field semantics or gradations are in
doubt, read [`REGISTERS.md`](REGISTERS.md). The volume is now visible, so decide **here, aloud**:
split this pass across subagents or run it alone, and why — the test is the observable volume,
never "wider than one context". The contract is *Delegation* below; the split itself runs at step 6.

**4 · Fill gaps.**
For each missing prerequisite, **ask the human** or **offer to help obtain it**. Never proceed on a
guessed input.

**5 · Clarify (in writing).**
If any **product decisions** are still open, ask concise written questions — each with 2–4 options
and a ⚙️ recommended default — and **wait**. Technical/implementation gaps are not asked; they are
noted as forks in the artifact.

**6 · Act — directly or through subagents.**
Follow the tool's `SKILL.md` and do the working in the tool's **worklog** —
`<step-folder>/<tool>.md`. The worklog is the **source of truth**; the **artifact section is its
projection** — the conclusion in shape, never holding anything the worklog does not, every claim
tagged per `CONVENTIONS.md`, proposals ⚙️. (Resolution rules — CONVENTIONS → *Step folders &
worklogs*.) The writing move is the
[`projection`](../tool-skills/operations/projection/SKILL.md) operations skill.

If step 3 decided to split, the split runs here: one **brief** per part, subagents spawned, **every
return scored against its passport before its content is used** — the procedure is the
`orchestration` operations skill; the contract is *Delegation* below.

Two obligations to the human **before anything lands on disk**:
- **Show reasoning first.** A section resting mainly on the agent's own reasoning or the human's
  spoken answer is shown **in chat, in full, before it is written**. A section that restates a
  source needs no preview.
- **Declare the write perimeter.** The same message names every file this pass will touch — worklog,
  artifact, registers, `state.yaml`. What gets written is never a surprise.

**7 · Update state.**
Only after every delegated return is accepted and any preview answered:
- **tick the gate items** now satisfied in `state.yaml` (keyed by `artifact#section`) and set
  `current_step` / `last_pass`. A tick on a section resting mainly on the agent's own reasoning is
  placed only after a `verify` subagent — one that did not write it — has checked it (the human may
  waive this explicitly; if the runtime cannot spawn agents, the tick stays `open` and the reason is
  surfaced);
- **seed / update the registers** with stable ids — **before writing rows, read**
  [`REGISTERS.md`](REGISTERS.md) (schemas, id discipline, the csv rule);
- **propose the human's sign-off of the step's theses** — the
  [`theses`](../tool-skills/operations/theses/SKILL.md) operations skill walks each written section
  (`scope: step`; a big re-projection or a step change → `scope: instance`);
- add a dated **change-log** entry (from → to · why · trigger);
- surface what remains open (`— to clarify —`).

> **Do not leave step 7** until: ticks keyed by `artifact#section` set ⊕ registers updated ⊕
> theses sign-off proposed ⊕ change-log entry written ⊕ open items surfaced. A gathering-only
> errand is still a pass — "I only collected data" does not skip this step.

**8 · Loop or bubble.**
Move to the next item or step. If this pass **invalidated** a higher or lower artifact (a refuted
hypothesis, a changed segment), raise it per the step's cadence & invalidation rules — the loops
feed each other both ways.

## What each plane contributes to a pass

| Plane | What the loop reads from it |
|-------|----------------------------|
| **Step** | goals · gate checklist (tied to artifact sections) · artifact skeleton · default tool per section · register touchpoints · cadence/invalidation |
| **Status** | per-step goals (focus) · per-step tool emphasis · gate emphasis |
| **Tool-skill** (`tool-skills/library/`) | prerequisites checklist · method (how) · template-fragment · questions |
| **Registers** | current hypotheses / risks / metric nodes to read and update |
| **Conventions** | confidence tags · sources · section IDs · links · change-log format |

## Session handoff (state transfer between sessions/agents)

Cycle position persists in `state.yaml`; for everything it doesn't hold (environment/access checks,
open forks in flight), run the [`handoff`](../tool-skills/operations/handoff/SKILL.md) operations
skill **before** the boundary — restart, session end, task transfer, imminent compaction. Two hard
rules: **a handoff restores state, not rules** — its reading order sends the next agent through
`process/` first; and **a source-gathering errand is still a pass of this loop** — it ends with
step 7 (for metric values, the `metrics-capture` operations skill).

## Delegation (orchestrator ↔ subagents) — the contract

One pass may be run by more than one agent: the agent holding the human's session is the
**orchestrator**; every agent it spawns is a **subagent**. Delegation moves the *gathering* out of a
context that must stay clear enough to think — it costs more tokens, never fewer.

- **The write rule.** A `draft` subagent writes **exactly one file — its method's worklog**
  `<step-folder>/<method>.md`; `gather`, `research` and `verify` write **nothing** and return text.
  Everything else is the orchestrator's alone: the **artifact**, the **registers** (a worklog
  allocates no register id — the orchestrator mints ids), the **projection**, `state.yaml`, the gate
  ticks and the change log. The rule is **transitive** down the subagent tree.
- **Never delegated:** a **fork with the human** (a subagent returns options, never picks) ·
  **register id allocation, register writes, gate ticks** · the **Step 1–4 reasoning chain** (one
  argument — cut into pieces it loses the coherence it exists for).
- **Task kinds — a closed list:** `gather` · `research` · `draft` · `verify`. Anything else stays
  with the orchestrator.
- **The return gate is hard.** Every return is scored against its **return passport** before its
  content is used; a failing return goes back **once** with the named defects, after the second
  failure stop — record `— to clarify —` and surface it. A brief carries the subagent's
  non-negotiables block verbatim (the template).
- **`delegation: off`** in `config.yaml` — or a runtime that cannot spawn agents — means **no
  subagents: the orchestrator runs every pass itself and writes the worklogs directly.** The write
  rule does not change (all shared writes were already its own); a tick that needed a `verify` then
  stays `open` with the reason surfaced (step 7).

The procedure — decomposition, the brief and return templates, the passport, the anti-patterns — is
the [`orchestration`](../tool-skills/operations/orchestration/SKILL.md) operations skill.

## Handling a late, cross-cutting hypothesis

A hypothesis that surfaces *after* the step where it belongs is placed **via the register, never by
forking the process** — the cheapest-first ladder is
[`reference/late-hypothesis.md`](reference/late-hypothesis.md).

## A worked micro-example

The loop end-to-end on one concrete pass: [`reference/worked-example.md`](reference/worked-example.md).
