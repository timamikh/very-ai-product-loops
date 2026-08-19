---
node_type: card
kind: method
name: market-sizing
steps: [2]
prerequisites: [arena/segment defined, price input (assumption on first pass)]
reads: [source:research, source:kb]
writes: [worklog, section:market-sizing, register:hypotheses]
opinionated: false
method_basis: "TAM/SAM/SOM — bottom-up preferred, top-down cross-check, named assumptions"
evidence_standard: external-sources
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.0
updated: 2026-08-16
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
- **A price input** — bottom-up sizing is *units × price*. The observed anchor comes from
  `{#competitor-pricing}` (`competitor-pricing`), which is filled later in this step; the first pass
  carries an `[assumption]` price from Step-1 value work and the sizing is **revisited** once the
  scan lands. *Neither available → the price is a named `[assumption]`, never an implied one.*

## How to do it
1. **Build SAM bottom-up.** Estimate *units × price*: number of reachable customers/accounts in the
   segment × the price they'd pay per period. This — not the headline TAM — is the number that
   matters. Show the arithmetic.
2. **Cross-check top-down.** Pull a published market figure or a defensible analog and derive the
   same SAM from it — from a source that survives the per-fact-type test in
   [`../references/evidence-standards.md`](../references/evidence-standards.md) (a vendor's "market
   size" is a claim about the vendor's interest). If bottom-up and top-down diverge by more than
   ~20%, report **both** and mark it `[CONFLICT]`; do not average them and do not quietly pick the
   more convenient one. Reconciling is allowed only when you can say *why* one is wrong.
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

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/market-sizing.md` (`node_type: worklog`,
e.g. `2-analysis/market-sizing.md`): the arena sized, the **bottom-up arithmetic** (units × price), the
top-down cross-check, every named assumption with its source tag, and the open items. That worklog is
the **source of truth**; the artifact section `{#market-sizing}` is its **projection** into the fixed
shape of [`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the
step's change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#market-sizing}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs
via [`questions.yaml`](questions.yaml); each load-bearing sizing assumption seeds `H-…` (`type: viability`).
