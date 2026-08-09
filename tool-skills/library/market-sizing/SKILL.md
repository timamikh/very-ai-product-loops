---
name: market-sizing
kind: research
produces: market-sizing
prerequisites: [arena/segment defined]
reads_registers: []
writes_registers: [hypotheses]
inputs: [analytics-search, kb]
used_by_steps: [2]
opinionated: false
method_basis: "TAM/SAM/SOM — bottom-up preferred, top-down cross-check, named assumptions"
evidence_standard: external-sources
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.1
updated: 2026-08-09
---

# Market Sizing

Size the opportunity as **TAM / SAM / SOM** — total, serviceable, and obtainable — with an
explicit method and a source behind every number. Fills `{#market-sizing}`.

**Method basis.** TAM/SAM/SOM built **bottom-up** (units × price) as the primary estimate, with a
**top-down** figure (published market reports, analogs) used only as a *cross-check*, not as the
answer. Every input is a **named assumption** traced to its source; sizing assumptions become
`H-…` (`type: viability`) so the business bet is testable, not asserted.

## When to apply
- Step 2, once the arena / segment is defined (you can only size a market you can name).
- When the segment, geography, or pricing changes enough to move the obtainable share.

## Prerequisites
- **Arena / segment defined** — the specific market you're sizing (who, where, which job).
  *Missing → run `segmentation` / `where-to-play-how-to-win` first.*

## How to do it
1. **Build SAM bottom-up.** Estimate *units × price*: number of reachable customers/accounts in the
   segment × the price they'd pay per period. This — not the headline TAM — is the number that
   matters. Show the arithmetic.
2. **Cross-check top-down.** Pull a published market figure or a defensible analog and derive the
   same SAM from it. If bottom-up and top-down diverge wildly, say why and don't average them —
   reconcile or flag the gap.
3. **Name and trace every assumption.** Each input (segment size, adoption %, price, frequency)
   gets a `[sourced: …]` or `[assumption]` tag. A number with no visible input is not a size.
4. **Keep SAM honest.** SAM is who you can actually serve — the right segment, geography, channel,
   and regulatory reach — not "the whole market". SOM is the share you can realistically win in the
   horizon, with a stated rationale.
5. **Avoid round-number theatre.** Derive figures from inputs; a clean "$1B" with no derivation is
   a red flag, not a result.
6. **Seed the register.** Each load-bearing sizing assumption → `H-…` (`type: viability`) so the
   business viability of the bet can be tested, not just stated.

## Anti-patterns
- **TAM as SOM.** Reporting the total market as if it were obtainable — the single most common
  sizing lie.
- **Sizing with no method or source.** A figure with no bottom-up arithmetic and no cited origin.
- **Round numbers with no derivation.** "$10B market" pulled clean from nowhere.
- **Averaging away divergence.** Splitting the difference between bottom-up and top-down instead of
  reconciling why they disagree.

## Output
Fills `{#market-sizing}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
