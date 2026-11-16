# 02 — Reliability architecture

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the reliability architecture responsibility of Trust and Reliability Engine. Expose evidence/source quality with uncertainty without permanently labeling communities or people.

## Proposed technical contract

Inputs: Provenance, audit matches, duplicate/correction history, dispositions, denominator, method version. Stages: validate source/consent/schema/time; deduplicate; apply versioned normalization; enforce relevance, independent-source, temporal, sample and evidence-quality gates; report factors, uncertainty, exclusions and algorithm version; route candidate to review. No threshold/accuracy is validated. Missing data is unknown, not a negative result.

## Failure and safety behavior

No penalty for appeal count alone, opaque permanent score, automatic source exclusion. Feedback loops, bias, false reports, small samples, retaliation. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Evidence Vault](../evidence-vault/README.md), [Global Ban System](../global-ban-system/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Sample floor; weights; reviewer; transparency; cadence. Proposed phase: 3 after governance/evaluation corpus. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
