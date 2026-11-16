# 01 — Overview and objectives: Invite Link Security Monitor

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Track authorized invite lifecycle metadata and identify suspicious invite campaigns.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Invite code hash/reference; creation/update/deletion events; inviter attribution; uses/max-age/max-uses; destination guild; join event invite attribution where exposed.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Invite attribution may not be available or reliable for every join; never claim origin from timing alone.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Cross-server sharing of invite indicators and hash key lifecycle require approval.
