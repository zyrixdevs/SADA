# 01 — Overview and objectives: AI Security and Prompt Injection Protection

**Status: proposed.** The repository documents no operational implementation. This module addresses the following problem: Constrain optional AI summarization/classification over untrusted evidence and preserve deterministic, human-led decisions.

## Threat scenarios and objectives

Threat scenarios include a malicious or compromised source submitting fabricated observations; an attacker exploiting incomplete attribution; stale intelligence being treated as current; and a consumer widening access beyond the originating guild. Objectives are to preserve provenance, minimize collection, expose uncertainty, enable correction, and produce reviewable findings with an owner and expiry.

**In scope:** Untrusted evidence refs; sanitized extracted text; task template/version; model/provider metadata; tool allowlist; reviewer output.

**Out of scope:** Discord moderation calls, independent identities/cases/evidence/audit, broad private conversation collection, and unreviewed cross-guild enforcement.

## Outputs and limits

The output is a versioned domain observation or finding linked to canonical event/incident/evidence references. It is not a verdict. Prompt filters cannot guarantee injection detection; external model providers may retain data; do not send private content without explicit policy/contract.

Success criteria are qualitative and testable: inputs are scoped and deduplicated; outputs name evidence, exclusions and version; corrections invalidate pending stale delivery; guild-level data remains isolated; operators can disable the feature without affecting local Zyrix moderation.

## Decisions

Model/provider, data processing terms, retention, evaluation corpus and permitted tasks require legal/security review.
