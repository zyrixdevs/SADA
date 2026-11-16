# Tenant Isolation Security

**Catalogue module 42 of 49. Status: proposed specification only; not implemented or deployed.**

## Purpose

Specify and continuously verify strict guild and installation data boundaries across APIs, workers, evidence, search and exports.

## What it does

Resolve tenant context from authenticated grants; bind it to transaction/query; enforce row/object ACL; audit denied cross-tenant attempts; run isolation test suite on every contract/schema change.

## What it must never do

- It must not execute Discord moderation or configuration changes. Zyrix Bot remains the only Discord action boundary and rechecks local consent, permissions and role hierarchy.
- It must not treat a score, anomaly or single report as proof or punishment authority.
- It must not bypass guild opt-in, shared case/review, evidence, identity or audit contracts.

## Signals and workflow

**Inputs:** Authenticated installation scope; authorized guild grants; query predicates; row ownership; evidence object ACL; reviewer role scope.

```mermaid
flowchart LR
 A[Authorized source event or advisory] --> B[Validate scope, version and consent]
 B --> C[Normalize and preserve provenance]
 C --> D[Module-owned analysis: Tenant Isolation Security]
 D --> E[Versioned explainable finding]
 E --> F[Shared incident, case and review services]
 F --> G[Scoped advisory or Zyrix local decision]
 C --> H[Canonical audit and correction path]
```

Use repository APIs with mandatory tenant scope and PostgreSQL row-level policies as defense-in-depth where appropriate; cross-tenant aggregates are separate approved products with minimum cohort rules.

## Ownership and integration

This module owns only domain-specific observations, snapshots, assessments and indicator references. It reuses canonical installation/consent, event inbox, incident/evidence, case/review, delivery/outbox and audit records. It does not create separate authentication, case management, evidence vault, reviewer quorum or audit systems.

Dependencies: [Threat Intelligence API](../threat-intelligence-api/README.md), [Evidence Vault](../evidence-vault/README.md), [SADA API Abuse Protection](../sada-api-abuse-protection/README.md), Security Observatory..

## Security, privacy and limitations

No caller-supplied tenant authority; conceal existence; test negative access at every layer; segregate object-store paths/keys. Global reviewer access is purpose-bound and not equivalent to unrestricted tenant access; operators use break-glass audited access.

Cross-guild sharing requires explicit purpose and permission. Missing, stale or inaccessible data is represented as unknown/partial. Corrections and revocations are versioned and propagate to pending deliveries.

## API and event contract

**Method:** `POST`. Proposed internal endpoint: `POST /v1/security/tenant-access-checks`. It uses the shared `/v1` authentication and authorization model, guild scope from authenticated grants, request ID, schema version, idempotency key, bounded JSON payload, and shared error shape. The endpoint accepts observations or recommendations only; it does not execute Discord actions. A durable inbox receipt is returned only after commit. Duplicate key + same canonical body returns the original receipt; changed body returns `409`. Retry only transient `retryable=true` errors.

Example request:
```json
{
  "schema_version": "1.0",
  "event_id": "018f0000-0000-7000-8000-000000000001",
  "source_guild_id": "123456789012345678",
  "occurred_at": "2026-11-16T10:00:00Z",
  "consent_version": "guild-consent-7",
  "correlation_id": "018f0000-0000-7000-8000-000000000003",
  "payload": { "observation_ref": "opaque-reference", "type": "module-specific" }
}
```

Example accepted response:
```json
{"event_id":"018f0000-0000-7000-8000-000000000001","receipt_id":"018f0000-0000-7000-8000-000000000004","status":"accepted","duplicate":false}
```

## Data model

See [module data model](data-model.md). Tables below are proposals only; canonical IDs and shared ownership follow [platform storage architecture](../system-architecture/05-database-and-storage-architecture.md). Retention and access remain subject to the platform policy register.

## Design status and implementation phase

**Current status:** architecture proposal. **Proposed phase:** Phase 0/1; mandatory architecture gate before any stored tenant data. No runtime behavior or algorithm has been validated. Resolve before implementation: RLS approach, operator break-glass quorum and aggregate cohort floor need architecture/security approval.

## Documents

- [01 Overview and objectives](01-overview-and-objectives.md)
- [02 System architecture](02-system-architecture.md)
- [03 Feature workflow](03-feature-workflow.md)
- [04 Detection and contract details](04-detection-and-contract-details.md)
- [data-model.md](data-model.md)
- [05 Security and abuse prevention](05-security-and-abuse-prevention.md)
- [06 Testing and acceptance criteria](06-testing-and-acceptance-criteria.md)
- [07 Implementation roadmap](07-implementation-roadmap.md)
