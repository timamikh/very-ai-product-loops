---
node_type: worklog
tool: product-surface
step: 3
fills: [product-surface]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — product-surface (fills `#product-surface`)

Touchpoint + instrumentation map. Sketched here, refined at Step 4 (instrumentation defines where the metric
tree's data comes from).

| Surface | Metric / instrumentation | Can we measure? |
|---------|--------------------------|-----------------|
| Web app (generate/edit/export) | product events: generate, export, keep-vs-redo (→ `M-ns-kept-decks-wk`) | needs event instrumentation (Step 5/6) |
| Export pipeline (native .pptx/.key) | `M-edit-fidelity` = share of natively-editable objects | needs pipeline instrumentation — **the concept-proving metric** |
| Landing pages (per channel) | funnel analytics per channel | standard analytics |
| Onboarding emails/notifications | open/click, time-to-first-export (`M-activation`) | email provider + events |
| Brand-kit setup | created/used | events |
| Admin panel (Team) | seats, usage | — to clarify — (Team tier later) |

- **Gaps → instrumentation work (Steps 5–6):** product events, export-pipeline fidelity capture.
- **Infra implied (Step-4 cost lines):** analytics stack, email provider, LLM inference (COGS).

## Change log
### 2026-08-14 — created (rebuild)
- **From → To:** — → 6 surfaces mapped to instrumentation; fidelity capture flagged as the key gap.
- **Why:** a channel with no instrumentation can't be judged; a metric with no collection point can't exist.
- **Trigger:** Step-3 strategy, rebuild.
