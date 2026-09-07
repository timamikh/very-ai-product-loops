---
node_type: decisions
title: Decisions — <product>
updated: <date>
version: 0.1.0
---

# Decisions

Every dated human decision the run rests on, one row each, append-only. Not a register (no
lifecycle, no flow back up) — a **log** with stable ids, so a `[sourced: decision D-…]` tag in an
artifact or worklog points at a row a `verify` can read inside the instance. `Where` names the
section or worklog the decision acted on; `Why` is the human's reason in their words, or the
alternative that lost. A fork closed here is also written into the worklog whose fork it was, the
same pass (`process/CONVENTIONS.md` → *Artifacts, step folders & worklogs*).

| ID <!--c:id--> | Date <!--c:date--> | By <!--c:by--> | Where <!--c:where--> | Decision <!--c:decision--> | Why <!--c:why--> |
|----|------|----|-------|----------|-----|
