# 02 — Monitoring architecture

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the monitoring architecture responsibility of Suspicious Admin Activity. Surface unusual privileged actions for evidence-led investigation.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Observe, match fresh target-specific audit record, compare baseline, explain anomaly, alert staff, review/correct. Inputs: Audit entries, actor/target IDs, role/channel changes, mass bans, webhook events, outcome and local baseline. Output: Attributed timeline event, attribution confidence and review case. Owned projections: admin_events, actor_attributions, behavior_baselines, cases, evidence_refs Acceptance invariant: Unmatched mass action opens unattributed event, not accusation.

## Failure and safety behavior

Unmatched remains unattributed; unusual is not proof of compromise; never revoke roles automatically. Audit ambiguity, legitimate bulk work, compromised bot, insider retaliation. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Baseline; maintenance annotations; notification privacy; thresholds. Proposed phase: 4 after attribution tests. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
