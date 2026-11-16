# 01 — Overview and objectives

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the overview and objectives responsibility of Early Raid Detection. Warn guild staff early using explainable local join and message velocity signals.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Aggregate locally, compare baseline, combine signals, explain deviation, alert staff, await human choice. Inputs: Join times, message/mention counts, channel, optional approved account-age bucket, local baseline. Output: Severity-banded explanation and reversible mitigation suggestions. Owned projections: guild_baselines, detection_windows, incidents, evidence_refs, alerts Acceptance invariant: Join and mention burst outranks one noisy signal; missing baseline is unknown.

## Failure and safety behavior

Rates alone do not prove coordination; no automatic bans, timeouts, locks, or configuration edits. Slow raids, legitimate surges, cold start, alert manipulation, privacy leak. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Threat Dna](../threat-dna/README.md), [Incident Timeline](../incident-timeline/README.md), [Evidence Vault](../evidence-vault/README.md), [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Attack Impact Simulator](../attack-impact-simulator/README.md), [Security Advisory Network](../security-advisory-network/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Baseline windows; sample sizes; alert thresholds; account-age use; retention. Proposed phase: 4 after local events and consent. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
