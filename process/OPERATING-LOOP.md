---
node_type: operating-loop
title: Operating Loop — how the agent runs one pass of a step
status: draft
version: 0.6.0
updated: 2026-08-09
---

# Operating Loop

This is the **runtime** that ties the four planes together. Everything else (steps, statuses,
library, registers, conventions) is data this loop consumes. One pass produces or updates one
part of one step's artifact. The agent repeats the loop, item by item, step by step.

> The golden rule holds throughout: **the agent prepares, the human decides.** The loop never
> silently invents — it drafts (⚙️), asks, or marks `— to clarify —`.

## The loop, step by step

**0 · Orient.**
Read the **active status** from `product/config.yaml` and the **current step** + **gate ticks** from
`product/state.yaml` (e.g. `current_step: 3`). Both are **read, not guessed** — `state.yaml` is the
home of the cycle's position, so a fresh session resumes without asking. If `state.yaml` is missing,
reconstruct it from the artifacts and confirm with the human.

**1 · Focus.**
Read the step's **gate checklist** and the **goals the active status sets for this step**
(status › per_step › goals). Propose to the human which checklist item / artifact section to
create or update next. The human can redirect.

> **Empty `per_step` for this step?** (goals/tools still `— to define —`.) Do **not** block:
> work by the **step defaults**, and at *Update state* (step 7) the agent **must propose filling
> that status's `per_step`** from what this pass just learned — so statuses get completed as a
> by-product of the first run through each stage, never left as standing stubs.

**2 · Recommend tools.**
Offer the tools tied to that item, **filtered by step and status**:
- the **step** gives the default tool for the section (step › skeleton);
- the **status** refines it for the stage (status › per_step › tools) — e.g. at
  `concept-viability` step 1 pains come from *interviews + analytics search*, at `growth` from
  *internal product metrics*.
- **Rule:** prefer the status's per-step tools when present; otherwise the step default. The
  human may pick any tool.

**3 · Check the tool's prerequisites.**
Every tool declares a **prerequisites checklist** — the info / artifacts / access it needs.
The agent checks what is already available from the source slots (git · metrics · kb ·
prior artifacts) against that checklist.

**4 · Fill gaps.**
For each missing prerequisite, the agent either **asks the human to provide it**, or **offers
to help develop or obtain it** (draft the analysis, prepare an interview guide, write the
access request). It does not proceed on a guessed input.

**5 · Clarify (in writing).**
Once inputs are in, if any **product decisions** are still open, the agent asks concise written
questions — each with 2–4 options and a ⚙️ recommended default — and **waits**. Technical /
implementation gaps are not asked; they are noted as forks in the artifact.

**6 · Act.**
With no blank spots, the agent follows the tool's `SKILL.md` instructions and fills its
`template-fragment.md` into the artifact section — tagging every claim with a source and
confidence per `CONVENTIONS.md`, marking its own proposals ⚙️. Gathering and drafting inside this
step may be **delegated to subagents** (see *Delegation* below); the writing never is.

**7 · Update state.**
The agent then:
- **records progress in `product/state.yaml`** — ticks the step's **gate checklist** items now
  satisfied (each keyed by its `artifact#section` target — see the step README's gate checklist) and
  sets `current_step` / `last_pass`. `state.yaml` is rewritten every pass; it is the single home of
  cycle position and ticks;
- **seeds / updates the registers** (hypotheses, risks, metric nodes) with stable IDs;
- adds a dated **change-log** entry (from → to · why · trigger);
- surfaces what remains open (`— to clarify —`);
- **reports its own friction** — appends to the instance's `FRICTION.md` wherever the loop, a skill
  or a rule got in the way this pass. Nothing to report is itself the report: say so. Procedure:
  the **`friction-log`** operations skill (`tool-skills/operations/friction-log/`).

**8 · Loop or bubble.**
Move to the next checklist item / section, or the next step. If this pass **invalidated** a
higher or lower artifact (e.g. a refuted hypothesis, a changed segment), raise that as a
trigger per the step's cadence & invalidation rules — the loops feed each other both ways.

## Instance state: `config.yaml` vs `state.yaml`

Two files at the instance root, deliberately split by **who writes them and how often**:

- **`config.yaml`** — *human-authored, rarely changes*: language, `active_status`, work directions,
  metric source slots. Decisions, not progress.
- **`state.yaml`** — *agent-written every pass*: `current_step`, `last_pass`, and the **gate ticks**.
  It is the home of the cycle's **position** — never rules or product truth (those live in the
  artifacts and registers). Keeping the frequent automatic write out of `config.yaml` is what stops
  an agent from ever clobbering the human's decisions.

