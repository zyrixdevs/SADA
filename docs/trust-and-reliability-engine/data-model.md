# Trust And Reliability Engine — data model appendix

**Status: proposed PostgreSQL design; no migration exists.** This appendix owns only module projections. Canonical installation, consent, event, incident, evidence, case, audit and outbox tables are defined in [platform storage](../system-architecture/05-database-and-storage-architecture.md).

## Primary table

Proposed table: source_quality_observations.

Columns and types: observation_id UUID PK, source_guild_id BIGINT, window_start/end TIMESTAMPTZ, denominator INTEGER, completeness NUMERIC, audit_match NUMERIC, correction_rate NUMERIC, methodology_version TEXT, sample_state TEXT.

Keys, constraints, and indexes: UNIQUE(source_guild_id,window_start,window_end,methodology_version); index guild/window; appeals count is not a negative factor. Use UUID primary keys; foreign keys point to canonical IDs. Store UTC timestamps and version every derived result. State values use a database CHECK constraint from a versioned enum vocabulary. Tenant-bearing queries include guild scope. Do not cascade-delete investigation or audit history.

## Transaction and retention

Write the module row, provenance references, audit event, and any delivery outbox entry in one transaction. Network delivery occurs after commit. Corrections create linked revisions and invalidate current projections without erasing their history. Retention is by data class and remains an open policy decision; apply expiry consistently to rows, object references, indexes, exports, and backups.

## Migration gate

Before implementation, confirm the field set against the approved event contract and threat model; create forward/rollback migration; test unique constraints under duplicate/concurrent writes; and verify tenant-scoped indexes from representative query plans. No database is created by this document.
