# 01 — Overview and objectives: Malicious File Campaign Correlation

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Group related attachment observations into expiring, explainable malware campaign candidates.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Exact file hashes; safe metadata; scanner/advisory provenance; time buckets; reviewed attachment observations.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. No fuzzy identity claims from filenames alone; hash collision and repackaging limitations are visible; no automatic file deletion.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Hash algorithms and cross-server visibility tiers need decision.
