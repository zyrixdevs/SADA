# 03 — Enforcement impact analysis

**Status: proposed specification; not implemented.**

## Scope

This chapter defines the enforcement impact analysis responsibility of Attack Impact Simulator. Estimate consequence of a proposed action against a frozen local snapshot.

## Proposed technical contract

Boundary: Zyrix adapter validates consent and submits events; Rust Core owns this workflow; PostgreSQL is authoritative; API returns scoped projection; Zyrix alone performs Discord actions. Process: Freeze input, validate age, dry-run rules, show uncertainty, reviewer revises or accepts. Inputs: Action plan, target set, snapshot revision, policy, uncertainty, reversibility. Output: Read-only estimate, affected counts, exclusions, false-positive scenarios, rollback requirements. Owned projections: simulation_runs, simulation_inputs, impact_estimates, rule_versions Acceptance invariant: Synthetic plan makes no mutation call; missing permission data yields unknown.

## Failure and safety behavior

No Discord write credential, mutating endpoint, or real action queue. Stale input, underestimated cascade, credential exposure. Retry transient failures only with idempotency; reject permanent authorization/schema errors. Reconcile ambiguous external outcomes by request ID before retry. SADA outage cannot authorize a Discord action.

## Related contracts

Related modules: [Emergency Response Playbooks](../emergency-response-playbooks/README.md), [Security Health Monitor](../security-health-monitor/README.md), [Incident Recovery Assistant](../incident-recovery-assistant/README.md), [Incident Timeline](../incident-timeline/README.md), [Global Ban System](../global-ban-system/README.md), [Security Observatory](../security-observatory/README.md). Canonical [event](../shared-standards/01-event-schema-standard.md), [evidence](../shared-standards/02-evidence-standard.md), [confidence](../shared-standards/04-confidence-standard.md), [audit](../shared-standards/08-audit-record-standard.md), [platform architecture](../system-architecture/README.md), and [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).

## Open decisions and implementation state

Freshness; estimate presentation; simulation retention. Proposed phase: 5 before action workflows. No numeric threshold, accuracy, operational target or deployed behavior is claimed.
## Estimation method

Freeze the target set and snapshot revision. Compute eligible, excluded, already-affected, hierarchy-blocked, permission-unknown, and stale-state counts separately. Report the set difference that drives each estimate and a snapshot age label. For cross-guild decisions, show each guild outcome separately rather than summing as universal enforcement. Recalculate when membership or permissions change; estimates are not guarantees and do not enqueue actions.
