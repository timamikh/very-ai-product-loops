---
name: brief
kind: template
produces: product-loops/briefs/<slug>.md
prerequisites: [the problem or opportunity this frames, who it is for, how success will be judged]
reads_registers: [hypotheses, metrics, risks]
writes_registers: []
inputs: []
used_by_steps: []
opinionated: false
method_basis: "Structured brief — problem · goal · target metric · scope in/out · constraints · success criteria · decision owner"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.2
updated: 2026-08-09
---

# Brief

A **one-page framing** that aligns a team before work starts — on an initiative, an experiment,
or an epic — by stating the problem, the one goal, the metric that will judge it, what's in and
out of scope, the constraints, and who decides. Produced as a **standalone one-page file** at
`product-loops/briefs/<slug>.md` (not an artifact section) — `to-document` can render it to `.docx` on request.

**Method basis.** The structured brief: `problem · goal · target metric · scope in/out ·
constraints · success criteria · decision owner`. Its whole value is forcing agreement on *why*
and *how we'll know* **before** anyone argues about *how to build*.

**Relation to neighbours.** `concept-formation` shapes the whole **product** concept (Step 1);
`feature-spec` / `activity-spec` are the concrete **build items** (Step 6). `brief` sits between
and above them — the **"why + what + how we'll know" wrapper for a chunk of work at any altitude**,
authored *before* it's decomposed. One brief per initiative — not per feature. When approved, it
hands off to `concept-formation` (product-level) or `feature-spec`/`activity-spec` (build-level).

## When to apply
- Before an initiative, experiment, or epic that several people will work on — to align on the why.
- **Any step**, at any altitude, when a chunk of work needs a shared frame before it's specced.
- When a discussion keeps jumping to "how" and no one has written down the "why" or the metric.

## Prerequisites
- **The problem or opportunity this frames** — the change in the world it exists to make; link the
  `H-…` / `R-…` if it has one. *Missing → there is nothing to brief yet; frame the problem first.*
- **Who it is for** — the segment/team/stakeholder the work serves.
- **How success will be judged** — at least a candidate metric. *Missing → run `metric-tree` to
  bind it to an `M-…`.*

## How to do it
1. **State the problem/opportunity.** The change this exists to make, tied to an `H-…` or `R-…`
   where one exists. If you can't state the problem, there's nothing to brief.
2. **Set one goal and its target metric.** A single outcome, read against an `M-…`. Not a list of
   goals — one.
3. **Draw scope in and out.** Explicitly what this does **not** cover. The out-of-scope list is
   what actually stops scope creep.
4. **Name the constraints.** Budget, time, tech, policy, dependencies.
5. **Fix success criteria and the decision owner.** What "done / it worked" means, and who calls it.
6. **Keep it to one page.** If it needs more, it's not a brief — it's a plan; hand the detail to
   the spec tools.

## Anti-patterns
- **Solution as problem.** "Build X" with no problem stated — the brief pre-decides the answer.
- **No metric.** A brief no result can be checked against.
- **No out-of-scope.** Everything's in, so scope creeps unchecked.
- **Goal soup.** Many goals, so none is *the* goal.
- **A brief that's really a spec.** It grows task lists and user stories — hand those to
  `feature-spec` / `activity-spec`.

## Output
Produced as a one-page file at `product-loops/briefs/<slug>.md` from
[`template-fragment.md`](template-fragment.md); inputs via [`questions.yaml`](questions.yaml). It is
its own document, not a section of a step artifact (an adapter may render it — `to-document` →
`.docx`). A framing wrapper callable at any altitude; on approval it
hands off to `concept-formation` (product-level) or `feature-spec` / `activity-spec` (build-level).
