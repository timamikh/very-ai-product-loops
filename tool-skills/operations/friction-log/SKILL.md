---
name: friction-log
kind: template
produces: FRICTION.md
reads_registers: []
writes_registers: []
inputs: []
prerequisites:
  - a pass of the loop that actually ran (there is nothing to report about work not done)
used_by_steps: [any]
opinionated: true
method_basis: "Blameless post-run reporting: the operator reports where the procedure failed them, every run, whether or not anything went wrong"
status: draft
version: 0.1.0
updated: 2026-08-09
---

# Friction log — what the framework got wrong this pass

**What it is.** A two-minute entry the agent appends to the instance's `FRICTION.md` at
[step 7](../../../process/OPERATING-LOOP.md) of **every** pass: where the loop, a skill, a rule or a
template got in the way. It is the framework's only feedback channel that does not depend on somebody
volunteering it.

**Why it exists.** This framework's largest single improvement came from one field report a human
happened to write. Everything in it had been visible to the agent at the time it happened and was
never recorded, because nothing asked. A channel that only opens when someone is annoyed enough to
write an essay reports the loud problems and loses every quiet one — and the quiet ones are the ones
that make an agent skip a step.

**The one thing it exists to prevent:** *the framework being wrong in the same way forever.* An
instruction that cannot be followed as written gets worked around silently, the work looks fine, and
the instruction survives to mislead the next agent.

> **It is not a diary and not a register.** It holds **friction with the framework** — never product
> values, never a decision, never state. Anything about the product belongs in an artifact, a register
> or a change log; putting it here creates a second home for it, which the framework does not allow.
> It fails the four-sign register test on every sign ([`process/REGISTERS.md`](../../../process/REGISTERS.md)):
> entries have no lifecycle, no state flows back into them, and nothing references them by id.

## When to apply

**Every pass, at step 7 — including passes where nothing went wrong.** "Nothing to report" is a
result, and a log with a run of clean entries is what makes the entry that is not clean readable.

Also worth an entry outside step 7:
- a **delegated return that failed the passport twice** — the brief was the problem, and that is
  framework friction, not subagent failure;
- **an instruction you had to interpret** to proceed, even though it worked out;
- **a rule you noticed you had broken** after the fact. Especially that one.

## Prerequisites

- The instance exists. If `FRICTION.md` does not, create it from
  [`template-fragment.md`](template-fragment.md) on the first pass.

## How to do it

1. **Ask the three questions**, in this order, and answer each in one line:
   - **What could not be done as written?** A step, a prerequisite, a template slot, a rule.
   - **What did you do instead?** The workaround is the actual finding — it is what the framework
     will keep costing every future pass.
   - **What would have made it work?** Concretely, at the level of a file and a line. A wish
     ("clearer docs") is not a report.
2. **Name the file and the place.** `process/OPERATING-LOOP.md` → *Delegation*, or
   `tool-skills/library/pricing/SKILL.md` step 3. An entry that does not say where is a mood.
3. **Separate the two causes, honestly.** *The rule was wrong / unfollowable* is a framework defect.
   *I did not read it* is not — it is still worth logging, because a rule nobody reads at the moment
   it applies is in the wrong place, which **is** a framework defect one level up. Say which you
   think it was; being wrong about that is cheap, hiding it is not.
4. **Keep the product out.** Describe the shape of the problem, never the numbers: "the metric node
   had no derivation, so the value could not be reproduced" — not the value.
5. **Append, newest first.** Never rewrite an old entry; an entry that turned out to be mistaken gets
   a new one that says so. The log's worth is that it is a record of what it felt like at the time.

## Anti-patterns

- **"Everything went smoothly."** Written by an agent that did not look. If a pass genuinely had no
  friction, say what you checked: which step, which skill, which template.
- **A complaint with no location.** "The instructions are confusing" cannot be acted on and will not be.
- **Blaming the human or the source.** Missing data is normal and is what `— to clarify —` is for; it
  is friction only when the *framework* had no way to record or route it.
- **Product content.** A number, a segment name, a decision. Wrong file — and in a vendored instance,
  possibly a leak.
- **Batching.** "I'll write it all up at the end of the day" is how the quiet items are lost; by then
  only the loud ones are left, which is the failure this skill exists to fix.
- **Writing it as a task list.** It is a report, not a backlog. What to do about it is the human's
  call, and turning it into work items is how it starts getting groomed instead of read.

## Output

Appends one dated entry to `FRICTION.md` at the instance root, per
[`template-fragment.md`](template-fragment.md). Nothing else reads it automatically: it is written for
the human who maintains the framework, and for the pass that proposes a change to it —
[`EXTENDING.md`](../../../EXTENDING.md) is where a change actually happens.
