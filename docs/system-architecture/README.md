# Shared Platform Architecture

**Proposed only; no service is deployed.** Feature docs may refine domain rules but cannot redefine event, evidence, case, identity, error or audit contracts.

```mermaid
flowchart LR
 D[Discord] <-->|Discord boundary| Z[Zyrix Python adapter]
 Z -->|authorized events| A[SADA versioned API]
 A --> I[(PostgreSQL inbox)]
 I --> R[Rust modular core]
 R --> P[(PostgreSQL domain store)]
 R --> O[(PostgreSQL outbox)]
 O --> Z
 P --> E[Encrypted evidence storage]
 R --> H[Reviewer surface]
```

Zyrix owns Discord, consent UI, live checks and every action. API authenticates and durably accepts; Rust processes; PostgreSQL stores structured state; reviewers decide. Start as independent modular API/worker plus PostgreSQL; defer broker/cache. See [governance](../security-and-governance/README.md), [standards](../shared-standards/README.md), [roadmap](../implementation-roadmap/README.md).
