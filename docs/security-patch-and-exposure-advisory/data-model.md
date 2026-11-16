# Data model — Security Patch and Exposure Advisory

**Proposed PostgreSQL tables only; no migrations exist.** Shared identity, consent, inbox, incidents, evidence, cases, reviews, outbox and audit remain canonical in [platform storage architecture](../system-architecture/05-database-and-storage-architecture.md). The following module-owned tables add domain projections and reference canonical IDs; never duplicate their source records.

## Proposed tables

patch_advisories(advisory_id UUID PK, source_ref TEXT, revision TEXT, disclosure_state TEXT, published_at TIMESTAMPTZ NULL, updated_at TIMESTAMPTZ, status TEXT); affected_components(advisory_id UUID FK, ecosystem TEXT, name TEXT, version_range TEXT, fixed_version TEXT NULL, PRIMARY KEY(advisory_id,ecosystem,name,version_range)); remediation_statuses(status_id UUID PK, advisory_id UUID FK, component_ref UUID, owner_ref UUID, state TEXT, verified_at TIMESTAMPTZ NULL, evidence_ref UUID NULL)

Column conventions: UUID module primary keys; `BIGINT` Discord snowflakes; UTC `TIMESTAMPTZ`; `BYTEA` for cryptographic digests; `JSONB` only for versioned factor/config snapshots, with validation and bounded size. Add foreign keys to canonical event/evidence/campaign IDs where the owning schema permits; use `ON DELETE RESTRICT` for audit-bearing references. Add `CHECK` constraints for state values, positive counts and valid time ranges. Guild-scoped access paths require indexes beginning with `guild_id` and time/state as appropriate. Unique constraints should include source/revision to make retries idempotent.

## Retention, ownership and migration

The domain module owns these projections; canonical services own shared records. Personal or incident-linked observations require an explicit `retention_until`; aggregate snapshots may outlive source rows only under approved aggregation policy. Expiration and deletion must append shared audit references and reconcile object storage. Corrections create revisions rather than overwriting history. Migrations require empty and previous-version tests, expand/migrate/contract sequencing, rollback/forward plan and tenant isolation review. Exact duration, partitioning and RLS decisions remain open until policy owners approve them.
