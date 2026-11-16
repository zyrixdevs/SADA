# 04 — Testing and release strategy

Layer unit/domain, disposable PostgreSQL, contract compatibility, fake Discord, tenant/auth, adversarial/false-positive, load/backpressure, restore/key rotation, tabletop. Stage synthetic local -> isolated staging -> invited opted-in guilds with reversible low-risk features -> limited intelligence -> separately reviewed high-impact. Each gate has feature flag, kill switch, telemetry, owner, rollback and notice. No global enforcement until quorum, appeals, reversals, live bot checks, partial receipts and circuit breaker pass. No unmeasured accuracy claims.
## Release decision record

For each cohort, record enabled guild count, event types, data fields, retention class, failure rate, correction path, rollback trigger, and approver. Canary only low-impact read-only outputs first. Halt rollout for tenant leakage, unexplained score change, delivery duplication, missing audit rows, or local-action mismatch. Rollback disables the feature flag and pending signal outbox; it does not erase audit or accepted source records.
