# 03 — Configuration snapshots

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the configuration snapshots responsibility of Incident Recovery Assistant. Prepare reviewable restoration plans from captured guild config after destructive incidents.

## Proposed technical contract

Proposed PostgreSQL ownership: configuration_snapshots, recovery_plans, recovery_steps, approvals, execution_receipts. Use UUID PK, FK to canonical IDs, UTC TIMESTAMPTZ, CHECK for finite states, unique source/revision keys, and tenant plus time/status indexes. Store policy/algorithm version and explanation. Write result, audit and outbox intent in one transaction. JSONB only for validated explanation snapshots. No cascade-delete of investigations. Retention and partitioning require policy/measurement.

## Failure and safety behavior

Never restore automatically, bypass hierarchy, claim deleted Discord IDs are identical or full rollback. Stale backup, injected snapshot, escalation, name collisions, partial execution. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Security Health Monitor](../security-health-monitor/README.md), [Evidence Vault](../evidence-vault/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Incident Timeline](../incident-timeline/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Snapshot cadence; restorable objects; owner verification; retention. Proposed phase: 6 after integrity/simulator. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
