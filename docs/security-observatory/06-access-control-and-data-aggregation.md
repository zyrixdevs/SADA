# 06 — Access control and data aggregation

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the access control and data aggregation responsibility of Security Observatory. Present role-scoped aggregate security trends without exposing allegations to broad audiences.

## Proposed technical contract

Threat-specific risks: Small-cell disclosure, differencing, misleading trend, export misuse. Accept only Authorized aggregates, time buckets, category/severity, source diversity, freshness, query scope.; reject unapproved fields. Encrypt restricted evidence, scope and audit reads, redact cross-guild summaries, rate-limit, and support revocation/suspension plus appeal. A suspicious pattern may route to review only. No public accused list or query differencing to reconstruct incidents.

## Failure and safety behavior

No public accused list or query differencing to reconstruct incidents. Small-cell disclosure, differencing, misleading trend, export misuse. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Incident Timeline](../incident-timeline/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Cohort floor; staff/public fields; windows; export rights. Proposed phase: 7 after privacy review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
## Aggregate query protection

Define an approved metric registry with dimensions, time buckets, data lineage, minimum cohort policy, and export scope. Suppress small groups before serialization and apply complementary suppression so totals cannot reveal a hidden cell. Rate-limit overlapping filters and audit exports. Do not permit arbitrary user ID filters. A metric snapshot records method version, freshness, suppression state, and source aggregate IDs without exposing individual incidents.
