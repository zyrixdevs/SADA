# Configuration and Admin Controls

## Participation is explicit

Installing Zyrix does not enable SADA. Guild owners or administrators must opt into each distinct capability. Recommended independent controls are:

| Setting | Default | Effect |
|---|---|---|
| Submit approved moderation incidents | Off | Sends selected structured events to SADA |
| Receive intelligence summaries | Off | Allows bot to request relevant case signals |
| Deliver local SADA alerts | Off | Sends eligible alerts to a configured private staff destination |
| Permit local Ban User alert action | Off | Enables the alert's local ban control, subject to fresh checks |
| Participate in global enforcement | Off | Allows approved global decisions to be applied locally under the selected policy |

Whether intelligence-only participation can be offered without incident submission is an **OPEN DECISION**. Do not bundle these permissions into one broad “Enable SADA” switch.

## Admin actions

A future admin interface should support viewing the data shared, enabling/disabling each capability, selecting a private alert channel, pausing participation, leaving the network, and reviewing local alert outcomes. It should show when settings take effect and explain what happens to existing records. No dashboard or command is implemented by this document.

## Safe change semantics

- Require a current guild owner/admin permission check for setting changes.
- Persist settings transactionally and audit actor, old/new values, and time.
- Disabling event submission stops new submissions; it does not silently rewrite prior records.
- Pausing alerts suppresses future delivery but does not delete existing case records.
- Leaving the network disables future participation and enforcement signals. Treatment of retained data and pending enforcement is policy-defined and an **OPEN DECISION**.
- A removed bot or unavailable guild is marked unavailable, not opted in or enforcement-successful.

## Threshold configuration

Potential settings include minimum independent source guild count, severity/category weighting, evidence quality requirements, recency windows, and case alert cooldown. Proposed initial ideas of five servers and a 5,000-member population condition are not finalized. Define precisely whether 5,000 means each source guild, target guild, aggregate population, or another measure before configuration is exposed. Both are **OPEN DECISIONS**.

## Central operations controls

Global operators need separate controls for reviewer membership, credential revocation, server suspension, queue pause, and global enforcement circuit breaker. These must not grant Discord moderation access to SADA. Emergency shutdown should stop new SADA signals while leaving Zyrix's ordinary moderation and AntiNuke functioning.

## Configuration example (illustrative only)

```yaml
sada:
  incident_submission: false
  intelligence: false
  alerts: false
  local_alert_ban: false
  global_enforcement: false
  alert_channel_id: null
```

This is a design example, not a current Zyrix configuration schema. Secrets and service credentials must be stored outside ordinary guild configuration.
