---
name: orchestration
kind: template
produces: (none — a return is integrated into whatever artifact the delegated task targeted)
reads_registers: [hypotheses, risks, metrics]
writes_registers: []
inputs: [kb]
prerequisites:
  - a pass of the loop already scoped (the step, the section or gate item, the method it needs)
  - the work splits into parts that can be stated without each other — one source, one question, one direction, one artifact to check
  - the orchestrator has the human's session (a subagent must never be the one holding it)
used_by_steps: [any]
opinionated: true
method_basis: "Supervisor/worker delegation with a written brief and an acceptance gate: a `draft` worker writes its own worklog, the orchestrator alone owns the projection, the registers and state, and every return is accepted against a passport rather than on trust"
status: draft
version: 0.2.1
updated: 2026-08-18
---

# Orchestration — running one pass with subagents

**What it is.** The procedure the **orchestrator** (the agent holding the human's session) follows
when a pass of the loop is too big for one context: how to cut the work, how to write the brief that
goes to a **subagent**, how to check what comes back, and how to integrate it. The *rules* of
delegation — who may write, what is never delegated, the closed list of task kinds, the two-iteration
cap — are canon, in [`process/OPERATING-LOOP.md`](../../../process/OPERATING-LOOP.md) →
*Delegation*. This file is the *how*.

**Why it exists.** Gathering fills a context window; a full context is where an agent starts skipping
loop steps (registers not updated, gate not ticked, a claim shipped without its tag). Delegation moves
the gathering out and keeps the reasoning in.

> **State the trade honestly, every time.** Delegation **costs more tokens**, not fewer — each
> subagent re-reads what it needs, and the orchestrator reads every return on top. What it buys is a
> context that stays clear enough to think in, and wall-clock time when parts run in parallel. If the
> pass fits in one context, **do not delegate it**: you would pay the premium for nothing and add a
> handoff where none was needed.

**The one thing it exists to prevent:** *a result nobody can stand behind.* Work done out of sight
comes back as fluent prose whose sourcing, gaps and guesses are invisible. Everything below —
the brief's rule block, the return contract, the passport — is there so that what arrives can be
checked, not believed.

## When to apply

Delegate when **at least one** is true:

1. **Breadth beats depth** — five sources, eight competitors, twelve segments: the work is *n* copies
   of the same small job, and the orchestrator would spend its context on volume.
2. **The material is bulky and the conclusion is small** — a large export, long transcripts, a
   documentation site. A subagent reads a hundred pages and returns ten lines.
3. **Steps 5–6 across directions** — each work direction (`development` · `go-to-market` · …) is an
   independent fill of the same section shape.
4. **Verification** — checking an artifact against a gate checklist is done better by an agent that
   did not write it. The author cannot see what they assumed.
5. **The pass is long and the context is already loaded** — delegation instead of a compaction.

**Do not delegate** when: the pass fits comfortably in one context · the work is the Step 1–4
reasoning chain · the next move depends on a human decision that has not been made · you cannot
state the task without also handing over your whole context (that is a sign the task is not
separable, not that the brief needs to be longer).

## Prerequisites

- **A scoped pass** — you know the step, the section or gate item, and the method that applies.
  Delegating "look into pricing" produces a subagent's opinion, not an input.
- **A separable part** — one source, one question, one direction, one artifact to check. If two parts
  need to talk to each other mid-flight, they are one task.
- **The inputs the subagent will need**, or the honest statement that it must find them (a `research`
  task may hunt for sources; a `gather` task may not invent one).
- **You hold the human's session.** A subagent never talks to the human, so any fork it hits comes
  back to you unresolved — plan for that before you launch, not after.

## How to do it

1. **Decide whether to split at all.** Estimate the pass: if the gathering is the bulk of it and the
   reasoning is small, split. If the reasoning is the bulk, do not — you would be delegating the part
   that must stay whole. Record the decision in one line; the human should be able to see why a pass
   was fanned out.

2. **Cut the work into task kinds.** Use the closed list (`gather` · `research` · `draft` · `verify`).
   One brief = one kind = one deliverable. A brief that mixes kinds ("collect the data and also draft
   the section") returns a blend you cannot check line by line, because the passport applies
   differently to each kind. Two briefs cost less than one bad merge.

3. **Write the brief from [`template-fragment.md`](template-fragment.md).** Every section is
   required, including the ones that look like boilerplate:
   - **Read first** — the *reading order*, not a pile of paths. A brief that omits the rule block
     produces output with no confidence tags, invented gaps, and a fork silently closed. This is the
     handoff lesson (*a handoff restores state, not rules*) in its second form.
   - **Scope and stop condition** — what is out of scope, and what "enough" is (four sources · the
     three named competitors · this section only). Without a stop condition a subagent expands until
     it runs out of room, and returns breadth where you needed depth.
   - **What to return** — the exact shape. You are going to read *n* of these; they must be
     comparable without re-reading the briefs.
   - **The passport** — pasted into the brief, so the subagent is checked against the same list it
     was given. Nothing about the acceptance test is a surprise.

4. **Launch.** Parallel where the parts are independent; sequential where one part's output is
   another's input (and then ask whether it is really two tasks). A subagent may spawn its own
   subagents — the write rule is transitive: the only file anything below you may write is a `draft`'s
   own worklog, never a register, an artifact section or `state.yaml`. Keep the fan-out to what you can
   actually read back: *n* returns you skim is worse than *n/2* you check.

5. **Check every return against the passport, before reading it for content.** In that order — a
   return that fails the passport is not evidence, and reading it for content first is how its
   conclusions get into your head anyway. Mark each line pass/fail yourself; the subagent's own
   self-check is a claim, not a verdict.

6. **Remediate once, then stop.** A failing return goes back with the **named defects** — not "improve
   the sourcing" but "claims 2 and 5 have no source; the URL in claim 4 was never opened". After the
   second failure, stop: record what is missing as `— to clarify —` and surface it to the human,
   saying that the brief did not produce a usable return. A third attempt is nearly always the
   brief's fault.

7. **Check the worklog, then project — this is the writing the orchestrator owns.** A `draft` return
   points at a **worklog the subagent wrote**; read it against the passport, then **project** it into
   the artifact section (the clean copy the human signs) — the writing move itself is the
   [`projection`](../projection/SKILL.md) operations skill. Delegation adds its own rules on top:
   a subagent's tag is never laundered (its `[assumption]` stays an assumption, and never re-tag a
   return as `[sourced: subagent]` — the source is what the subagent opened, named in your text);
   you **mint the register ids** the worklog described in words, you write the rows, you tick the
   gate (after a `verify`), you write the change log — none of that is ever the subagent's. A
   `gather`/`research` return is **not** a worklog: you file its values where they belong (the
   method's worklog, a source, a register row) yourself. Where a return named an unresolved fork, it
   becomes your fork with the human — with the options as returned.

8. **Close the pass normally.** Delegation changes who read the material, not what a pass owes:
   step 7 of the loop still runs — registers, change log, open items — and anything the delegation
   itself made awkward is surfaced to the human with the rest.

## The return passport

The acceptance gate. It is **hard**: a return that fails any line is not integrated (canon —
OPERATING-LOOP → *Delegation*). The **one home of the wording** is §7 of the brief in
[`template-fragment.md`](template-fragment.md) — that is the copy pasted into every brief and the
copy the subagent self-checks against. The table below is the same nine lines with what each one is
guarding against; if the two ever read differently, the template is right and this table is the bug.

| # | The check | Fails when |
|---|-----------|-----------|
| 1 | **Every claim carries a confidence tag** and names its origin | a bare sentence with no `[sourced: …]` / `[assumption]` |
| 2 | **Every source given was actually opened**, with the date it was read | a plausible URL that was never fetched, or a title with no link |
| 3 | **Unreachable sources are declared**, not dropped | a 404 or a paywall silently omitted from the list |
| 4 | **Headline numbers are cross-checked** against a second independent source; a divergence over 20% is reported as a conflict, not silently resolved | the number that will end up in a conclusion rests on one source, or two sources disagreed and one was quietly chosen |
| 5 | **Nothing invented** — gaps are `— to clarify —` | a filled-in plausible value where the source had none |
| 6 | **No fork closed** — decisions come back as options | the return picked one and moved on |
| 7 | **No secrets or PII**, and no raw capture pasted in | a token, a customer name, an exported row set |
| 8 | **Scope covered, or the uncovered part named** | four of six sources done, silently |
| 9 | **The "could not do" block is present** | absent, or "everything went fine" with no detail |

A line that cannot apply to a task kind is answered **`n/a`, in writing** — a `verify` return has no
headline numbers, so line 4 is `n/a` and its Cross-checks table says so. Every return carries every
section; the shape does not vary by kind, only its content does. Two shapes would be two things to
read, and the orchestrator reads *n* of these.

Lines 2–4 come from the failure this gate is really about: an agent that cannot reach a source and
fills the hole with something reasonable. **Fail loudly** is the instruction to the subagent, and
lines 3 and 9 are where a loud failure is supposed to land.

## Decomposition patterns

| Pattern | Cut by | Typical kind | Watch for |
|---------|--------|--------------|-----------|
| **One source, one agent** | source | `gather` | two agents reading the same source and reporting different totals — that is a real finding, not a bug: it means the derivation is not written down (see `metrics-capture`) |
| **One question, one agent** | question | `research` | overlapping questions producing the same digest twice |
| **One direction, one agent** | work direction (Steps 5–6) | `draft` | drafts that assume different capacity — state the shared constraints in every brief |
| **One lens, one agent** | the angle of the check (sourcing · internal consistency · gate coverage) | `verify` | one "review this" agent instead of three lenses: a single reviewer converges on the most obvious defect |
| **Fresh reader** | nothing — one agent, no context | `verify` | using the agent that drafted the section. It cannot see its own assumptions |

## Anti-patterns

- **Delegating the fork.** "Decide which segment we lead with and tell me." The agent prepares, the
  human decides — a subagent has neither the human nor the accumulated context.
- **A brief without a reading order.** The subagent invents its own conventions and the return has to
  be rewritten rather than integrated.
- **Trusting a fluent return.** Length and confidence are free; sourcing is not. Score the passport
  before you read for content.
- **Laundering a tag.** A subagent's assumption arriving in your artifact as `[sourced: research]`.
  One step, and a guess has become a fact with a citation.
- **A subagent writing past its worklog.** A `draft` writes its own worklog and nothing else; the
  moment it also writes a register row or the artifact section, two agents can allocate `H-0xx` at once
  and the register is corrupt — the fix costs more than the delegation saved. `gather` / `research` /
  `verify` write nothing at all.
- **Fan-out you cannot read back.** Twelve returns skimmed is worse than five checked, and the
  passport is unenforceable at volume.
- **Delegating to avoid the context limit at the wrong moment.** If the pass is nearly done, finish it
  and hand off (`handoff`); a brief written from an exhausted context is a bad brief.
- **A brief that is a copy of your context.** If it takes everything you know to state the task, the
  task is not separable — do it yourself.
- **Skipping step 7 because "the subagents did the work".** A delegated pass is still a pass.

## On the runtime (Claude Code and others)

The rules above are **markdown and hold on any agent runtime** — that is the framework's promise. On
a runtime that supports typed subagents with restricted tools, enforce as much of the write rule
*mechanically* as the split allows. This framework ships one definition per task kind for Claude Code
in [`.claude/agents/`](../../../.claude/agents/) — `loops-gather` · `loops-research` · `loops-draft` ·
`loops-verify`. Three of them (`gather`, `research`, `verify`) carry **no write tools at all** — they
cannot write even if a full context forgets they should not, which is exactly the population that
forgets. `loops-draft` is the deliberate exception: it carries `Write`, because its job *is* to write
its method's worklog. That one write is scoped **by instruction** — the definition says the only file
it may write is its own `<step-folder>/<method>.md` — because a tool list can grant `Write` but cannot
pin it to a single path. So the draft's worklog is the one seam where the machine guarantee stops and
the passport check takes over: the orchestrator reads the worklog before projecting it, and a draft
that wrote anything but its own worklog fails there.

> **Stated weakness — the one hole in the mechanical enforcement.** Those definitions keep the
> ability to spawn further subagents, because fan-out below the first level is often the point. That
> tool is the hole: an agent that can spawn *any* agent type can reach one that writes. It is closed
> by instruction only — every definition says "spawn only `loops-*` types" — and instruction is what
> a loaded context forgets. If you are running a deep fan-out on material you care about, close it
> the certain way: drop `Agent` from the definition's tools and let the orchestrator do the second
> level of fan-out itself.

**A definition added mid-session is not available in that session.** Claude Code reads
`.claude/agents/` when the session starts, so a `loops-*` type created or renamed during a session
cannot be spawned until the session restarts — the spawn simply fails with "agent type not found".
Two consequences worth knowing before you plan a fan-out: after re-vendoring the framework or writing
your own definition, **restart before delegating**; and when a restart is not on the table, fall back
to the paragraph below rather than rewriting the brief.

On a runtime with no subagent mechanism — or in a session that has not picked the definitions up yet
— the same briefs work against any general-purpose read-only agent, or by hand: paste the brief into a
second session and paste the return back. One thing does change: a read-only fallback agent cannot
write, so a `draft` brief there **returns its worklog as text** and the orchestrator writes the file
itself — the write rule then rests on the brief's rule block instead of on the tool list, which is
weaker. Say so when you report the pass, rather than letting the difference go unrecorded. The
procedure is otherwise the same; only the plumbing changes.

## Output

No artifact section of its own. It produces **briefs** (ephemeral — handed to a subagent, and if
written down at all, written outside the repository like any raw capture) and it produces the
**integration**: a `draft` subagent has already written its method's worklog, and the orchestrator
**projects** that worklog into the artifact section and writes the registers, the gate ticks and the
change log around it. A `gather`/`research`/`verify` return carries no worklog — the orchestrator files
its values into whatever worklog, register or source they serve. The one writing that is never a
subagent's: the artifact, the registers and `state.yaml`.
