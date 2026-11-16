# 02 — Campaign data model

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the campaign data model responsibility of Attack Campaign Tracker. Group related incidents into versioned investigations while preserving uncertainty and source facts.

## Proposed technical contract

Proposed PostgreSQL ownership: campaigns, campaign_revisions, campaign_incident_links, relationship_edges. Use UUID PK, FK to canonical IDs, UTC TIMESTAMPTZ, CHECK for finite states, unique source/revision keys, and tenant plus time/status indexes. Store policy/algorithm version and explanation. Write result, audit and outbox intent in one transaction. JSONB only for validated explanation snapshots. No cascade-delete of investigations. Retention and partitioning require policy/measurement.

## Failure and safety behavior

No merge from weak indicator or campaign membership as individual guilt. Over-connection, hijack, stale infrastructure, circular corroboration. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Early Raid Detection](../early-raid-detection/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Security Advisory Network](../security-advisory-network/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Merge gate; independent sources; lifecycle owner; public language. Proposed phase: 4 after graph/evidence/timeline. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
