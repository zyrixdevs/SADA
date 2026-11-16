# 01 — Overview and objectives

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the overview and objectives responsibility of Threat Intelligence API. Expose scoped, versioned summaries to authorized integrations with audited access and no action authority.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Authenticate, authorize tenant/object, validate limits, query projection, redact, return cursor, audit. Inputs: Authenticated identity, scopes, bounded query, cursor, fields, idempotency. Output: Versioned allowed summary, freshness, provenance, correction. Owned projections: installations, access_grants, rate_windows, audit_events, delivery_receipts Acceptance invariant: Guild key cannot read another guild evidence; revoke fails; cursor cannot widen.

## Failure and safety behavior

No public accused-user search, raw evidence by default, secrets, or Discord action authority. Key theft, enumeration, tenant escape, replay, overbroad scope. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Global Ban System](../global-ban-system/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Early Raid Detection](../early-raid-detection/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Suspicious Admin Activity](../suspicious-admin-activity/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Ban Evasion Intelligence](../ban-evasion-intelligence/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Security Simulation Mode](../security-simulation-mode/README.md), [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Audience; identity; quota; public aggregate policy. Proposed phase: 2 internal; external after review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
