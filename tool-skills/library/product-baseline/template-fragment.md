<!--
  template-fragment: product-baseline → contributes to {#product-surface} (Step 3, second marker)
  and writes `live` rows to registers/surfaces.md + registers/features.md.
  This is the WORKLOG's shape — the register headers come verbatim from the skeletons
  (process/reference/register-skeletons/), never retyped from here.
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## As-is inventory — <date>, from <source(s)>

_Trigger: <first pmf pass / drift: … / release: …>. Sources read: <walkthrough / analytics export /
interview / git passport — cite each>. Unit = feature, not control._

**Surfaces walked:**

| Surface | Type | State found | Evidence |
|---------|------|-------------|----------|
| e.g. Landing | landing | live | [sourced: walkthrough <date>] |
| e.g. Old blog | content | retired (quietly, ~<when>) | [sourced: interview <who>] |

**Features per surface:**

| Feature | Surface | Direction | Serves | Owner | Evidence |
|---------|---------|-----------|--------|-------|----------|
| e.g. Autopay | S-… | development | `M-retention` | … | [sourced: analytics <date>] |
| e.g. AI content line | S-… | go-to-market | — to clarify — | … | [sourced: walkthrough] |

**Reconciliation diff (register ↔ product):**

| Register said | Product shows | Action |
|---------------|---------------|--------|
| `F-…` planned | shipped | flip → live · why did its readout never run? |
| `F-…` live | gone | → retired, note when/why |
| — (unknown) | <feature> | new live row · what shipped outside the loop? |

**Written to registers:** S-… rows → `surfaces.md` · F-… rows → `features.md` (all `[sourced: …]`).
**Section refresh:** `{#product-surface}` updated where the inventory moved it (cites `S-…` in prose).
**Open serves-links:** — to clarify — …
