# 05 — Security and abuse prevention: Mass Mention and Role Abuse Protection

## Threat model

Assets include guild-scoped observations, source identities, evidence references, derived findings, service credentials and reviewer trust. Adversaries include compromised installations, report brigades, malicious feed/content submitters, curious tenants, compromised operators and retry/replay attackers.

| Threat | Control |
|---|---|
| Forged or replayed observation | Signed/scoped service identity, timestamp/nonce, schema validation, inbox idempotency |
| Cross-guild enumeration or evidence leakage | Authenticated tenant context, object-level checks, concealed 404, audited reads, tenant isolation tests |
| Poisoned or malformed input | Bounded parsing, allowlisted types, safe rendering, dead-letter and source quarantine |
| False correlation or feedback loop | Preserve provenance, independent-source rules, factor explanation, correction/revocation path, human review |
| Secret or private content exposure | Data minimization, redaction, encryption, secret manager, no raw tokens in event/log/output |
| Stale output used downstream | Expiry, revision binding, outbox cancellation and consumer freshness check |

Collect aggregate counts instead of message bodies; restrict role/member identifiers; retain only incident-linked windows.

## Authorization and response

Guild configuration requires a guild administrator and creates a shared audit event. Submission, reception, alerts and enforcement remain separate capabilities, off by default. A feature output cannot authorize local Discord action. Zyrix rechecks current consent, actor permission, bot permission, membership, hierarchy and guild exceptions. On SADA outage, local moderation and AntiNuke remain operational.

Incident response suspends the affected source/principal, stops relevant deliveries, preserves safe audit metadata, assesses data exposure, rotates credentials through platform owners, and issues correction/revocation where needed. Do not delete audit history to remediate a compromise.
