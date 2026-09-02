---
node_type: library-reference
title: Ranking by gate contribution — the RICE/ICE procedure shared by the two prioritization cards
status: draft
version: 0.1.0
updated: 2026-09-02
---

# Ranking by gate contribution

The one procedure behind `prioritization-tactical-plan` (goals, Step 5) and
`prioritization-sprint-plan` (items, Step 6). Each card says what it ranks and where it lands.

1. **State the gate first.** The period gate is a metric node to move (`M-…`) or a Definition of
   Done. Every candidate is ranked against it — never against a generic score.
2. **List every candidate and record N.** Nothing is pre-cut; without N "we prioritized" reads the
   same whether ten candidates competed or three.
3. **Score — RICE or ICE, as an aid.** Reach · Impact · Confidence · (Effort; skip for ICE). The
   score orders, never decides, and carries a confidence tag. The agent proposes it (⚙️) from what
   the artifact holds and asks only for what no section answers.
4. **Rank by gate contribution; the score breaks ties.** A high score that does not move the gate
   ranks below a lower score that does. Equal gate contribution → the higher score first.
5. **Check the link.** A candidate that moves no `M-…` and tests no `H-…` is a cut candidate.
6. **Bound by capacity.** Keep what fits the capacity `resource-check` recorded (`5#resources`).
   If the minimum set overflows, cut scope or renegotiate the gate — never inflate the set.
7. **Show every reject with its reason.** A candidate cut before or after the ranking is recorded,
   never deleted — no `M-…`/`H-…` link · over capacity (below the line) · out of period scope ·
   superseded by <which>. Without it the next pass re-proposes the same candidate, and nobody can
   tell a filter that was applied from one never reached.

**Shared anti-patterns.** A flat list with no rank · a set inflated past capacity · score for
score's sake (no tie back to the gate) · orphan candidates with no `M-…`/`H-…` link · invisible cuts.
