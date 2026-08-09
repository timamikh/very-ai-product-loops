---
name: guardrails
kind: method
produces: guardrails
reads_registers: [metrics, risks]
writes_registers: [risks]
inputs: [interview, metrics]
prerequisites: [metric-tree, period-goals]
used_by_steps: [5]
opinionated: false
method_basis: "Guardrail metrics + red lines (steering-committee reconciliation pattern)"
evidence_standard: decision
volume_rule: "all 7 break-categories checked against every period goal before any guardrail is picked"
selection_rule: "a category becomes a guardrail only with an M- node and a stated floor/ceiling; the rest are logged as considered"
rejects_shown: required
status: draft
version: 0.1.2
updated: 2026-08-09
---

# Guardrails

Define **what must not drop while we chase the period's goals** — the metrics and limits we
refuse to sacrifice. Fills `{#guardrails}`. A goal without guardrails invites winning the number
and losing the product (e.g. spiking signups while retention or unit economics collapse).

**Method basis.** Guardrail metrics + red lines, in the spirit of a steering-committee
reconciliation: each cycle names the gate it moves *and* the things it protects.

## When to apply
- Step 5, once period goals are set — every goal gets its guardrails.
- Revisit if a goal starts eroding a protected metric.

## Prerequisites
- **Metric tree** (`M-…`) — guardrails are usually protected metric nodes. *Missing → Step 4.*
- **Period goals** — you guardrail *against* the current goals. *Missing → set them first.*

## How to do it
1. **For each goal, ask "what could this break?"** Retention, unit economics, CAC, quality,
   brand/trust, support load, churn.
2. **Pick guardrail metrics** — the `M-…` nodes that must not cross a threshold. State the
   threshold (floor/ceiling).
3. **State red lines** — qualitative "never do" limits (e.g. dark patterns, off-brand content).
4. **Assign monitoring** — where each guardrail is watched and how often.
5. **Log as risks-not-to-realize** — breaching a guardrail is a risk (`R-…`).

## Anti-patterns
- **Goal without guardrail.** A target with nothing protecting the rest of the system.
- **Unmeasurable guardrail.** "Don't hurt the brand" with no metric or check behind it.
- **Threshold-free.** A protected metric named but no floor/ceiling to breach.

## Output
Fills `{#guardrails}` via [`template-fragment.md`](template-fragment.md); inputs via
[`questions.yaml`](questions.yaml).
