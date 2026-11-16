# 08 — Testing and acceptance criteria

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the testing and acceptance criteria responsibility of Attack Impact Simulator. Estimate consequence of a proposed action against a frozen local snapshot.

## Proposed technical contract

Use unit, PostgreSQL integration, API contract, tenant authorization, adversarial, privacy, load, and failure/restart tests. Fixtures include duplicate floods, forged/stale timestamps, source collusion, correction races, revoked consent, and dependency outages. Acceptance invariant: Synthetic plan makes no mutation call; missing permission data yields unknown. Every result has source refs, version, uncertainty and exclusions. No live Discord mutation calls.

## Failure and safety behavior

No Discord write credential, mutating endpoint, or real action queue. Stale input, underestimated cascade, credential exposure. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Incident Timeline](../incident-timeline/README.md), [Global Ban System](../global-ban-system/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Freshness; estimate presentation; simulation retention. Proposed phase: 5 before action workflows. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
