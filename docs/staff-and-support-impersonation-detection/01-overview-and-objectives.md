# 01 — Overview and objectives: Staff and Support Impersonation Detection

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Help identify accounts falsely claiming to be a server or SADA support authority.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Guild-authorized staff reference list; message/report context explicitly submitted; role metadata; account display/name changes; verified support channel/domain references.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Do not continuously monitor private messages or expose staff rosters cross-server.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Whether an opted-in guild may submit message excerpts needs privacy/legal review.
