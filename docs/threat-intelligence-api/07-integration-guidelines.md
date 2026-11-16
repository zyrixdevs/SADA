# 07 — Integration guidelines

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the integration guidelines responsibility of Threat Intelligence API. Expose scoped, versioned summaries to authorized integrations with audited access and no action authority.

## Proposed technical contract

Use versioned /v1/threat-intelligence-api; authenticate installation/reviewer and authorize guild/object/fields server-side. Example read: GET /v1/threat-intelligence-api?case_id=opaque&cursor=opaque. Response shape: {"data":[{"id":"opaque","revision":2,"status":"candidate","source_event_ids":["opaque"],"explanation":{"version":"policy-1","factors":[]}}],"next_cursor":null,"request_id":"req-id"}. Writes use Idempotency-Key; same key/body returns stored receipt, changed body conflicts. Scope-bind cursors, bound page size, shared error envelope; never put sensitive reasons in URLs.

## Failure and safety behavior

No public accused-user search, raw evidence by default, secrets, or Discord action authority. Key theft, enumeration, tenant escape, replay, overbroad scope. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Global Ban System](../global-ban-system/README.md), [Threat Intelligence Network](../threat-intelligence-network/README.md), [Threat Dna](../threat-dna/README.md), [Early Raid Detection](../early-raid-detection/README.md), [Scam And Phishing Intelligence](../scam-and-phishing-intelligence/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Suspicious Admin Activity](../suspicious-admin-activity/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Ban Evasion Intelligence](../ban-evasion-intelligence/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Trust And Reliability Engine](../trust-and-reliability-engine/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Attack Campaign Tracker](../attack-campaign-tracker/README.md), [Security Simulation Mode](../security-simulation-mode/README.md), [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Security Advisory Network](../security-advisory-network/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Audience; identity; quota; public aggregate policy. Proposed phase: 2 internal; external after review. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
