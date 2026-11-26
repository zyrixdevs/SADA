# SADA Development Path

## Mission and current state

SADA is planned as an independent security-intelligence platform for Discord communities that explicitly opt in. It should support explainable investigation and coordinated defense while leaving Discord credentials and local enforcement with the connected bot.

This repository currently contains architecture and repository-governance documentation for 49 proposed feature modules. It does **not** contain the SADA Rust Core, Python adapter, production database migrations, APIs, detection engines, or deployed functionality. CI currently validates repository content; it is not application test evidence. This path is a staged proposal, not a claim that planned work exists.

## Security boundaries

1. Rust is the planned language for independent SADA Core. Python is reserved for a separate Zyrix adapter responsible for Discord-specific integration.
2. SADA Core must never receive or store Discord bot tokens and must never execute Discord moderation or configuration actions.
3. The Zyrix adapter must independently validate guild scope, explicit consent, current case state, membership, actor and bot permissions, role hierarchy, and local policy before any local action.
4. SADA is optional. An outage must not block or disable ordinary Zyrix moderation or AntiNuke.
5. A score, report, correlation, or remote recommendation is not proof and cannot alone authorize global punishment.
6. High-impact decisions require explainable evidence, human review and, where policy requires, independent approval. Audit, appeal, correction, reversal, and revocation must be supported.
7. Submission, intelligence reception, alerts, and enforcement are separate explicit opt-ins and default to off.
8. Minimize data, preserve provenance and uncertainty, isolate tenants, define retention/deletion, and do not expose public searchable lists of accused people.

## Staged implementation path

### Stage 0 — Decisions and contracts

Resolve policy and operational questions before production data collection: data ownership, operator responsibilities, consent, permitted fields, retention/deletion, user notice, reviewer authority and quorum, appeal timelines, data residency, incident response, and deployment topology. Define versioned events and APIs, installation-scoped authentication, tenant authorization, idempotency, safe errors, audit records, and correction/revocation behavior. Keep unresolved choices visible in the [decision register](docs/implementation-roadmap/06-open-questions-and-decisions.md).

**Exit gate:** security boundaries and privacy policy have review; contracts specify compatibility and examples; abuse cases and threat model have review owners.

### Stage 1 — Independent Rust service foundation

Create the smallest workspace that can start safely and be tested independently: domain/application boundaries, validated configuration, structured redacted logs, versioned HTTP routes, liveness/readiness, PostgreSQL pooling and migrations, generic safe API errors, bounded requests, graceful shutdown, and CI. Add only foundational metadata; do not create speculative tables for all 49 modules.

**Exit gate:** stable Rust checks pass; API errors do not leak internals; readiness reflects dependencies; no Discord credential or moderation capability exists in Core; migration and service tests are reproducible.

### Stage 2 — Shared security primitives

Build installation identity, explicit per-guild consent, guild-scoped authorization and tenant isolation, versioned event envelopes, durable inbox/outbox, idempotent acceptance, audit records, retention hooks, evidence references, shared case identifiers/revisions, and correction/revocation propagation. Add rate limits and bounded retry/dead-letter handling when needed. Keep PostgreSQL authoritative; add brokers or caches only for measured requirements.

**Exit gate:** cross-tenant access, replay, duplicate, transaction/crash-recovery, audit, consent, retention and deletion tests pass. Do not acknowledge an event as durable before its transaction commits.

### Stage 3 — Zyrix adapter in shadow mode

Add a narrowly scoped Python adapter only after the wire contract is stable. It submits only approved structured data for opted-in guilds, uses durable bounded retry, and never puts a SADA request in a local moderation or AntiNuke critical path. Initially receive non-enforcing synthetic/test signals only.

**Exit gate:** synthetic integration tests prove local moderation and AntiNuke continue during SADA failure; authentication, consent, acknowledgements, idempotency and revocation work end to end. Live collection remains off by default.

