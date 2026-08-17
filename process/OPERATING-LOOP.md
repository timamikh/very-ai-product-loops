---
node_type: operating-loop
title: Operating Loop — how the agent runs one pass of a step
status: draft
version: 0.11.0
updated: 2026-08-18
---

# Operating Loop

This is the **runtime** that ties the four planes together. Everything else (steps, statuses,
library, registers, conventions) is data this loop consumes. One pass produces or updates one
part of one step's artifact. The agent repeats the loop, item by item, step by step.

> The golden rule holds throughout: **the agent prepares, the human decides.** The loop never
> silently invents — it drafts (⚙️), asks, or marks `— to clarify —`.

## The loop, step by step

**0 · Orient.**
Read the **active status** from `product-loops/config.yaml` and the **current step** + **gate ticks** from
`product-loops/state.yaml` (e.g. `current_step: 3`). Both are **read, not guessed** — `state.yaml` is the
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
  human may pick any tool. A status's `tools:` list holds **library methods only** — *how the data
  is gathered* (interviews, metrics pulls) is named in the status's goals prose, not the list
  (linter check V).

**3 · Check the tool's prerequisites — and size the pass.**
Every tool declares a **prerequisites checklist** — the info / artifacts / access it needs.
The agent checks what is already available from the source slots (git · metrics · kb ·
prior artifacts) against that checklist. The volume is now visible — how many sources, how large,
how many independent parts — so the agent decides **here, aloud**: split this pass across
subagents or run it alone, and why. The test is the observable volume, never "wider than one
context" — that one can only be checked after the context is already spent. The contract is
*Delegation* below; the split work itself happens at step 6.

**4 · Fill gaps.**
For each missing prerequisite, the agent either **asks the human to provide it**, or **offers
to help develop or obtain it** (draft the analysis, prepare an interview guide, write the
access request). It does not proceed on a guessed input.

**5 · Clarify (in writing).**
Once inputs are in, if any **product decisions** are still open, the agent asks concise written
questions — each with 2–4 options and a ⚙️ recommended default — and **waits**. Technical /
implementation gaps are not asked; they are noted as forks in the artifact.

**6 · Act — directly or through subagents.**
With no blank spots, the agent follows the tool's `SKILL.md` and does the working in the tool's
**worklog** — `<step-folder>/<tool>.md` (e.g. `2-analysis/market-sizing.md`): the inputs it reached,
the reasoning, the numbers, the open items. This worklog is the **source of truth** for the method.
The **artifact section** is a **projection** of it into the fixed schema of its `template-fragment.md`
— the conclusion in shape, not the working; it never holds anything the worklog does not. Every claim
in both carries a source and confidence per `CONVENTIONS.md`, with the agent's own proposals ⚙️.
(One method → one worklog → one section; the mechanism is `CONVENTIONS.md` → *Step folders & worklogs*.)
The **procedure** of that writing move — the fragment shape, tags carried verbatim, the section's
`<!-- card -->` headline, sign-off markers dropped on a changed conclusion — is the
[`projection`](../tool-skills/operations/projection/SKILL.md) operations skill.

If step 3 decided to split, this is where the split runs: one **brief** per part (the task, the
context and where to find it, the allowed tools, the return shape — procedure in the
`orchestration` operations skill), subagents spawned, and **every return scored against its
passport before its content is used** — one remediation round with the defects named, then stop
and mark the gap `— to clarify —`. A `draft` subagent does the method's working and **writes its own
worklog**; `gather`, `research` and `verify` are delegated as return-only. What is **never** delegated
is the writing the orchestrator owns: the **projection** of the worklog into the artifact section, the
**registers**, `state.yaml`, the gate ticks and the change log. (If `config.yaml` sets `delegation:
off`, the orchestrator runs the pass itself and writes the worklog directly — no subagents.)

Two obligations to the human before anything lands on disk:
- **Show reasoning first.** A section that rests mainly on the agent's own reasoning or on the
  human's spoken answer is shown **in chat, in full, before it is written** — the human reacts to
  a draft, not to a fait accompli. A section that restates a source needs no preview.
- **Declare the write perimeter.** In the same message, name the files this pass will touch — now
  the step's **worklog** as well as the artifact, the registers and `state.yaml`. What gets written
  must never be a surprise.

