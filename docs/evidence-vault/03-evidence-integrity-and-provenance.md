# 03 — Evidence integrity and provenance

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the evidence integrity and provenance responsibility of Evidence Vault. Store structured references and approved artifacts with integrity, access, retention, deletion.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Authorize, validate size/type, minimize/redact, encrypt, hash, store, audit reads, expire/delete. Inputs: Evidence metadata/reference, authorized artifact, digest, provenance, retention class. Output: Opaque evidence ID and integrity metadata; content separately authorized. Owned projections: evidence_objects, evidence_versions, evidence_access_events, retention_holds Acceptance invariant: Unauthorized read denied; mismatch blocks display; expiry reconciles blob and metadata.

## Failure and safety behavior

No public blobs, private content by default, or claim hash proves truth. Insider access, key compromise, malicious files, orphan objects, legal holds. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Incident Timeline](../incident-timeline/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Global Ban System](../global-ban-system/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Evidence classes; duration; rights; provider; hold authority. Proposed phase: 1 policy before capture. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
