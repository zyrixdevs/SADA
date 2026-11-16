> **Repository scope:** Proposed design only. SADA contains no Zyrix Bot source. Any bot/ paths below describe an earlier Zyrix&Dash assessment and must be revalidated against the target revision before implementation.

# SADA Global Ban System — blueprint

**Status: proposed; documentation only.** No SADA service, schema, configuration, command, API, alert, or global-ban workflow is implemented in this repository.

SADA (Suspicious Activity Detection Algorithm) is intended to analyze cross-server security evidence for participating Zyrix Bot communities. The Global Ban System is its first major feature. SADA creates an explainable suspicious-activity signal and case for human review. It does not determine guilt and never bans from a score alone.

## What it is and why SADA needs it

The Global Ban System is a reviewed cross-server decision workflow for eligible, evidence-backed cases. It addresses repeated threats that affect opted-in communities while keeping each guild's authority local.

## What it does

It correlates relevant incidents, opens an explainable case, collects independent reviewer decisions, supports appeal/correction/reversal, and sends scoped approved-decision signals. Zyrix records each guild outcome independently.

## What it must never do

It must never ban from a score, treat a local ban as proof, enroll a server silently, expose an accused-user directory, or let SADA call Discord moderation endpoints. Every local action requires fresh guild consent, membership, actor/bot permission, and hierarchy checks.

## Main workflow

Opt in separately -> submit authorized event -> preserve provenance -> correlate -> human review/quorum -> appeal/correction path -> issue scoped signal -> Zyrix local checks -> record per-guild receipt.

## Data and API boundaries

The module uses canonical incidents, evidence references, cases, reviews, audit events, and delivery receipts. It does not duplicate source evidence. It follows the shared event and API contracts and keeps local alert choices separate from global review.

## Security and privacy

Share only approved structured metadata; restrict original reasons and evidence; redact source identities where policy requires; audit reads and decisions; cancel stale signals after reversal. Retention, notice, quorum, and sharing permissions remain open decisions requiring policy/legal review.

## Dependencies

Threat Intelligence Network, Trust and Reliability Engine, Evidence Vault, Incident Timeline, Appeals, Threat Intelligence API, and the Zyrix Python adapter. The adapter is the only Discord action boundary.

## Implementation phase

Proposed after the independent foundation, event/evidence contracts, case lifecycle, source-quality review, appeals, and reviewer governance. See the feature roadmap; no implementation is claimed.

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

## Prior Zyrix source assessment (not code in this repository)

The earlier Zyrix&Dash source assessment (external to this repository) described a Python discord.py bot under bot/ with cogs registered by bot/cogs/__init__.py. Revalidate these details against the target Zyrix revision before implementation. Local warn state in bot/cogs/moderation/warn.py is a count keyed by guild/user; it does not persist reason, moderator, timestamp, or case ID. Ban, kick, and timeout commands call Discord directly. The Logging cog in bot/cogs/commands/logging.py uses configured channels and Discord audit-log lookups to create human-readable guild logs; it is not a structured case database.

bot/cogs/commands/owner2.py contains an owner-only global GB command. It builds a cached list of mutual guilds, asks the command author to confirm, then attempts a ban in each mutual guild and reports names/counts in messages. It has no SADA opt-in, durable review record, distinct reviewer approval, or durable per-guild outcome ledger. It is not the proposed SADA workflow and is not a safe substitute for it.

That assessment also described AntiNuke under bot/cogs/antinuke/ and is registered from bot/cogs/__init__.py. It reads local enable/whitelist state from SQLite and handles Discord events using audit-log lookups. Some handlers immediately ban, kick, unban, or otherwise remediate locally. In particular, the assessed bot/cogs/antinuke/antiprune.py used the latest prune audit entry and can ban its executor; the assessment did not find the safer target-specific correlation helper described in an earlier standalone Phase 1 report. These observations may be stale. A SADA integration must not delay or weaken local protection.

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

## Cross-module integration

Global Ban consumes reviewed cases, provenance, quality factors, appeals and corrections; it owns no duplicate incident/evidence ledger.

- [Threat Network](../threat-intelligence-network/README.md), [Trust Engine](../trust-and-reliability-engine/README.md), [Timeline](../incident-timeline/README.md), and [Evidence Vault](../evidence-vault/README.md) provide scoped context.
- [Advisories](../security-advisory-network/README.md), [Playbooks](../emergency-response-playbooks/README.md), and [Impact Simulator](../attack-impact-simulator/README.md) support decisions.
- Canonical [event](../shared-standards/01-event-schema-standard.md), [case](../shared-standards/05-case-lifecycle-standard.md), and [audit](../shared-standards/08-audit-record-standard.md) rules apply.

Five-guild and 5,000-member suggestions remain unresolved; see [decision register](../implementation-roadmap/06-open-questions-and-decisions.md).
