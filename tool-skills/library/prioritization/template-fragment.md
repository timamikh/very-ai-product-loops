<!--
  template-fragment: prioritization → fills {#period-goals} (Step 5) and {#must} / {#backlog} / {#excluded} (Step 6)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Period Goals {#period-goals}

_Step 5 — measurable goals for the period, grouped by direction, ranked by contribution to the gate._

**Gate of the period:** … (metric node to move `M-…`, or a Definition of Done) [assumption]
**Capacity (from `resource-check`):** … (people · budget · time) [sourced: tactical-plan#resources]

**Ranking**
| Item | Contribution to the gate | Score (RICE or ICE) | must / backlog | Moves / tests |
|------|--------------------------|---------------------|----------------|---------------|
| … | how it moves the period gate | e.g. RICE 8.4 · [assumption] | must | M-… / H-… |
| … | … | e.g. ICE 6 · [assumption] | backlog | H-… |

_Rank is by gate contribution; the score only aids ordering. An item with no `M-…`/`H-…` is a cut candidate._

## Must {#must}

_Step 6 — minimal mandatory items per direction; the set without which the period goal is unreachable. Fits inside capacity._

| Item | Contribution to the gate | Score (RICE or ICE) | must / backlog | Moves / tests |
|------|--------------------------|---------------------|----------------|---------------|
| … | … | e.g. RICE 9.1 · [assumption] | must | M-… / H-… |

_The must/backlog line is drawn by capacity — if must overflows, cut scope or renegotiate the gate, don't inflate must._

## Backlog {#backlog}

_Step 6 — the rest, prioritized (not a flat list), grouped by direction._

| Item | Contribution to the gate | Score (RICE or ICE) | must / backlog | Moves / tests |
|------|--------------------------|---------------------|----------------|---------------|
| … | … | e.g. ICE 5 · [assumption] | backlog | H-… |

**Links:** each item references the `M-…` it moves or the `H-…` it tests → registers.

## Excluded {#excluded}

_Step 6 — candidates that entered the ranking (N = …) and left it entirely, as opposed to landing in
backlog. Backlog is the visible reject of the must-set; an item cut before that has nowhere else to be
seen._

| Item | Direction | Why excluded |
|------|-----------|--------------|
| … | … | no `M-…`/`H-…` link · out of period scope · superseded by <item> |
