<!--
  template-fragment: prioritization-sprint-plan → fills {#must} / {#backlog} / {#excluded} (Step 6)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Must {#must}

_Minimal mandatory items per direction; the set without which the period goal is unreachable. Fits
inside capacity. Item blocks follow their spec (`feature-spec` / `activity-spec` / `task-spec`);
this method contributes the ranking and the line._

**Gate of the period:** … (metric node to move `M-…`, or a Definition of Done) [assumption]
**Capacity:** … (people · budget · time) [sourced: tactical-plan#resources]
**Candidates that entered the ranking:** N = …

| Item | Direction | Contribution to the gate | Score (RICE or ICE) | must / backlog | Moves / tests |
|------|-----------|--------------------------|---------------------|----------------|---------------|
| … | development | how it moves the period gate | e.g. RICE 9.1 · [assumption] | must | M-… / H-… |

_The must/backlog line is drawn by capacity — if must overflows, cut scope or renegotiate the gate,
don't inflate must._

## Backlog {#backlog}

_The rest, prioritized (not a flat list), grouped by direction._

| Item | Direction | Contribution to the gate | Score (RICE or ICE) | must / backlog | Moves / tests |
|------|-----------|--------------------------|---------------------|----------------|---------------|
| … | go-to-market | … | e.g. ICE 5 · [assumption] | backlog | H-… |

**Links:** each item references the `M-…` it moves or the `H-…` it tests → registers.

## Excluded {#excluded}

_Candidates that entered the ranking (N = …) and left it entirely, as opposed to landing in
backlog. Backlog is the visible reject of the must-set; an item cut before that has nowhere else to
be seen._

| Item | Direction | Why excluded |
|------|-----------|--------------|
| … | … | no `M-…`/`H-…` link · out of period scope · superseded by <item> |
