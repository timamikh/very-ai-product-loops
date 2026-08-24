---
node_type: register
register: surfaces
title: Surface register — <product>
updated: <date>
version: 0.1.0
---

# Surface register

Every surface through which the product meets its audience — a landing page, the in-product UI, an
admin panel, a mailing, a content channel, an internal system. Few and long-lived; features
(`features.md`) reference them by `S-…`. Born at Step 3 (`product-surface` chooses them,
`product-baseline` inventories them); the strategic *why* stays in `3#product-surface` — this file
is the ledger. Schema: `process/REGISTERS.md` in the vendored framework. `type` is a free
descriptor (landing · in-product · admin · mailing · content · channel · internal — or the
product's own word).

| ID <!--c:id--> | Name <!--c:name--> | Type <!--c:type--> | Purpose <!--c:purpose--> | State <!--c:state--> | Source <!--c:source--> | Note <!--c:note--> |
|----|------|------|---------|-------|--------|------|

## Change log

### <date> — register created
- **From → To:** — → empty register (skeleton copied at setup)
- **Why:** every register carries its own dated history (`process/CONVENTIONS.md` → Change logs); rows arrive by method passes, each pass adds an entry naming the ids it moved.
