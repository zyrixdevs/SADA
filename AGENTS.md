# Instructions for AI and automated contributors

Before changing this repository, inspect its current branch and working tree, read [`PATH.md`](PATH.md), the root [`README.md`](README.md), and the relevant architecture, standards, feature, and engineering documents. These instructions apply to coding agents; they do not replace the user's latest task-specific direction.

## Current maturity

This repository documents 49 proposed SADA modules and repository infrastructure. It does not contain the Rust SADA Core, Python Zyrix adapter, production APIs, migrations, detection engines, or deployed functionality. Never describe a proposal as implemented. Do not create empty modules, fake endpoints, placeholder test suites, or success-shaped stubs.

## Non-negotiable security boundaries

- SADA Core is independent and Rust-based. Python is for the separate Zyrix adapter and Discord-specific integration.
- Never request, accept, store, print, or commit a Discord bot token in SADA.
- Never give SADA Core Discord moderation/configuration authority or implement ban, kick, timeout, message deletion, role changes, or other Discord actions in Core.
- The adapter independently checks explicit guild consent, scope, current case state, target membership, actor/bot permissions, role hierarchy, and local policy before local actions.
- SADA outages must not block ordinary Zyrix moderation or AntiNuke.
- Never allow an algorithmic score or unverified report alone to trigger a global punishment.
- Preserve evidence provenance, uncertainty, tenant isolation, minimization, audit history, retention controls, appeals, corrections, revocation, and reversal.

## Change process

1. Inspect relevant callers, tests, fixtures, configs, CI, and docs. Preserve unrelated work; never stage it accidentally.
2. Implement a small complete vertical slice using shared identity, event, case, evidence, audit, authorization, and storage contracts. Do not invent module-local duplicates.
3. For detection logic, define permitted input signals, threat assumptions, explanation, uncertainty, false-positive behavior, limits, and adversarial tests. Never invent accuracy or call thresholds validated without measurement.
4. For APIs or schemas, specify versioning, authentication, guild-scoped authorization, idempotency, bounded inputs, safe errors, retention, and compatibility.
5. Update docs, tests, indexes, and the module status registry. Advance a module to Implemented or Tested only with code and test evidence.
6. Run applicable checks and report exact results and skipped checks. Never claim an unrun test, audit, or CI workflow passed.
7. Do not deploy, enable live collection, publish, or perform destructive Git operations unless explicitly authorized.

## Documentation and decisions

Distinguish existing facts, proposals, implemented behavior, and open decisions. Do not silently decide legal, privacy, retention, source-trust, reviewer-quorum, data-residency, or operational policies. Link to canonical shared standards and update affected navigation. Keep public views from exposing private member or incident data.

## Git workflow

Follow the user's latest explicit branch, commit, and delivery instructions. Never force-push, discard changes, or overwrite another contributor's work. When no task-specific workflow is given, use the repository contribution and review process.

For a compact continuation brief, read [`docs/ai/IMPLEMENTATION-HANDOFF.md`](docs/ai/IMPLEMENTATION-HANDOFF.md).
