# Testing and Acceptance Criteria

Tests use fake Discord objects, deterministic clocks, a temporary database, and service mocks. No test uses production credentials, live guilds, or actual moderation API calls.

## Incident collection

- A supported local moderation event creates one structured incident with source guild, target, action, original reason, actor, timestamp, and case reference when available.
- A warning count without actor/reason history is not fabricated into a verified incident.
- Missing case IDs use the documented idempotency fallback and are marked with appropriate confidence.
- Duplicate delivery returns the existing incident and does not increment source-guild diversity.
- Malformed/oversized input is rejected without storing partial data.

## Evidence and reason classification

- Preserve original reason byte-for-byte or in a documented normalized-text field; classification is stored separately.
- Unknown or ambiguous reasons remain Unknown; no unsupported category is inferred as fact.
- Verified, Reviewed, Unverified, Disputed, and Reversed statuses follow allowed transitions.
- Reversed incidents are excluded from active scoring while their audit history remains.
- An appeal count by itself does not lower server reliability.

## Detection and cross-server correlation

- Repeated incidents from one guild do not satisfy an independent-server threshold.
- Different categories produce different recommendations; personal disputes do not count as phishing evidence.
- Minor warnings do not equal severe bans.
- Thresholds are configuration-driven and test both sides of boundaries; unresolved five-server/5,000-member semantics block release of that policy.
- A suspicious flag never directly creates an enforcement job.
- Unsupported or anomalous source patterns are quarantined for review.

## Alerts and local decision

- Only opted-in guilds where the target is a current member receive an alert.
- Alert displays the required identity, case ID, reason/category separation, counts, source scope, evidence quality, and review state.
- Alert has exactly two primary controls: Ban User and Ignore.
- Ban User rejects unauthorized actor, missing membership, missing bot permission, role hierarchy violation, expired case revision, and replay.
- A successful local ban affects only that guild and does not modify global status.
- Ignore is guild-scoped, idempotent, audited, and a materially new revision can be re-alerted per policy.

## Global review and enforcement

- Guild admins cannot approve global cases unless separately authorized as global reviewers.
- Approval/rejection records reviewer, timestamp, reason, and case revision.
- If quorum is selected, one reviewer cannot satisfy a multi-reviewer quorum.
- Non-opted-in guilds receive no enforcement action.
- Success, failure, skipped, and unavailable outcomes are independently recorded per guild.
- Partial failures never render as a fully successful global ban.
- Reversal stops pending retries, updates current status, and notifies affected guilds; local unban is not automatic.

## Reliability, privacy, and operations

- SADA service/database outage does not block local moderation or AntiNuke.
- AntiNuke local action completes before or independently from SADA event submission.
- Outbox retries do not duplicate alerts or cases; exhausted retries are visible in dead-letter status.
- Sensitive tokens, webhook URLs, private message content, and full evidence do not appear in logs.
- Guild data queries are isolated by guild scope.
- Credential revocation prevents further event submission and signals.

## Acceptance criteria

1. A single-server local ban cannot by itself label a user globally banned.
2. Case summaries distinguish original claims, normalized classification, evidence quality, and reviewer decision.
3. Every SADA switch is off by default and independently auditable.
4. Only explicit global approval can create an enforcement signal, and only opted-in Zyrix installations can act on it.
5. Zyrix performs live permission, membership, and hierarchy checks for every local action.
6. Every decision and per-server outcome is queryable from the structured store and has an audit event.
7. Unknown, disputed, unavailable, or partial outcomes are displayed honestly.
8. Appeals and corrections alter current derived status without erasing the historical audit trail.

## Release gate

Do not enable production collection or enforcement until policy decisions in [Configuration and Admin Controls](12-configuration-and-admin-controls.md), privacy review, database recovery, service authentication, and staging failure tests are complete. This document does not claim those tests or implementation exist today.
