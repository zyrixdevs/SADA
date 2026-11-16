# 04 — Campaign lifecycle

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the campaign lifecycle responsibility of Attack Campaign Tracker. Group related incidents into versioned investigations while preserving uncertainty and source facts.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Open candidate, propose links, evaluate independence/time, review, merge/split/close with history. Inputs: Candidate links from time, indicators, fingerprints, human edges with provenance/version. Output: Campaign lifecycle, evidence graph, timeline, inclusion/exclusion, review state. Owned projections: campaigns, campaign_revisions, campaign_incident_links, relationship_edges Acceptance invariant: Reversal recomputes current campaign; merge/split preserves revision history.

## Failure and safety behavior

No merge from weak indicator or campaign membership as individual guilt. Over-connection, hijack, stale infrastructure, circular corroboration. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Early Raid Detection](../early-raid-detection/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Security Advisory Network](../security-advisory-network/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Merge gate; independent sources; lifecycle owner; public language. Proposed phase: 4 after graph/evidence/timeline. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
