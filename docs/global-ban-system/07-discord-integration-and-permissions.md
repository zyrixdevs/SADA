# Discord Integration and Permissions

This chapter defines how the future SADA service integrates with Discord through Zyrix Bot. SADA itself has no Discord token and cannot invoke Discord moderation endpoints.

## Existing integration points

The current workspace is a Python bot under `bot/`, not the standalone repository layout referenced in earlier planning. Relevant verified source includes:

- `bot/cogs/moderation/ban.py`, `kick.py`, and `timeout.py`: local moderation command handlers.
- `bot/cogs/moderation/warn.py`: stores only a per-guild/user warning count in `db/warn.db`; the moderation reason and actor are not kept as a detailed incident ledger.
- `bot/cogs/commands/logging.py`: sends event/audit information to configured channels; it is not durable case management.
- `bot/cogs/commands/owner2.py`: the owner-only `GB` flow currently iterates mutual guilds and calls `guild.ban`; it has no SADA opt-in or durable per-guild result ledger. It must not be treated as an implementation of the proposed approval flow.
- `bot/cogs/antinuke/`: local AntiNuke event handlers. Their existing response path must remain independent of SADA.
- `bot/cogs/__init__.py`: explicit cog registration; any future adapter needs deliberate registration.

These are integration candidates, not approved modification instructions. SADA implementation requires a later scoped approval and migration plan.

## Authority boundaries

| Actor | May do | Must not do |
|---|---|---|
| SADA Core | Correlate accepted events, open cases, make recommendations, publish approved decision signals | Call Discord APIs, ban/kick/timeout members, change a server's settings |
| Zyrix Bot adapter | Authenticate service traffic, verify guild/user context, submit events, retrieve signals | Trust a SADA action request without local checks |
| Guild moderator | Decide whether to make a local ban from an alert when locally authorized | Approve a global ban unless separately granted global reviewer authority |
| Global reviewer | Approve/reject a global case under global policy | Force enforcement in a guild that opted out |
| Guild owner/admin | Configure that guild's SADA participation and local policy | Alter records belonging to another guild |

## Local ban permission checks

For the **Ban User** button, Zyrix Bot must validate all of the following at click time, not merely when the alert was sent:

1. The interaction is authentic and the component belongs to an active alert/case for this guild.
2. The alert has not expired, been superseded, or already received a terminal local decision.
3. The target is currently a member of the interaction's guild. A cached member lookup is insufficient when stale; fetch when appropriate and handle `NotFound` as a safe skip.
4. The actor is still a member and has the configured local permission (recommend `Ban Members` or a locally configured moderation role with equivalent bot-enforced authority). Do not infer permission from button visibility.
5. The bot has `Ban Members` in that guild.
6. Discord role hierarchy and target constraints permit the action. Treat Discord's response as authoritative and record a failure if rejected.
7. Local SADA policy is enabled for alerts and the action is explicitly local. The operation cannot change global status.
8. An idempotency/decision record is claimed transactionally before or around the call so duplicate interaction delivery cannot cause duplicate case transitions.

Record the actor, guild, target, case, decision time, reason/reference, interaction outcome, and Discord result code. Do not include private message content or tokens.

## Global reviewer permissions

Global reviewers are a separate, centrally managed role set. Guild `Administrator` does not grant global reviewer status. Authorization must be checked server-side on every review action, with revocation taking effect promptly. A reviewer must see the evidence summary and status before approving. Any proposed quorum is an **OPEN DECISION**; until decided, implementation should require an explicit safe policy rather than silently assuming one-person approval.

## Interaction component controls

Each alert exposes exactly two primary controls: **Ban User** and **Ignore**. Component identifiers should contain opaque case/alert references, not trusted guild, user, permission, or decision data. On every click, load authoritative records and compare their guild/target binding with the Discord interaction context. Expired controls return a neutral explanation and do not mutate records.

Discord interaction tokens and webhook URLs are secrets. Do not log them or persist them beyond Discord's documented need. Defer interactions when work could exceed the acknowledgement deadline, then edit/respond with the result. If the bot cannot acknowledge or complete an operation, preserve a retryable failure state without claiming success.

## Guild isolation

An alert record is scoped to exactly one guild. Every query and update must include guild ID and alert ID; client-provided IDs alone are never authority. Cross-guild incident summaries should reveal only the approved fields described in [Security and Abuse Prevention](09-security-and-abuse-prevention.md). A guild must not be able to enumerate another guild's settings or private evidence.

## Existing behavior compatibility

The existing owner-only `GB` command is broad mutual-guild enforcement. SADA must not silently route to it, expand its authority, or represent it as a SADA global ban. A future migration must define whether that legacy command is retired, narrowed, or retained as a separate owner tool, with explicit review logging and user-facing behavior. This is an **OPEN DECISION** and code change is outside this documentation task.
