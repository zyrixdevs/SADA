# 10 — Testing and acceptance criteria

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the testing and acceptance criteria responsibility of Emergency Response Playbooks. Coordinate human-approved containment, communication, and recovery steps.

## Proposed technical contract

Use unit, PostgreSQL integration, API contract, tenant authorization, adversarial, privacy, load, and failure/restart tests. Fixtures include duplicate floods, forged/stale timestamps, source collusion, correction races, revoked consent, and dependency outages. Acceptance invariant: Revoked approval blocks execution; ambiguous timeout reconciles; partial recovery stays visible. Every result has source refs, version, uncertainty and exclusions. No live Discord mutation calls.

## Failure and safety behavior

No score-triggered action, cross-guild action, or irreversible step without explicit local authorization. Urgency abuse, compromised approver, stale case, duplicate/destructive action. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Suspicious Admin Activity](../suspicious-admin-activity/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Incident Timeline](../incident-timeline/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Automation scope; approval quorum; emergency fallback; response goals. Proposed phase: 6 after authorization and rollback. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
