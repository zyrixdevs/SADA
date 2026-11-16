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

## Additional module decisions

The entries below are unresolved proposals. Legal, privacy, security or operational review is required where identified. Record an owner, approver, decision version, rationale and review trigger before implementation.

| Question | Why it matters | Options | Recommended default | Risk | Decide before |
|---|---|---|---|---|---|
| Bot identity and cross-server linking | Same display name can refer to different applications | Application ID only; publisher plus app; reviewer-linked aliases | Use stable application IDs and typed publisher evidence; no name-only merge | Incorrect cross-guild linkage | Bot intelligence |
| Integration metadata availability | OAuth scopes and publisher state may not be visible to the adapter | Available metadata only; user-provided; external registry | Treat inaccessible fields as unknown; verify Discord API first | False assurance | OAuth monitoring |
| Bot permission baseline authority | Baselines can be poisoned or stale | Owner-only; dual admin; periodic reconfirmation | Guild admin approval plus revision and audit | Malicious baseline acceptance | Permission drift |
| Bot behavior retention | Long history increases surveillance exposure | Short windows; incident-linked; configurable | Keep bounded aggregates and incident-linked details only | Missing historical context or overcollection | Bot anomaly detection |
| Admin anomaly feature set | Behavioral baselines can encode unfair assumptions | Rules only; factors; no baselines | Start explainable action factors; avoid sensitive proxies | False compromise claims | Identity protection |
| Circuit-breaker semantics | A false trigger can interrupt legitimate moderation | Alert only; local soft hold; local hard limit | Local, opt-in, dry-run first; explicit owner recovery | Lockout or missed containment | Circuit breaker |
| Invite fingerprint and sharing | Invite codes can be sensitive and cross-linkable | Raw code; global hash; guild HMAC; aggregate only | Guild-keyed HMAC, short retention; share only reviewed indicators | Invite exposure or linkage | Invite monitoring |
| Staff reference verification | Stale staff rosters can mislabel legitimate accounts | Manual owner list; role sync; external identity | Guild-managed private list with expiry/revision | Impersonator remains unflagged or false match | Impersonation |
| Message evidence capture | Social engineering and spam may require content context | Structured report; excerpt; full content | Structured report and evidence reference by default | Privacy and reporter safety | Social engineering/spam |
| Unicode normalization profile | NFKC/confusable rules may conflate legitimate multilingual text | Exact match; versioned map; locale profiles | Versioned features, local-only comparison and reviewer correction | Language bias | Spam evasion |
| Mention action thresholds | Community norms differ substantially | Global limits; per-guild thresholds; alert only | Guild-owned configurable limits; read-only rollout | False alarms or abuse | Mention protection |
| Invite attribution sources | Discord event availability can change | Confirmed only; probabilistic; no attribution | Label confirmed/probable/unavailable separately; never infer unknown | Misattributed raid source | Raid analysis |
| Audit reconciliation window and anchoring | Audit events can be delayed or unavailable | Fixed window; source cursor; external digest anchor | Pending before missing; versioned match window; independent anchor later | False tamper claim | Audit integrity |
| Configuration snapshot scope | Snapshots can include secrets or excessive personal data | Full config; security subset; event deltas | Security-relevant fields only; exclude secrets/messages | Overcollection and stale restoration | Drift detection |
| File scanning provider and artifact policy | Files are dangerous and scanners may retain samples | Hash only; isolated scan; external vendor | Hash/metadata first; isolated scanner only after vendor review | Malware exposure or vendor disclosure | Attachment intelligence |
| QR extracted URL retention | Query parameters can contain tokens | Host only; redacted URL; encrypted full URL | Keep host and redacted path; encrypted full value only if case needs it | Credential leakage | QR detection |
| Redirect scanner egress | Resolution can reach internal services or change over time | Hosted sandbox; proxy; no live resolution | Isolated egress proxy with DNS/IP checks on every hop | SSRF or DNS rebinding | Redirect analysis |
| Malware hash algorithms | Equality and feed compatibility depend on digest choice | SHA-256 only; multiple digests | SHA-256 baseline; store algorithm explicitly | Incompatible indicators | File correlation |
| External feed trust/licensing | Feed ingestion may be poisoned or restricted by license | Manual curated; signed feeds; broad feeds | Curated signed feeds with per-source validation and terms review | Poisoning, unlawful redistribution | Feed integration |
| API abuse restriction authority | Client throttling can deny legitimate service | Automated short cooldown; operator-only; key revocation | Reversible route-scoped cooldown with audit and alert | Denial of service against tenant | API abuse |
| Tenant isolation defense | Query filters alone may be bypassed | App-only; RLS; separate schemas | Mandatory scoped repositories plus defense-in-depth RLS review | Cross-tenant exposure | Any production data |
| Operator critical actions and quorum | Operations need safe emergency paths | Single admin; dual approval; break-glass | Dual approval for exports/key changes; emergency access expires and gets post-review | Insider abuse or delayed incident response | Production operations |
| Secret scanner scope and response SLA | Findings can themselves expose secrets | CI only; repo history; logs/config | CI and approved repos; persist fingerprints only; rotate with owner | Leaked credential remains active | Build pipeline |
| SBOM and provenance profile | Signature does not establish trustworthy build | Format/tool choice; signed attestations; reproducible build | Standard signed provenance + SBOM, independent verifier | Supply-chain compromise | First release |
| Vulnerability remediation priority | Severity alone misses actual exposure/context | CVSS; exploitability; service exposure | Versioned factors; operator-owned deadlines; no automatic claims | Unpatched high-risk component | Dependency intelligence |
| Intelligence TTL and correction duty | Stale data can continue influencing decisions | Fixed TTL; per-type policy; source TTL | Per-indicator class and source validity with revisioned correction | Delayed correction or unnecessary retention | Cross-server distribution |
| AI provider and evidence processing | Evidence may contain private data or hostile instructions | Local only; approved provider; no AI | Non-AI path is complete; no evidence leaves boundary without explicit review | Data disclosure or unsafe recommendation | Optional AI |

**Review gates:** legal/privacy review for message/file capture, invite cross-server correlation, identity anomaly data, external feed licensing and AI processing. Security review for scanner egress, signing keys, tenant isolation, operator access and API restrictions. Operational review for circuit-breaker recovery, patch SLAs, data residency and advisory recipients.
