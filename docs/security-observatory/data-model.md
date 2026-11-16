# Security Observatory — data model appendix

**Status: proposed PostgreSQL design; no migration exists.** This appendix owns only module projections. Canonical installation, consent, event, incident, evidence, case, audit and outbox tables are defined in [platform storage](../system-architecture/05-database-and-storage-architecture.md).

## Primary table

Proposed table: metric_snapshots.

Columns and types: snapshot_id UUID PK, metric_name TEXT, scope_type TEXT, scope_ref TEXT, bucket_start/end TIMESTAMPTZ, cohort_size INTEGER, value NUMERIC NULL, suppression_state TEXT, method_version TEXT, created_at TIMESTAMPTZ.

Keys, constraints, and indexes: UNIQUE(metric_name,scope_type,scope_ref,bucket_start,method_version); index metric/bucket; suppressed rows expose no raw count. Use UUID primary keys; foreign keys point to canonical IDs. Store UTC timestamps and version every derived result. State values use a database CHECK constraint from a versioned enum vocabulary. Tenant-bearing queries include guild scope. Do not cascade-delete investigation or audit history.

## Transaction and retention

Write the module row, provenance references, audit event, and any delivery outbox entry in one transaction. Network delivery occurs after commit. Corrections create linked revisions and invalidate current projections without erasing their history. Retention is by data class and remains an open policy decision; apply expiry consistently to rows, object references, indexes, exports, and backups.

## Migration gate

Before implementation, confirm the field set against the approved event contract and threat model; create forward/rollback migration; test unique constraints under duplicate/concurrent writes; and verify tenant-scoped indexes from representative query plans. No database is created by this document.
