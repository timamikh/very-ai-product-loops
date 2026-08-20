---
node_type: register
register: metric-tree
title: Metric tree — <product>
updated: <date>
version: 0.1.0
---

# Metric tree

Node **definitions** only (North Star → drivers → input metrics); dated **values** live in
`metrics.csv`, append-only. The tree is born at Step 4. Schema: `process/REGISTERS.md` in the
vendored framework. Exactly one id per row; a changed definition mints a NEW id, never reuses
the old one.

| ID <!--c:id--> | Name <!--c:name--> | Definition <!--c:definition--> | Unit <!--c:unit--> | Kind <!--c:kind--> | Parent <!--c:parent--> | Population <!--c:population--> | Instrumentation <!--c:instrumentation--> | Target <!--c:target--> | Owner <!--c:owner--> | Source <!--c:source--> | Note <!--c:note--> |
|----|------|------------|------|------|--------|------------|-----------------|--------|-------|--------|------|
