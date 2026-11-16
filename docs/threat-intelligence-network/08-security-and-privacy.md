# 08 — Security and privacy

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the security and privacy responsibility of Threat Intelligence Network. Correlate provenance-bearing security incidents across independently opted-in installations.

## Proposed technical contract

Threat-specific risks: Sybil reports, collusion, graph traversal leakage, evidence poisoning. Accept only Authorized incidents, source-guild scope, event/evidence references, correction state, consent version.; reject unapproved fields. Encrypt restricted evidence, scope and audit reads, redact cross-guild summaries, rate-limit, and support revocation/suspension plus appeal. A suspicious pattern may route to review only. One guild, installation, retry, or copied report never counts as several independent sources.

## Failure and safety behavior

One guild, installation, retry, or copied report never counts as several independent sources. Sybil reports, collusion, graph traversal leakage, evidence poisoning. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Dna](../threat-dna/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Global Ban System](../global-ban-system/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Cross-guild pseudonymous links; independence policy; source identity visibility. Proposed phase: 2 after consent and event contracts. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
