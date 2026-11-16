# 01 — Platform overview

**Existing:** documentation only. **Proposed:** independent security-intelligence platform for opted-in guilds. Bounded contexts: identity/consent, ingestion, incidents/evidence, analysis, cases/review/appeals, distribution, operations, and Discord execution in Zyrix only.

```mermaid
sequenceDiagram
 participant G as Guild admin
 participant Z as Zyrix adapter
 participant S as SADA
 participant H as Reviewer
 participant D as Discord
 G->>Z: Enable one capability
 Z->>S: Submit scoped event
 S-->>Z: Durable receipt
 S->>S: Correlate into candidate
 S->>H: Explainable review
 H->>S: Authorized decision
 S-->>Z: Scoped signal
 Z->>Z: Recheck local rules
 Z->>D: Local action if allowed
```

PostgreSQL is source of truth; Discord messages/UI are projections; optional encrypted object store holds approved evidence. Missing data is unknown. SADA outage affects intelligence only.
