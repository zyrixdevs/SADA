# 04 — Service communication

Initial transport: HTTPS intake and cursor polling over PostgreSQL outbox. Proposed operations: POST /v1/events; GET /v1/installations/{id}/deliveries?cursor=...; POST /v1/deliveries/{id}/ack; GET /v1/cases/{id}; POST /v1/enforcement-receipts. Envelope includes schema/event IDs, type, authenticated installation, authorized guild, occurred/observed times, consent version, bounded payload, correlation and idempotency keys. Durable commit before success. Same key/body returns same receipt; changed body conflicts. TLS and scoped credentials with replay control. At-least-once, not exactly-once. No bot token or raw private messages.

## Contract compatibility

Each endpoint declares accepted schema versions, required scope, body cap, idempotency behavior, and retry class. Clients reject unknown major response versions and retain the request ID for support. Cursor tokens bind installation, query filter, and schema revision; clients cannot alter them to broaden the result set.
