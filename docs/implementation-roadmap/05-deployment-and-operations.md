# 05 — Deployment and operations

Name service/database owner, security/privacy contacts, reviewer admin, incident commander and on-call. Decide residency, encrypted backups, recovery targets, monitoring and rotation. Runbooks cover migration, restore, outbox replay, evidence reconciliation, credential compromise, source suspension, reviewer lockout and signal stop. SADA outage cannot degrade Zyrix. Start independent API/worker + PostgreSQL; provider/topology/RPO/RTO/staffing open.
## Minimum runbook contents

Every runbook identifies alert signal, severity, operator role, safe preconditions, exact containment action, verification query, recovery/rollback, communication owner, and follow-up audit. Restore exercises include PostgreSQL and object metadata, then verify evidence digests and outbox consistency. A queue replay requires a dry-run count and expiry/consent recheck before dispatch.
