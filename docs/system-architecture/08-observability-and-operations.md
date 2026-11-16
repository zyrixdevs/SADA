# 08 — Observability and operations

Separate liveness/readiness; readiness covers DB/worker, not Discord. Measure queue age, rejects by safe code, duplicates, expired leases, dead letters, review backlog, integrity errors, delivery, local receipts. Logs use request IDs and opaque IDs, never credentials, messages, raw evidence, interaction tokens, webhook URLs, unrestricted reasons. Runbooks: failover, outbox replay, key rotation, compromised installation, abusive source, restore failure, global signal stop. RPO/RTO and staffing open.

## Alerting thresholds

Set operational thresholds only after staging baselines. Page on sustained queue age beyond the agreed service objective, repeated database readiness failure, evidence digest mismatch, or unexpected enforcement receipt state. Notify operators about retry/dead-letter growth without including subject IDs. Every alert has an owner, runbook, and severity; dashboards show freshness.
