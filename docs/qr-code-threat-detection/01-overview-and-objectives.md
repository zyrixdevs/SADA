# 01 — Overview and objectives: QR Code Threat Detection

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Extract and assess URLs from authorized QR image evidence without treating decoded destinations as safe.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Image evidence reference; bounded image metadata; decoded URL; OCR/decoder version; URL/domain reputation reference.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. QR decode can fail or yield multiple/obfuscated links; no browser execution; do not retain image after evidence policy expiry.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Image formats and whether to retain extracted full URL require review.
