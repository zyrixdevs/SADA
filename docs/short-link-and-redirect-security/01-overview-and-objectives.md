# 01 — Overview and objectives: Short Link and Redirect Security

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Resolve URL redirect chains in an isolated service and identify deceptive destination transitions.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Submitted URL; DNS/HTTP redirect observations; TLS/domain metadata; scanner egress policy; domain reputation refs.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Live resolution is time-dependent and may expose the scanner to malicious content; no page scripts, downloads, credentials or browser session.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Resolver infrastructure, data residency and submitted URL retention need security review.
