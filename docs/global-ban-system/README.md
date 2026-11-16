# SADA Global Ban System — blueprint

**Status: proposed; documentation only.** No SADA service, schema, configuration, command, API, alert, or global-ban workflow exists in the current workspace's bot source.

SADA (Suspicious Activity Detection Algorithm) is intended to analyze cross-server security evidence for participating Zyrix Bot communities. The Global Ban System is its first major feature. SADA creates an explainable suspicious-activity signal and case for human review. It does not determine guilt and never bans from a score alone.

## Safety invariants

1. A server installation does not silently enable SADA. Incident sharing, intelligence receipt, local alerts, and enforcement opt-in are independent controls, disabled by default.
2. The source moderator's original reason is preserved. A normalized reason category is a separate, fallible classification with its own provenance and review state.
3. Evidence status is explicit: unverified, verified, reviewed, disputed, or reversed. Verified means the action/report provenance passed defined checks; it does not mean the moderator's conclusion is true.
4. Cross-server correlation requires distinct guilds and reason/evidence relevance. Four unrelated personal disputes are not equivalent to four well-supported phishing incidents.
5. A local ban is one guild's action. A SADA suspicious flag is a review signal. A global ban is a distinct authorized global decision. Never collapse these states.
6. Recipient guilds are alerted only if the target is confirmed to be a current member and the guild opted into alerts. The local alert has exactly two primary buttons: **Ban User** and **Ignore**.
7. Ban User can affect only the interaction guild and repeats current membership, moderator permission, bot permission, and hierarchy checks. Ignore is recorded for that guild and does not erase evidence or reject a global case.
8. SADA Core has no Discord token and cannot call Discord moderation APIs. Zyrix Bot independently validates every local action.
9. The structured database is authoritative; Discord channels and UI are projections. Partial enforcement is reported as partial.
10. SADA outage must never disable existing Zyrix moderation or AntiNuke.

## What current code does

The current workspace is a Python discord.py bot under bot/. Cogs are explicitly registered by bot/cogs/__init__.py. Local warn state in bot/cogs/moderation/warn.py is a count keyed by guild/user; it does not persist reason, moderator, timestamp, or case ID. Ban, kick, and timeout commands call Discord directly. The Logging cog in bot/cogs/commands/logging.py uses configured channels and Discord audit-log lookups to create human-readable guild logs; it is not a structured case database.

bot/cogs/commands/owner2.py contains an owner-only global GB command. It builds a cached list of mutual guilds, asks the command author to confirm, then attempts a ban in each mutual guild and reports names/counts in messages. It has no SADA opt-in, durable review record, distinct reviewer approval, or durable per-guild outcome ledger. It is not the proposed SADA workflow and is not a safe substitute for it.

AntiNuke exists separately under bot/cogs/antinuke/ and is registered from bot/cogs/__init__.py. It reads local enable/whitelist state from SQLite and handles Discord events using audit-log lookups. Some handlers immediately ban, kick, unban, or otherwise remediate locally. In particular, current bot/cogs/antinuke/antiprune.py uses the latest prune audit entry and can ban its executor; this path does not use the safer target-specific correlation helper described in the earlier standalone Phase 1 repository report. Do not assume the separate zyrix-main branch fixes are present in this monorepo checkout. A SADA integration must not delay or weaken this current local protection.

There is no SADA endpoint in the bot's embedded FastAPI service, no cross-server incident ledger, no general migration framework, and no central case ID implementation in the inspected moderation paths.

## Document index

| # | Document | Purpose |
|---|---|---|
| 01 | [Overview and objectives](01-overview-and-objectives.md) | Scope, trust promises, terminology, existing/proposed separation |
| 02 | [System architecture](02-system-architecture.md) | Components, data flow, independent engine boundary |
| 03 | [Feature workflow](03-feature-workflow.md) | Participation through appeal and closure |
| 04 | [Detection and scoring logic](04-detection-and-scoring-logic.md) | Reason-based detection, evidence, source reliability, open thresholds |
| 05 | [Global ban and local enforcement](05-global-ban-and-local-enforcement.md) | Local action, suspicious flag, global decision, guild-by-guild execution |
| 06 | [Database and data model](06-database-and-data-model.md) | Proposed PostgreSQL records, keys, constraints, indexes, retention |
| 07 | [Discord integration and permissions](07-discord-integration-and-permissions.md) | Permission matrix and bot-side enforcement checks |
| 08 | [Alerts and interactive controls](08-alerts-and-interactive-controls.md) | Member-only delivery and two-button local choice |
| 09 | [Security and abuse prevention](09-security-and-abuse-prevention.md) | Threat model, malicious sources, privacy and trust |
| 10 | [Audit logs and case management](10-audit-logs-and-case-management.md) | Case record, registry channels, audit history |
| 11 | [Appeals and corrections](11-appeals-and-corrections.md) | Review, corrections, reversal and local remediation |
| 12 | [Configuration and admin controls](12-configuration-and-admin-controls.md) | Server adoption, independent controls and open policy choices |
| 13 | [Error handling and edge cases](13-error-handling-and-edge-cases.md) | Retry, offline, permission and partial-outcome behavior |
| 14 | [Testing and acceptance criteria](14-testing-and-acceptance-criteria.md) | Safe mocked scenarios and workflow release gates |
| 15 | [Implementation roadmap](15-implementation-roadmap.md) | Sequenced planning only; no implementation in this task |
| 16 | [Future expansion](16-future-expansion.md) | Non-duplicative later SADA capabilities |

## OPEN DECISIONS

These must be approved and versioned before implementation:

- Whether five independent reporting guilds is a threshold, a review priority, or neither.
- What the proposed 5,000-member condition measures: each source guild, all participating members, population at event time, current population, or no size gate.
- Reason-category weights, evidence quality rules, lookback, decay, independent-guild caps, and minimum supporting evidence.
- Global reviewer authority and quorum (single reviewer versus two-person approval); two independent reviewers are recommended but remain a policy choice.
- Data retention, original-reason sharing, user notice, correction/deletion, appeal timing, and reversal policy.
- Server reliability methodology and how to avoid penalizing small communities or communities with many legitimate appeals.
- Whether “intelligence-only” participation receives signals only, or also submits incidents; submission must never be implied by installation.
- Deployment topology, central-service operator, service availability target, and data residency.
- Whether local alerts are delivered in a distinct private SADA channel or an existing private moderation channel.

## Suggested central registry channels

The official Zyrix staff server may create private channels such as #sada-global-registry, #sada-global-alerts, and #sada-case-files. These are proposed names only. The SADA database remains the source of truth.
