# 05 — Correction and appeal history

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the correction and appeal history responsibility of Trust and Reliability Engine. Expose evidence/source quality with uncertainty without permanently labeling communities or people.

## Proposed technical contract

Represent a correction as a new linked revision with authority, actor, reason, time and superseded ID. Recompute current views and cancel stale pending delivery; notify authorized recipients if policy requires. Preserve audit linkage but do not present reversed data as current. Set separate expiry for source payload, metadata, evidence, derived features, audit and backups. Holds are scoped, time limited, reviewed and audited. Exact periods require legal/privacy review.

## Failure and safety behavior

No penalty for appeal count alone, opaque permanent score, automatic source exclusion. Feedback loops, bias, false reports, small samples, retaliation. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Evidence Vault](../evidence-vault/README.md), [Global Ban System](../global-ban-system/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Sample floor; weights; reviewer; transparency; cadence. Proposed phase: 3 after governance/evaluation corpus. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
