---
node_type: worklog
tool: architecture-c4
step: 3
fills: [architecture]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — architecture-c4 (fills `#architecture`)

C4 **Context** level only (product · users · external systems). Refined at Step 4 (external systems → COGS /
dependency risks).

- **System:** Decksmith.
- **Actors:** deck-maker (lead segment); team admin (Team tier).
- **External systems / dependencies:**
  - LLM provider(s) — content + layout reasoning. Cost + availability outside our control → COGS (Step 4) +
    `R-004`. Mitigation: multi-model abstraction.
  - **Native-fidelity render/export engine — in-house, the moat** (NOT external; the thing incumbents don't do).
  - Auth; payments (e.g. Stripe); product analytics; email/notifications; design-corpus + font/brand asset store.
- **Flow:** user → app → LLM (draft content/structure) → **fidelity engine** (native render) → export .pptx/.key.
- **Feeds downstream:** LLM → Step-4 COGS + `R-004`; fidelity engine → the moat (`value-definition`); no exclusive
  external integration yet → no new lock-in moat at concept stage.

## Change log
### 2026-08-14 — created (rebuild)
- **From → To:** — → C4 context sketch; LLM as the cost/dependency, the fidelity engine as the in-house moat.
- **Why:** enough to reason about cost, dependency, and moat — not to design the build.
- **Trigger:** Step-3 strategy, rebuild.
