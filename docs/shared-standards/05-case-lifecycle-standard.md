# 05 — Case lifecycle standard

Proposed candidate -> open -> in_review -> on_hold/approved/rejected -> reopened/revoked/closed. Immutable case_id, revision, scope, state, timestamps, policy version, evidence snapshot. Transitions compare-and-set and append actor/reason/request/audit. Source incidents are not mutated. Signals bind case and revision, expire, and stale versions reject.
## Transition checks

Every transition validates current revision, actor scope, allowed prior state, appeal hold, evidence snapshot, and policy version inside one transaction. Rejection and approval require a reason. Reversal cancels pending outbound work before another worker can claim it. Reopen requires material new evidence or a documented correction and links the prior closed revision.
