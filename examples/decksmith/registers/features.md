---
node_type: register
register: features
title: Feature register — Decksmith (fictional sample)
updated: 2026-08-23
version: 0.1.0
---

# Feature register

What Decksmith is made of, per work direction — as-is and to-be in one table. All rows are
`planned`: the product is pre-build at `concept-viability`, so there is no live inventory yet —
rows were minted by the Sprint-1 item specs (`6#must`, `6#backlog`, `6#excluded`) and flip to
`live` at the Step-5 gate once `impact-readout` reads them. A feature outlives its sprint items:
the item advances the row, it never replaces it.

| ID <!--c:id--> | Name <!--c:name--> | Direction <!--c:direction--> | Surface <!--c:surface--> | State <!--c:state--> | Serves <!--c:serves--> | Owner <!--c:owner--> | Confidence <!--c:confidence--> | Source <!--c:source--> | Note <!--c:note--> |
|----|------|-----------|---------|-------|--------|-------|------------|--------|------|
| F-001 | Native export engine (`.pptx`/`.key`/Slides) | development | S-04 | planned | H-001 · M-design-acceptance | founder-engineer ⚙️ | [assumption] | `6#must` (feature spec) | Sprint-1 item 1 builds the `.pptx` first slice |
| F-002 | Design-acceptance / edit-behaviour instrumentation | development | S-05 | planned | M-design-acceptance · M-northstar · R-012 | engineer ⚙️ | [assumption] | `6#must` (feature spec) | Sprint-1 item 2 |
| F-003 | Founder-community partner recruitment (campaign line) | go-to-market | S-09 | planned | H-011 · M-cac · M-activated | founder ⚙️ | [assumption] | `6#must` (activity spec) | Sprint-1 item 1 (g2m) runs B-01/B-05; shipped post id lands here after the run |
| F-004 | Landing + waitlist + price page + analytics events | back-office | S-01 | planned | M-activated · M-paid-conv | back-office contractor ⚙️ | [assumption] | `6#must` (task spec) | Sprint-1 item 1 (b/o), lean scope |
| F-005 | Eval harness (≥50 briefs × ≥5 verticals) | development | S-05 | planned | H-001 · M-design-acceptance | founder-engineer ⚙️ | [assumption] | `6#backlog` | backlog rank 1 — reads F-001's output |
| F-006 | WTP price-talk script + prep | go-to-market | S-09 | planned | H-010 · M-paid-conv | founder ⚙️ | [assumption] | `6#backlog` | backlog rank 2 |
| F-007 | Billing / seats integration | back-office | S-07 | planned | M-arppu · M-contribution | back-office contractor ⚙️ | [assumption] | `6#backlog` | backlog rank 4 |
| F-008 | Brand-kit storage | development | S-06 | planned | H-012 | — to clarify — | [assumption] | `6#excluded` | cut at Step 5 — a cut candidate's row stays `planned`, it re-enters a later ranking |

## Change log

### 2026-08-23 — register born (Sprint-1 item specs)
- **From → To:** — → `F-001`…`F-008`, all `planned`
- **Why:** the Step-6 item specs (`feature-spec` / `activity-spec` / `task-spec`) declared the writes for the must-set and backlog; the orchestrator minted the rows. `F-008` enters already cut (`6#excluded`) — a cut candidate keeps its row.
