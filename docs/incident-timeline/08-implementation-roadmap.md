# 08 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Incident Timeline. Provide chronology that distinguishes source time, receipt time, attribution confidence, and correction.

## Proposed technical contract

Prerequisites: decide Retention; cross-case view; time precision.; approve fields/retention; complete shared contracts. Sequence: define events, timeline_links, correction_events, source_refs, audit_events migrations; implement deterministic read-only evaluation of Typed events, occurred/observed/received times, source refs, revisions and case/campaign links.; integrate evidence-vault;attack-campaign-tracker;threat-intelligence-network;security-observatory through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: Late event appears at source time with late-received marker; correction links original. This is a proposal, not started work.

## Failure and safety behavior

Never overwrite source or hide clock uncertainty; order is not proof. Clock skew, forged time, floods, unauthorized discovery. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Evidence Vault](../evidence-vault/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Retention; cross-case view; time precision. Proposed phase: 1 shared foundation. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
