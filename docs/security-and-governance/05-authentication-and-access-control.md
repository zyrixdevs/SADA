# 05 — Authentication and access control

Guild admins manage own guild only; reviewers assigned centrally; operators lack implicit decision authority. Authorize every object/field, recheck at decision, deny on unknown scope. Use MFA/step-up where supported, session expiry, rapid revocation, periodic access review, audited break glass and dual control for sensitive changes.

## Access review

Maintain a machine-readable scope inventory and review it periodically. Revoke a compromised installation before reissuing credentials; rotate key IDs and invalidate active sessions. Reviewer role changes invalidate cached authorization promptly. Queries must bind tenant scope in the repository layer, not only in UI filtering. Log denied sensitive reads without revealing another tenant’s object existence.
