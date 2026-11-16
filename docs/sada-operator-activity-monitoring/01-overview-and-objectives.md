# 01 — Overview and objectives: SADA Operator Activity Monitoring

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Record and review sensitive operator access and platform administration using the canonical audit ledger.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Operator principal; privileged command/API; database role/session metadata; change request/approval refs; outcome and request ID.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. DB superuser/provider access may bypass application audit; supplement with infrastructure logs and independent review.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Operator identities, critical action list, audit retention and independent reviewer require named owners.
