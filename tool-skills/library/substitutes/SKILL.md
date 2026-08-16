---
name: substitutes
kind: research
produces: substitutes
prerequisites: [the job/segment]
reads_registers: []
writes_registers: [risks]
inputs: [interview, kb, research]
used_by_steps: [2]
opinionated: false
method_basis: "JTBD-competition — alternatives incl. do-nothing / do-it-manually / self-build; Porter threat-of-substitutes"
evidence_standard: external-sources
volume_rule: "the three baseline substitutes (do nothing · do it manually · build it themselves) always enumerated, plus ≥2 adjacent"
selection_rule: "a substitute that wins in a real segment is promoted to the risk register; the rest stay in the map"
rejects_shown: required
status: draft
version: 0.1.3
updated: 2026-08-09
---

# Substitutes

Map the **non-obvious competition** — everything the customer could use instead of us to get the
same job done, including **doing nothing**, **doing it manually**, and **building/hosting it
themselves**. Competition is defined by the *job* the customer is hiring for, not by our product
category. Fills `{#substitutes}`.

**Method basis.** JTBD competition: the customer already has a way to make progress on the job, and
that incumbent way — however crude — is our real competitor. Paired with Porter's threat of
substitutes: a substitute is any alternative that satisfies the same need, and a strong one caps
our price and adoption regardless of how few "direct" rivals exist.

## When to apply
- Step 2, once the job/segment is defined (competition is scored against a specific job).
- Whenever direct-competitor analysis looks thin — a near-empty competitor table usually means the
  real competition is a substitute, not a category peer.

## Prerequisites
- **The job/segment** — whose job, and which job, we score substitutes against. *Missing → run
  `segmentation` / `jtbd`.*

## How to do it
1. **Frame by the job, not the category.** Start from the customer's job-to-be-done and ask "what
   else gets this job done?" — not "who else sells a product like ours?".
2. **Force the three baseline substitutes.** Always enumerate, even if they feel trivial:
   - **Do nothing** — living with the problem / status quo.
   - **Do it manually** — spreadsheets, email, a person, a one-off script.
   - **Build / host it themselves** — in-house build or self-hosted open source.
3. **Add at least two adjacent ones.** Repurposed tools, generalist platforms, and services from
   other categories that happen to close the job. The baseline three plus two adjacent is the floor:
   a substitute map that stops at "do nothing" has not left the room the product was designed in.
4. **For each substitute, answer two questions.** *Why does the customer choose it?* and *When does
   it win against us?* — the specific segment, price point, or trigger where the substitute is the
   rational pick. Both answers are claims about the outside world: tag each `[sourced: interview …]` /
   `[sourced: <named source>, as_of …]` / `[assumption]`, judged per fact type against
   [`../references/evidence-standards.md`](../references/evidence-standards.md). "Everyone just uses
   spreadsheets" with nothing behind it is an assumption, and usually a comforting one.
5. **Find the self-build threshold.** Name the point where "just build it ourselves" beats buying
   from us (team capability, volume, data sensitivity, cost crossover).
6. **Name the switching friction.** What keeps a customer on the substitute — habit, sunk cost,
   integration, trust — is the barrier our offer must overcome.
7. **Seed the risk register.** Every *strong* substitute — one that wins in a real segment — becomes
   `R-…`; weak or purely theoretical ones stay in the table only.

## Anti-patterns
- **Direct-analogs-only.** Counting as competition only products in our own category, so the table
  looks empty while the customer quietly stays on a spreadsheet.
- **Ignoring do-nothing.** Treating the status quo as a non-competitor — it is usually the strongest
  one, and the hardest to displace.
- **Underrating self-build.** Assuming customers won't build it themselves when the capable ones
  will, especially past a volume or data-sensitivity threshold.
- **Listing without the "when it wins."** A substitute with no stated winning condition can't be
  compared, defended against, or triaged into the risk register.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/substitutes.md` (`node_type: worklog`,
e.g. `2-analysis/substitutes.md`): the job framed by JTBD, the three baseline substitutes (do nothing ·
do it manually · build/host it themselves) plus the ≥2 adjacent ones, each with its *why the customer
chooses it* and *when it wins*, the self-build threshold, the switching friction, and which strong
substitutes were promoted to the risk register. That worklog is the **source of truth**; the artifact
section `{#substitutes}` is its **projection** into the fixed shape of
[`template-fragment.md`](template-fragment.md) — it holds nothing the worklog does not, and the step's
change-log history lives in the worklog, not the section
(`process/CONVENTIONS.md` → *Step folders & worklogs*). External figures arrive here dispatched from
`sources/` by `source-intake`, cited in the worklog, never linked from the artifact.

## Output
Projects `{#substitutes}` via [`template-fragment.md`](template-fragment.md) from the worklog; inputs via
[`questions.yaml`](questions.yaml).
