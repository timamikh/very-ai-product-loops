---
node_type: extending
title: Extending — which dial to turn, and where its instruction lives
status: draft
version: 0.7.0
updated: 2026-08-20
---

# Extending the framework

The framework is built to be adapted: a company brings its own methods, its own stages, its own
execution streams. This file is the **door** — it names the dial for what you want and routes to the
one instruction that runs it. The instructions live in [`extending/`](extending/), one per kind of
change, each read **only** when you are making that change. This file is read first, every time.

**How a change happens: you ask the agent.** Every dial below is a file in the repo, and every file in
the repo is written by an agent running the loop — describe what you want, or point at an existing
skill to adapt. There is no settings screen: the local console
([`tools/ui/`](tools/ui/README.md)) *shows* what you have and never changes it, on purpose (a form
that fills a method is the failure this framework exists to prevent).

## The dials

| You want to | Instruction | Owner |
|---|---|---|
| **add a product method**, or bend a shipped one to how you work (segmentation, pricing, your own framework) | [`extending/method.md`](extending/method.md) | your product |
| **add a runtime skill** — how the agent works across sessions, not what the product decides | [`extending/operation.md`](extending/operation.md) | your product |
| **add a deliverable format** (a branded deck, a board card, an authored document) | [`extending/output.md`](extending/output.md) | your product or upstream |
| **add or rename a product stage**, or change what a stage asks per step | [`extending/status.md`](extending/status.md) | upstream / your fork |
| **change a section or its columns** in a step artifact (add a field, key a column, reshape a table) | [`extending/section.md`](extending/section.md) | upstream / your fork |
| **add, remove or reorder a step** | [`extending/step.md`](extending/step.md) | **almost never** — read it before trying |
| **change what the console shows** | [`extending/interface.md`](extending/interface.md) | upstream / your fork |
| **change the work directions or the documentation language** | [`extending/config.md`](extending/config.md) | your product |
| **write your product's own pull or push** across the instance boundary | [`process/reference/boundary-layout.md`](process/reference/boundary-layout.md) — an instance card the goal map routes to by trigger | your product |
| **add a rule of your own** (a convention, a gate, a habit you want held) | [`extending/rules.md`](extending/rules.md) — classify it first: check · method · contract | your fork / upstream |
| **add a fourth register** | [`extending/register.md`](extending/register.md) — the four-sign test. The three schemas themselves are canon, not a dial | canon |
| **change what a delegated subagent may do** (its tools, its instructions) | [`tool-skills/operations/orchestration/SKILL.md`](tool-skills/operations/orchestration/SKILL.md) → *On the runtime*. The **rule** is canon and not a dial: only the orchestrator writes ([`process/OPERATING-LOOP.md`](process/OPERATING-LOOP.md) → *Delegation*) | your fork / your setup |
| **contribute a method to the framework itself** | [`extending/method.md`](extending/method.md) → *Contributing it upstream* + [`CONTRIBUTING.md`](CONTRIBUTING.md) | upstream |
| **move to a newer framework version** | [`install/UPDATE.md`](install/UPDATE.md) | your product |

Everything in the vendored framework is **read-only**: updating means re-vendoring at a newer tag,
which overwrites it. That is why your own skills live under `product-loops/` — they survive the update,
and a local skill of the same name wins.

## Rules that hold for any change

- **One mechanism, one way.** If your change introduces a second format or a second path for something
  the framework already does one way, it is the wrong change — see
  [`process/CONVENTIONS.md`](process/CONVENTIONS.md).
- **Classify before you write it.** A rule a machine can verify belongs in the linter; a procedure
  belongs in a skill; only a contract two readers must agree on belongs in `process/`. The three
  classes and the order to try them: [`extending/rules.md`](extending/rules.md). This is what keeps the
  always-loaded rule set from thickening with every lesson learned.
- **The agent never invents the method.** If you have not said what a new method *does*, its content
  lines stay `— to clarify —`. A plausible-looking method nobody chose is worse than a blank one.
- **The linter is the gate.** `python3 tools/lint.py <instance>` reports 0 errors before a change is
  done — name the instance, and check the line it prints (`instances checked: …`): a run that found
  nothing to check is a failure wearing a success message. It checks wiring and enums — not whether
  your method is any good.
- **A checklist never re-implements the linter.** Every instruction here ends in a checklist, and it
  holds only what a machine cannot judge. Anything a machine *can* judge is a check in
  [`tools/lint.py`](tools/lint.py) instead — a hand-held copy of a machine rule is one more thing to
  drift.
- **History is recorded where the file lives:** instance files (artifacts, registers, sources, handoff)
  carry a dated change log; framework files carry a `version` bump and a line in
  [`CHANGELOG.md`](CHANGELOG.md).
- **Subtraction is part of the job.** A rule stated in two files is two places to drift. When a change
  touches a duplicated rule, delete the copy in the same change and leave a pointer.
