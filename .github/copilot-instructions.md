# GitHub Copilot instructions

Read [`../AGENTS.md`](../AGENTS.md) and [`../PATH.md`](../PATH.md) before changing SADA. The 49 feature modules are documented proposals; none is operational. Use the shared contracts and standards instead of creating module-local copies.

Keep Core Rust-based, independent, and without Discord tokens or moderation authority. Require explicit opt-in and tenant-scoped access. The Zyrix adapter retains Discord authority and rechecks local consent, membership, permissions, hierarchy, and case state. Preserve privacy, evidence provenance, audit/correction paths, and failure isolation from local moderation and AntiNuke.
