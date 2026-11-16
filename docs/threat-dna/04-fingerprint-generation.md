# 04 — Fingerprint generation

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the fingerprint generation responsibility of Threat DNA. Create privacy-bounded, versioned fingerprints of attack behavior for explainable comparison.

## Proposed technical contract

Inputs: Permitted timing buckets, action sequences, URL/domain indicators, approved template hashes, provenance. Stages: validate source/consent/schema/time; deduplicate; apply versioned normalization; enforce relevance, independent-source, temporal, sample and evidence-quality gates; report factors, uncertainty, exclusions and algorithm version; route candidate to review. No threshold/accuracy is validated. Missing data is unknown, not a negative result.

## Failure and safety behavior

Similarity is not identity or guilt; no private conversations, device fingerprints, or permanent cross-context links. Dictionary attacks, re-identification, mutation, collision, overfitting. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Allowed features; key rotation; scope; threshold; evaluation corpus. Proposed phase: 3 after privacy review and synthetic corpus. No numeric threshold, accuracy, operational target or deployed behavior is claimed.

## Fingerprint pipeline

Input extraction is an allowlist by event type. Convert timestamps to coarse buckets, action sequences to enumerated tokens, URLs to normalized indicator references, and approved template signatures to keyed digests. Drop author prose, private message bodies, attachments, and unrelated user data. Store feature-set and normalization version beside every digest so rotation or rule changes can invalidate old comparisons. Candidate similarity reports the matching dimensions and missing dimensions; collision handling sends both records to review rather than merging them.
