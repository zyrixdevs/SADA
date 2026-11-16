# 07 — Idempotency and delivery standard

Intake key is scoped by installation/operation. Same canonical body returns receipt; changed body conflicts. Retain dedupe through retry horizon (duration open). Commit inbox before acknowledge. Delivery is at-least-once with stable ID, revision, expiry, recipient scope; consumer ack idempotently. Bounded jitter for transient errors; permanent errors dead-letter. Replay requires operator auth, renewed consent/expiry check and audit. Ambiguous Discord outcome is reconciled. Exactly-once is not claimed.

## Outbox state transitions

Use pending, leased, delivered, retry_wait, dead_letter, cancelled, and expired states with compare-and-set transitions. Lease expiry permits recovery by another worker, while a stable delivery ID prevents duplicate logical effects. Cancel when consent is revoked, the aggregate revision is superseded, or expiry passes. Keep a safe reason code and attempt timestamps for reconciliation.
