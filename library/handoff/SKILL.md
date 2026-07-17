---
name: handoff
kind: template
produces: HANDOFF.md (instance root — operational state doc, not a step artifact)
prerequisites:
  - the instance exists (product/ or instances/<name>/ working area)
  - current position in the process is known (step, section, open gate items)
  - open forks and pending human decisions are known
reads_registers: [hypotheses, risks, metrics]
writes_registers: []
inputs: [kb]
used_by_steps: [any]
status: draft
version: 0.1.0
updated: 2026-07-17
---

# Handoff — session-to-session state transfer

**What it is.** A tool that writes/updates the instance's `HANDOFF.md` — the single file a
fresh agent reads to resume work after a session restart, context loss, or agent switch,
**without re-asking the human**. It restores *state*; the framework's rules restore *behavior*
(see the required reading order below — a handoff must never become a substitute for the rules).

**When to apply (triggers — see also OPERATING-LOOP → "Session handoff"):**
1. **Environment change requires a session restart** — MCP servers added/reconfigured, browser
   extensions installed, tokens issued, permissions changed. Write the handoff BEFORE the restart.
2. **End of a working session** on an instance with work in flight (an artifact mid-fill, an
   open fork awaiting the human).
3. **Context is about to be compacted / the task is being transferred** to another agent.
4. **On request** — the human says "подготовь хэндофф" / "prepare a handoff".

**How to do it.**
1. Read the current `HANDOFF.md` (if any) and the registers — carry forward what is still true,
   drop what is done, update what changed. The handoff is an **operational state doc**: unlike
   step artifacts it IS updated in place (keep `updated:` in frontmatter current and keep the
   change log at the bottom — motivations still matter; only the *state sections* are overwritable).
2. Fill every section of `template-fragment.md`. Sections that deserve special care, from
   field-tested failures:
   - **Reading order** must start with the framework rules (`process/OVERVIEW → OPERATING-LOOP →
     CONVENTIONS → REGISTERS`), *then* the handoff, *then* `sources/INDEX.md`. A handoff that
     routes straight to sources produces an agent that works without rules.
   - **Environment & access** must be *verifiable*: for each dependency record (a) what it is,
     (b) how to CHECK it works (a command / a tool call), (c) how to RECOVER it (exact install
     link, profile/account it lives under, where the token goes). "It worked yesterday" is not
     a state; extensions vanish, tokens rot, sessions expire.
   - **Open forks** carry the full 2–4 options + the ⚙️ recommendation, not just "next action" —
     the next agent must be able to present the fork again verbatim, per CONVENTIONS "Forks & options".
   - **Registers** are referenced by ID (`H-…`, `R-…`, `M-…`), never copied — the registers are
     the single home; a handoff duplicate goes stale silently.
3. Keep it under ~2 pages. A handoff is an index into the instance, not a second copy of it.
4. Tell the human the handoff is written and what (if anything) they must do across the restart
   (e.g. "restart Claude Code", "install extension X into profile Y").

**After resume (the receiving agent):** verify the Environment & access section by actually
running the listed checks before relying on it; fix and update the handoff if reality drifted.

## Anti-patterns

- **Handoff as rulebook.** Routing the next agent only to sources/tasks; the rules reading
  order must come first.
- **Unverifiable environment.** "Browser access works" without the check command and the
  recovery recipe (which profile, which extension id, where the token lives).
- **State without forks.** Recording the chosen path but not the options — the human's choice
  disappears from history and the fork can't be re-presented.
- **Register copies.** Pasting hypothesis/risk tables into the handoff instead of IDs.
- **Append-only theatre.** Treating the handoff like a step artifact and never pruning done
  items — a handoff that only grows stops being readable at exactly the moment it's needed.
