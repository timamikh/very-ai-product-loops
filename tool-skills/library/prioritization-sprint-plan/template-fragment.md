<!--
  template-fragment: prioritization-sprint-plan → fills {#must} / {#backlog} / {#excluded} (Step 6)
  The clean copy's {#must} carries item blocks per direction (the specs' form); the ranking table here is
  the draft's working. Column names follow steps/6-sprint-plan/template.md's backlog table so the
  orchestrator maps by meaning; column keys never live here (column-keys.md).
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Must {#must}

_Minimal mandatory items per direction — the set without which the period goal is unreachable, inside
capacity. Item blocks follow their spec (`feature-spec` / `activity-spec` / `task-spec`); this method
contributes the ranking and the line._

<!-- card -->
**Gate of the period:** … (metric node to move `M-…`, or a Definition of Done) — <one clause: the
sprint's contribution to it and the must-set that carries it> [assumption]

**Capacity:** … (people · budget · time) [sourced: tactical-plan#resources] · **Candidates that entered
the ranking:** N = …

**Ranking** _(`Feature` and `Est.` repeat the spec's `F-…` and estimate class, so the thread from spec to
rank never breaks; the estimate is the spec's, never re-estimated here)_

| Rank | Direction | Item | Format | Feature | Links (`H-…`/`M-…`/`B-…`) | Est. | Score (RICE or ICE) | Contribution to the gate | must / backlog | Confidence |
|------|-----------|------|--------|---------|---------------------------|------|---------------------|--------------------------|----------------|------------|
| 1 | development | … | Feature | F-… | H-… / M-… | M | e.g. RICE 9.1 | how it moves the period gate | must | [assumption] |
| 2 | go-to-market | … | Activity | F-… | H-… / B-… | S | e.g. ICE 6 | … | must | [assumption] |

_The must/backlog line is drawn by capacity — the estimate classes inside the line must fit `5#resources`;
if must overflows, cut scope or renegotiate the gate, don't inflate must. A `priority: now` row of the
feature register left out of the must-set owes a written reason._

## Backlog {#backlog}

_The rest, prioritized (not a flat list), grouped by direction. Same item formats as `{#must}`._

<!-- card -->
**Backlog read:** <one sentence — how many items sit below the line, the first to move up if capacity
frees, and what it waits on>.

| Rank | Direction | Item | Format | Feature | Links (`H-…`/`M-…`/`B-…`) | Est. | Confidence |
|------|-----------|------|--------|---------|---------------------------|------|------------|
| 1 | development | … | Feature | F-… | H-… / M-… | … | [assumption] |
| 2 | go-to-market | … | Activity | F-… | H-… / B-… | … | [assumption] |
| 3 | back-office | … | Task+DoD | F-… | M-… / R-… | … | [assumption] |

## Excluded {#excluded}

_Candidates that entered the ranking (N = …) but left it entirely — cut before backlog, shown with why.
Backlog is the visible reject of the must-set; this is the reject of the ranking itself. An excluded
item's `F-…` stays `planned` in the register, with the cut noted._

<!-- card -->
**Excluded read:** <one sentence — how many of the N were excluded, and the commonest reason>.

| Item | Direction | Why excluded |
|------|-----------|--------------|
| … | … | no `M-…`/`H-…` link · out of period scope · superseded by <item> |
