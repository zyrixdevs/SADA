# Appeals and Corrections

## Appeal intake

A user may submit an appeal of a global decision through a future verified channel. The appeal should reference the SADA case ID and identify the challenged decision; avoid requiring the appellant to disclose unrelated personal data. Intake creates a durable appeal record and acknowledges receipt without promising an outcome or timeline until service policy is approved.

## Review safeguards

- Route the appeal to a reviewer authorized for appeals and, where practical, not the sole original approver.
- Preserve the appealed decision and evidence snapshot for review; do not rewrite history.
- Permit outcomes such as upheld, reversed, remanded for more evidence, or partially corrected.
- Require a reason and timestamp for every outcome.
- Escalate conflicts of interest and suspected forged evidence.
- A pending appeal does not automatically erase a local server's independent moderation decision.

Reviewer separation, service-level timelines, and whether an appeal pauses future global enforcement are **OPEN DECISIONS**.

## Correction and reversal

If a source server corrects or withdraws an incident, append a correction linked to the original. Preserve original text in restricted audit history as policy permits, but mark the original as disputed/reversed so active detection and reviewer views do not count it as current verified evidence. Recompute affected cases and record before/after status.

If a global approval is reversed:

1. Mark the global decision reversed with reviewer, timestamp, reason, and case revision.
2. Stop queued or retrying enforcement signals for that decision.
3. Create correction notifications for every affected participating guild where delivery is permitted.
4. Do not claim that a local Discord ban is undone automatically. Notify each guild and let its local policy/authorized staff decide whether to unban.
5. Track notification and local follow-up results separately.
6. Ensure current summaries no longer say the user is globally approved/banned.

## Incident status effects

`Reversed` incidents do not contribute as active verified evidence. `Disputed` incidents are visible with a warning and excluded from high-confidence thresholds unless policy explicitly permits a lower-confidence signal. A reviewer decision does not convert a source moderator opinion into a fact; record what was reviewed and the scope of the finding.

## Notifications and privacy

Notify guilds that received an alert or enforcement signal when a material correction changes their decision context, subject to approved privacy policy. Do not broadcast appeals or sensitive evidence to every participant. Keep appeal status private to authorized global reviewers and the appellant-facing channel.

## Open policy questions

- Appeal eligibility and identity verification.
- Review deadlines and escalation.
- Reviewer independence and quorum.
- Whether enforcement pauses while an appeal is pending.
- Which corrections require notifying all alerted guilds.
- Retention and deletion treatment for withdrawn evidence.
