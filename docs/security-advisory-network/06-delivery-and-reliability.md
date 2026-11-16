# 06 — Delivery and reliability

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the delivery and reliability responsibility of Security Advisory Network. Deliver relevant, deduplicated opt-in notices by subscription and access policy.

## Proposed technical contract

Inputs: Reviewed indicator/campaign/case revision, category, severity, confidence, subscription, expiry. Stages: validate source/consent/schema/time; deduplicate; apply versioned normalization; enforce relevance, independent-source, temporal, sample and evidence-quality gates; report factors, uncertainty, exclusions and algorithm version; route candidate to review. No threshold/accuracy is validated. Missing data is unknown, not a negative result.

## Failure and safety behavior

No accused-user list, source/evidence leakage, or enforcement implied by subscription. Flooding, deanonymization, stale notices, enumeration. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Global Ban System](../global-ban-system/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Categories; channels; redaction; critical criteria. Proposed phase: 5 after scopes/outbox. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
