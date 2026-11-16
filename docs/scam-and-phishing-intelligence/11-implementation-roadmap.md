# 11 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Scam and Phishing Intelligence. Verify and distribute scam indicators while isolating URL analysis from bot infrastructure.

## Proposed technical contract

Prerequisites: decide Sandbox; source use; review quorum; expiry; exception authority.; approve fields/retention; complete shared contracts. Sequence: define threat_indicators, indicator_observations, domain_relationships, evidence_refs migrations; implement deterministic read-only evaluation of Submitted URL/domain, source context, time, isolated redirect chain, provenance.; integrate threat-intelligence-network;threat-dna;evidence-vault;trust-and-reliability-engine;security-advisory-network;incident-timeline through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: Unicode/punycode normalize consistently; private redirects blocked; revocation stops delivery. This is a proposal, not started work.

## Failure and safety behavior

Never fetch arbitrary URLs from bot/operator hosts; a report is not proof; reporter hidden by default. SSRF, DNS rebinding, private redirect, malware, homographs, stale reputation. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Incident Timeline](../incident-timeline/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Sandbox; source use; review quorum; expiry; exception authority. Proposed phase: 3 after isolated analyzer design. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
