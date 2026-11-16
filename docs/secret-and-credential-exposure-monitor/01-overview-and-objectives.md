# 01 — Overview and objectives: Secret and Credential Exposure Monitor

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Find accidentally committed or logged credentials and coordinate safe revocation/rotation.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** CI secret scanner finding; repository/commit metadata; config inventory keys (names only); log-pattern alert; credential provider revocation status.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Scanning repository does not prove secret remains valid; rotation requires provider-specific owner action and cannot be automated without explicit approved capability.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Repository scope, secret detector, notification route and response SLA need owner assignment.
