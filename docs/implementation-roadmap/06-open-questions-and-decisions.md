# 06 — Open questions and decisions

**Unresolved; proposed defaults are not policy.** Record owner, approver, version, rationale, date, review trigger, tests.

| Question | Why | Options | Proposed default | Risk | Decide before |
|---|---|---|---|---|---|
| Global reviewer quorum | Prevent single-review error | One, two, panel | Two independent; no self-approval | Delay/collusion | Enforcement |
| Evidence retention | Privacy and appeal | Per class, fixed, jurisdiction | Minimize per class; reviewed hold | Lose appeal context or overretain | Collection |
| User notification | Transparency/safety | Immediate, decision, delayed | Verified private notice when safe | Reporter exposure/evasion | Cases |
| Appeal timeline | Fairness/load | Fixed, rolling | Publish target; allow material new evidence | Backlog/cutoff | Decisions |
| Sharing permissions | Scope | Per field, category, case | Explicit purpose/field/guild controls | Fragmentation/overcollection | Adapter |
| Source reliability | Evidence weighting | Factors, model, none | Explainable factors with denominator | Feedback bias | Scoring |
| Threat weights | Review priority | Rules, calibrated model, none | Versioned gates; never punish from score | Gaming/bias | Detection |
| Correlation threshold | Candidate quality | Category gates, human-only | Candidate-only gates evaluated offline | False/missed links | Network |
| Independent reports | Collusion | 1, 2, N | Proposed two candidate sources; humans decide | Collusion/blind spot | Global case |
| Data residency | Legal transfer | Single/selected/per tenant | Decide after legal inventory | Transfer exposure | Production |
| Deployment topology | Failure/ops | Modular, split, broker first | Independent API/worker + PostgreSQL | Blast radius | Production |
| Operator roles | Accountability | Owner, vendor, shared | Named separation before collection | Unowned incident | Production |
| Advisory delivery | Noise/disclosure | Category, critical, all | Subscription/category, dedupe, expiry | Missed/flooded | Advisory |
| Five-guild proposal | Existing GBS ambiguity | Candidate/review/omit | Unapproved; evaluate offline | Arbitrary gate | GBS |
| 5,000-member proposal | Denominator unclear | Per source/aggregate/target/omit | Do not use until justified | Small-guild bias | GBS |
| Trusted domain exception | Bypass risk | Local/global | Expiring local; reviewed global | Abuse | Scam |
| Ban-evasion signals | Privacy/bias | Public/local/device | No device/IP; legal review | False identity | Evasion |
| Evidence artifact scope | Context/privacy | Ref only/redacted/full | Reference by default | Weak case/overcollect | Vault |
| Observatory cohort floor | Re-identification | Fixed/adaptive | Suppress small/overlap queries | Utility loss | Observatory |
| Emergency authority | Urgency abuse | Owner/quorum/narrow | Current local auth, reversible only | Delay/abuse | Playbooks |
| Holds and deletion | Holds can defeat expiry | Ops/counsel/dual | Scoped time-limited dual review | Indefinite retention | Vault |
| API audience | Exfiltration/support | Internal/partner/public | Internal first; reviewed partner | Abuse | External API |

Legal/privacy/operational review required for retention, notice, lawful basis, residency, evasion, export, operator roles. Gate order: auth/data inventory before foundation; consent/retention before collection; quorum/appeal/notice before global decision; scopes/suppression before public surfaces.
