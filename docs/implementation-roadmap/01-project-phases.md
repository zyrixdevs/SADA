# 01 — Project phases

0 Governance: consent, retention, appeals, owners; gate reviewed policy.

1 Contracts/foundation: schemas, auth, migrations, inbox/outbox, audit, restore; synthetic event durably deduplicates without Discord credential.

2 Adapter/case: explicit consent, durable local outbox, incident/timeline/correction/appeal; outages leave local protection unchanged.

3 Reviewable intelligence: trust, Global Ban candidate, indicators, graph, fingerprints, campaigns; no score enforcement.

4 Detection/simulation: raid/admin/health and isolated simulations; adversarial/false-positive review.

5 Response/recovery: playbook, impact, owner-approved recovery; simulator cannot mutate; adapter checks live Discord permissions.

6 Sensitive/public: ban evasion, partner API, observatory only after legal/privacy and aggregation tests.
