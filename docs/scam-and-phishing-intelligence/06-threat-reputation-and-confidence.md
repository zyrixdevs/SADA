# 06 — Threat reputation and confidence

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the threat reputation and confidence responsibility of Scam and Phishing Intelligence. Verify and distribute scam indicators while isolating URL analysis from bot infrastructure.

## Proposed technical contract

Inputs: Submitted URL/domain, source context, time, isolated redirect chain, provenance. Stages: validate source/consent/schema/time; deduplicate; apply versioned normalization; enforce relevance, independent-source, temporal, sample and evidence-quality gates; report factors, uncertainty, exclusions and algorithm version; route candidate to review. No threshold/accuracy is validated. Missing data is unknown, not a negative result.

## Failure and safety behavior

Never fetch arbitrary URLs from bot/operator hosts; a report is not proof; reporter hidden by default. SSRF, DNS rebinding, private redirect, malware, homographs, stale reputation. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Incident Timeline](../incident-timeline/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Sandbox; source use; review quorum; expiry; exception authority. Proposed phase: 3 after isolated analyzer design. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
