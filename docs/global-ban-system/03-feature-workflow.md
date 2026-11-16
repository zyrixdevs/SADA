# 03 — Feature workflow

**Status: proposed technical specification; not implemented.**

## Participation setup

A guild owner or authorized administrator opens SADA setup from a private context. The setup must explain the data categories and ask separately:

1. **Share incidents:** may approved bot/AntiNuke events from this guild be submitted to SADA?
2. **Receive intelligence:** may SADA return cross-server signals to this guild?
3. **Local alerts:** may eligible cases generate a staff-channel alert here?
4. **Global enforcement:** may this bot installation apply an approved global decision in this guild, subject to local checks?

Every control defaults off, can be paused independently, and logs who changed it and when. The interface must not bundle collection and enforcement into one “enable SADA” switch. **OPEN DECISION:** define whether “intelligence-only” means receive-only, or whether a guild can submit verified incidents but receive no alerts. The interface must state the exact direction of data flow.

## Incident-to-case workflow

1. **Local action occurs.** A moderator uses an existing command, or Discord emits a security event. For command-based incidents, submit only after the Discord action succeeds. If the command action fails, do not label it verified.
2. **Local response remains primary.** AntiNuke executes its configured local response immediately. It must not await SADA. After local detection/action, it may enqueue a typed security event with its confidence and audit provenance; SADA outage only affects intelligence delivery.
3. **Outbox submission.** The bot checks this guild's data-sharing setting and attaches installation identity, guild/user IDs, event ID, original reason, action/source, time, provenance, and consent/policy version. It queues durably and sends asynchronously.
4. **SADA validates intake.** The API checks installation credentials, source guild authorization, active consent, schema version, idempotency, rate limits, size, timestamp, and event type. Rejected events have an explicit safe reason and are not counted.
5. **Evidence evaluation.** SADA assigns an evidence status and quality factors. A confirmed Discord action may be Verified as an action occurrence. A report without provenance is Unverified. A moderator's reason remains an attributed statement, not a platform finding.
6. **Reason classification.** A classifier proposes one or more normalized categories and confidence with model/rule version. It never changes the original reason. Ambiguous, unknown, personal-dispute, or mixed reasons remain visible as such. Human review can confirm, amend, or reject a category.
7. **Reliability adjustment.** Source completeness, audit consistency, duplicate/correction history, review outcomes, and unsupported reports affect evidence confidence/triage. Volume alone and number of appeals do not reduce a server's trust.
8. **Cross-server correlation.** SADA groups evidence by target, relevant reason category, source-guild independence, time window, verification status, quality, and corrections. The result is an explainable suspicious flag and candidate case; it does not execute moderation.
9. **Find eligible alert guilds.** For each guild with alert delivery enabled, confirm the target is currently a member. Cache-only uncertainty is not treated as membership; use a bounded member fetch or defer. Do not alert guilds where the user is absent or unknown.
10. **Send local alert.** Post to that guild's configured private moderation channel once per open alert/evidence version. Alert includes original reasons permitted for sharing, normalized categories, evidence status/quality, relevant counts, reporting guilds subject to policy, and case ID. Exactly two primary buttons: Ban User and Ignore.
11. **Local choice.** Ban User revalidates the current moderator and bot permissions, membership, hierarchy, alert state, and opt-in, then calls Discord for this guild only. Ignore records actor/time for this guild only. Neither click approves a global ban.
12. **Global review.** An eligible candidate enters a reviewer queue. Authorized global reviewers see provenance, categories, source reliability, unverified/disputed evidence, score version, and appeal state. They approve or reject with reasons. **OPEN DECISION:** reviewer quorum; two independent reviewers is the conservative recommendation.
13. **Approved enforcement signal.** SADA sends an authenticated, idempotent approved-decision event, not an arbitrary ban instruction. Each Zyrix Bot installation rechecks that its guild opted into global enforcement and that the decision is current and not appealed/reversed.
14. **Per-guild operation.** The bot checks member, bot permission, role hierarchy, existing ban, local policy, and case state. It performs no action for absent/unknown/opted-out guilds. Each result is persisted independently.
15. **Appeal/correction/reversal.** Appeals and corrections create new history events, trigger reevaluation, pause pending work according to policy, and notify affected guilds when materially changed. Reversal updates the current global state and launches separately tracked remediation; it does not erase successful historical actions.

## State separation

An incident status, reason-category review, source reliability assessment, suspicious case, local alert decision, global review, and guild enforcement attempt each have their own state. A local Ignore cannot set global review to Rejected. A Global Approved state cannot imply all guild enforcement succeeded. See the schema and case-management chapters.

## Scenarios

### Same count, different threat

- Guilds A–D report verified bans for phishing/scam promotion, with consistent timestamps and supporting links. If categories are reviewed and policy criteria are met, SADA may raise a high-priority suspicious case for human review.
- Guilds A–D report bans with reasons “argument,” “rude,” or unrelated disputes. The raw count is similar, but category relevance and evidence quality are weak. SADA should not classify these as a repeated phishing threat. It may show a low-confidence/manual-review case or no cross-server flag, depending on approved policy.

### One malicious source

Guild A submits many repeated “malware” events with missing evidence. Idempotency removes duplicates; per-source caps prevent volume inflation; low completeness and repeated unsupported corrections lower evidence confidence and may trigger source review. The events do not count as independent reports from many servers.

### Partial enforcement

A global decision is approved. Guilds A and B opted into enforcement; C opted out; D is unavailable; E has the target above the bot's role. Results are recorded: A/B attempted and confirmed; C skipped by policy; D unavailable; E skipped for hierarchy. The case summary reports the exact states and never says “banned everywhere.”
