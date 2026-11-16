# 10 — Deployment and infrastructure

Deploy independently from Zyrix without Discord credentials. Minimum logical roles: API/worker, PostgreSQL, secret manager, encrypted backups; object store only if evidence capture approved. Network policy blocks SADA moderation access and restricts analyzer egress. Separate dev/staging/prod keys, data and Discord endpoints; no production evidence in dev. Gate deploy on artifact review, migration compatibility, readiness, rollback, restore. Hosting, region, residency, RPO/RTO, provider and operators are unresolved.
## Release sequencing

Deploy schema expansion before code that writes new columns; backfill and verify; deploy readers; then enable writers behind a flag. Rollback disables new behavior before reverting compatible code. Restore a backup in an isolated environment before any destructive migration. Production secrets and evidence never enter staging, CI artifacts, or developer laptops.
