# 11 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Security Health Monitor. Assess opt-in guild configuration and provide prioritized, reversible recommendations.

## Proposed technical contract

Prerequisites: decide Cadence; retention; risk rubric; identity fields.; approve fields/retention; complete shared contracts. Sequence: define configuration_snapshots, snapshot_objects, health_findings, remediation_reviews migrations; implement deterministic read-only evaluation of Authorized roles, permissions, bot/integration scopes, webhook metadata without tokens, channel overwrites.; integrate incident-recovery-assistant;incident-timeline;evidence-vault;emergency-response-playbooks;attack-impact-simulator;security-observatory through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: Change creates a new snapshot/diff; stale data is labelled stale. This is a proposal, not started work.

## Failure and safety behavior

Read-only; never mutate roles/channels/integrations/webhooks/settings or export tokens. Overbroad permissions, stale snapshot, leakage, mistaken risk classifications. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Cadence; retention; risk rubric; identity fields. Proposed phase: 5 after scope and retention review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
