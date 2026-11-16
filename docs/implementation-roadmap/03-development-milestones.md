# 03 — Development milestones

M0 owners/policy. M1 event/evidence/case/error/audit contracts. M2 migrations, inbox/outbox, encryption, restore. M3 identity/consent/revocation. M4 adapter/outage isolation. M5 incident/timeline/correction/appeal. M6 first bounded read-only feature. M7 indicators/network/fingerprint/campaign/trust. M8 raid/admin/simulation. M9 controlled playbook/recovery. M10 API/observatory. Every milestone requires acceptance tests, migration proof, threat-model update, runbook, retention behavior, rollback and no unresolved critical finding.

## Milestone evidence

Each milestone records the contract revision, migrations, feature flags, owning team, rollout cohorts, rollback, and operational owner. Keep acceptance evidence attached to the milestone: CI run, database restore log, threat-model review, and signed policy decision. A milestone may be paused without enabling dependent features. Use backward-compatible expand/migrate/contract database changes and verify the old binary can read during rollout.
