# 11 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Suspicious Admin Activity. Surface unusual privileged actions for evidence-led investigation.

## Proposed technical contract

Prerequisites: decide Baseline; maintenance annotations; notification privacy; thresholds.; approve fields/retention; complete shared contracts. Sequence: define admin_events, actor_attributions, behavior_baselines, cases, evidence_refs migrations; implement deterministic read-only evaluation of Audit entries, actor/target IDs, role/channel changes, mass bans, webhook events, outcome and local baseline.; integrate early-raid-detection;incident-timeline;evidence-vault;emergency-response-playbooks;attack-impact-simulator;security-health-monitor;trust-and-reliability-engine through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: Unmatched mass action opens unattributed event, not accusation. This is a proposal, not started work.

## Failure and safety behavior

Unmatched remains unattributed; unusual is not proof of compromise; never revoke roles automatically. Audit ambiguity, legitimate bulk work, compromised bot, insider retaliation. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Baseline; maintenance annotations; notification privacy; thresholds. Proposed phase: 4 after attribution tests. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
