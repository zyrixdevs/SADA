# Future Expansion

**Status: proposed technical specification; not implemented.**

Every item below is a future proposal, not an existing Zyrix or SADA feature. SADA should extend cross-server intelligence without cloning local AutoMod, AntiNuke, moderation, or logging.

| Proposal | SADA role | Boundary with existing Zyrix features |
|---|---|---|
| Cross-server ban-evasion intelligence | Correlate a previously reviewed account or behavioral signal across opted-in servers and recommend review | Does not replace local ban lists or automatically punish an account |
| Raid Fingerprint | Correlate timing, account-age patterns, invitation paths, and repeated payload fingerprints across servers | AntiNuke/AutoMod continue immediate local containment |
| Moderator compromise detection | Detect unusual moderator action patterns across time or credential/session anomalies reported by trusted telemetry | Does not revoke Discord roles or accuse a moderator without review |
| Server trust and evidence reliability | Track completeness, audit consistency, corrections, and reviewed outcomes with confidence ranges | Does not penalize a server merely for having many appeals or high activity |
| Attack-chain detection | Link precursor signals, raids, phishing, and coordinated actions into an investigation timeline | Complements local logs; does not replace them as the guild's source of truth |
| Security health checks | Produce opt-in recommendations about risky permissions, backup readiness, or bot configuration | Local controls remain configured and applied by the guild |
| Bot/integration threat monitoring | Aggregate reports about compromised integrations or suspicious bot behavior | Does not silently uninstall integrations or mutate guild configuration |
| Emergency recovery intelligence | Share tested containment and recovery indicators after an incident | No remote changes to roles, channels, or permissions without local authorization |
| Member scam and phishing intelligence | Correlate verified scam-link or impersonation patterns and share safe indicators | AutoMod remains responsible for local message filtering and configured actions |
| Security simulation/readiness tests | Offer opt-in, non-destructive tabletop or synthetic event exercises | Never run surprise live raids or destructive actions |

## Expansion gates

Each feature needs a distinct threat model, data minimization review, false-positive evaluation, opt-in setting, and clear handoff to Zyrix for any local action. Avoid creating duplicate command systems or sending every local log event to SADA. Prioritize validated user benefit and reliable evidence over raw incident volume.

## Open design questions

Before expansion, decide whether SADA Core remains a single service or gains separate ingestion/analysis workers, how source-server trust is communicated, and which signals may be shared without exposing private moderation context. These depend on measured scale and policy, not speculation.
