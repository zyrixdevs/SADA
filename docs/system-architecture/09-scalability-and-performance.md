# 09 — Scalability and performance

Start one independent Rust API/worker and PostgreSQL queue. Bound request, concurrency, graph depth, page and tenant rate. Add worker pools, NATS, Redis, replicas or partitioning only after measured need. Redis is never source of truth. Use tenant fairness quotas, scoped indexes, asynchronous expensive analysis, explicit 429/503 backpressure. Load-test synthetic bursts, hot target, slow DB and skewed tenants. No performance target claimed.
## Capacity evaluation

Benchmark realistic guild-size distributions, sparse and dense graph components, duplicate bursts, and slow evidence storage. Report per-tenant latency and queue fairness rather than only aggregate throughput. Tune indexes from observed query plans. Do not introduce NATS, Redis, sharding, or partitioning until an explicit trigger and operations owner are recorded.
