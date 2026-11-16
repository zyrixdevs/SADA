# 08 — Scheduled and event-driven scans

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the scheduled and event-driven scans responsibility of Security Health Monitor. Assess opt-in guild configuration and provide prioritized, reversible recommendations.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Authorize snapshot, evaluate versioned rules, show findings/diff, admin reviews, re-scan. Inputs: Authorized roles, permissions, bot/integration scopes, webhook metadata without tokens, channel overwrites. Output: Versioned findings, object IDs, rationale, severity, confidence, remediation and staleness. Owned projections: configuration_snapshots, snapshot_objects, health_findings, remediation_reviews Acceptance invariant: Change creates a new snapshot/diff; stale data is labelled stale.

## Failure and safety behavior

Read-only; never mutate roles/channels/integrations/webhooks/settings or export tokens. Overbroad permissions, stale snapshot, leakage, mistaken risk classifications. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Cadence; retention; risk rubric; identity fields. Proposed phase: 5 after scope and retention review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
