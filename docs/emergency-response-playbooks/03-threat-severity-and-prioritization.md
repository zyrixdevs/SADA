# 03 — Threat severity and prioritization

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the threat severity and prioritization responsibility of Emergency Response Playbooks. Coordinate human-approved containment, communication, and recovery steps.

## Proposed technical contract

Inputs: Reviewed case severity/confidence, guild scope, playbook version, local state, prerequisites. Stages: validate source/consent/schema/time; deduplicate; apply versioned normalization; enforce relevance, independent-source, temporal, sample and evidence-quality gates; report factors, uncertainty, exclusions and algorithm version; route candidate to review. No threshold/accuracy is validated. Missing data is unknown, not a negative result.

## Failure and safety behavior

No score-triggered action, cross-guild action, or irreversible step without explicit local authorization. Urgency abuse, compromised approver, stale case, duplicate/destructive action. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Suspicious Admin Activity](../suspicious-admin-activity/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Incident Timeline](../incident-timeline/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Automation scope; approval quorum; emergency fallback; response goals. Proposed phase: 6 after authorization and rollback. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