**7 · Update state.**
Only after every delegated return is accepted and any preview is answered, the agent writes:
- **records progress in `product-loops/state.yaml`** — ticks the step's **gate checklist** items now
  satisfied (each keyed by its `artifact#section` target — see the step README's gate checklist) and
  sets `current_step` / `last_pass`. `state.yaml` is rewritten every pass; it is the single home of
  cycle position and ticks. A tick on a section that rests mainly on the agent's own reasoning is
  placed only after a `verify` subagent — one that did not write the section — has checked it
  (the human may waive this explicitly; if the runtime cannot spawn agents, the tick stays `open`
  and the reason is surfaced);
- **seeds / updates the registers** (hypotheses, risks, metric nodes) with stable IDs;
- **confirms the step's results with the human** — a section is a *thesis*, and the
  [`theses`](../tool-skills/operations/theses/SKILL.md) skill walks the human through each written
  section's conclusion for sign-off, stamping `<!-- confirmed: <date> -->` (CONVENTIONS → *Section
  confirmation*). This is the **semantic** half of the two-layer check — the linter holds a section's
  structure, the human holds its meaning — and it is never self-issued. A section re-projected later
  drops its marker and is re-confirmed. This step-7 sign-off runs at `scope: step`; a **big**
  re-projection or a **step change** calls the same skill at `scope: instance`, which additionally
  clears cross-step *rests-on* debt (a confirmed thesis standing on an unsigned foundation);
- adds a dated **change-log** entry (from → to · why · trigger);
- surfaces what remains open (`— to clarify —`).

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

## Delegation (orchestrator ↔ subagents) — the contract

One pass may be run by **more than one agent**. The agent holding the human's session is the
**orchestrator**; every agent it spawns is a **subagent**. This section is the contract both roles
obey; the moving parts live in the loop itself — the split **decision** at step 3, the briefs and
return acceptance at step 6, the verify-before-tick rule at step 7.

The reason for the split is narrow: *gathering* fills a context window, and a full context is where
an agent starts skipping loop steps. Delegation moves the gathering out and keeps the reasoning in.
It does **not** save tokens — every subagent re-reads what it needs — it buys the orchestrator a
context that stays clear enough to think.

**The write rule.** The instance is split into what a subagent may write and what only the orchestrator
may. A **`draft` subagent writes exactly one file — its method's worklog** `<step-folder>/<method>.md`
(the draft where the method's working lives), and nothing else. `gather`, `research` and `verify`
subagents write nothing at all; they read, search, fetch, reason, and **return text**. Everything that
is not a draft's own worklog stays the orchestrator's alone: the **artifact** (the chistovik the human
signs), the **registers**, the **projection** of each worklog into its section, `state.yaml`, the gate
ticks and the change log. The rule is transitive: a subagent may spawn its own subagents, and the only
file anything below the orchestrator may write is a `draft`'s own worklog.

This split is what keeps the two failure modes delegation would otherwise add from returning. A worklog
**allocates no register id** — a draft that implies a hypothesis describes it in words, and the
orchestrator mints the id when it writes the register row and projects the section — so concurrent
subagents never collide over id allocation. And no subagent touches `state.yaml`, so a gate is never
ticked by an agent that did not read it.

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
| `draft` | one library method + the inputs it needs | its method's **worklog** (the draft), written by the subagent; ⚙️-marked — plus a summary + passport for the orchestrator to check before projecting |
| `verify` | one artifact/section + the checklist to hold it against | findings: file · anchor · what fails · why |

**A brief is a scoped handoff.** Same problem as a session handoff — give a fresh agent enough state
without giving it your context — so it is the same mechanism, narrowed: reading order first, then
scope, inputs, the return contract, and the **non-negotiables block** the subagent works under. A
subagent does not need the whole canon (registers, change logs and gate ticks are never its to touch —
a `draft` writes only its worklog, and the worklog conventions it needs come with the method's
`SKILL.md`), but it does need the rules that make its output usable: never invent, tag every claim,
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

A hypothesis that surfaces *after* the step where it belongs is placed **via the register, never by
forking the process** — escalate along a cheapest-first ladder (register-first → scoped spike → full
parallel run). The ladder, its triggers and the decision-criterion rule are in
[`reference/late-hypothesis.md`](reference/late-hypothesis.md).

## A worked micro-example

The loop shown end-to-end on one concrete pass (status `2-pmf`, step `1-concept`, section `problems`)
is [`reference/worked-example.md`](reference/worked-example.md).
