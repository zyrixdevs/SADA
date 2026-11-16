# Data model — External Threat Feed Intelligence

**Proposed PostgreSQL tables only; no migrations exist.** Shared identity, consent, inbox, incidents, evidence, cases, reviews, outbox and audit remain canonical in [platform storage architecture](../system-architecture/05-database-and-storage-architecture.md). The following module-owned tables add domain projections and reference canonical IDs; never duplicate their source records.

## Proposed tables

threat_feed_sources(source_id UUID PK, name TEXT, endpoint_ref TEXT, credential_ref TEXT NULL, enabled BOOLEAN, policy_version TEXT, last_success_at TIMESTAMPTZ NULL); feed_indicator_revisions(revision_id UUID PK, source_id UUID FK, external_id TEXT, indicator_type TEXT, value_digest BYTEA, normalized_value TEXT, source_revision TEXT, published_at TIMESTAMPTZ NULL, expires_at TIMESTAMPTZ NULL, status TEXT)

Column conventions: UUID module primary keys; `BIGINT` Discord snowflakes; UTC `TIMESTAMPTZ`; `BYTEA` for cryptographic digests; `JSONB` only for versioned factor/config snapshots, with validation and bounded size. Add foreign keys to canonical event/evidence/campaign IDs where the owning schema permits; use `ON DELETE RESTRICT` for audit-bearing references. Add `CHECK` constraints for state values, positive counts and valid time ranges. Guild-scoped access paths require indexes beginning with `guild_id` and time/state as appropriate. Unique constraints should include source/revision to make retries idempotent.

## Retention, ownership and migration

The domain module owns these projections; canonical services own shared records. Personal or incident-linked observations require an explicit `retention_until`; aggregate snapshots may outlive source rows only under approved aggregation policy. Expiration and deletion must append shared audit references and reconcile object storage. Corrections create revisions rather than overwriting history. Migrations require empty and previous-version tests, expand/migrate/contract sequencing, rollback/forward plan and tenant isolation review. Exact duration, partitioning and RLS decisions remain open until policy owners approve them.
