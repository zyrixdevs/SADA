# 01 — Overview and objectives: Integration Supply Chain Intelligence

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Correlate reviewed security advisories about integrations, publishers and shared dependencies.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Application/publisher identifiers; package/component identifiers from trusted advisories; reviewed compromise reports; dependency and build provenance references.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Do not infer a guild uses a dependency from application name alone; external feed claims can be stale or malicious.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Trusted source criteria, allowed ecosystems and distribution scope require review.
