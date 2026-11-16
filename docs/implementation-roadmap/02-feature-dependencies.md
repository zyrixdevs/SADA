# 02 — Feature dependencies

```mermaid
flowchart TD
 G[Governance and consent] --> E[Event and evidence contracts]
 E --> B[Identity API inbox/outbox audit]
 B --> C[Cases timeline appeals]
 C --> T[Trust engine]
 E --> D[Threat DNA]
 E --> R[Raid detection]
 E --> A[Admin activity]
 E --> S[Scam indicators]
 D --> N[Network and campaigns]
 R --> N
 S --> N
 T --> N
 N --> V[Advisories]
 C --> GB[Global Ban review]
 C --> P[Playbooks]
 P --> I[Impact simulator]
 I --> X[Recovery assistant]
 N --> O[Observatory]
 B --> API[External API]
```

All features require consent, tenant auth, provenance, audit, idempotency, corrections, retention and operations. Global Ban depends on appeals/trust/review governance; scam analysis on isolated egress; recovery on simulation/owner approval; ban evasion on legal review; public surfaces on aggregation privacy.

## Additional module dependencies

```mermaid
flowchart TD
 C[Consent, tenant auth, event/evidence/audit contracts] --> BI[Bot security intelligence]
 BI --> BS[Bot compromise early warning]
 BI --> SI[Integration supply-chain intelligence]
 C --> O[OAuth and third-party app security]
 O --> BP[Bot permission drift]
 BP --> PE[Privilege path analyzer]
 C --> CB[Destructive action circuit breaker]
 C --> INV[Invite link monitor]
 INV --> RE[Raid source and entry analysis]
 RE --> RD[Early raid detection]
 C --> SE[Social engineering detection]
 SE --> IMP[Staff/support impersonation]
 SE --> SP[Advanced spam evasion]
 C --> MM[Mass mention and role abuse]
 C --> MI[Moderation audit integrity]
 MI --> AD[Suspicious admin activity]
 C --> CD[Configuration drift]
 CD --> HM[Security health monitor]
 C --> ATT[Attachment intelligence]
 ATT --> MF[Malicious file campaign correlation]
 QR[QR threat detection] --> URL[Short-link/redirect security]
 URL --> SC[Scam intelligence]
 TF[External threat feeds] --> TI[Threat Intelligence Network]
 MF --> TI
 TI --> EX[Expiration and revocation]
 EX --> AN[Security Advisory Network]
 C --> API[SADA API abuse protection]
 API --> TEN[Tenant isolation security]
 TEN --> OP[Operator activity monitoring]
 BUILD[Secure build/release verification] --> DEP[Dependency vulnerability intelligence]
 DEP --> PATCH[Security patch advisory]
 VAULT[Evidence Vault] --> AI[AI prompt-injection protection]
 AI --> REVIEW[Shared human review]
```

Specific boundaries: bot intelligence is a domain projection on the shared threat graph; bot compromise analyzes bot behavior while Suspicious Admin Activity focuses human administrative events. Invite monitoring owns invite lifecycle facts; Early Raid Detection owns local rates; Raid Source Analysis owns attribution state. Social Engineering classifies interaction tactics; Scam Intelligence owns URL/domain reputation. Configuration Drift owns change deltas and baselines; Health Monitor owns point-in-time assessment. Attachment Intelligence owns file observations/scanner facts; File Campaign Correlation groups them. External feeds ingest provenance; shared Threat Intelligence owns cross-domain relationships. Expiration/revocation controls indicator lifecycle; Evidence Vault controls artifact retention. API Abuse uses shared authentication; Tenant Isolation tests/enforces authorization across modules. Operator Monitoring projects the shared audit ledger. AI adds optional guarded recommendations to existing case review and never owns decisions.
