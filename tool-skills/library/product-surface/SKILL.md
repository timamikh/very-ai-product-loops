---
name: product-surface
kind: method
produces: product-surface
reads_registers: []
writes_registers: []
inputs: [interview, kb, git]
prerequisites: [product-concept, channels-draft]
used_by_steps: [3, 4]
opinionated: false
method_basis: "Touchpoint mapping + instrumentation planning (every user-interaction surface and every behavior/metric collection point)"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.2
updated: 2026-08-09
---

# Product Surface

Map **every surface through which the product meets the user, and how each is instrumented**.
Fills `{#product-surface}` (sketched at Step 3, refined at Step 4). This is the bridge from
strategy to measurability: a channel with no instrumentation can't be judged; a metric with no
collection point can't exist.

**Method basis.** Touchpoint mapping + instrumentation planning.

## When to apply
- Step 3, alongside channels — to see the full interaction surface.
- Step 4, refined — the instrumentation defines where the metric tree's data comes from.

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

Where `product-surface` **contributes** to the Step-4 `{#architecture}` section (primary
`architecture-c4`), its working for that section lands in `architecture-c4`'s worklog, not a file of its
own — the first tool in a `<!-- tool: A, B -->` marker owns the section's worklog
(`process/CONVENTIONS.md` → *Several methods → one section: the first is primary*).

## Output
Projects `{#product-surface}` via [`template-fragment.md`](template-fragment.md) from its worklog;
contributes to `{#architecture}` through `architecture-c4`'s worklog. Inputs via
[`questions.yaml`](questions.yaml).
