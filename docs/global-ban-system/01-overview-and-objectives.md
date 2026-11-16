# 01 — Overview and objectives

## Product intent

SADA means **Suspicious Activity Detection Algorithm**. It is proposed as an independent service that accepts explicitly shared security events from opted-in Zyrix Bot servers, correlates evidence, and gives humans actionable, explainable information. The Global Ban System is the first major feature, not an automatic punishment engine.

SADA should increase awareness of repeated cross-server behavior while respecting each community's authority. A guild can use Zyrix Bot and its existing local moderation without joining SADA. A guild that joins can choose what it shares, what it receives, whether local SADA alerts are enabled, and separately whether approved global decisions may be enforced there.

## Objectives

- Make adoption transparent and opt-in at each data-sharing/enforcement boundary.
- Preserve the source moderator's original punishment reason exactly as provided, subject to safe length/secret filtering and access controls.
- Keep the normalized reason category, supporting evidence, evidence quality, and reviewer outcome as separate fields.
- Distinguish evidence that an action occurred from a claim that the target is guilty or dangerous.
- Identify repeated, relevant, well-supported activity across independent servers; discount unrelated reasons and unreliable sources.
- Notify only participating guilds where the target currently belongs, without mass-DMing owners/admins.
- Offer each recipient guild a local Ban User or Ignore decision.
- Keep global approval separate from local action and ensure every guild outcome is independently recorded.
- Support appeals, corrections, reversals, source reliability review, and operational recovery.
- Keep existing bot commands, local permission gates, and AntiNuke behavior independent of SADA uptime.

## Non-goals for the first release

- Score-triggered, automatic, or silent bans.
- Treating each local ban as a verified finding of wrongdoing.
- Sharing every moderation log or every member event from an installed bot by default.
- Replacing AutoMod, AntiNuke, the Logging cog, Discord's own moderation/reporting tools, or local staff policy.
- Sending SADA's Rust service a Discord bot token or permission to call Discord.
- Automatically expanding enforcement to servers that opted into intelligence but not enforcement.
- AI-only classification or review, public searchable ban lists, or public accusation channels.

## Three concepts that must not be conflated

| Concept | Meaning | Who decides / effect |
|---|---|---|
| Local ban | A server independently bans a user under its own policy. | Local authorized moderators; affects that guild only. |
| SADA suspicious flag | A cross-server evidence pattern merits human attention. | SADA Core computes a recommendation; does not change Discord state. |
| Global ban decision | Authorized Zyrix global reviewers approve a cross-server enforcement decision under a policy version. | Global reviewer workflow; actual attempts still require each guild's explicit enforcement opt-in and bot-side checks. |

A user can be locally banned in one server without a SADA case, flagged by SADA without being globally banned, globally approved but not enforceable in opted-out servers, or partially enforced across a participating subset.

## Evidence vocabulary

- **Verified:** the occurrence and provenance passed a defined validation rule, such as a successful Zyrix moderation callback or strongly correlated Discord audit entry. It does not verify the moderator's motive or the target's guilt.
- **Reviewed:** an authorized human reviewed the reason/evidence and recorded an interpretation. Review may support, question, or reject a category; it is not a verdict unless an explicit policy says otherwise.
- **Unverified:** a report or observation lacks enough provenance to count as a confirmed action. It may be retained for triage but must not drive a global ban.
- **Disputed:** the source action, identity, reason, category, or context is contested and awaits resolution. It should not be silently counted as reliable supporting evidence.
- **Reversed:** a prior action or finding has been withdrawn/overturned by an authorized correction or appeal. Preserve its audit history but exclude it from active support as policy defines.

These statuses track evidence lifecycle. The separately stored reason-category review status and global reviewer decision avoid turning “verified event” into “verified allegation.”

## Trust and data-sharing contract

Before enabling any SADA feature, a guild administrator must see a plain-language disclosure describing each event field, destination, retention, reviewer access, and enforcement effect. Separate toggles should govern incident sharing, intelligence receipt, local alert delivery, and global enforcement. New installations start with every SADA toggle off. Pausing or leaving stops new transmissions and future enforcement; handling previously submitted records follows the approved retention/correction policy and must be explained at opt-in.

## Current versus proposed

**Current code:** bot/ is a Python discord.py bot with explicit cog registration and an optional FastAPI server. Moderation is mostly direct callbacks; warn stores only a guild/user count. Logging creates configured guild messages after events but does not persist a structured case ledger. AntiNuke processes local Discord events/audit logs and may perform local responses. owner2.py has an owner-only global GB flow that acts over mutual guilds after one confirmation and stores no durable SADA review/result ledger.

**Proposed SADA:** an independent Rust service and database receive only authorized structured events, classify reasons with provenance/uncertainty, correlate evidence across opted-in sources, manage cases/reviews/appeals, and send recommendations/approved decision signals. Zyrix Bot owns all Discord interactions and enforces local policies. See [independent engine architecture](../architecture/independent-sada-engine.md).

## Trust principles

1. Preserve source facts and original reason separately from inference.
2. Explain why a case was flagged, what evidence was excluded, and which policy version ran.
3. Require independent sources and category relevance; raw ban counts are inadequate.
4. Give source servers a correction path and a reliability review path.
5. Keep local moderator authority and global reviewer authority distinct.
6. Record global approval separately from each local enforcement result.
7. When in doubt, show uncertainty and ask for review instead of acting.
