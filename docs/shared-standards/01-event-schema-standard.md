# 01 — Event schema standard

Proposed v1 fields: schema_version, event_id, event_type, authenticated installation_id, authorized source_guild_id, occurred_at, observed_at, consent_version, source, optional minimal subject, bounded typed payload, correlation_id, idempotency_key. Server sets received_at/processed_at/request_id.

Example:
{
  "schema_version":"1.0",
  "event_id":"018f0000-0000-7000-8000-000000000001",
  "event_type":"moderation.action.confirmed",
  "installation_id":"018f0000-0000-7000-8000-000000000002",
  "source_guild_id":"123456789012345678",
  "occurred_at":"2026-11-16T10:00:00Z",
  "observed_at":"2026-11-16T10:00:01Z",
  "consent_version":"guild-consent-7",
  "source":{"component":"zyrix.moderation","attribution":"actor-confirmed"},
  "subject":{"discord_user_id":"234567890123456789"},
  "payload":{"action":"ban","reason_ref":"evidence:opaque"},
  "correlation_id":null,
  "idempotency_key":"installation-event-opaque"
}

Reject unsupported major version, oversized body, time skew, unauthorized guild and unknown critical fields. Semantic change requires major version; golden fixtures required. Exclude private chat, token, webhook secret, IP/device. Confirmed action is emitted only after API success; uncertain AntiNuke is a separate signal event.
