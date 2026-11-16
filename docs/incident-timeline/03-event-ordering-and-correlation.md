# 03 — Event ordering and correlation

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the event ordering and correlation responsibility of Incident Timeline. Provide chronology that distinguishes source time, receipt time, attribution confidence, and correction.

## Proposed technical contract

Inputs: Typed events, occurred/observed/received times, source refs, revisions and case/campaign links. Stages: validate source/consent/schema/time; deduplicate; apply versioned normalization; enforce relevance, independent-source, temporal, sample and evidence-quality gates; report factors, uncertainty, exclusions and algorithm version; route candidate to review. No threshold/accuracy is validated. Missing data is unknown, not a negative result.

## Failure and safety behavior

Never overwrite source or hide clock uncertainty; order is not proof. Clock skew, forged time, floods, unauthorized discovery. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Evidence Vault](../evidence-vault/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Retention; cross-case view; time precision. Proposed phase: 1 shared foundation. No numeric threshold, accuracy, operational target or deployed behavior is claimed.

## Ordering key

Preserve occurred_at, observed_at, received_at, and source sequence independently. Render primarily by occurred_at, then source event sequence when trusted, then received_at and immutable event ID for deterministic ties. Flag implausible clock skew and late arrivals; never rewrite source timestamps. Corrections appear adjacent to the superseded event with a link and current-state marker. Correlation IDs group workflows but do not imply causal order.
