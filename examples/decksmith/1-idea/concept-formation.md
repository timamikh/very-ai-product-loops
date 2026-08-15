---
node_type: worklog
method: concept-formation
step: 1-idea
produces: [concept, solution]
status: draft
source_of_truth: true
drafted_by: loops-draft
drafted: 2026-08-14
---

# Worklog — Concept Formation (Decksmith)

> Method: `concept-formation` (April Dunford "the shift" + problem→solution articulation).
> Applied to `examples/decksmith/sources/founder-brief.md` (captured 2026-07-16), read 2026-08-14.
> This is the **source of truth**; `{#concept}` and `{#solution}` are projections of what follows.
> Concept stage — no product in market, so most content is `[assumption]`. Everything ⚙️ (agent
> proposal awaiting human confirmation).

## 0 · Inputs used (from the founder brief)

- **The idea:** current AI slide tools force one of two bad options — **pretty-but-locked** (exports
  images / a rigid template you can't really edit) **or editable-but-ugly** (dumps plain text into
  default PowerPoint styling). Founder wants a generator that outputs **native, fully editable**
  `.pptx`/`.key` (real shapes, text, editable layouts) that **also look designed**. [sourced: founder brief]
- **Product name:** Decksmith (fictional sample). [sourced: founder brief frontmatter]
- **Stated pains** (founder's observations):
  - **P1 — "looks templated":** sales/marketing regenerate AI output by hand because it looks
    templated; the tool saves less time than promised. [sourced: founder brief]
  - **P2 — wrong structure/story:** decks come back with the wrong structure/story for the audience,
    not only a visual problem. [sourced: founder brief]
  - **P3 — editability is table-stakes:** locked/image output is a non-starter in this crowd. [sourced: founder brief]
- **Have / can build (honest inventory):** prototype that emits native slide objects + applies
  layout/spacing rules, quality-at-scale unproven; a small corpus of well-designed decks to learn
  from (to be assembled); founder's design taste/credibility. [assumption]
- **Founder's early bets (inputs, not my discoveries):** lead with salespeople & marketers; riskiest
  thing is **feasibility**; monetization deferred to Strategy. [sourced: founder brief] / [assumption]

## 1 · One-line concept  → projects into `{#concept}` first line

⚙️ **Decksmith is an AI slide generator that produces native, fully editable `.pptx`/`.key` decks
that already look designed — for the people who make client-facing decks (salespeople & marketers).**
[sourced: founder brief]

- Category: AI slide/deck generator.
- Core thing: output is *simultaneously* native-editable **and** designed (the whole point).
- Who: salespeople & marketers — carried from the founder's lead-segment bet [assumption]; sharper
  segmentation is out of scope here (that is `segmentation` / `segment-pains`, later in Step 1/2).
- A stranger should be able to repeat it as: "it makes AI decks you can actually edit that don't look
  templated."

## 2 · The shift (Dunford — the either/or it collapses)  → `{#concept}` shift line

⚙️ **Today**, every AI slide tool makes you pick one of two bad options: a deck that looks good but is
**locked** (images / rigid template), or a deck you can **edit** but that looks **ugly/templated** — so
you either accept a deck you can't change or you regenerate the "designed" one by hand. **With
Decksmith**, that either/or disappears: the output is native-editable **and** already designed, so you
*edit* the deck instead of *rebuilding* it.

- The current-alternative half ("pick one of two bad options", "regenerate by hand") is
  [sourced: founder brief].
- That Decksmith actually collapses the trade-off is [assumption] — unproven until the engine ships.
- The shift is the concept's spine: remove either "editable" or "designed" and Decksmith degrades into
  one of the two existing bad options.

## 3 · Riskiest assumption  → `{#concept}` riskiest line + one hypothesis to mint

⚙️ **The engine can *reliably* produce files that are both genuinely editable and genuinely
well-designed — at scale, not just in a hand-picked demo.** [sourced: founder brief — the founder's
stated riskiest bet] / [assumption]

- Why it sinks the concept if false: the entire concept *is* the collapse of the editable-vs-designed
  trade-off (§2). If output at scale is either not truly editable or not truly designed, Decksmith
  becomes just another instance of the two bad options it set out to replace — there is no shift left.
- This aligns with the founder's own call (riskiest = **feasibility**); I am not treating it as my
  discovery, I concur with it.
- **Hypothesis to mint (words only — orchestrator allocates the id):** *"An AI engine can reliably
  emit `.pptx`/`.key` files that are simultaneously fully native-editable and judged well-designed by
  the target buyers, at production scale."* Belongs in the `hypotheses` register; `concept-viability`
  will make it the center of gravity. **I do not allocate `H-0xx`.**
- **Secondary assumption worth a second hypothesis (⚙️, orchestrator's call whether to mint):** a
  *demand-side* belief — that "editable **and** designed" is genuinely what makes buyers stop
  hand-regenerating (i.e. the trade-off, not price/structure/trust, is the binding pain). Feasibility
  is the riskiest *build* bet; this is the riskiest *value* bet. Named here so it is not hidden; not
  proposed as the single riskiest, which per the founder is feasibility.

## 4 · Solution stub  → projects into `{#solution}` (moves ↔ pains; not feature design)

Two-to-three moves that deliver the shift, each tied to a stated pain. This seeds `{#solution}`; it is
**not** feature design (that is downstream of `segment-pains`).

| ⚙️ Move | Delivers | Pain it answers | Tag / note |
|---|---|---|---|
| **M1 — Native-object rendering.** Emit real shapes/text/layouts (not images), so output opens fully editable in PowerPoint/Keynote. | the "editable" half of the shift | **P3** (editability table-stakes) | [sourced: founder brief — prototype exists] / quality-at-scale [assumption] |
| **M2 — Design-pattern learning + layout rules.** Learn from a curated corpus of well-designed decks and apply layout/spacing rules so output "looks designed," not templated. | the "designed" half of the shift | **P1** ("looks templated" → hand-regeneration) | [assumption] (corpus to be assembled) |
| **M3 — Audience-aware structure/story (proposed).** Build the deck's narrative for the target audience, not just fill slides. | the "right story" beyond visuals | **P2** (wrong structure/story) | [assumption] — see gap below |

- M1 + M2 together are the minimal pair that produces the shift (editable AND designed). M3 answers a
  pain the founder named but sits on shakier ground (see §5 gap / fork).

## 5 · Gaps, forks, and what I could not settle

- **Gap — M3 has no matching build capability.** The founder names P2 (wrong structure/story) as a
  real pain, but the have/can-build inventory only covers rendering (M1) and a design corpus (M2) —
  **nothing about narrative/structure generation.** Whether audience-aware story is *in the concept's
  first bet* is **— to clarify —** and is a human-owned decision (see fork).
- **Open fork — concept scope (NOT decided; 2–4 options):**
  - **A. Narrow (editable + designed only).** Concept = M1 + M2; structure/story is a later expansion.
    *Trade-off:* tightest, most testable feasibility bet; concept sentence stays crisp; but leaves P2
    (a pain the founder called out) unaddressed at launch.
  - **B. Full (editable + designed + right story).** Concept = M1 + M2 + M3.
    *Trade-off:* answers all three stated pains and a richer shift; but widens the riskiest-assumption
    surface (now also "can it get the *story* right?") and needs a capability the inventory doesn't yet
    claim.
  - **C. Sequenced.** Ship A now, commit to B as the roadmap's next bet once feasibility of M1+M2 holds.
    *Trade-off:* de-risks the build while keeping the fuller vision; but the concept sentence must not
    over-promise story on day one.
  - ⚙️ **Recommendation: C (sequenced).** Keeps the riskiest assumption focused on the one thing the
    founder already flagged (feasibility of editable+designed), honours P2 as a stated pain without
    betting the concept on an unbuilt capability. Human owns the choice.

## 6 · Confidence & provenance summary

- One-liner: [sourced: founder brief] (derived from the stated idea + lead-segment bet).
- Shift: current-alternative half [sourced: founder brief]; collapse-of-trade-off half [assumption].
- Riskiest assumption: [sourced: founder brief] as the founder's bet, [assumption] as unevidenced.
- Solution moves M1/M2/M3: M1 grounded in a stated prototype [sourced] but scale [assumption]; M2/M3
  [assumption].
- Everything is ⚙️ — no human has confirmed the concept. Concept stage, no product in market.

## 7 · Projection notes for the orchestrator (fragment fill)

- `{#concept}` line 1 ← §1 one-liner, tag `[sourced: founder brief]`.
- `{#concept}` shift line ← §2, tag `[assumption]`.
- `{#concept}` riskiest line ← §3 primary; the hypothesis text in §3 is the row to mint in
  `hypotheses` (id is the orchestrator's to allocate). Consider the secondary demand-side hypothesis
  in §3 as a possible second row.
- `{#solution}` stub ← §4 table (M1–M3 ↔ P3/P1/P2). M3 carries the §5 `— to clarify —` / fork.
- `{#concept}` **Decided:** line ← `2026-08-14 · by: ⚙️ (PO to confirm) · alternatives considered:
  the two rejected framings — "pretty-but-locked" and "editable-but-ugly" — which the shift collapses`.
  Mark ⚙️: agent-proposed, not human-confirmed.

## Change log

- 2026-08-14 — Initial draft from founder brief (loops-draft). Four items drafted: one-liner, shift,
  riskiest assumption (feasibility, described for minting), solution stub M1–M3. One open fork
  (concept scope) and one `— to clarify —` (M3 build capability) recorded.
