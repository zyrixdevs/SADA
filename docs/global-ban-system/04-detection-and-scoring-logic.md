# 04 — Detection and scoring logic

## Reason-first analysis

Raw punishment counts alone are too weak. SADA should prioritize the reason category and supporting evidence: four independent, well-supported scam/phishing actions may represent a repeated pattern; four unrelated interpersonal disputes should not receive the same classification.

Preserve these fields independently:

1. **Original reason:** exact moderator-provided text, attributed to source guild/actor and stored under restricted access/retention. Never silently rewrite it.
2. **Normalized category:** one or more controlled taxonomy labels, proposed by a versioned classifier and separately reviewed.
3. **Supporting evidence:** references/metadata allowed by policy (audit-entry ID, message ID/link where access permits, evidence hash, moderator statement). Do not copy private messages by default.
4. **Evidence quality:** structured provenance/completeness/consistency factors and source reliability context, not a claim of guilt.
5. **Reviewer decision:** who reviewed which version, what category/evidence interpretation they accepted/rejected, when, and why.

### Initial category taxonomy

| Category | Examples of signal | Caution |
|---|---|---|
| Phishing and scams | Credential theft, fake giveaways, payment fraud, scam promotion | Require evidence/reference and context; do not treat a word match as proof. |
| Malware and malicious links | Confirmed malicious payload/link distribution | Link analysis must be safe; do not fetch arbitrary user URLs in the bot. |
| Coordinated raids | Repeated coordinated join/message disruption across communities | AntiNuke/automod events are local signals; actor attribution may be uncertain. |
| Harassment and targeted abuse | Repeated targeted conduct with context/evidence | Avoid turning interpersonal conflict or a single allegation into verified fact. |
| Repeated spam | Repeated unwanted message activity | Distinguish local spam from network-scale campaigns and ordinary advertising. |
| Advertising | Unsolicited promotion/spam | Usually lower severity; policy must specify when it is security relevant. |
| Personal dispute | Interpersonal conflict, moderation disagreement, unrelated grievance | Exclude from high-risk threat categories unless independent evidence supports a different category. |
| Unknown / unspecified | Empty, generic, contradictory, or unclassifiable reason | Never map unknown to severe by default. |

A record may have multiple proposed categories. Category confidence below an approved threshold remains Unknown/needs review. The original reason stays visible next to the normalized label so reviewers can identify mismatch.

## Evidence status and transitions

Evidence status is about provenance/review lifecycle, not target guilt:

| Status | Meaning | Scoring treatment proposal |
|---|---|---|
| Unverified | Report/observation without sufficient source validation | Excluded from verified-action threshold; available in separate review section only. |
| Verified | Defined provenance checks confirm the event/action occurred, e.g. successful bot action or target-matched fresh audit evidence | May contribute to a candidate only within category, quality, independence, and correction policy. It still does not prove reason accuracy. |
| Reviewed | Authorized human examined the action context/category/evidence and recorded a disposition | May receive a separate reviewed-support factor. Does not mean “guilty”; reviewer can reject the category. |
| Disputed | Source or affected user contests identity/action/reason/category and review is pending | Flag visibly; reduce/pause contribution according to approved policy; do not hide dispute. |
| Reversed | Source action/finding was corrected, withdrawn, or overturned | Excluded from active support; retain as audit history and point to the correction/reversal. |

Recommended transitions: new input → Unverified; successful source validation → Verified; human review → Reviewed or remain Verified with a separate category decision; a dispute may transition a record to Disputed from Verified/Reviewed; appeal/correction resolution may return it to an appropriately qualified active state or mark Reversed. Reversal is not silently undone; a materially new event receives a new incident ID. Store status changes append-only. **OPEN DECISION:** exact transition authority and whether a disputed event is fully excluded or only unavailable for high-impact decisions.

## Proposed scoring model

Use transparent gates and a versioned score, not a black-box total:

1. Filter by event time/lookback and source consent version.
2. Exclude duplicate, reversed, and ineligible unverified evidence. Keep disputed evidence separate.
3. Evaluate whether the reason category is relevant to the threat pattern. Category overlap matters; unrelated categories must not pool as one threat.
4. Apply evidence-quality factor based on provenance completeness, audit consistency, evidence references, and review outcome.
5. Aggregate within each source guild with a conservative cap; repeated actions in one guild cannot create multiple independent-guild votes.
6. Count distinct source guilds separately from action volume. A source guild, moderator, or bot installation cannot impersonate multiple independent sources.
7. Apply time window/decay only after approval. Avoid using current member_count without defining the measurement time and denominator.
8. Return a breakdown: category cluster, included incident IDs, excluded/disputed IDs and reasons, source guild count, per-guild contribution, evidence-quality summary, policy/scorer version, and uncertainty.
9. Candidate output is recommendation-only. Human review is required before any global decision.

An example abstract formula is: threat signal(category) = sum over independent guilds of capped verified/reviewed category support × evidence-quality factor × approved recency factor. Add a separate minimum independent-guild gate and category-specific evidence gate. This equation is a design shape, not an approved scoring policy.

## Server evidence quality and reliability

Use transparent, explainable quality measures rather than an opaque permanent “trust score.” Candidate inputs:

- completeness of source/action/actor/time/reason fields;
- audit-log consistency and event-to-audit freshness/target match;
- duplicate rate after idempotency and retry handling;
- correction/reversal outcomes and whether corrections were timely;
- proportion of reviewed records supported, disputed, or unsupported;
- report patterns by moderator, category, timeframe, and event volume relative to source activity;
- source guild's consent and integration version health.

Do not treat a high appeal count as evidence that a server is unreliable. Normalize rates by a minimum denominator and report uncertainty; a low-volume guild should be “insufficient data,” not “untrusted.” A pattern of unsupported reports can trigger more human review, temporary contribution caps, or an audited source suspension; it must not silently erase records or permanently penalize the whole community. **OPEN DECISION:** methodology, window, minimum denominator, source appeal path, and how reliability affects evidence weight.

## Open numeric thresholds

No numeric threshold below is active until the owner approves a versioned policy:

| Proposal | Unresolved interpretation |
|---|---|
| Five-server threshold | Five distinct participating guilds with relevant verified/reviewed evidence? A candidate alert threshold? A minimum for global review only? Decide action categories and window. |
| 5,000-member condition | Minimum per source guild, total participating population, member total at incident time, current population, or no size gate. These mean different things. |
| Category weights | Relative effect of scam, malware, raid, harassment, spam, advertising, disputes and unknown; never assume all bans equal. |
| Evidence gate | Whether one verified event plus two reviewed events is sufficient; what supporting evidence qualifies. |
| Recency | Lookback duration and decay; retention must align. |
| Source caps | Maximum independent contribution by guild and moderator; separate a guild from the bot installation identity. |
| Review gate | Human reviewers required and whether one or two independent reviewers. |

## False-positive resistance

- Count unique event IDs once; source event IDs and idempotency keys have database uniqueness constraints.
- Count distinct guilds, not actions, messages, channels, shards, or duplicate bot retries.
- Cluster by semantically compatible reason category; unrelated reasons do not pool into a severe pattern.
- Keep personal dispute/unknown categories from silently mapping to phishing or abuse.
- Require provenance and evidence quality; preserve category confidence and reviewer change history.
- Cap one guild/moderator's contribution; flag coordinated patterns for review.
- Use anomaly indicators for triage, never as proof.
- Make the scorer deterministic, versioned, explainable and incapable of Discord writes.
