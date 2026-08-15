---
node_type: reference
title: Handling a late, cross-cutting hypothesis
status: draft
version: 0.1.0
updated: 2026-08-15
---

# Handling a late, cross-cutting hypothesis

*Read this when a hypothesis surfaces **after** the step where it belongs and you must place it
without forking the process. Pointed at from* [`OPERATING-LOOP.md`](../OPERATING-LOOP.md).

Sometimes a hypothesis surfaces *after* the step where it belongs — e.g. at Step 3 someone
realizes a new use-case that reframes the **concept** (Step 1). Do **not** fork the whole process
per hypothesis; the register is the single home. Escalate along a ladder, cheapest first:

| Level | Action | Use when |
|-------|--------|----------|
| **A · Register-first** | Log it in the hypothesis register with its type; tag it a **concept-variant** and an **invalidation trigger** on the step it touches; validate cheaply (a few interviews / a metric read) **before** editing the core artifact. | Default. It's a new segment / job / scenario — not a new product. |
| **B · Scoped spike** | Run the hypothesis as an **alternative lens through the affected steps only** (e.g. 1→3), in a separate `variants/<name>/` doc, then **compare to the main line** against a stated decision criterion and merge if it wins. Do **not** touch steps below the affected range. | Level-A signal is positive and the strategic implications need to be seen before committing. |
| **C · Full parallel run** | Treat it as a separate product/line and run all six steps. | Only when it is genuinely a different product, not a variant. |

Record the level chosen and the decision criterion in the change log. A spike (B) that loses is
kept, not deleted — it becomes a `[refuted: …]` note and a guard against re-litigating it.
