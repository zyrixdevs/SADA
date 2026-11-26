# SADA implementation handoff

Use this as a compact brief for another coding assistant. Read the linked repository documents before changing code; this handoff does not override the user's latest instructions.

## Repository state

SADA currently has documentation for 49 planned security modules, shared architecture and standards, governance guidance, and repository-level CI. There is no Rust application, Python adapter, production database schema/API, detection implementation, or deployment. The CI badges indicate repository checks only.

Start with [`../../PATH.md`](../../PATH.md), [`../README.md`](../README.md), the relevant feature README and numbered specifications, and [`../../AGENTS.md`](../../AGENTS.md).

## Architecture and safety

- Rust is the planned independent SADA Core; PostgreSQL is the proposed authoritative structured store.
- A separate Python Zyrix adapter owns Discord credentials, gateway integration, and every Discord action.
- SADA Core must never receive/store a Discord bot token or call Discord moderation/configuration APIs.
- The adapter independently checks guild consent/scope, case revision, target membership, actor and bot permissions, role hierarchy, and local policy before acting.
- SADA must remain optional; outages cannot block local moderation or AntiNuke.
- No global punishment based solely on a score or unverified report. High-impact decisions require explainable evidence, authorized human review, and any required independent approval.
- Submission, intelligence reception, alerts, and enforcement are distinct opt-ins, off by default.
- Minimize data; preserve provenance, uncertainty, tenant isolation, audit, retention, appeal, correction, expiration, revocation, and reversal.

## How to proceed

1. Inspect repository state, current branch, working tree, existing code, tests, docs, and CI. Preserve unrelated changes.
2. Pick the earliest unblocked milestone in [`../../PATH.md`](../../PATH.md). Establish shared identity, consent, tenant, event, audit, and durable idempotency primitives before integrating detection features.
3. Implement one small vertical slice with real behavior and meaningful tests. Do not create empty feature shells or claim interfaces are operational.
4. Reuse shared case, evidence, event, audit, auth, and storage contracts. Update affected docs, navigation, and the module-status registry.
5. Mark features Implemented only when behavior exists; mark Tested only after relevant tests pass. Report exact checks and limits.
6. Never enable production collection, deploy, publish, or take Git delivery actions unless the latest user request explicitly authorizes them.

## Current priority

Resolve policy/security/operational decisions and define stable event/API contracts. Then create the minimal Rust foundation and shared tenant-scoped auth, consent, audit, inbox/outbox, idempotency, and correction/revocation infrastructure. Add the Python adapter only after contracts and failure-isolation tests are ready. Keep early detection advisory and synthetic until privacy, review, appeals, retention, and operating controls are implemented.

## Final report

Report actual code changes, capabilities with working behavior, tests and results, migrations/API changes, integration readiness, security limitations, unresolved decisions, and branch/commit only when known. Do not claim CI, deployment, accuracy, or operational status without evidence.
