# 06 — Event-driven processing

Validate identity/schema/consent/size/time/idempotency, commit inbox, then acknowledge. Bounded workers lease jobs, apply revision-checked transition, write audit/outbox transactionally, deliver after commit, record receipt. Expired leases recover; dead letters are visible. At-least-once with stable IDs; corrections are new linked events; global ordering is not assumed. Retry only transient failures with jitter; permanent auth/schema errors do not retry. Unknown Discord outcome is reconciled before retry.
## Worker concurrency

Claim work with short database transactions and leases; do not hold row locks while doing analysis or external I/O. Use per-aggregate revision checks and bounded retries. Poison events move to dead letter with a safe code and payload reference. Operator replay creates a new replay audit event but preserves the original receipt and event ID.
