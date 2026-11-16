# 01 — Overview and objectives: Administrative Identity Protection

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Help guilds investigate suspicious use or changes involving administrative accounts.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Role grants/removals; admin action audit records; account age/verification metadata only where authorized; action velocity; historical admin event references.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Discord does not expose reliable login/session or IP telemetry to SADA; no device fingerprinting or cross-guild private behavior surveillance.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Notice, retention and admin baseline minimum sample need governance review.
