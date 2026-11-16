# 05 — Case and campaign timelines

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the case and campaign timelines responsibility of Incident Timeline. Provide chronology that distinguishes source time, receipt time, attribution confidence, and correction.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Persist immutable event, normalize time, order with tie-breakers, annotate uncertainty, append corrections, rebuild view. Inputs: Typed events, occurred/observed/received times, source refs, revisions and case/campaign links. Output: Case/campaign timeline with ordering uncertainty and provenance. Owned projections: events, timeline_links, correction_events, source_refs, audit_events Acceptance invariant: Late event appears at source time with late-received marker; correction links original.

## Failure and safety behavior

Never overwrite source or hide clock uncertainty; order is not proof. Clock skew, forged time, floods, unauthorized discovery. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Evidence Vault](../evidence-vault/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Retention; cross-case view; time precision. Proposed phase: 1 shared foundation. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
