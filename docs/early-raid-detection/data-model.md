# Early Raid Detection — data model appendix

**Status: proposed PostgreSQL design; no migration exists.** This appendix owns only module projections. Canonical installation, consent, event, incident, evidence, case, audit and outbox tables are defined in [platform storage](../system-architecture/05-database-and-storage-architecture.md).

## Primary table

Proposed table: guild_baselines.

Columns and types: baseline_id UUID PK, guild_id BIGINT, signal_type TEXT, window_seconds INTEGER, sample_count INTEGER, median_value NUMERIC, percentile_bands JSONB, method_version TEXT, computed_at TIMESTAMPTZ, expires_at TIMESTAMPTZ.

Keys, constraints, and indexes: UNIQUE(guild_id,signal_type,window_seconds,method_version,computed_at); index guild/signal/time; low sample is insufficient data. Use UUID primary keys; foreign keys point to canonical IDs. Store UTC timestamps and version every derived result. State values use a database CHECK constraint from a versioned enum vocabulary. Tenant-bearing queries include guild scope. Do not cascade-delete investigation or audit history.

## Transaction and retention

Write the module row, provenance references, audit event, and any delivery outbox entry in one transaction. Network delivery occurs after commit. Corrections create linked revisions and invalidate current projections without erasing their history. Retention is by data class and remains an open policy decision; apply expiry consistently to rows, object references, indexes, exports, and backups.

## Migration gate

Before implementation, confirm the field set against the approved event contract and threat model; create forward/rollback migration; test unique constraints under duplicate/concurrent writes; and verify tenant-scoped indexes from representative query plans. No database is created by this document.
