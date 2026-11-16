# 09 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Security Observatory. Present role-scoped aggregate security trends without exposing allegations to broad audiences.

## Proposed technical contract

Prerequisites: decide Cohort floor; staff/public fields; windows; export rights.; approve fields/retention; complete shared contracts. Sequence: define aggregate_views, metric_snapshots, dashboard_access_events, audit_events migrations; implement deterministic read-only evaluation of Authorized aggregates, time buckets, category/severity, source diversity, freshness, query scope.; integrate incident-timeline;attack-campaign-tracker;security-advisory-network;threat-intelligence-network;trust-and-reliability-engine through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: Sub-floor and overlapping queries cannot reveal suppressed counts. This is a proposal, not started work.

## Failure and safety behavior

No public accused list or query differencing to reconstruct incidents. Small-cell disclosure, differencing, misleading trend, export misuse. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Incident Timeline](../incident-timeline/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Cohort floor; staff/public fields; windows; export rights. Proposed phase: 7 after privacy review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