A **gate item's stable id is its `artifact#section` target** (unique within a step — see each step
README's gate checklist); where an item spans or repeats sections it carries an explicit `tick-id`.
That id is its key in `state.yaml`. Tick values: `done` · `open` · `n/a` · `deferred`.

## What each plane contributes to a pass

| Plane | What the loop reads from it |
|-------|----------------------------|
| **Step** | goals · gate checklist (tied to artifact sections) · artifact skeleton · default tool per section · register touchpoints · cadence/invalidation |
| **Status** | per-step goals (focus) · per-step tool emphasis (which method fits this stage) · gate emphasis |
| **Tool-skill** (`tool-skills/library/`) | prerequisites checklist · method (how) · template-fragment · questions |
| **Registers** | current hypotheses / risks / metric nodes to read and update |
| **Conventions** | confidence tags · sources · section IDs · links · change-log format |

## Session handoff (state transfer between sessions/agents)

The loop assumes one continuous context; reality restarts. **Cycle position (current step, gate
ticks) persists in `state.yaml`** — a fresh session resumes from it directly. For everything
`state.yaml` doesn't hold (environment/access checks, open forks in flight), whenever a session
boundary approaches run the **`handoff` operations skill** (`tool-skills/operations/handoff/`) to
write/update the instance's `HANDOFF.md` — *before* the boundary, not after:

- **Environment change needs a restart** (MCP config, extensions, tokens) → write the handoff,
  tell the human what to do, restart, then verify the handoff's "Environment & access" checks.
- **End of session / task transfer / imminent context compaction** → same.

Two hard rules, learned from failures:
1. A handoff restores **state, not rules** — its reading order must send the next agent through
   `process/` first. An agent resuming from a handoff alone will violate the loop (typically
   step 7: registers not updated).
2. A source-gathering errand (pulling metrics, fetching docs) is still a **pass of this loop**: it
   ends with step 7 — register updates, a change-log entry, open items surfaced. "I only collected
   data" does not skip Update state. For metric values the procedure is the **`metrics-capture`**
   operations skill (`tool-skills/operations/metrics-capture/`).

## Delegation (orchestrator ↔ subagents)

One pass may be run by **more than one agent**. The agent holding the human's session is the
**orchestrator**; every agent it spawns is a **subagent**. The reason for the split is narrow:
*gathering* fills a context window, and a full context is where an agent starts skipping loop steps.
Delegation moves the gathering out and keeps the reasoning in. It does **not** save tokens — every
subagent re-reads what it needs — it buys the orchestrator a context that stays clear enough to think.

**The write rule (absolute).** Only the orchestrator writes to the instance. Subagents read, search,
fetch and reason; they **return text**. The rule is transitive: a subagent may spawn its own
subagents, and none of them writes either. This is what removes the two failure modes delegation
would otherwise add — concurrent register writes colliding over id allocation, and a gate ticked by
an agent that never read the gate.

**Never delegated**, however busy the orchestrator is:

- a **fork with the human** — the agent prepares, the human decides, and a subagent has neither the
  human nor the context to decide in their place. It returns the options; it never picks;
