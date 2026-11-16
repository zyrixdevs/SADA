# 01 — Overview and objectives: Moderation Audit Integrity Monitor

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Reconcile expected moderation/configuration events with available audit records and preserve tamper-evident local history.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Confirmed action receipts; Discord audit entry IDs; event times; actor attribution; source sequence/cursor; prior digest.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Discord audit access/retention/permissions may be incomplete; SADA cannot promise completeness or detect deletion before capture.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Digest anchoring and completeness expectations require operator/security review.
