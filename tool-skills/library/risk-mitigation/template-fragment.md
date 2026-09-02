<!--
  template-fragment: risk-mitigation → fills {#risk-mitigation}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Risk mitigation {#risk-mitigation}
_Every carried `R-…` becomes managed: mitigation + owner + observable trigger + review date +
status. Carried risks arrive triaged from `pre-mortem` (Step 3) and `niche-risks` (Step 2) — pull
them from the R- register; never re-surface or re-score here. Upsert the same register row; this
section is a projection of it._

<!-- card -->
**Exposure read:** <one sentence — the top carried risk by P×I, whether its mitigation is in place
(its status), and the trigger being watched>.

| `R-…` | Risk | Likelihood | Impact | Mitigation | Owner | Trigger (act-now signal) | Due (mitigation review date) | Status |
|-------|------|------------|--------|------------|-------|--------------------------|------------------------------|--------|
| R-… | <concrete failure story, from triage> | H/M/L | H/M/L | <what we'll actually do — an action, not "monitor"> | <one person> | <observable signal: metric crossing a line / event occurring> | <YYYY-MM-DD — when the mitigation is reviewed> | open / mitigating / contained / realized / closed / accepted |

_**Trigger vs Due:** the trigger is the signal to act; the due is the date the mitigation is
reviewed even if the trigger never fired. Both, or the risk isn't managed. Ranked by the P×I score
carried on the register row (5/3/1 backing, set at triage — not re-derived here)._

**Written back:** each row upserted into the R- register (mitigation · owner · trigger · due ·
status on the same `R-…` entry the upstream triage created).

**Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while unconfirmed> ·
**alternatives considered:** <!--d:alts--> <one alternative weighed and why it lost, or what makes
the choice forced — a bare "none" is a defect>
