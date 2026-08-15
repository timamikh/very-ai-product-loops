---
name: value-definition
kind: method
produces: value-defensibility
reads_registers: []
writes_registers: [hypotheses]
inputs: [interview, kb]
prerequisites: [concept, segments, what-we-have-or-can-build, competitor-context]
used_by_steps: [1, 3]
opinionated: true
method_basis: "7 Powers (Helmer) → base/derivative moats; post-AI lens (software isn't the moat, position is)"
evidence_standard: derived
volume_rule: n/a
selection_rule: "the post-AI test — a value that does not survive an LLM rebuild is a feature, not a moat"
rejects_shown: required
status: draft
version: 0.2.3
updated: 2026-08-09
---

# Value & Defensibility

Define **why the product is valuable and why that value is defensible** — the moat. Fills the
`value-defensibility` section of the passport (Step 1) and is revisited at Strategy (Step 3),
where *derivative* values become relevant.

> **This is an opinionated method** (a post-AI view of defensibility). It lives in the library,
> not the process core, precisely so a company that thinks about value differently can swap it
> for its own. State the lens you use; don't present it as the only one.

## The premise (post-AI)

The software itself is **no longer a moat**. If ten people already built it and a hundred more
can tomorrow with an LLM, the *thing* is a commodity. Value lives in the **position**, not the
artifact. So we define value by what is hard to replicate cheaply — data, distribution, trust,
access, and execution — not by features.

## When to apply

- Step 1: to state the **value hypothesis** and the intended moat(s), early and as assumptions.
- Step 3: to pressure-test how the product **wins** — including derivative moats that only
  exist once you have a customer or scale.
- Any time a "why us / why now / why can't this be copied" question is on the table.

## The taxonomy — two layers

**Base (primitive) values** — things you can hold directly.

- *Hard (durable, hard to copy):*
  - **Unique data** — proprietary datasets others can't assemble.
  - **Unique algorithms / IP** — genuinely differentiated methods, protected or tacit.
  - **Exclusive access / integrations / rights** — privileged data, distribution, or legal rights.
- *Soft (barriers, copyable over time):*
  - **Audience / distribution** — you can reach demand others can't, cheaply.
  - **Brand / trust** — chosen because of who you are.
  - **Expertise** — depth that's slow to build.
  - **Processes (speed & precision)** — you ship and iterate faster/more accurately.
  - **Product complexity / depth** — hard-to-replicate surface area.
  - **Real-world assets / IRL processes** — physical assets (servers, facilities, licences) or
    offline operations that an IT-only competitor can't cheaply replicate.

**Derivative values** — emerge when a base value meets a **customer** or **scale**. Do not
claim these at concept stage; they appear at Strategy once there are customers.

- **Lock-in / switching costs** ← exclusive access/integration **+ an existing customer**.
- **Network effects** ← audience.
- **Economies of scale / cost advantage** ← audience / scale.

## Prerequisites

Checked before the tool runs (see [operating loop](../../../process/OPERATING-LOOP.md)). If any is
missing, the agent asks for it or offers to help produce it — it does not guess.

- **Concept** — what the product is (from `{#idea}`). *Missing → run `concept-formation` first.*
- **Segments** — who it's for (from `{#segments}`). *Missing → run `segmentation` first.*
- **What we have or can build** — honest inventory of data / algorithms / access / audience /
  brand / expertise. *Missing → agent interviews the human to elicit it.*
- **Competitor context** (Step 3) — to judge whether a moat is actually differentiated.
  *Missing → offer to run `competitor-analysis`.*

## How to do it

1. **Name the base value(s).** Which primitives do we actually have or can build? Be honest —
   an aspiration is `[assumption]`, not a moat yet.
2. **Test each against the post-AI premise.** Would this survive someone rebuilding the app
   with an LLM tomorrow? If not, it's a feature, not a moat. **Keep the candidates this test
   killed, with the reason.** They are the most valuable output of the step: a team that cannot see
   what was rejected as "not a moat" re-proposes it as a moat within two quarters, and the list is
   also the honest answer to "why don't we just say our UX is the advantage".
3. **Identify derivatives (from status `pmf` onward).** Given a base value and customers/scale,
   which derivative moats become reachable? Note the dependency (e.g. "lock-in *if* we land
   integration X and a customer"). **Skip the derivative *table* at `concept-viability`** — there
   are no customers or scale to derive from (a status-driven suppression: the active status decides
   whether this sub-section applies). Leave **one line** pointing to where it's picked up ("deferred
   to Step 3 — derivatives need a customer/scale") rather than silently omitting it, so a reader
   knows it was considered, not forgotten. Do not leave an empty table.
4. **Rate defensibility & confidence.** For each claimed moat: how durable, and how sure are
   we? Tag every claim per `process/CONVENTIONS.md`.
5. **Seed hypotheses.** Turn each unproven moat into a hypothesis (`H-…`) for the register —
   e.g. "customers will accept the switching cost of integration X".

## Anti-patterns

- **Feature-as-moat.** Listing capabilities an LLM can reproduce as if they were defensible.
- **Derivative at concept stage.** Claiming network effects / lock-in / scale before there is
  an audience or a customer.
- **Aspiration stated as fact.** A moat you *hope* to build tagged `[validated]` instead of
  `[assumption]`.
- **One-lens dogma.** Presenting this taxonomy as the only way to think about value. Say it's a
  lens; allow substitution.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/value-definition.md` (`node_type: worklog`):
the base value(s) named, each tested against the post-AI premise **with the killed candidates and their
reasons** (the step's most valuable output), any derivative moats and their dependencies, the
defensibility/confidence ratings, and the seeded hypotheses. That worklog is the **source of truth**;
the artifact section `{#value-defensibility}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md), holding nothing the worklog does not, with the
change-log history in the worklog (`process/CONVENTIONS.md` → *Step folders & worklogs*).

Where `value-definition` **contributes** to a section another method owns — `{#how-to-win}` (primary
`where-to-play-how-to-win`) and `{#bets}` (primary `jtbd`) — its working for that section lands in the
**primary's** worklog (`where-to-play-how-to-win.md` / `jtbd.md`), not a file of its own: the first
tool in a `<!-- tool: A, B -->` marker owns the section's worklog
(`process/CONVENTIONS.md` → *Several methods → one section: the first is primary*).

## Output

Projects `{#value-defensibility}` via [`template-fragment.md`](template-fragment.md) from its worklog;
contributes to `{#how-to-win}` / `{#bets}` through their primary methods' worklogs. Inputs gathered via
[`questions.yaml`](questions.yaml); each unproven moat seeds `H-…`. Deeper notes:
[`references/moat-taxonomy.md`](references/moat-taxonomy.md).
