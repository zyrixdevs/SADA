# 09 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Security Advisory Network. Deliver relevant, deduplicated opt-in notices by subscription and access policy.

## Proposed technical contract

Prerequisites: decide Categories; channels; redaction; critical criteria.; approve fields/retention; complete shared contracts. Sequence: define advisories, advisory_revisions, subscriptions, delivery_outbox, delivery_receipts migrations; implement deterministic read-only evaluation of Reviewed indicator/campaign/case revision, category, severity, confidence, subscription, expiry.; integrate scam-and-phishing-intelligence;threat-intelligence-network;attack-campaign-tracker;global-ban-system;emergency-response-playbooks;security-observatory through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: One logical delivery per revision; revocation sends eligible correction. This is a proposal, not started work.

## Failure and safety behavior

No accused-user list, source/evidence leakage, or enforcement implied by subscription. Flooding, deanonymization, stale notices, enumeration. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Global Ban System](../global-ban-system/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Categories; channels; redaction; critical criteria. Proposed phase: 5 after scopes/outbox. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
