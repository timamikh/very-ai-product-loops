<!--
  template-fragment: projection → writes EXISTING artifact sections; it adds no section of its own.
  The section's content shape comes from the METHOD's template-fragment.md (or the step template for
  a synthesis section). What this fragment fixes is the anatomy every projected section shares.
-->

# The anatomy of a projected section

```markdown
## Market sizing {#market-sizing}
<!-- tool: market-sizing -->

TAM is bounded by the 4,100 mid-size clinics in the region [sourced: registry 2026-05]. <!-- card -->

<the conclusion, in the shape of tool-skills/library/market-sizing/template-fragment.md>
```

- **`{#id}` + `<!-- tool: … -->` (or `<!-- synthesis -->`)** — from the step skeleton, kept exactly;
  the tool id resolves the worklog (`<step-folder>/<tool>.md`) the section projects from.
- **`<!-- card -->`** — at most one per section, on a line the section already has (CONVENTIONS →
  *Card line*). Trailing → that line is the board card's face; alone on a line → the paragraph below
  it. No qualifying line → no mark; the card shows title + status.
- **Sign-off markers** (`confirmed:` / `contested:`) — never written by this pass. Present ones
  are **removed** when the re-projection changes the conclusion; the `theses` pass re-adds them.
- **Content** — the worklog's conclusion in the method fragment's shape: same tags, ⚙️ kept,
  `— to clarify —` for gaps, forks as options.
