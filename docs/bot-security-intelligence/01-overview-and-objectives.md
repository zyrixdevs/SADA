# 01 — Overview and objectives: Bot Security Intelligence

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Share reviewed, provenance-bearing intelligence about bot identities, service compromise and abuse across opted-in guilds. It specializes the bot/integration domain on the existing Threat Intelligence Network graph.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Bot application ID; installation-scoped bot identity; permitted moderation/audit events; report and advisory references; source reliability snapshot.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. A shared bot name/avatar is not identity; public bot listings and a single report are not proof. Discord metadata may be unavailable or stale.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Identity keying across application ID, guild install and publisher needs review.
