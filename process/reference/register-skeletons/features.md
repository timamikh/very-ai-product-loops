---
node_type: register
register: features
title: Feature register — <product>
updated: <date>
version: 0.1.0
---

# Feature register

What the product is made of, per work direction — **as-is and to-be in one table**: `state: live`
rows are the current product, `state: planned` rows are the accumulating candidates (two documents
would drift; one table with states cannot). Born at Step 3 (`product-baseline` inventories live
features from sources) and Step 6 (the item specs mint `planned` candidates); Step-5 item readouts
flip `planned → live` against the pre-registered expectation. Schema: `process/REGISTERS.md` in the
vendored framework. Each row names the surface it lives on (`S-…`, `surfaces.md`) and what it
serves (`M-…` / `R-…` / `H-…`) — a feature serving nothing is a candidate to cut. A feature
outlives its sprint items: the sprint item advances the row, it never replaces it.

| ID <!--c:id--> | Name <!--c:name--> | Direction <!--c:direction--> | Surface <!--c:surface--> | State <!--c:state--> | Serves <!--c:serves--> | Owner <!--c:owner--> | Confidence <!--c:confidence--> | Source <!--c:source--> | Note <!--c:note--> |
|----|------|-----------|---------|-------|--------|-------|------------|--------|------|

## Change log

### <date> — register created
- **From → To:** — → empty register (skeleton copied at setup)
- **Why:** every register carries its own dated history (`process/CONVENTIONS.md` → Change logs); rows arrive by method passes, each pass adds an entry naming the ids it moved.
