# Security and Abuse Prevention

SADA is a cross-server moderation intelligence system and therefore treats every participating server, moderator, event, and service boundary as potentially fallible.

## Trust boundaries

1. Discord event to Zyrix Bot: Discord authentication and gateway event context.
2. Zyrix Bot to SADA: authenticated service request with narrowly scoped identity.
3. SADA ingestion to evidence store: schema, size, replay, and rate validation.
4. Global reviewer interface to case decisions: fresh authorization, reason, and audit record.
5. SADA signal to Zyrix Bot: authenticated, signed or otherwise integrity-protected decision message.
6. Zyrix Bot to Discord moderation API: local permission and hierarchy checks at execution time.

SADA never has a Discord bot token. Its API credentials cannot be used to execute guild moderation.

## Server and reporter abuse

- Treat moderator-provided reason text as a claim. Preserve the original and attribute it to its source; normalized category is separate metadata.
- Accept only defined action types, bounded text, timestamps, IDs, and evidence references. Sanitize rendered text to prevent mentions, markdown abuse, and injection.
- Require authenticated server identity and idempotency key. Do not trust source guild ID supplied without binding it to the service credential.
- Deduplicate by source guild plus stable moderation case/event ID. If none exists, use a documented fingerprint and mark confidence lower rather than merging distinct incidents blindly.
- Detect unusual volume, repeated identical reports, impossible timestamps, inconsistent actor/audit data, and correction/reversal patterns. Quarantine anomalies for review rather than silently scoring them.
- Use independent-server diversity; repeated actions from one guild do not count as multiple servers.
- Measure evidence completeness and validated outcomes proportionally. A high appeal count alone is not misconduct; small sample sizes should be marked insufficient data.
- Rate limit per server and credential, and provide suspension/revocation procedures for a compromised or abusive participant.

The server reliability methodology is an **OPEN DECISION**. Do not implement a punitive score until its inputs, minimum sample size, appeal treatment, transparency, and review process are approved.

## Evidence and privacy

Store only the minimum information needed for moderation review. Separate original reason, normalized category, evidence description/reference, evidence quality, reviewer finding, and final status. Access to raw evidence must be narrower than access to a summary. Do not share private messages across servers by default. Redact unrelated users and secrets before any approved evidence sharing.

Retention, deletion, user access requests, and lawful basis are **OPEN DECISIONS** requiring policy and legal review. A correction must preserve a protected audit trail while ensuring active views no longer represent reversed information as valid. Do not promise deletion or retention behavior until policy is settled.

## Authentication, authorization, and replay protection

- Use mutual service authentication or rotated, scoped credentials; store secrets in deployment secret management, never source or logs.
- Bind each bot installation credential to its registered installation and allowed guild scope.
- Use TLS, strict request schemas, payload limits, timestamp windows, and idempotency keys.
- Verify signed messages where signals can traverse queues or untrusted intermediaries.
- Enforce authorization server-side on every global review and guild-specific setting request.
- Store component actions as opaque identifiers; reload authoritative state on interaction.
- Use unique constraints and transactionally claimed state transitions to prevent replay and double approval.
- Require step-up authentication and/or second reviewer for high-impact global approvals if policy selects quorum.

## Preventing unsafe global action

A suspicious score is never an execution instruction. Global approval is a durable case decision by authorized global reviewers; enforcement is a separate operation per opted-in guild. Each bot independently validates its local policy, membership, actor context where applicable, bot permissions, role hierarchy, and the authenticated approval signal. A revoked or reversed approval must stop future enforcement retries and trigger correction notifications.

## Operational security

Use least-privilege database roles, encrypted backups, key rotation, access logs, and separate development/staging/production credentials. Avoid logging tokens, webhook URLs, private messages, full evidence bodies, or unnecessary personal data. Monitor service health and queue age without exposing case payloads. Incident response must support credential revocation, event quarantine, signal suspension, and safe recovery.

## Threat model gaps

Open decisions include policy jurisdiction, retention and privacy, server reliability scoring, reviewer quorum, and deployment topology. Discord policy compliance and applicable privacy/legal review must be completed before production collection or cross-server sharing.
