# 01 — Overview and objectives: SADA API Abuse Protection

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Detect and contain API flooding, credential abuse and replay using platform authentication and delivery controls.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Authenticated principal/key ID; request IDs; nonce/timestamp; route, response code, bytes, rate windows; failed auth class; idempotency key digest.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Do not build a parallel auth system; trusted client IP exists only behind verified proxy; shared NAT can trigger false positives.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Quota defaults, restriction authority, proxy topology and emergency exception need operational decision.
