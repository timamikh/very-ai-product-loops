---
name: where-to-play-how-to-win
kind: method
produces: [winning-aspiration, where-to-play, how-to-win]
reads_registers: [hypotheses]
writes_registers: [hypotheses]
inputs: [kb, interview]
prerequisites: [product-concept, market-analysis, value-moats]
used_by_steps: [3]
opinionated: true
method_basis: "Playing to Win (Lafley/Martin) — winning aspiration, where-to-play, how-to-win cascade"
evidence_standard: decision
volume_rule: "≥3 distinct where-to-play / how-to-win possibilities before one cascade is chosen"
selection_rule: "the chosen cascade must be internally consistent end to end; the others are recorded with why they lose"
rejects_shown: required
status: draft
version: 0.1.1
updated: 2026-08-09
---

# Where to Play / How to Win

Strategy is **a cascade of integrated choices**, not a plan or a wish list. Fills
`{#winning-aspiration}`, `{#where-to-play}`, `{#how-to-win}`.

> **This is an opinionated method** (Playing to Win). It lives in the library so a company that
> frames strategy differently can swap it. State the lens; don't present it as the only one.

**Method basis.** Lafley & Martin's five-choice cascade: winning aspiration → where-to-play →
how-to-win → capabilities → management systems. This tool authors the first three; capabilities
and systems land in later steps. The two rules that make it strategy: **where-to-play must state
what's excluded**, and **how-to-win must be a coherent logic** that names how we beat the specific
players in that arena — not a list of things we'd like to be good at.

## When to apply
- Step 3, once the market and our moats are understood.
- When the arena or the winning logic is being reconsidered (new segment, new entrant).

## Prerequisites
- **Product concept** — what we're building. *Missing → run `concept-formation`.*
- **Market analysis** — arenas, sizes, dynamics to choose among. *Missing → run `market-sizing` + `competitor-analysis`.*
- **Value & moats** — what we can actually win with. *Missing → run `value-definition`.*

## How to do it
1. **Winning aspiration.** State what winning *means* here — not "be a player", but a specific
   outcome (who we serve, what result, by when). Vague aspirations produce vague strategy.
2. **Where to play.** Choose the arena: which segments, geographies, channels, product scope,
   stage of value chain. **List the exclusions explicitly** — the segments/arenas we deliberately
   will NOT pursue. A where-to-play with nothing excluded is not a choice.
3. **How to win.** State the coherent logic for beating the specific competitors in that arena.
   **Name which moats** (from `value-definition`) this logic leverages — cost, differentiation,
   data, distribution, lock-in — and how each translates into an advantage a rival can't cheaply
   copy. If the "how" doesn't connect to a named moat, it's a hope, not a strategy.
4. **Check integration.** The three choices must reinforce each other: does the how-to-win
   actually win in *this* where-to-play, given *this* aspiration? Break and re-choose if not.
5. **Seed hypotheses.** Each load-bearing assumption in the cascade (a moat holds, a segment
   will switch, a channel works) → `H-…` for the register.

## Anti-patterns
- **Where-to-play with no exclusions.** "Everyone, everywhere" — a scope, not a choice.
- **How-to-win as a wish list.** "Best product, best price, best service" with no coherent logic
  or named moat behind it.
- **Aspiration as slogan.** A mission statement standing in for a definition of winning.
- **Disconnected cascade.** A winning logic that doesn't actually win in the chosen arena.

## Output
Fills the three sections via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
