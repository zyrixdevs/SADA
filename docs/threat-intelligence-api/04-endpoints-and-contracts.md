# 04 — Endpoints and contracts

**Status: proposed v1 API; no server is implemented.** All routes use HTTPS, authenticated installation/reviewer identities, tenant authorization, bounded bodies/pages, request IDs, and the shared error envelope.

## Installation-facing routes

| Method and route | Scope | Idempotency / result |
|---|---|---|
| POST /v1/events | Active installation and guild submission consent | Idempotency-Key; 202 only after inbox commit |
| GET /v1/installations/{installation_id}/deliveries?cursor=. | Own installation and eligible delivery types | Scope-bound cursor; bounded page |
| POST /v1/deliveries/{delivery_id}/ack | Delivery recipient installation | Stable delivery ID; repeated ack returns same result |
| GET /v1/cases/{case_id} | Only fields allowed to installation/guild or reviewer | Revision returned; hidden cross-tenant objects return 404 |
| GET /v1/indicators/{indicator_id} | Approved indicator scopes only | Includes freshness, status, correction revision |
| GET /v1/advisories?cursor=. | Explicit subscription scope | Deduplicated delivery sequence |
| GET /v1/campaigns/{campaign_id} | Approved campaign summary only | No raw evidence by default |
| POST /v1/enforcement-receipts | Authenticated Zyrix installation and guild | Unique decision+guild; outcome is success/skip/failure/unknown |

Reviewer-only routes are separate scopes: POST /v1/cases/{case_id}/reviews, POST /v1/reviews/{review_id}/votes, POST /v1/appeals/{appeal_id}/resolution. They require fresh reviewer authorization, expected case revision, reason, policy version, and audit. Guild administrators cannot call global reviewer operations.

## Request example: event intake

{
  "schema_version":"1.0",
  "event_id":"018f0000-0000-7000-8000-000000000001",
  "event_type":"moderation.action.confirmed",
  "installation_id":"018f0000-0000-7000-8000-000000000002",
  "source_guild_id":"123456789012345678",
  "occurred_at":"2026-11-16T10:00:00Z",
  "observed_at":"2026-11-16T10:00:01Z",
  "consent_version":"guild-consent-7",
  "correlation_id":null,
  "idempotency_key":"installation-event-opaque",
  "payload":{"action":"ban","subject_user_id":"234567890123456789","evidence_refs":[]}
}

Send Idempotency-Key as an HTTP header with the stable value matching the envelope. The authenticated installation identity is bound to the request; body installation ID cannot override it. The source guild must be in the active consent scope.

## Response example

{
  "data":{"receipt_id":"018f0000-0000-7000-8000-000000000003","event_id":"018f0000-0000-7000-8000-000000000001","status":"accepted","deduplicated":false},
  "request_id":"req-opaque"
}

Acceptance means durable inbox commit, not case creation or approval. Replays return the original receipt with deduplicated=true. Same key and different body returns 409.

## Errors, limits, and versioning

Use the common error envelope from the shared standard. Enforce per-installation and per-route quotas, body limits, cursor limits, and burst controls; exact values are open operational settings. 429 includes retry guidance. Retry only transient errors when idempotent. API major version is in path; schema version is explicit in payload. Deprecation requires published overlap and migration window. Raw reasons/evidence require separate field scope and never appear in URLs.
