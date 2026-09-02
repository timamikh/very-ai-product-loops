---
node_type: card
kind: method
name: capabilities-systems
steps: [4]
prerequisites: [strategy-cascade]
reads: [section:where-to-play, section:how-to-win, register:risks, register:features, register:surfaces]
writes: [worklog, section:capabilities, register:risks]
opinionated: true
method_basis: "Playing to Win (Lafley/Martin) — choices 4 & 5 of the cascade: must-have capabilities and the management systems that build and measure them"
evidence_standard: decision
volume_rule: "every moat / winning-logic element in 3#how-to-win maps to ≥1 capability"
selection_rule: "a capability that serves no element of the winning logic is rejected as nice-to-have; kept in the reject table with why"
rejects_shown: required
status: draft
version: 0.2.1
updated: 2026-09-02
---
# Capabilities & Management Systems

Name **what the organization must be great at** for the chosen strategy to work — and **the
systems that build, maintain, and measure** those capabilities. Fills `{#capabilities}`. This is
where the Playing-to-Win cascade lands its last two choices: `where-to-play-how-to-win` (Step 3)
authors the first three; this method authors choices 4 and 5.

> **This is an opinionated method** (Playing to Win). It lives in the library so a company that
> frames strategy differently can swap it. State the lens; don't present it as the only one.

**Method basis.** Lafley & Martin: a how-to-win that no capability supports is a hope, and a
capability with no management system decays — nobody builds it, nobody notices it slipping. The
test runs in both directions: every winning-logic element needs a capability behind it, and every
capability named must serve the winning logic.

## When to apply
- Step 4, once the strategy cascade is chosen — before mitigations, so capability gaps can land in
  the risk register.
- When the strategy changes (a new how-to-win invalidates the old capability set), or when
  execution keeps missing for reasons no metric explains.

## Prerequisites
- **Strategy cascade** — the chosen winning aspiration / where-to-play / how-to-win from
  `3-strategy.md`. *Missing → run `where-to-play-how-to-win` first.*

## How to do it
1. **Walk the winning logic element by element.** For each moat or claim in `{#how-to-win}`
   ("we win on data quality", "we win on distribution through partners"), ask: *what must we be
   reliably great at for this to be true?* Every element gets ≥1 capability; an element with none
   is an unbacked claim — flag it, don't paper over it. Ground the walk in the feature register
   (`registers/features.md` / `surfaces.md`): the `live` rows are what the team demonstrably can
   build and run — a capability claim with no live feature or surface behind it starts as an
   assumption, not a fact.
2. **State each capability as an ability, not an asset.** "Ship a model-eval cycle in under a
   week" is a capability; "our dataset" is an asset (assets enable capabilities, they aren't one).
3. **Rate honestly: `have` / `partial` / `missing`.** The rating is a decision-grade statement —
   name who confirmed it, the way `resource-check` attributes capacity. A flattering rating here
   surfaces later as an execution miss no metric explains.
4. **For each `partial` / `missing` — the gap and the close.** What's missing, how it gets built
   (hire, train, buy, partner), by when, owned by whom. A gap with no close date is a risk:
   seed `R-…` (category: execution) so `risk-mitigation` picks it up in the same step.
5. **Name the management system per capability.** How it is *built, maintained, and measured*:
   the process, the review cadence, the signal that shows it slipping (a metric node `M-…` where
   one exists). A capability without a system is a one-time hire that erodes.
6. **Reject the nice-to-haves.** Capabilities proposed that serve no winning-logic element go to
   the reject table with why — they are the org's wish list, and unnamed they creep back into
   hiring plans.

## Anti-patterns
- **Capability = asset.** Naming things owned instead of things done reliably well.
- **Wish-list capabilities.** "World-class engineering" serving no specific winning-logic element.
- **Flattering ratings.** Everything `have` — then the strategy needs nothing, and the section
  says nothing.
- **Systemless capabilities.** Named, hired for once, never measured — eroded by the next quarter.

## Worklog & projection
Worklog: `4-strategic-plan/capabilities-systems.md` — the element-by-element walk of the winning logic, each capability's rating with who confirmed it, the gap-and-close with the `R-…` it seeds, the management system per capability, the rejected nice-to-haves. Projects `{#capabilities}`; face: the **Capability read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#capabilities}` via [`template-fragment.md`](template-fragment.md) from the worklog;
inputs via [`questions.yaml`](questions.yaml).
