# 07 — Implementation roadmap: Threat Intelligence Expiration and Revocation

**Proposed phase:** Phase 2 foundational lifecycle before broad distribution.

## Prerequisites

- Approve module owner, privacy purpose, guild opt-in surface, data classification, retention and correction policy.
- Finalize shared event schema, module payload, authorization scopes, audit actions, error mapping and idempotency behavior.
- Confirm needed Discord/source fields and failure semantics against the API version selected for implementation.
- Complete threat-model review and test fixtures using synthetic data.

## Work sequence

1. Define typed domain vocabulary, state machine, policy version and OpenAPI/event examples.
2. Implement reviewed database design with indexes, FKs, constraints, retention and migration plan.
3. Add pure Rust normalization/analysis functions and deterministic tests; feature flag off by default.
4. Add shared inbox/outbox, audit, tenant scope and operational metrics; no new identity/case/audit service.
5. Add Python adapter capture only for explicitly permitted event fields; durable retry; no SADA token access to Discord.
6. Run integration, adversarial, false-positive, load and outage tests; review source owner’s acceptance evidence.
7. Roll out to synthetic environment, then a limited opted-in cohort with read-only outputs; observe corrections and disable switch before expanding.

## Completion gate and risks

Complete only when all acceptance criteria in [06](06-testing-and-acceptance-criteria.md) pass, data deletion/revocation is demonstrated, an operations owner/runbook exists, unresolved policy decisions are recorded, and SADA outage isolation is verified. Risks: incomplete upstream events, overcollection, poisoning, false-positive harm, stale indicators, tenant leakage, and maintenance burden. No release or detection performance is claimed by this specification.
