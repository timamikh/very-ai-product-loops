---
node_type: card
kind: method
name: where-to-play-how-to-win
steps: [3]
prerequisites: [product-concept, market-analysis, value-moats]
reads: [section:idea, section:segments, section:market-sizing, section:competitors, section:competitor-strategy, section:competitor-dynamics, section:substitutes, section:opportunity, section:value-defensibility, register:hypotheses]
writes: [worklog, section:winning-aspiration, section:where-to-play, section:how-to-win, register:hypotheses]
opinionated: true
method_basis: "Playing to Win (Lafley/Martin) — winning aspiration, where-to-play, how-to-win cascade"
evidence_standard: decision
volume_rule: "≥3 distinct where-to-play / how-to-win possibilities before one cascade is chosen"
selection_rule: "the chosen cascade must be internally consistent end to end; the others are recorded with why they lose"
rejects_shown: required
status: draft
version: 0.3.1
updated: 2026-09-02
---
# Where to Play / How to Win

Strategy is **a cascade of integrated choices**, not a plan or a wish list. Fills
`{#winning-aspiration}`, `{#where-to-play}`, `{#how-to-win}`.

> **This is an opinionated method** (Playing to Win). It lives in the library so a company that
> frames strategy differently can swap it. State the lens; don't present it as the only one.

**Method basis.** Lafley & Martin's five-choice cascade: winning aspiration → where-to-play →
how-to-win → capabilities → management systems. This tool authors the first three; choices 4 and 5
are authored at Step 4 by `capabilities-systems`, which walks the chosen winning logic element by
element and seeds execution `R-…` for every capability gap. The two rules that make it strategy: **where-to-play must state
what's excluded**, and **how-to-win must be a coherent logic** that names how we beat the specific
players in that arena — not a list of things we'd like to be good at.

## When to apply
- Step 3, once the market and our moats are understood.
- When the arena or the winning logic is being reconsidered (new segment, new entrant).

## Prerequisites
- **Product concept** — what we're building. *Missing → run `concept-formation`.*
- **Market analysis** — arenas, sizes, each player's game and whether it works (`2#competitor-strategy`,
  `2#competitor-dynamics`). *Missing → run `market-sizing` + `competitor-analysis` (+ the
  `competitor-dynamics` scan for the trend read).*
- **Value & moats** — what we can actually win with. *Missing → run `value-definition-concept`.*

## How to do it
1. **Winning aspiration.** State what winning *means* here — not "be a player", but a specific
   outcome (who we serve, what result, by when). Vague aspirations produce vague strategy.
2. **Generate at least 3 distinct possibilities before choosing.** A possibility is a whole
   candidate cascade — a different arena *with* the winning logic that would fit it — not three
   variations on the arena you already assumed. One strategy, arrived at directly, is a rationalized
   default: nobody can tell it from the only option that was ever on the table. Record the ones that
   lost **and why they lose**, which is also the answer to the question a board asks first.
3. **Where to play.** Choose the arena: which segments, geographies, channels, product scope,
   stage of value chain. **List the exclusions explicitly** — the segments/arenas we deliberately
   will NOT pursue. A where-to-play with nothing excluded is not a choice.
4. **How to win.** State the coherent logic for beating the specific competitors in that arena.
   **Name which moats** (from `value-definition-concept`, revisited by `value-definition-strategy`) this logic leverages — cost, differentiation,
   data, distribution, lock-in — and how each translates into an advantage a rival can't cheaply
   copy. If the "how" doesn't connect to a named moat, it's a hope, not a strategy.
5. **Check integration.** The three choices must reinforce each other: does the how-to-win
   actually win in *this* where-to-play, given *this* aspiration? Break and re-choose if not.
6. **Seed hypotheses.** Each load-bearing assumption in the cascade (a moat holds, a segment
   will switch, a channel works) → `H-…` for the register.

## Anti-patterns
- **Where-to-play with no exclusions.** "Everyone, everywhere" — a scope, not a choice.
- **How-to-win as a wish list.** "Best product, best price, best service" with no coherent logic
  or named moat behind it.
- **Aspiration as slogan.** A mission statement standing in for a definition of winning.
- **Disconnected cascade.** A winning logic that doesn't actually win in the chosen arena.

## Worklog & projection
Worklog: `3-strategy/where-to-play-how-to-win.md` — one worklog for three sections: the aspiration, the ≥3 candidate cascades with why the losers lose, the arena with its exclusions, the winning logic with the moats it leverages, the integration check. Projects `{#winning-aspiration}` (face: **Aspiration**), `{#where-to-play}` (face: **Arena call**) and `{#how-to-win}` (face: **Winning logic**), each ending in its own Decided line, via [`template-fragment.md`](template-fragment.md). Primary of the `{#how-to-win}` marker; `value-definition-strategy`'s moat contribution reaches that section at re-projection, from its own worklog. Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#winning-aspiration}`, `{#where-to-play}`, `{#how-to-win}` via
[`template-fragment.md`](template-fragment.md) from the single worklog; inputs via
[`questions.yaml`](questions.yaml).
