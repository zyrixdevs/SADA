# Claude Code notes

Read [`AGENTS.md`](AGENTS.md), [`PATH.md`](PATH.md), and the relevant SADA architecture and feature documents before editing. This repository currently contains documentation and repository checks only; the 49 modules are proposals, not working software.

Follow the security boundaries in `AGENTS.md`: Rust for independent Core, no Discord bot tokens or Discord actions in SADA, explicit opt-in, tenant isolation, human review for high-impact decisions, and failure isolation from Zyrix moderation/AntiNuke. Use [`docs/ai/IMPLEMENTATION-HANDOFF.md`](docs/ai/IMPLEMENTATION-HANDOFF.md) to continue work in a new session.
