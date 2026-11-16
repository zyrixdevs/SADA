# Threat Intelligence Network — data model appendix

**Status: proposed PostgreSQL design; no migration exists.** This appendix owns only module projections. Canonical installation, consent, event, incident, evidence, case, audit and outbox tables are defined in [platform storage](../system-architecture/05-database-and-storage-architecture.md).

## Primary table

Proposed table: relationship_edges.

Columns and types: edge_id UUID PK, source_incident_id UUID FK, target_incident_id UUID FK, relation_type TEXT, algorithm_version TEXT, evidence_refs UUID[], factor_snapshot JSONB, review_state TEXT, created_at TIMESTAMPTZ, expires_at TIMESTAMPTZ.

Keys, constraints, and indexes: UNIQUE(source_incident_id,target_incident_id,relation_type,algorithm_version); indexes source/target incident and review_state/created_at; reversed evidence marks edge inactive, not deleted. Use UUID primary keys; foreign keys point to canonical IDs. Store UTC timestamps and version every derived result. State values use a database CHECK constraint from a versioned enum vocabulary. Tenant-bearing queries include guild scope. Do not cascade-delete investigation or audit history.

## Transaction and retention

Write the module row, provenance references, audit event, and any delivery outbox entry in one transaction. Network delivery occurs after commit. Corrections create linked revisions and invalidate current projections without erasing their history. Retention is by data class and remains an open policy decision; apply expiry consistently to rows, object references, indexes, exports, and backups.

## Migration gate

Before implementation, confirm the field set against the approved event contract and threat model; create forward/rollback migration; test unique constraints under duplicate/concurrent writes; and verify tenant-scoped indexes from representative query plans. No database is created by this document.
