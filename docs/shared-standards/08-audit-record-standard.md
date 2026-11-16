# 08 — Audit record standard

Fields: audit_id, occurred_at, recorded_at, actor type/id, action, object type/id/revision, request/correlation ID, policy, outcome, reason code, minimal before/after. Cover consent, evidence access, votes, approval/reversal, appeals, delivery, local receipts, retention and overrides. No secrets/private content/full evidence. Application role cannot mutate/delete; correction appends. Access restricted; tamper evidence/retention open.

## Integrity and query rules

Audit writes share the transaction with the state change they describe; if the audit insert fails, the state change rolls back. Index by object/time and actor/time, but apply the same authorization rules to audit search as to the source object. Periodically verify row counts and backup restore. Never expose internal actor identifiers to a tenant that cannot see the underlying action.
