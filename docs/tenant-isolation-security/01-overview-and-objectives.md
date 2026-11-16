# 01 — Overview and objectives: Tenant Isolation Security

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Specify and continuously verify strict guild and installation data boundaries across APIs, workers, evidence, search and exports.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Authenticated installation scope; authorized guild grants; query predicates; row ownership; evidence object ACL; reviewer role scope.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Global reviewer access is purpose-bound and not equivalent to unrestricted tenant access; operators use break-glass audited access.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

RLS approach, operator break-glass quorum and aggregate cohort floor need architecture/security approval.
