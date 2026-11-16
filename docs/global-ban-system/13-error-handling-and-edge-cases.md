# Error Handling and Edge Cases

Fail closed for SADA decisions and fail independently for ordinary local moderation: uncertainty must never create an unapproved Discord action.

| Situation | Required behavior |
|---|---|
| Target leaves after alert | Ban action rechecks membership. Record skipped/not-member; no ban call and no global status change. |
| Target joins after case creation | Re-evaluate membership for that guild. Deliver only if opted in and alert policy allows; do not assume the old alert was delivered. |
| Bot offline | Durable outbox/retry may deliver later if alert is still valid. Expired or superseded alerts are not replayed. Ordinary Discord commands resume independently. |
| Bot lacks Ban Members or role is too low | Show a safe failure, record the categorized result, and do not claim success. |
| Server disables SADA | Stop new data sharing/alerts/signals according to each switch. Do not silently erase prior records; apply approved exit policy. |
| Server leaves network | Revoke installation scope, stop future signals, mark pending operations unavailable, and apply the approved data-retention policy. |
| Bot removed | Revoke/expire installation credentials and mark enforcement unavailable, not skipped-success. |
| Central database unavailable | SADA ingestion returns retryable failure or queues only if a durable local outbox exists. No false success response. Zyrix local moderation and AntiNuke continue. |
| Discord API failure | Record per-guild failure category and retry only safe transient failures with idempotency. Permission/unknown target errors are not blindly retried. |
| Duplicate event delivery | Unique idempotency key returns the existing result; do not double count. |
| Moderator changes local decision | Append a new local decision event with actor/time. Do not rewrite the original alert history. |
| Global approval reversed | Cancel pending retries, recompute case, notify affected guilds; do not automatically unban members. |
| Alert ignored then new evidence arrives | New material case revision may reopen alert eligibility under configured policy; same revision remains suppressed. |
| Membership fetch times out | Mark membership unknown and defer/skip action; do not assume the user is present. |
| Reviewer service failure | No global approval is created. Preserve draft/retry state and show unavailable. |
| Malformed or oversized event | Reject with safe validation error and audit source/request metadata without logging secret or full payload. |

## Retry rules

Retry only idempotent submissions and transient delivery failures with bounded exponential backoff and jitter. Use an outbox or durable queue before acknowledging an event as accepted. Dead-letter after a configured limit, surface the reason to operators, and allow safe replay after correction. Never retry a Discord ban if the outcome is unknown without first checking current guild membership/ban state and applying an idempotent reconciliation policy.

## Health states

Expose liveness separately from readiness. Readiness should include required database connectivity and event-processing capability. If SADA is degraded, Zyrix should mark only the SADA integration unavailable; the bot's own health and local protection should not be represented as failed solely because SADA is offline. Avoid health output containing secrets, guild lists, or user IDs.