- **register id allocation and register writes**, and **gate ticks in `state.yaml`**;
- the **Step 1–4 reasoning chain** — one argument, where Step 3 is entitled to contradict Step 2.
  Cut into parallel pieces it loses exactly the coherence it exists for.

**Delegatable task kinds** — a closed list; anything else stays with the orchestrator:

| Kind | The subagent is given | It returns |
|------|-----------------------|------------|
| `gather` | one source + the question the number/fact must answer | dated tagged values + what it could not reach |
| `research` | one question + its scope and stop condition | a sourced digest, every claim tagged |
| `draft` | one library method + the inputs it needs | proposed section text, ⚙️-marked, written nowhere |
| `verify` | one artifact/section + the checklist to hold it against | findings: file · anchor · what fails · why |

**A brief is a scoped handoff.** Same problem as a session handoff — give a fresh agent enough state
without giving it your context — so it is the same mechanism, narrowed: reading order first, then
scope, inputs, the return contract, and the **non-negotiables block** the subagent works under. A
subagent that is read-only does not need the whole canon (registers, change logs, gate ticks are not
its to touch), but it does need the rules that make its output usable: never invent, tag every claim,
mark proposals ⚙️, no secrets or PII, `— to clarify —` for a gap, and never close a fork.

**The return gate is hard.** Unlike this framework's step gates, which are soft ticks for a human,
a return is checked by the orchestrator against the **return passport** and is *not integrated* if it
fails. A failing return goes back **once** with the named defects; after the second failure the
orchestrator stops re-trying, records what is missing as `— to clarify —`, and surfaces it to the
human. Two iterations is the cap because a third is nearly always the brief's fault, not the
subagent's — rewrite the brief instead.

The procedure — how to decompose, the brief and return templates, the passport, the anti-patterns —
is the **`orchestration`** operations skill (`tool-skills/operations/orchestration/`).

## Handling a late, cross-cutting hypothesis

Sometimes a hypothesis surfaces *after* the step where it belongs — e.g. at Step 3 someone
realizes a new use-case that reframes the **concept** (Step 1). Do **not** fork the whole process
per hypothesis; the register is the single home. Escalate along a ladder, cheapest first:

| Level | Action | Use when |
|-------|--------|----------|
| **A · Register-first** | Log it in the hypothesis register with its type; tag it a **concept-variant** and an **invalidation trigger** on the step it touches; validate cheaply (a few interviews / a metric read) **before** editing the core artifact. | Default. It's a new segment / job / scenario — not a new product. |
| **B · Scoped spike** | Run the hypothesis as an **alternative lens through the affected steps only** (e.g. 1→3), in a separate `variants/<name>/` doc, then **compare to the main line** against a stated decision criterion and merge if it wins. Do **not** touch steps below the affected range. | Level-A signal is positive and the strategic implications need to be seen before committing. |
| **C · Full parallel run** | Treat it as a separate product/line and run all six steps. | Only when it is genuinely a different product, not a variant. |

Record the level chosen and the decision criterion in the change log. A spike (B) that loses is
kept, not deleted — it becomes a `[refuted: …]` note and a guard against re-litigating it.

## A worked micro-example

Active status `2-pmf`, step `1-idea`, section `problems`:
1. Focus → "update `problems` for the lead segment" (a gate item).
2. Recommend → status `pmf` says pains come from *product metrics + a few interviews*
   (vs pure interviews at `concept-viability`); tool `segment-pains`.
3. Prerequisites → `segment-pains` needs: the segment list, access to usage metrics, ≥3
   recent user conversations.
4. Gaps → metrics access is missing → agent offers to pull it via the metrics slot or asks
   for an export.
5. Clarify → "Which pain do we treat as primary for pricing — A or B? ⚙️ A." → waits.
6. Act → fills `problems` with severity × frequency, each `[sourced: metrics …]` / `[assumption]`.
7. Update → ticks the `problems` gate item, seeds `H-007` ("pain A blocks payment"), logs the change.
8. Loop → next section `solution`.
