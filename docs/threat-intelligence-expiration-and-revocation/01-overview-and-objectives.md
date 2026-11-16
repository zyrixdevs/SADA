# 01 — Overview and objectives: Threat Intelligence Expiration and Revocation

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Provide one lifecycle for intelligence freshness, correction, withdrawal and propagation across consumers.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Indicator/revision refs; source validity; evidence status; expiry policy; correction/reversal event; downstream pending deliveries.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Expiration does not prove an indicator was false; historical decisions must retain the version actually seen and later correction linkage.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Default TTLs, retroactive correction obligations and appeal interaction require governance decisions.
