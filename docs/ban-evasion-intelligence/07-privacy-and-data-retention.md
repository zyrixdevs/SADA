# 07 — Privacy and data retention

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the privacy and data retention responsibility of Ban Evasion Intelligence. Provide cautious candidate links where permitted signals suggest possible ban evasion.

## Proposed technical contract

Threat-specific risks: False identity links, shared accounts, mimicry, discriminatory proxies. Accept only Approved public metadata and opt-in guild observations, time, source confidence.; reject unapproved fields. Encrypt restricted evidence, scope and audit reads, redact cross-guild summaries, rate-limit, and support revocation/suspension plus appeal. A suspicious pattern may route to review only. No IP/device fingerprints, weak-similarity identity claims, surveillance, automatic punishment.

## Failure and safety behavior

No IP/device fingerprints, weak-similarity identity claims, surveillance, automatic punishment. False identity links, shared accounts, mimicry, discriminatory proxies. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Global Ban System](../global-ban-system/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Allowed signals; weights; retention; visibility. Proposed phase: 7 after legal/privacy and false-positive review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
