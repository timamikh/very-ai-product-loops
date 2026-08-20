<!--
  template-fragment: handoff → writes the instance-root HANDOFF.md (a whole file, not a section).
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
  The fenced block below is the HANDOFF.md file skeleton the tool emits.
-->

# HANDOFF template (instance root)

```markdown
---
node_type: handoff
product: "<product name>"
updated: <YYYY-MM-DD>
reflects: "<the newest artifact change-log entry this note was written against>"
read_me_first: true
---

# HANDOFF — read first after a restart

> Operational state doc (private to the instance). Restores context without asking the human.
> **Reading order on return:** framework rules (`process/OVERVIEW.md` → `OPERATING-LOOP.md` →
> `CONVENTIONS.md`; `REGISTERS.md` at its named moments) → **this file** → `sources/INDEX.md` →
> only the artifacts the task needs.
>
> **Check its age first.** `reflects:` names the newest change-log entry this note was written
> against. Nothing in the loop forces a pass to update it — no `surfaces` holds it and its trigger
> only fires if the previous agent reached it — so a note several passes behind is a *normal* state,
> not a malfunction. Compare `reflects:` with the artifacts' newest change-log entries; everything
> after that point is read from the files, never from here.

## Who / what / where
- PO / decision-maker, working language, product + scope boundary (one line each).
- Framework repo/branch; instance path; commit rules (what may / may not be committed).

## Where we are in the process
- Active status · current step · current section/gate item; what is DONE (steps closed).

## Environment & access (verify before relying)
| Dependency | Check (command / tool call) | Recover (exact recipe) |
|---|---|---|
| <e.g. browser bridge MCP> | <how to test it now> | <install link · profile/account · where the token goes> |

## Open forks (awaiting the human)
For each fork: 2–4 options with one-line trade-offs + the ⚙️ recommendation — verbatim
re-presentable, per CONVENTIONS "Forks & options".

## Key decisions already made (do not re-ask)
Dated one-liners with source (`[PO 2026-07-17]`), newest first.

## Registers (by reference only)
Current ID ranges + the items that matter now (e.g. "`H-009` is the cross of this tact") —
IDs and links, no copied tables.

## Framework fixes accumulated this run (for the future PR)
Bullet list of sanitized framework changes already on the run branch.

## Immediate next step
Numbered, concrete, executable-without-asking. If a restart is needed: what the human must do,
what the agent does after.

## Change log
### <date> — <summary>   (why the state changed; state sections above are overwritable)
```
