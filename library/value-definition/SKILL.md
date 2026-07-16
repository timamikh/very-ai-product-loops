---
name: value-definition
kind: method
produces: value-defensibility
reads_registers: []
writes_registers: [hypotheses]
inputs: [interview, kb]
used_by_steps: [1, 3]
opinionated: true
status: draft
version: 0.1.0
updated: 2026-07-16
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

**Derivative values** — emerge when a base value meets a **customer** or **scale**. Do not
claim these at concept stage; they appear at Strategy once there are customers.

- **Lock-in / switching costs** ← exclusive access/integration **+ an existing customer**.
- **Network effects** ← audience.
- **Economies of scale / cost advantage** ← audience / scale.

## How to do it

1. **Name the base value(s).** Which primitives do we actually have or can build? Be honest —
   an aspiration is `[assumption]`, not a moat yet.
2. **Test each against the post-AI premise.** Would this survive someone rebuilding the app
   with an LLM tomorrow? If not, it's a feature, not a moat.
3. **Identify derivatives (Step 3+).** Given a base value and customers/scale, which
   derivative moats become reachable? Note the dependency (e.g. "lock-in *if* we land
   integration X and a customer").
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

## Output

Fills `value-defensibility` using [`template-fragment.md`](template-fragment.md). Inputs
gathered via [`questions.yaml`](questions.yaml). Deeper notes: [`references/moat-taxonomy.md`](references/moat-taxonomy.md).
