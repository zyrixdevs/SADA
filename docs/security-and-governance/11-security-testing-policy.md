# 11 — Security testing policy

Test tenant isolation, auth/signatures/replay, idempotency, SQL constraints, evidence access, deletion, quorum, parser fuzzing, source poisoning, load/backpressure, restore/key rotation and response tabletop. Synthetic isolated staging only; no live moderation without scoped authorization. Track severity, owner, remediation and retest. Release needs review, threat model, restore proof and residual risk acceptance.

## Required security scenarios

Include credential replay after revocation, signature canonicalization differences, changed-body idempotency reuse, concurrent reviewer votes, cross-guild cursor reuse, object-key guessing, evidence expiry with a legal hold, and restore from a compromised-key rotation window. A release owner records results and accepted residual risk; a failing security gate blocks production enablement.
