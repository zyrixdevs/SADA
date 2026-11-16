# 04 — Access control and encryption

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the access control and encryption responsibility of Evidence Vault. Store structured references and approved artifacts with integrity, access, retention, deletion.

## Proposed technical contract

Threat-specific risks: Insider access, key compromise, malicious files, orphan objects, legal holds. Accept only Evidence metadata/reference, authorized artifact, digest, provenance, retention class.; reject unapproved fields. Encrypt restricted evidence, scope and audit reads, redact cross-guild summaries, rate-limit, and support revocation/suspension plus appeal. A suspicious pattern may route to review only. No public blobs, private content by default, or claim hash proves truth.

## Failure and safety behavior

No public blobs, private content by default, or claim hash proves truth. Insider access, key compromise, malicious files, orphan objects, legal holds. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Incident Timeline](../incident-timeline/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Global Ban System](../global-ban-system/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Evidence classes; duration; rights; provider; hold authority. Proposed phase: 1 policy before capture. No numeric threshold, accuracy, operational target or deployed behavior is claimed.

## Read and export controls

Authorize a read against case membership, reviewer role, purpose, evidence classification, and current appeal/hold state. Issue short-lived object access only after the authorization decision; do not expose stable storage keys to clients. Log requester, evidence ID, purpose, time, result, and export form without copying the content into logs. Revoke access on role change and key rotation. A hash mismatch quarantines the object and prevents reviewer reliance.
