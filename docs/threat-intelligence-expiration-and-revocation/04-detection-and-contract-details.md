# 04 — Detection and contract details: Threat Intelligence Expiration and Revocation

## Inputs and normalization

Indicator/revision refs; source validity; evidence status; expiry policy; correction/reversal event; downstream pending deliveries.

Validate identifiers, source authorization, event/schema version, UTC timestamps, bounded collections and allowed enum values. Normalize only fields whose semantics are defined; preserve source values by opaque reference when needed. Record the normalizer/ruleset version and do not store secrets or unrelated content.

## Proposed analysis

Lifecycle state is active, stale, expired, disputed, revoked or superseded; no state is overwritten without revision. Expiry differs from retraction; consumers receive idempotent revision notifications.

The assessment record should expose: proposition; source/event/evidence references; observed and received times; included/excluded inputs with reason; independent-source count where applicable; missing/unknown fields; factor-level results; policy/algorithm version; reviewer state; expiry and correction links. Scores are uncalibrated prioritization unless a separate evaluation and calibration decision is approved. No accuracy claim is made.

## API/event integration

**Method:** `POST`. **Version:** `/v1`. This is an internal intake contract, not a public endpoint commitment.

`POST /v1/intelligence/{id}/revisions` is an internal v1 operation protected by the shared service identity and guild-scoped grants. The authenticated principal supplies `Idempotency-Key`; the server binds the guild, verifies current capability, validates body size and schema, and records request/correlation IDs. Responses use the [shared API error contract](../shared-standards/06-api-error-standard.md). The intake commits before returning `202`; client retries reuse the same key. `409` signals key/body or revision conflict; `410` signals expired/revoked resource; `429` includes bounded retry guidance.

Canonical event fields and delivery rules are defined by [event schema](../shared-standards/01-event-schema-standard.md) and [idempotency standard](../shared-standards/07-idempotency-and-delivery-standard.md); this feature adds only its typed payload and does not introduce an alternate API convention.

## Failure behavior

Reject malformed, unauthorized or unsupported critical fields without retry. Retry transient database/object-store/provider failures only when no durable receipt exists. After commit, return the same receipt on retry. Dead-letter repeatedly failing poison events with a safe code. Reconcile any uncertain downstream receipt before delivery retry.
