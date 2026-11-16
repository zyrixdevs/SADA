# 04 — Multi-signal correlation

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the multi-signal correlation responsibility of Ban Evasion Intelligence. Provide cautious candidate links where permitted signals suggest possible ban evasion.

## Proposed technical contract

Inputs: Approved public metadata and opt-in guild observations, time, source confidence. Stages: validate source/consent/schema/time; deduplicate; apply versioned normalization; enforce relevance, independent-source, temporal, sample and evidence-quality gates; report factors, uncertainty, exclusions and algorithm version; route candidate to review. No threshold/accuracy is validated. Missing data is unknown, not a negative result.

## Failure and safety behavior

No IP/device fingerprints, weak-similarity identity claims, surveillance, automatic punishment. False identity links, shared accounts, mimicry, discriminatory proxies. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Global Ban System](../global-ban-system/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Allowed signals; weights; retention; visibility. Proposed phase: 7 after legal/privacy and false-positive review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.

## Correlation safeguards

Signals are grouped by provenance and independence before evaluation. A single display name, avatar, join pattern, or shared public link cannot establish identity. A candidate must list each signal, source permission, temporal relation, alternative explanation, and missing data. Keep a source-level observation distinct from a derived relationship. Similarity thresholds remain unapproved and require bias/false-positive review before any reviewer-facing high-confidence label.
