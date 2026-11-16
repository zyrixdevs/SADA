# 05 — Isolation and safety guards

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the isolation and safety guards responsibility of Security Simulation Mode. Exercise detection and response with synthetic events in isolated namespace.

## Proposed technical contract

Threat-specific risks: Environment crossing, credential leak, synthetic/real confusion. Accept only Synthetic scenarios, seeded stream, detector versions, simulation identity.; reject unapproved fields. Encrypt restricted evidence, scope and audit reads, redact cross-guild summaries, rate-limit, and support revocation/suspension plus appeal. A suspicious pattern may route to review only. Never call Discord mutations, share synthetic incidents as real, or use production delivery.

## Failure and safety behavior

Never call Discord mutations, share synthetic incidents as real, or use production delivery. Environment crossing, credential leak, synthetic/real confusion. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Suspicious Admin Activity](../suspicious-admin-activity/README.md), [Threat Dna](../threat-dna/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Incident Timeline](../incident-timeline/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Local/staging/hosted; scenario review. Proposed phase: 4 after fixtures and isolation. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
## Isolation controls

Simulation uses a synthetic tenant namespace, separate database/schema or a type-enforced simulation ID, fake Discord transport, and egress policy that denies Discord mutation domains. Production delivery workers reject simulation IDs at the database boundary. Scenario fixtures are reviewed and versioned; exports are labeled synthetic. A safety test fails if a simulated event can create a production case, advisory, enforcement job, or local action receipt.
