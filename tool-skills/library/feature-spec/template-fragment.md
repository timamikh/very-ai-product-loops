<!--
  template-fragment: feature-spec → one item block in {#must} / {#backlog}, development direction
  (the "### Development — Features" subsection). Item form = steps/6-sprint-plan/template.md, field for
  field, in its order; items are numbered 1, 2, 3 within their subsection (sprint-local — the cross-sprint
  identity is the F-…). No card slot: the section's face is the ranking's (prioritization-sprint-plan),
  never one item's. The Decided line closes each item block (evidence_standard: decision).
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

**<n> · <feature name>** — links: `H-…` / `M-…`
- **Feature:** `F-…` (the register row this item advances — an existing `planned` row picked up, or a
  new row minted `planned`: direction · surface `S-…` · serves)
- **Description:** what the feature is
- **Scope:** the tasks to implement it
  - …
- **Acceptance criteria:** binary, checkable — each answerable yes/no (how we know it's done, not what
  we build)
  - …
- **Business value:** value to the business (the `M-…` it moves / `H-…` it tests)
- **User value:** value to the user
- **User stories:** (if applicable) As a <role>, I want <capability>, so that <benefit>.
- **Expected impact:** `M-…` <baseline → expected> / closes `R-…` / tests `H-…` · check-by <sprint/date> [assumption]
- **Owner:** who is accountable for it landing
- **Estimate:** class <S | M | L> + range (~…) — [assumption] until the readout reads the actual
- **Groom:** spec-ready | blocked: <fork> — `6-sprint-plan/feature-grooming.md` (written by
  `feature-grooming` when groomed; the spec itself is authored by `outputs/feature-to-spec` into
  `export-files/<feature>-spec.md`)

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while unconfirmed> ·
**alternatives considered:** <!--d:alts--> <the scope or shape not chosen and why — a bare "none" is a defect>
