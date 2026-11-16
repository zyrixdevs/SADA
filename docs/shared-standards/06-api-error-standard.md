# 06 — API error standard

{
  "error":{"code":"consent.inactive","message":"This installation is not authorized for this operation.","retryable":false,"request_id":"req-opaque","details":{}}
}

Do not reveal other-tenant object existence. Details are safe field paths/retry data, never secrets. Suggested statuses: 400 malformed, 401 unauthenticated, 403 scope, 404 concealed/not found, 409 idempotency/revision, 410 expired/revoked, 413 oversized, 422 policy/schema, 429 limited, 5xx temporary. Version and test mapping. Retry only when retryable and idempotent.

## Error behavior examples

A duplicate request with the same key and body returns the saved receipt; a changed body returns 409. A revoked installation returns a non-retryable authorization error. A temporarily unavailable database returns 503 only when no durable acceptance was committed. If acceptance committed but response delivery failed, the client retries with the same key and receives the original receipt.
