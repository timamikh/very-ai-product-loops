<!--
  template-fragment: architecture-c4 → fills {#architecture}
  C4 Context level only. Follow process/CONVENTIONS.md.
-->

## Architecture (C4 Context) {#architecture}

**System:** <the product — one line>

**Actors:** <who uses it — map to segments>

**External systems / dependencies:**
| External system | Role | Cost driver? | Dependency risk? | Moat? |
|-----------------|------|--------------|------------------|-------|
| e.g. LLM provider | generation | yes (COGS) | yes | — |
| e.g. Payments | billing | small | medium | — |

**Context sketch (optional Mermaid):**
```mermaid
%% keep at C4 Context level
```

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while the agent's
proposal is unconfirmed> · **alternatives considered:** <!--d:alts--> <at least one alternative
actually weighed and why it lost — or what makes the choice forced; a bare "none" is a defect.
Weighed none? Order a refutation — `operations/orchestration` → *The two lenses of a `verify`*>
