# Gemini project guidance

Before work, read [`AGENTS.md`](AGENTS.md), [`PATH.md`](PATH.md), and the relevant architecture or feature specifications. Treat the 49 feature modules as proposed designs; this repository does not contain the SADA application yet.

Never put Discord tokens or Discord moderation authority in SADA Core. Preserve explicit guild opt-in, independent Zyrix-side checks, tenant isolation, privacy, provenance, auditability, human review, and local moderation availability during SADA outages. Implement only real, testable behavior; update documentation and report only checks actually run.
