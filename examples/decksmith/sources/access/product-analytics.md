---
node_type: access-passport
title: Access passport — product analytics panel (fictional)
slug: product-analytics
updated: 2026-08-18
version: 0.1.0
---

# Passport — product analytics panel

One external **point** the instance reads from, recorded from the founder's answers at setup. It is
not evidence and not reasoning — only *how to reach the point*. Values arrive as dated snapshots in
`sources/snapshots/` (via the `pull-analytics-weekly` skill) and are landed into the metric register
by `metrics-capture`. Fictional sample: the panel does not exist yet — it goes live with the
prototype; this passport is the recorded plan for reaching it.

| Field | Recorded answer |
|-------|-----------------|
| What it is | The product's own event-analytics panel for the prototype (activation, generation, export events). |
| Location | Founder's analytics workspace; project **decksmith-proto** (URL supplied to the operator at first live run — not committed). |
| Owner | The founder (also the register `owner` for the metrics it feeds). |
| How to verify reach | The workspace lists project `decksmith-proto` and the last-7-days event count is non-zero. |
| How to recover access | Founder re-invites the operator's account from the workspace members page; no shared credential. |
| Secret handling | No token is written here or anywhere in the repo. It lives only in the operator's own secret store; rotation is a re-invite (see *How to recover access*). |

## Change log

### 2026-08-18 — created
- **From → To:** — → passport recorded from the founder's setup answers
- **Why:** register the analytics point the `pull-analytics-weekly` skill reaches, so the pull has a
  reachable destination and never invents a source
- **Trigger:** framework 0.10 boundary layer — instrumentation prep for the prototype
