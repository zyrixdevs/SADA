# 03 — Synthetic attack scenarios

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the synthetic attack scenarios responsibility of Security Simulation Mode. Exercise detection and response with synthetic events in isolated namespace.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Create isolated run, inject events, evaluate, simulate response, compare, export sanitized report. Inputs: Synthetic scenarios, seeded stream, detector versions, simulation identity. Output: Detection outcomes, simulated decisions, run manifest, safe report. Owned projections: simulation_runs, scenario_fixtures, simulated_events, detector_results Acceptance invariant: No mutation egress; synthetic tenant cannot query production cases.

## Failure and safety behavior

Never call Discord mutations, share synthetic incidents as real, or use production delivery. Environment crossing, credential leak, synthetic/real confusion. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Early Raid Detection](../early-raid-detection/README.md), [Suspicious Admin Activity](../suspicious-admin-activity/README.md), [Threat Dna](../threat-dna/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Incident Timeline](../incident-timeline/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Local/staging/hosted; scenario review. Proposed phase: 4 after fixtures and isolation. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
