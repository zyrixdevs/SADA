# 01 — Overview and objectives: Secure Build and Release Verification

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Define verifiable build provenance, SBOM publication and signed release artifact checks.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Source revision; build workflow identity; builder environment; artifact digest; SBOM; signing identity; attestation result.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. A signature proves control of a key, not source safety; compromised build identity can produce signed malicious artifacts.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Attestation format, signer trust root and whether builds must be reproducible require decision.
