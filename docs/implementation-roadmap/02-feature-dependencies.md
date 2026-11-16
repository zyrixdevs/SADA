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
