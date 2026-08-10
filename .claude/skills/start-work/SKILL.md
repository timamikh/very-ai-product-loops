---
name: start-work
description: >
  Begin or resume product work on a very-ai-product-loops instance (not onboarding — use
  product-setup for first run). Self-bootstraps the rules (does NOT trust AGENTS.md auto-load, which
  doesn't fire when invoked as a skill or from another session), orients on the instance state, then
  runs the operating loop ONE pass at a time — one section produced through its method, never a bulk
  fill. Use at the start of any working session, on resume after a restart/compaction, or when
  picking up an instance someone else set up.
status: draft
version: 0.2.0
updated: 2026-08-10
---

# Start work (begin / resume a session)

The reliable entry point into the working loop. Onboarding (`product-setup`) sets a product up once;
**this skill runs every working session after that.** Its whole job is to make sure the rules are
loaded and the agent works the disciplined loop instead of bulk-filling.

> Golden rule holds: **the agent prepares, the human decides.** One section per pass, drafts are ⚙️,
> real product forks are 2–4 options + a recommendation and then you **wait**; gaps stay `— to clarify —`.

## Step 0 — bootstrap the rules (before anything)

**Do not trust auto-load.** When this skill is invoked (or the repo wasn't opened as a fresh
session, or on a tool that auto-loads nothing), the framework's root `AGENTS.md` was not read for you. So load the rules
yourself, in order, before touching any artifact:
`process/OVERVIEW.md` → `OPERATING-LOOP.md` → `CONVENTIONS.md` → `REGISTERS.md`. These are the
authority for everything below — this skill only walks you into them, it does not restate them.

**Check delegation availability, now.** The loop delegates gathering, drafting and verification to
subagents (`loops-gather` · `loops-research` · `loops-draft` · `loops-verify`). Confirm two things
before the first pass and tell the human if either fails:
1. the `loops-*` agent types are visible to this session — definitions vendored mid-session are
   picked up only on the **next** session start; if absent, ask the human to restart;
2. spawning agents is permitted — the host repo's root `AGENTS.md` carries the owner's standing
   approval (written at install); if this session is still restricted, say so: every pass then runs
   solo and gate ticks that need a `verify` stay `open`. Never work around it silently.

## Step 1 — Orient (read state, never guess)

Read the instance's current state (state, not rules — verify it against the registers/artifacts):

1. **`HANDOFF.md`** (if present) — where the last session left off. It restores *state, not rules or
   truth*; treat anything older than its last change-log entry as suspect, and run its
   "Environment & access" checks before relying on them.
2. **`config.yaml`** — `active_status`, `language`, `directions`, source slots.
3. **`sources/INDEX.md`** — the knowledge map; open only the sources a task needs, not the whole folder.
4. Determine the **active status** and the **current step**. Both are read, not guessed; if unclear, ask.

Then read only what this task needs: the current step's `README.md` (its gate checklist + skeleton)
and the active status's `per_step[N]` (goals + tool emphasis). Do not pre-load the whole framework.

## Step 2 — Run ONE pass of the operating loop

`OPERATING-LOOP.md` is the authority; one pass produces or updates **one** section / gate item:

1. **Focus** — propose the single next section/gate item (the human may redirect).
2. **Recommend the tool** — from the status `per_step` tools first, else the step default.
3. **Check prerequisites and size the pass** — **open that tool's `SKILL.md`** under
   `tool-skills/library/` and read its prerequisites. Filling from `template.md` without opening the
   method is the failure this skill exists to prevent. The volume is now visible — decide **aloud**:
   split this pass across subagents or run it solo, and why.
4. **Fill gaps** — for each missing input, ask the human or offer to obtain it; never guess an input.
5. **Clarify** — only real **product** decisions, each as 2–4 options + a ⚙️ recommendation, then
   **wait**. Technical/implementation gaps are not asked — note them as forks in the artifact.
6. **Act — directly or through subagents** — produce the section via the tool's
   `template-fragment.md`, tagging every claim with a source + confidence per `CONVENTIONS.md`;
   mark your own proposals ⚙️. If step 3 said split: brief each subagent (task · context · tools ·
   return shape) per the **`orchestration`** operations skill and score every return against its
   passport before using it. A section built mainly on your own reasoning or the human's spoken
   answer is **shown in chat before it is written**, together with the list of files this pass will
   touch.
7. **Update state** — only now write: the section, registers (`H-…`/`R-…`/`M-…`), a dated
   change-log entry, what's still `— to clarify —`. A tick on a reasoning-based section waits for
   a `verify` subagent's findings (the human may waive this).
8. **Loop or bubble** — propose the next pass; if this pass invalidated a higher/lower artifact,
   raise it as a trigger per the step's cadence/invalidation rules.

**Hard rule: one section per pass.** Propose the next section and let the human steer — do **not**
barrel through the artifact set in one go. A bulk fill bypasses the method, the prerequisites, and
the human's decisions all at once (see anti-patterns).

**Delegation is the loop's default posture, not an exception:** subagents gather, research, draft
and verify; **only you write** — they never edit a file, close a fork or tick a gate, and a return
that fails its passport is not integrated. The contract is canon (`process/OPERATING-LOOP.md` →
*Delegation*); the procedure is `tool-skills/operations/orchestration/`. The one case not to
delegate: the pass fits comfortably in one context — delegation costs more tokens, not fewer.

## Step 3 — At a session boundary

Before context compaction, a restart, an environment change, or end of session, run the **`handoff`**
operations skill (`tool-skills/operations/handoff/`) to write/update `HANDOFF.md` *before* the
boundary — so the next `start-work` can resume cleanly.

## Anti-patterns

- **Trusting auto-load.** Starting work without Step 0 because "AGENTS.md is in the repo" — it isn't
  in context unless it auto-loaded, which a skill invocation / cross-session start does not do.
- **Bulk-filling.** Producing several sections (or a whole "first cycle") in one pass. One section,
  one method, one pass — then propose the next.
- **Template without method.** Filling `template.md` sections without opening each one's `SKILL.md`.
- **Working from the handoff alone.** It restores state, not rules — Step 0 still runs first.
- **Letting a subagent write.** Even "just the register row". Two agents allocating `H-0xx` at once
  is a corrupted register, and the fix costs more than the delegation saved.
- **Asking technical gaps as forks.** Only product decisions become 2–4 options; implementation gaps
  are noted as forks in the artifact, not put to the human.
