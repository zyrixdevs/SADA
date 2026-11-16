# 05 — Global ban and local enforcement

## Three separate decisions

### 1. Local ban
A guild's authorized moderator independently bans a member under that guild's rules. The ban affects one guild. SADA may receive a structured event only if the guild opted into incident sharing and the event meets the configured provenance requirements. A local ban alone is not a global finding.

### 2. SADA suspicious flag
SADA Core correlates evidence and suggests that reviewers or eligible guild staff examine a case. This flag is not a punishment, does not modify a Discord ban list, and must not be described as a global ban.

### 3. Global ban decision
Authorized Zyrix global reviewers approve a cross-server enforcement decision under a documented policy and evidence snapshot. Each participating guild's bot independently decides whether it is eligible and able to apply a local ban. Discord has no API call that bans a user from every unrelated server.

## Global review and approval

1. A candidate enters a restricted reviewer queue only after policy gates are met.
2. Reviewers see exact original reasons (access-controlled), proposed normalized categories, source provenance, evidence quality, server reliability summary, disputes/reversals, appeals, exclusions, and the score-policy version.
3. A reviewer may approve, reject, request additional evidence, or put the case on hold. Every decision requires an explanation.
4. Store proposal and each review vote independently. A decision must bind to the case ID, evidence snapshot hash/version, policy version, reviewer IDs, time, and reasons.
5. **OPEN DECISION:** one reviewer or a quorum. Recommend two distinct reviewers, prohibit self-approval, and require a second review for high-impact or disputed cases.
6. Recheck that case has not been appealed/paused/reversed and reviewer authorization remains valid before emitting an approval event.
7. Publish an authenticated approved-decision signal with a unique decision ID. It is a signed case/policy status, not a command with arbitrary guild/user targets.

Rejection produces no enforcement tasks. A later review requires a new version or materially new evidence and preserves the rejected decision history.

## Global enforcement rollout

For each guild installation receiving the decision:

1. Verify signature, issuer, event ID, timestamp/replay window, case ID, target ID, decision status, evidence/policy version, and that the decision is not revoked.
2. Load current local settings. If that guild has not explicitly enabled global enforcement for the policy scope, record skipped_opt_out and stop.
3. Confirm the bot is in the guild and target membership is current. Unknown membership is not presence.
4. Check target is not guild owner and target's top role is below bot's highest role.
5. Check bot has BAN_MEMBERS. The decision signal does not grant permissions.
6. Check current ban state. If already banned, store already_banned; do not claim SADA created the action.
7. Write an idempotent enforcement intent keyed by decision+guild+policy version, then call Discord's guild-scoped ban API. Reconcile uncertain timeouts before retrying.
8. Persist confirmed success, skip, failure, unavailable, or unknown result. Do not aggregate until individual results are durable.
9. Return a signed outcome receipt to SADA. The receipt must not contain unrelated member information.

The central result may read “approved; 12 succeeded, 4 opted out, 2 unavailable, 1 permission failure.” It may not state universal success when any required target guild did not enforce.

## Local alert Ban User

The local button follows a separate path from global rollout. On click, Zyrix Bot validates alert origin/guild/message, current case and alert status, current moderator permission, target still-member state, bot Ban Members permission, role hierarchy, guild owner protection, policy opt-in, and duplicate decision key. It then calls the guild-local ban once. A stale, unauthorized, removed-member or hierarchy-invalid action is rejected and recorded. It does not send an approval to global reviewers.

## Existing owner-only command conflict

The current bot/cogs/commands/owner2.py global GB command gathers mutual guilds from the cache, asks the command author for a yes/no confirmation, and iterates direct guild.ban calls. It has no SADA opt-in, case/evidence snapshot, durable approval ledger, quorum, per-guild durable outcome rows, or appeal/reversal model. It should remain outside this proposed SADA flow. Any change to, disablement of, or migration from that existing command requires a separate code task and compatibility review; this document does not modify it.

## Enforcement states

Use distinct per-guild statuses: queued, skipped_opt_out, skipped_bot_absent, skipped_target_absent, skipped_membership_unknown, skipped_already_banned, skipped_permission, skipped_hierarchy, succeeded, failed_forbidden, failed_rate_limited, failed_api, outcome_unknown, reversal_pending, reversed, reversal_failed. A compact implementation may group codes but must preserve success versus skip versus failure versus unknown. Do not rely on one global_banned boolean.
