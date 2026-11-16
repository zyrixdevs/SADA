# 08 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Attack Campaign Tracker. Group related incidents into versioned investigations while preserving uncertainty and source facts.

## Proposed technical contract

Prerequisites: decide Merge gate; independent sources; lifecycle owner; public language.; approve fields/retention; complete shared contracts. Sequence: define campaigns, campaign_revisions, campaign_incident_links, relationship_edges migrations; implement deterministic read-only evaluation of Candidate links from time, indicators, fingerprints, human edges with provenance/version.; integrate threat-intelligence-network;threat-dna;scam-and-phishing-intelligence;early-raid-detection;incident-timeline;evidence-vault;trust-and-reliability-engine;security-advisory-network through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: Reversal recomputes current campaign; merge/split preserves revision history. This is a proposal, not started work.

## Failure and safety behavior

No merge from weak indicator or campaign membership as individual guilt. Over-connection, hijack, stale infrastructure, circular corroboration. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Early Raid Detection](../early-raid-detection/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Security Advisory Network](../security-advisory-network/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Merge gate; independent sources; lifecycle owner; public language. Proposed phase: 4 after graph/evidence/timeline. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
