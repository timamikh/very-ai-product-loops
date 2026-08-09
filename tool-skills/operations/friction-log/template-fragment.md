---
node_type: template-fragment
title: FRICTION.md — the instance's framework-friction log
status: draft
version: 0.1.0
updated: 2026-08-09
---

# `FRICTION.md`

The whole file. Frontmatter once, then dated entries newest first, appended at step 7 of every pass.
Written in the instance's documentation language (`config.yaml` → `language`).

```markdown
---
node_type: friction
title: Friction log — <product>
status: living
updated: <YYYY-MM-DD>
---

# Friction log

Where the *framework* got in the way. Never product values, never decisions, never state — those live
in the artifacts, the registers and their change logs. Newest entry first; entries are appended,
never rewritten.

## <YYYY-MM-DD> — <step N · what the pass was doing>

- **Could not be done as written:** <the step / prerequisite / template slot / rule, and where it
  lives: `process/OPERATING-LOOP.md` → *Delegation*, `tool-skills/library/pricing/SKILL.md` step 3>
- **Did instead:** <the workaround — this is the finding>
- **Would have worked if:** <concretely, at the level of a file and a line>
- **Cause:** framework defect · rule in the wrong place (nobody reads it where it applies) · agent
  error <— say which you think it was>

## <YYYY-MM-DD> — <step N · …>

- **Nothing to report.** Checked: <the steps, skills and templates this pass actually exercised>.
```

## A filled example

```markdown
## 2026-08-09 — step 4 · attaching a metric to a hypothesis

- **Could not be done as written:** `steps/4-strategic-plan/README.md` gate item "every hypothesis in
  `testing` has a metric" — two hypotheses needed two different verdicts, so no single metric could
  satisfy either of them.
- **Did instead:** attached the metric that fit the first half and left the second untested, without
  recording that the item was only half done.
- **Would have worked if:** the gate item said what to do when one hypothesis needs two verdicts —
  the split rule exists in `process/CONVENTIONS.md` → *Links & register item IDs*, but nothing at the
  gate points to it.
- **Cause:** rule in the wrong place — the rule was correct and I did not reach it where it applied.

## 2026-08-09 — step 5 · tactical plan, go-to-market direction

- **Nothing to report.** Checked: the step README's gate checklist, `prioritization` and
  `segment-cvp` including their template fragments, and the `state.yaml` tick keys.
```