### Stage 4 — Foundational security capabilities

Implement the first low-risk, explainable capabilities over shared infrastructure: Security Health Monitor, event processing, Early Raid Detection, Suspicious Admin Activity, Mass Mention and Role Abuse Protection, Invite Link Security Monitor, Bot Permission Drift Detection, Configuration Drift Detection, and Destructive Action Circuit Breaker. Keep results advisory and reviewable. Define exact inputs, server-specific baselines, uncertainty, false-positive controls, and disable/rollback behavior.

**Exit gate:** unit, integration, adversarial, false-positive, load, and tenant-isolation tests meet documented criteria; each finding explains its evidence and limitations.

### Stage 5 — Intelligence and incident lifecycle

Implement Threat Intelligence Network, Threat DNA, Scam and Phishing Intelligence, Ban Evasion Intelligence, Incident Timeline, Evidence Vault, Trust and Reliability Engine, Attack Campaign Tracker, Security Advisory Network, and Threat Intelligence Expiration and Revocation. Reuse canonical case, event, evidence, and audit records; preserve revisions and prevent stale, disputed, or reversed indicators from appearing current.

**Exit gate:** provenance is inspectable; corrections propagate through derived cases, pending alerts, and delivery queues; access and retention are enforced; unverified reports do not become confirmed facts.

### Stage 6 — Advanced capabilities

Build remaining modules only after their dependencies, threat models, privacy and operational controls are ready. Use isolated egress for URL/file scanning, strong authorization and monitoring for operator/API features, and strict tool boundaries and non-AI fallbacks for any AI-assisted workflow. Simulation must never execute live Discord actions. Recovery plans require owner authorization and rollback.

**Exit gate:** each module passes its own acceptance criteria and shared isolation/security tests; module status is independently tracked.

### Stage 7 — Reviewed high-impact workflows and controlled operation

Implement global review/quorum and any local enforcement signal only after governance, legal/privacy, appeal, staffing, incident-response, and operational readiness review. A global decision remains distinct from each guild action. The adapter repeats all local checks at execution time, reports outcomes per guild, and never treats a failed or unknown action as success. Maintain emergency stop and reversal paths.

**Exit gate:** independent approval, replay resistance, opt-in, fresh local authorization, partial failure, cancellation, appeal, reversal, audit, backup, and recovery scenarios pass. Enabling production enforcement requires a separate explicit operational decision.

## Feature tracking

The canonical catalogue is the [49-module documentation index](docs/README.md), with implementation dependencies in [the roadmap](docs/implementation-roadmap/README.md). Track each module as **Planned**, **Designed**, **In development**, **Implemented**, **Tested**, and **Integrated**. A status advances only when matching code, review, and test evidence exists. At the current repository state, all feature modules are documented proposals; none is operational.

## Engineering and release gates

- Keep Rust Core tests independent of Discord and the Python bot. Adapter contract tests use synthetic data and mocks.
- Database tests use disposable PostgreSQL and cover migrations, transactions, tenant isolation, and recovery.
- CI should enforce formatting, lint, workspace tests/build, dependency security checks when source dependencies exist, documentation/link validation, and workflow security.
- Approved releases should use trusted tags, release notes, artifact checksums, SBOM, provenance/attestation, signing, and rollback guidance. Never expose signing or publishing credentials to pull-request workflows.
- Roll out through local development, isolated testing, and staging with synthetic identities. Passing CI does not imply production readiness.

## Related guidance

- [System architecture](docs/system-architecture/README.md)
- [Security and governance](docs/security-and-governance/README.md)
- [Feature dependencies](docs/implementation-roadmap/02-feature-dependencies.md)
- [Open decisions](docs/implementation-roadmap/06-open-questions-and-decisions.md)
- [AI contributor guide](AGENTS.md)
- [AI implementation handoff](docs/ai/IMPLEMENTATION-HANDOFF.md)
