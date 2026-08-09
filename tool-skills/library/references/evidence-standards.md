---
node_type: library-reference
title: Evidence standards — what a source may be used for, and what must be checked before it counts
status: draft
version: 0.1.0
updated: 2026-08-09
---

# Evidence standards

Shared by every library method whose claims rest on evidence — the ones that declare
`evidence_standard: external-sources` or `primary-research` in their frontmatter, and any method
carrying a number into a conclusion. It is read **when a method sends you here**, not on every pass;
that is why it can afford to be specific.

Confidence tags (`[sourced: …]`, `[assumption]`, …) answer *how established is this claim*. This file
answers two different questions the tags do not: **what class of source is this**, and **what may that
class be used for**. A claim can be honestly tagged `[sourced: …]` and still be worthless because the
source cannot carry that kind of fact.

## 1 · A source is judged per fact type

This is the rule that does the most work, so it comes first. There is no such thing as a reliable
source — only a source that is reliable *for a particular kind of fact*.

| The same source | Authoritative for | Worthless for |
|---|---|---|
| A company's own filing / annual report | its own revenue, headcount, segments as *it* defines them | its competitors' shares, the size of "the market" |
| A national statistics office | the indicator it actually measures, on its own definition | anything requiring a different definition of the same word |
| A trade press article | that a statement was made, and by whom | whether the statement is true |
| A vendor's "state of the industry" report | what the vendor wants believed; sometimes their own product data | market size, growth, competitor comparison |
| A named expert with a stated position | an informed opinion, and what practitioners currently believe | a measurement |
| An app-store / registry listing | that the thing exists, its public price, its public claims | usage, revenue, retention |

**How to apply it:** before citing, write the fact and the source next to each other and ask *is this
source in a position to know this?* If not, the claim is `[assumption]` at best, and usually
`— to clarify —`.

## 2 · The credibility pyramid

Top to bottom. Each row says what it is good for; none of them is a blanket permission.

1. **Primary** — the party's own filing, registry record, official statistics, product documentation,
   court record, the raw export. Closest to the event; still bounded by whose definition it uses.
2. **Databases and registries** — statistical bases, company registries, aggregators that report a
   *traceable* original. Good when they name their source; a "database" that does not is press.
3. **Named experts** — a person with a name, a position, and a stake you can see. Opinion, dated.
4. **Reporting / press** — inherits the reliability of whatever it cites, and never exceeds it. If the
   original cannot be reached, treat the number as unsourced.
5. **Research and analyst reports** — method matters more than brand. A report that states its
   sample, definition and date is evidence; one that does not is marketing with charts.
6. **Meta-analyses and reviews** — strong when the underlying studies are named; otherwise a summary
   of unknowns.

**The forbidden zone** — do not use, at any confidence tag:

- content marketing with no stated method, and "X industry statistics 2026" listicles;
- influencer and newsletter summaries of a source you have not opened;
- report mills that sell a number and hide the derivation behind a paywall abstract;
- **anything whose original source cannot be reached.** This is the general case of all of the above.
  A number you cannot trace is not a weak source; it is not a source.

If the forbidden zone is *all* you found, that is itself the finding. Write `— to clarify —` and say
the question currently has no reachable source. A framework that will not let you invent a value also
will not let you launder one.

## 3 · Label what kind of statement it is

Five labels, because they age and fail in different ways. Put the label in the text where the
distinction is load-bearing; always put it in a table column when the artifact tabulates claims.

| Label | What it is | The failure it prevents |
|-------|-----------|--------------------------|
| **fact** | measured or recorded, with a definition and a date | — |
| **estimate** | someone's calculation; the method may be unstated | an estimate quoted as a measurement |
| **forecast** | a statement about the future | a forecast becoming a fact by being repeated |
| **statement** | someone said it | attributing a claim's truth to the fact it was made |
| **pledge** | someone promised to do it | a roadmap promise planned against as if shipped |

This is **orthogonal to the confidence tag** — a vendor's pledge to ship a feature in December is
`[sourced: vendor blog, 2026-06-14]` *and* a pledge, and building a strategy on it is a risk that the
tag alone does not show.

## 4 · Provenance: what must be recorded for every claim

- **The source, as something openable** — a URL, a file path, an export name. Not "industry reports".
- **`as_of` — the date you actually read it.** Not the date on the page; the date you opened it. A
  source that moved or vanished is a normal event, and the read date is what makes the record honest.
- **Whether you opened it.** If you did not, you have no claim. A citation assembled from a search
  result snippet is a fabrication with a footnote.
- **The class** from §2, when the artifact tabulates sources.

**Fail loud.** A source that 404s, sits behind a paywall, or needs credentials you do not have is
reported by name — never quietly dropped from the list, never replaced by a similar-looking one.
Silent substitution is how a research pass ends up with a clean bibliography and a wrong answer.

## 5 · The headline check

**Any number that will end up in a conclusion, a headline, a chart or a decision gets a second,
independent source — before the synthesis, not after it.**

- *Independent* means it does not trace back to the same original. Two articles citing one report are
  one source.
- Agreement within ~20%: use the primary of the two, note the other.
- **Divergence over 20%: report both, mark it `[CONFLICT]`, and do not resolve it yourself.** The
  resolution belongs in the synthesis where the reader can see both numbers, or it belongs to the
  human. Quietly picking the more convenient one is the single most common way a research pass
  produces a confident wrong answer.
- A number with **no** second source is not forbidden — it is *labelled*: single-sourced, and it may
  not carry a decision on its own.

Doing this after the analysis instead of before is worse than not doing it: by then the number is
already load-bearing, and the check becomes a search for permission to keep it.

## 6 · Six questions for any source

Fast pass. Any "no" downgrades the claim; two "no"s and it does not enter the artifact.

1. **Who** produced it, and what do they gain from the reader believing it?
2. **When** — is the date the measurement's or the republication's?
3. **How** — is the method, sample and definition stated?
4. **Of what** — is the thing measured the thing you are claiming? (the definition trap: "users",
   "SMB", "the market" mean different things per source)
5. **Reachable** — can the original be opened, by you, today?
6. **Independent** — does it trace back to something you already counted?

## 7 · What this does not cover

- **Your own product's numbers.** A reading from your own data is reproducible only if its population,
  window and derivation are written down — that is
  [`tool-skills/operations/metrics-capture/`](../../operations/metrics-capture/SKILL.md), and it is
  the internal counterpart of this file.
- **How established a claim is.** That is the confidence tag, in
  [`process/CONVENTIONS.md`](../../../process/CONVENTIONS.md).
- **Whether the method is the right one.** A perfectly sourced answer to the wrong question is a
  method problem, and lives in the method's own `SKILL.md`.
