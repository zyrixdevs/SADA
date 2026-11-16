# Social Engineering Attack Detection

**Catalogue module 30 of 49. Status: proposed specification only; not implemented or deployed.**

## Purpose

Correlate reports of deceptive requests for credentials, codes, money, or fake moderation/support actions.

## What it does

Accept report with consent and provenance; classify tactic with versioned taxonomy; link URL indicators to Scam Intelligence; correlate reviewed campaign; issue correction-aware advisory.

## What it must never do

- It must not execute Discord moderation or configuration changes. Zyrix Bot remains the only Discord action boundary and rechecks local consent, permissions and role hierarchy.
- It must not treat a score, anomaly or single report as proof or punishment authority.
- It must not bypass guild opt-in, shared case/review, evidence, identity or audit contracts.

## Signals and workflow

**Inputs:** Authorized structured report category; redacted evidence ref; claimed authority; request type; URL/domain indicator reference; source and time provenance.

```mermaid
flowchart LR
 A[Authorized source event or advisory] --> B[Validate scope, version and consent]
 B --> C[Normalize and preserve provenance]
 C --> D[Module-owned analysis: Social Engineering Attack Detection]
 D --> E[Versioned explainable finding]
 E --> F[Shared incident, case and review services]
 F --> G[Scoped advisory or Zyrix local decision]
 C --> H[Canonical audit and correction path]
```

Rule-based tactic labels identify credential/code/payment requests and urgency/secrecy language only on authorized submitted content. Model outputs remain suggestions with excerpts minimized and reviewer disposition.

## Ownership and integration

This module owns only domain-specific observations, snapshots, assessments and indicator references. It reuses canonical installation/consent, event inbox, incident/evidence, case/review, delivery/outbox and audit records. It does not create separate authentication, case management, evidence vault, reviewer quorum or audit systems.

Dependencies: [Scam and Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Staff and Support Impersonation Detection](../staff-and-support-impersonation-detection/README.md), [Security Advisory Network](../security-advisory-network/README.md), Threat Intelligence Network..

## Security, privacy and limitations

Minimize submitted text; default to structured facts; redact secrets and verification codes immediately; user-facing messages never echoed in alerts. A phrase alone is not malicious; no passive private-channel scanning or auto-punishment.

Cross-guild sharing requires explicit purpose and permission. Missing, stale or inaccessible data is represented as unknown/partial. Corrections and revocations are versioned and propagate to pending deliveries.

## API and event contract

**Method:** `POST`. Proposed internal endpoint: `POST /v1/social-engineering/reports`. It uses the shared `/v1` authentication and authorization model, guild scope from authenticated grants, request ID, schema version, idempotency key, bounded JSON payload, and shared error shape. The endpoint accepts observations or recommendations only; it does not execute Discord actions. A durable inbox receipt is returned only after commit. Duplicate key + same canonical body returns the original receipt; changed body returns `409`. Retry only transient `retryable=true` errors.

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

**Current status:** architecture proposal. **Proposed phase:** Phase 5 after evidence policy and human review workflow. No runtime behavior or algorithm has been validated. Resolve before implementation: Allowed content capture and notification policy need privacy review.

## Documents

- [01 Overview and objectives](01-overview-and-objectives.md)
- [02 System architecture](02-system-architecture.md)
- [03 Feature workflow](03-feature-workflow.md)
- [04 Detection and contract details](04-detection-and-contract-details.md)
- [data-model.md](data-model.md)
- [05 Security and abuse prevention](05-security-and-abuse-prevention.md)
- [06 Testing and acceptance criteria](06-testing-and-acceptance-criteria.md)
- [07 Implementation roadmap](07-implementation-roadmap.md)
