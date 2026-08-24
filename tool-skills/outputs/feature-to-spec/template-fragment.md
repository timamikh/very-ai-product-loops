<!--
  template-fragment: feature-to-spec → one deliverable per groomed feature at
  product-loops/export-files/<feature>-spec.md (node_type: deliverable).
  Two skeletons — the groom's doc type picks one. The BRD is the default.
  The deliverable carries its own frontmatter (node_type: deliverable, updated:) and its own
  dated change log — it is authored, not rendered: once delivered, the file is the source.
-->

# Skeleton A — BRD / PRD (product behaviour; audience: product + development)

```markdown
# BRD: <Feature name> — <Product>

> Source: sprint <n> · item <n> · feature `F-…` · links `H-…` / `M-…` · groomed <date>
> (`6-sprint-plan/feature-grooming.md`). Product decisions below are fixed — agreed with the
> product owner; open items are technical only.

## 1. Why (short)
2–4 lines: the problem it closes, what changes, how success will be read (`M-…`). Context, not a
strategy retelling.

## 2. Scope
- **In scope:** one line per groom scope item — one-to-one, nothing beyond the groom.
- **Out of scope (non-goals):** what is deliberately not done, each with its reason (separate
  initiative · not needed now · deferred). Ideas that surfaced during writing land here, never in
  scope.

## 3. Functional requirements
One block per scope item: FR-1, FR-2, …
- Normative lines — "<the product> must …" — behaviour and result, one per line. WHAT, not HOW.
- `[assumption]` — only for small, reversible defaults; consequential ones are forks (section 4).
- **Acceptance criteria** — Given / When / Then, covering happy path, boundaries, errors, empty
  states, irreversible actions:
  - [ ] Given <precondition>, When <action>, Then <checkable result>.

## 4. Technical forks (for the tech lead)
Only technical/implementation forks — carried from the groom, same structure (context · options ·
selection criterion · recommended default · owner). A fork owned by product/design here is a
defect: it should have been asked in grooming.

## 5. Analytics (only if in the groomed scope)
By meaning: what is tracked and for which metric/decision (`M-…`), proposed names in parentheses.
> Names below are recommendations; the codebase's existing event schema wins — reconcile with
> development. Acceptance tests the presence of data by meaning, not a specific name.

## 6. Success metrics
Leading (days–weeks) and lagging (weeks–months); mark the key business-value metric. Metrics rest
on section-5 data.

## 7. Non-functional requirements & constraints
Only what this feature touches: privacy/data isolation, plan/tier limits and billing, behaviour
when dependencies are down. No section the feature doesn't concern. The groom's **required
inputs** (what the developer can't produce — token sets, definitions, example sets) also land
here, each with its owner and due — a criterion in section 3 with no input here is a defect.

## 8. Open questions
Technical only, each with an owner — or questions the product owner explicitly deferred (named as
such, with the groom's deferral note).
- [ ] **[tech lead]** <question> — what it affects.

## Change log
### <date> — authored
- **From → To:** — → v1 from the groom of <date>
- **Why:** …
```

# Skeleton B — tech spec (engine-internal; audience: engineer / AI agent)

Use when the groom's doc type says so: the feature's essence is internal mechanics (algorithms,
contracts, routing, data formats). Describing mechanism here is the point — but the groom's
boundaries still hold: no scope beyond the groom; a mechanism the groom never set and that
matters is a **fork**, not a prescription; contracts and names are proposals under the
codebase-wins disclaimer.

```markdown
# Tech spec: <Feature name> — <Product>

> Audience: the engineer / AI agent implementing this in the existing service. Logic and
> behaviour, not concrete files — follow the current architecture. All IDs, field/event/endpoint
> names and numeric limits are illustrative; the codebase's existing entities win.

## 1. Concept — the flow from input to result, numbered; when it runs / doesn't run
## 2. Entity catalogue (if applicable) — models/services/states with purpose
## 3. Data contracts — input/output objects with every `status`, backend contracts, state objects
## 4. Algorithms & behaviour — each non-trivial branch as pseudocode or steps
## 5. Decision trees — where logic forks on conditions, with final outcomes in the leaves
## 6. Message / UI-data templates — concrete texts (title/body/CTA) where the feature has them
## 7. Limits, plans, access — how limits are checked, what shows when exhausted
## 8. Pipelines (if any) — step contract and context
## 9. Edge cases & errors — the explicit list, each with what the system does
## 10. Observability — the log-record structure; no PII, no dialogue content
## 11. End-to-end order — one pseudocode function from input to return, with early exits
## 12. Acceptance criteria — Given / When / Then on the key paths and edge cases
## 13. Not in this layer — what someone else does (auth, billing, rendering, storage)
## 14. Forks, assumptions, open questions — technical only; product decisions arrived fixed

## Change log
### <date> — authored
```
