# 08 — Privacy and data minimization

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the privacy and data minimization responsibility of Threat DNA. Create privacy-bounded, versioned fingerprints of attack behavior for explainable comparison.

## Proposed technical contract

Threat-specific risks: Dictionary attacks, re-identification, mutation, collision, overfitting. Accept only Permitted timing buckets, action sequences, URL/domain indicators, approved template hashes, provenance.; reject unapproved fields. Encrypt restricted evidence, scope and audit reads, redact cross-guild summaries, rate-limit, and support revocation/suspension plus appeal. A suspicious pattern may route to review only. Similarity is not identity or guilt; no private conversations, device fingerprints, or permanent cross-context links.

## Failure and safety behavior

Similarity is not identity or guilt; no private conversations, device fingerprints, or permanent cross-context links. Dictionary attacks, re-identification, mutation, collision, overfitting. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Allowed features; key rotation; scope; threshold; evaluation corpus. Proposed phase: 3 after privacy review and synthetic corpus. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
