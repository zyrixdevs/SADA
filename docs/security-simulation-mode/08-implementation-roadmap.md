# 08 — Implementation roadmap

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the implementation roadmap responsibility of Security Simulation Mode. Exercise detection and response with synthetic events in isolated namespace.

## Proposed technical contract

Prerequisites: decide Local/staging/hosted; scenario review.; approve fields/retention; complete shared contracts. Sequence: define simulation_runs, scenario_fixtures, simulated_events, detector_results migrations; implement deterministic read-only evaluation of Synthetic scenarios, seeded stream, detector versions, simulation identity.; integrate early-raid-detection;suspicious-admin-activity;threat-dna;emergency-response-playbooks;attack-impact-simulator;incident-timeline;security-observatory through outbox; add scoped review and correction; pass privacy, adversarial, restore and ops gates. Complete when: No mutation egress; synthetic tenant cannot query production cases. This is a proposal, not started work.

## Failure and safety behavior

Never call Discord mutations, share synthetic incidents as real, or use production delivery. Environment crossing, credential leak, synthetic/real confusion. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Suspicious Admin Activity](../suspicious-admin-activity/README.md), [Threat Dna](../threat-dna/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Incident Timeline](../incident-timeline/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Local/staging/hosted; scenario review. Proposed phase: 4 after fixtures and isolation. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
