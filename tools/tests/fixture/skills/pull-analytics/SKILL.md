---
node_type: card
kind: exchange
name: pull-analytics
prerequisites: []
reads: [source:metrics]
writes: ["file:product-loops/export.md"]
surfaces: [register:metrics]
direction: pull
reaches: the analytics panel
cadence: weekly
status: draft
version: 0.1.0
updated: 2026-09-01
---

# pull-analytics

An exchange card with a host-relative `file:` atom (check X) and a cadence with no `last_run` (check T).
