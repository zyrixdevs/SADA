# 06 — Testing and acceptance criteria: Bot Compromise Early Warning

No tests or detection validations are claimed. Implementation must include:

- **Unit/property:** normalization boundaries, version handling, factor explanation, expiry and state transition invariants.
- **Database integration:** constraints, idempotent writes, revision compare-and-set, rollback, retention and previous-schema migration.
- **Contract/integration:** shared v1 event/request/response fixtures, inbox/outbox retry, correction/revocation, cursor and error compatibility.
- **Security/adversarial:** forged guild scope, replay, oversized/malformed payload, poisoned source, injection, timing races, secret redaction and cross-tenant read attempts.
- **False-positive:** benign/authorized activity, missing or stale data, low sample size, ambiguous attribution and conflicting evidence.
- **Reliability/load:** duplicate bursts, slow PostgreSQL, worker lease expiry, dead-letter recovery, rate limits and per-tenant fairness.
- **Adapter safety:** fake Discord only; prove no call from SADA Core and ordinary local moderation remains available during SADA outage.

## Acceptance criteria

1. Unauthorized, revoked-consent and cross-tenant events are rejected without leaking object existence.
2. Duplicate same-body requests return the original receipt; changed body with same key conflicts.
3. Every generated assessment records evidence references, exclusions, version, uncertainty and expiry.
4. Correction/reversal cancels stale pending delivery and remains historically traceable.
5. Missing/stale source data is unknown or partial and cannot authorize an action.
6. Database state, audit and outbox commit atomically; failed audit insertion leaves no partial state transition.
7. Tests use synthetic fixtures; no live moderation action, real member data or accuracy percentage is claimed.

Feature-specific adversarial tests: Test planned release burst, missing baseline, duplicate events, advisory revocation, and recommendation-only behavior.
