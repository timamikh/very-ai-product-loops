---
node_type: card
kind: method
name: product-surface
steps: [3]
prerequisites: [product-concept, channels-draft]
reads: [source:interview, source:kb, source:git]
writes: [worklog, section:product-surface]
opinionated: false
method_basis: "Touchpoint mapping + instrumentation planning (every user-interaction surface and every behavior/metric collection point)"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.2.0
updated: 2026-08-16
---
# Product Surface

Map **every surface through which the product meets the user, and how each is instrumented**.
Fills `{#product-surface}` at Step 3. This is the bridge from strategy to measurability: a channel
with no instrumentation can't be judged; a metric with no collection point can't exist.

**Method basis.** Touchpoint mapping + instrumentation planning.

## When to apply
- Step 3, alongside channels — to see the full interaction surface.
- Step-4 refinement into the instrumentation map: see `instrumentation-plan` (Step 4).

## Prerequisites
- **Product concept** and a **channels draft** (from `channels-expansion`). *Missing → run those first.*

## How to do it
1. **List every surface** the user touches: acquisition/comms **channels**, **landing pages**,
   **mailings/notifications**, in-product UI, the **admin panel**, integrations.
2. **List every instrumentation point**: what **metrics** are collected, where, and the
   **behavior-study** tools (analytics, session capture, surveys, funnels).
3. **Link surface → metric.** For each surface, what do we measure and can we? Gaps become
   instrumentation work (a back-office/dev item later) and `— to clarify —` here.
4. **Note infra implications** for Step 4's cost lines (e.g. analytics stack, email provider).

## Anti-patterns
- **Channels without instrumentation.** Listing where users come from with no way to measure it.
- **Orphan metrics.** Wanting a metric with no collection point defined.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/product-surface.md` (`node_type: worklog`):
the full list of surfaces the user touches (channels, landing pages, mailings, in-product UI, admin,
integrations), the instrumentation points, the surface→metric links with their gaps (`— to clarify —`),
and the infra implications for Step 4's cost lines. That worklog is the **source of truth**; the
artifact section `{#product-surface}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md), holding nothing the worklog does not, with the
change-log history in the worklog (`process/CONVENTIONS.md` → *Step folders & worklogs*).

## Output
Projects `{#product-surface}` via [`template-fragment.md`](template-fragment.md) from its worklog;
inputs via [`questions.yaml`](questions.yaml). At Step 4, `instrumentation-plan` refines this map
(with `#architecture`) into `{#architecture-instrumentation}`.
