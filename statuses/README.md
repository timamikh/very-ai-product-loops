---
node_type: statuses-index
title: Statuses — product-stage plane
status: draft
version: 0.3.0
updated: 2026-07-19
---

# Statuses

A **status** is the product's current stage. It is the framework's adaptation dial: it
parameterizes the loops without changing the process core. For **each step**, a status sets:

- **the goals** that keep the agent focused this stage (not abstract), optionally split by
  work direction;
- **the tools** to lean on — the same section can call for different methods at different
  stages (e.g. pains from *interviews* early vs *internal metrics* later);
- and, once, a **gate emphasis** — what the step checklists should weigh most.

Whether a stage's goals lean technical or product is expressed by the goals themselves, not a
fixed flag — it varies with the product. The process core reads whatever status is active and
applies its per-step parameters (see [`../process/OPERATING-LOOP.md`](../process/OPERATING-LOOP.md)).

## File naming — numbered by maturity

Status files are **numbered so they sort in maturity order**, not alphabetically:
`1-concept-viability.md`, `2-pmf.md`, `3-growth.md`. The number matches the `order` field.
This avoids confusion — the folder always reads youngest → most mature top to bottom.

## The active status

Set at the instance level (referenced from the product config / strategy artifact). It changes
as the product matures; the change is a dated change-log entry like any other.

## Default statuses

| # | Status | In one line |
|---|--------|-------------|
| 1 | [concept-viability](1-concept-viability.md) | Prototype/MVP: can it be built, is there demand worth chasing toward PMF |
| 2 | [pmf](2-pmf.md) | First clients; validate repeatable value + monetization so it can scale |
| 3 | [growth](3-growth.md) | Working, profitable product to develop and expand |

## Choosing a status (used at product setup)

During onboarding the agent **proposes** a status rather than asking cold: it presents the options
below with a recommendation, and the human confirms. Pick by where the product actually is today.

| Status | You're here when | This stage optimizes for | Main evidence |
|--------|------------------|--------------------------|---------------|
| **concept-viability** | no product in market yet (or just a prototype/MVP), few or no users, demand unproven | learning fast — is it buildable, is there real demand worth chasing toward PMF | interviews + desk/analytics search (no product metrics yet) |
| **pmf** | first paying/active clients, but repeatable value & monetization not yet proven | proving value repeats and you can charge for it, so it can scale with confidence | internal product metrics + a few interviews for the "why" |
| **growth** | a working, profitable product | scaling acquisition/revenue within guardrails, opening new segments, defending the moats | internal product metrics (dominant) |

Each status file's body adds a fuller description; the agent surfaces this table plus a
recommendation, and the human decides. A company can add or rename stages (see *Add or change a
status*); the setup presents whatever statuses exist.

## Anatomy of a status

Each status is a file `statuses/<order>-<name>.md`:

```yaml
---
name: <status>
order: <n>                       # maturity order; matches the filename number
gate_emphasis: <what the step checklists should weigh most at this stage>
per_step:
  "1":
    goals:                       # a flat list …
      - <goal>
    tools: [<tool>, ...]
  "5":
    goals:                       # … or split by work direction where the step is direction-organized
      development: [<goal>]
      go-to-market: [<goal>]
      back-office: [<goal>]
    tools: [<tool>, ...]
---
```
Body: a description + a dated change log. Directions default to `development · go-to-market ·
back-office` but are an instance config; use whichever the product has.

## Add or change a status

1. Create `statuses/<order>-<name>.md` (numbered by maturity) with the anatomy above.
2. Fill `gate_emphasis` and, **for each step**, its `goals` (optionally by direction) and
   `tools`. Keep goals concrete — they exist to keep the agent focused, not to restate theory.
3. Slot it into the maturity order via both the filename number and the `order` field; renumber
   neighbours if you insert one in the middle.
4. That's it — the process core applies it automatically. No step needs editing.

A company can add stages (e.g. `pre-seed-validation`, `scale-up`, `harvest`) or rename these to
its own vocabulary. The framework only assumes that *a* status is active and exposes its
per-step goals and tools.

## Change log

### 2026-07-19 — added "Choosing a status" (onboarding presentation)
- **From → To:** added a comparison the agent presents at product setup (you're here when · optimizes
  for · main evidence) so it can **propose** a status with context instead of asking cold.
- **Why:** `product-setup` now proposes the status with a recommendation; the human picks with
  context. Supports the corrected onboarding flow.
- **Trigger:** onboarding-flow fix, 2026-07-19.
