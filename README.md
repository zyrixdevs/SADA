# SADA — Suspicious Activity Detection Algorithm

SADA is a proposed, independent security-intelligence service for Zyrix Bot communities that explicitly choose to participate. The first major feature is the Global Ban System. This folder is the design blueprint; SADA is not currently implemented in the opened workspace.

## Start here

- [Global Ban System](global-ban-system/README.md) — requirements, current-code findings, invariants, and chapter index.
- [Independent SADA engine architecture](architecture/independent-sada-engine.md) — Rust core, service boundary, communication, security, and AntiNuke integration.
- [Overview and objectives](global-ban-system/01-overview-and-objectives.md)
- [Implementation roadmap](global-ban-system/15-implementation-roadmap.md)

## Trust promise

Installing Zyrix Bot must not silently enroll a server in cross-server intelligence collection or enforcement. SADA collection, receipt of intelligence, local alerts, and global-enforcement participation are separate, explicit choices. All are off until an authorized server administrator enables them. Local moderation and AntiNuke continue to work when SADA is disabled or unavailable.

SADA flags patterns for review. Evidence that an action occurred is not proof that the target deserved it. Local ban decisions remain local. A global ban requires a separately authorized review; rollout is attempted only in guilds that opted into enforcement, and every guild result is reported independently.
