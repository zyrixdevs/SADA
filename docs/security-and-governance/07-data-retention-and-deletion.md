# 07 — Data retention and deletion

Separate retention for intake, incident metadata, reason, evidence, fingerprints, cases, audit, delivery and backups. Expiry covers primary DB, object store, indexes, cache, exports and backup. Correction changes active use but is not deletion. Holds are scoped/time-limited/reviewed/audited. Durations, rights, jurisdiction and authority need legal/privacy review; do not invent periods.
## Expiry processing

An expiry worker claims due records transactionally, checks for active case references and approved holds, marks content unavailable, deletes external objects, and records a minimal audit result. Failed object deletion stays retryable and visible; metadata is not marked fully deleted until reconciliation. Backup expiration follows a published schedule and is included in deletion statements.
