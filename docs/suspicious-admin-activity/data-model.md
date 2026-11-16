# Suspicious Admin Activity — data model appendix

**Status: proposed PostgreSQL design; no migration exists.** This appendix owns only module projections. Canonical installation, consent, event, incident, evidence, case, audit and outbox tables are defined in [platform storage](../system-architecture/05-database-and-storage-architecture.md).

## Primary table

Proposed table: admin_events.

Columns and types: admin_event_id UUID PK, guild_id BIGINT, source_event_id UUID FK, actor_id BIGINT NULL, target_type TEXT, target_id TEXT, action_type TEXT, audit_entry_id TEXT NULL, attribution_state TEXT, observed_at TIMESTAMPTZ, confidence_factors JSONB.

Keys, constraints, and indexes: UNIQUE(guild_id,audit_entry_id) WHERE audit_entry_id IS NOT NULL; index guild/action/observed_at and actor/observed_at; uncertain actor remains NULL. Use UUID primary keys; foreign keys point to canonical IDs. Store UTC timestamps and version every derived result. State values use a database CHECK constraint from a versioned enum vocabulary. Tenant-bearing queries include guild scope. Do not cascade-delete investigation or audit history.

## Transaction and retention

Write the module row, provenance references, audit event, and any delivery outbox entry in one transaction. Network delivery occurs after commit. Corrections create linked revisions and invalidate current projections without erasing their history. Retention is by data class and remains an open policy decision; apply expiry consistently to rows, object references, indexes, exports, and backups.

## Migration gate

Before implementation, confirm the field set against the approved event contract and threat model; create forward/rollback migration; test unique constraints under duplicate/concurrent writes; and verify tenant-scoped indexes from representative query plans. No database is created by this document.
