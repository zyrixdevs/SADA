# 02 — Rust core architecture

No Rust workspace exists. Start as one modular monolith with identity/consent, ingestion, incident/evidence, analysis, case, review/appeal, distribution, audit and operations modules. Split only on measured security/scaling need.

Layers: HTTP auth/schema/limits; application authorization/transaction; pure domain state; PostgreSQL repositories; bounded leased workers; clock/secret/object-store adapters. Reject unknown critical enums. Commit inbox before acknowledge; commit domain, audit and outbox together; network calls after commit. Use revision checks for concurrent review. Library/crate choices remain open.

## Runtime limits

Apply request deadlines, SQL statement timeouts, bounded worker batches, lease expiry, and per-tenant concurrency caps. Domain functions should be deterministic and free of network I/O so policy versions can be replayed against fixtures. Keep migration execution as an explicit deployment step with a compatibility check, not a background API startup side effect.
