# Audit Logs and Case Management

## Source of truth

The SADA structured database is authoritative. A proposed private Zyrix operations server may use `#sada-global-registry`, `#sada-global-alerts`, and `#sada-case-files` as readable views; these names are proposals, not existing channels. Discord messages are not the source of truth and must be rebuildable from durable records.

## Case record

Each case has an immutable SADA case ID, subject user ID, lifecycle status, current revision, created/updated timestamps, and links to incidents. Case summaries are derived from incident records and reviewer decisions; do not overwrite original reports when normalizing or correcting them.

## Append-only audit events

Record at least:

- Incident received, deduplicated, verified/reviewed, disputed, reversed, or corrected.
- Case created, recomputed, escalated, closed, or reopened.
- Alert eligibility, delivery result, ignore, local ban request, local Discord result.
- Global review approval/rejection, reviewer identity, timestamp, decision reason, and policy version.
- Per-guild enforcement attempted, succeeded, failed, skipped, or unavailable, with a safe error category.
- Appeal submitted, assigned, resolved, and resulting correction/reversal.
- Participation setting changes, server suspension, and credential revocation.

Audit rows should identify actor type and actor ID, affected entity, request/idempotency ID, event time and recorded time, and a minimal structured change summary. Avoid copying raw private content into audit logs.

## Registry projections

The central registry can show case timelines and aggregate status. Access should be role-gated and channel permissions restrictive. Project only necessary fields; redact evidence and reporter identities unless authorized. Failed Discord message delivery must not roll back a database decision. A reconciliation task can repost or update a registry projection from source records.

## Case management controls

Global reviewers need search by case ID/user ID, evidence timeline, status filters, and approve/reject/needs-more-evidence actions. These are proposed controls; implementation UI is not part of this blueprint. Every transition records the actor and policy version. A reviewer cannot silently edit the source incident; corrections create a new linked record.

## Consistency and integrity

Use a database transaction for case state and audit entry. Use an outbox for messages or service signals emitted after commit. Enforce unique event/idempotency identifiers and optimistic revision checks. An export or backup must retain referential relationships and audit ordering. Protect audit storage from ordinary application update/delete privileges; correction is represented by new events.

## Retention

Retention periods, archival, deletion requests, and backup expiry remain **OPEN DECISIONS**. The design must support policy-driven retention without turning Discord channel history into the only copy. Maintain a documented procedure for correcting public or staff-visible projections when an incident or global decision is reversed.
