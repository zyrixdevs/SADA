# 01 — Overview and objectives: Configuration Drift Detection

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Track authorized guild configuration snapshots and identify changes from approved baselines.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Role/channel/overwrite/webhook/invite/integration metadata; baseline revision; source change event; scan completeness.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Drift can be intentional; scans can be partial or stale; a difference is not necessarily a risk.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Baseline refresh policy, categories and retention need operational/privacy review.
