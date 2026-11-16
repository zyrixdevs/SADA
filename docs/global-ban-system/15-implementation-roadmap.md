# Implementation Roadmap

This roadmap is a proposal. No phase below is implemented by creating this blueprint.

## Phase 1: Independent foundation and policy

**Dependencies:** owner decisions for participation, data fields, privacy/retention, deployment boundary, service auth, and current bot integration strategy.

**Expected modules:** standalone SADA Core service skeleton (Rust), versioned API/event schema, PostgreSQL schema/repository, migrations, health/readiness, authentication, audit/outbox.

**Tests:** schema constraints, auth scope, idempotency, outbox crash recovery, migrations on disposable DB, no-secret logs.

**Complete when:** service can accept and durably deduplicate a synthetic event; bot is not yet required; no Discord token exists in SADA.

## Phase 2: Moderation event adapter

**Dependencies:** stable event contract and approval of which local actions are submitted.

**Expected modules:** narrow Python adapter/service client in Zyrix; integration points around existing moderation handlers; feature flags and explicit guild settings.

**Tests:** ban/kick/timeout/warn event payloads, unavailable SADA behavior, retries, duplication, no delay to AntiNuke/local moderation.

**Complete when:** only opted-in event types are sent and original local outcomes remain unchanged if SADA is offline.

## Phase 3: Reason taxonomy and evidence review

**Dependencies:** approved categories, statuses, and evidence policy.

**Expected modules:** Rust normalization/classification pipeline with human-review path; preserve original reason; source reliability signals.

**Tests:** ambiguous reasons, personal disputes, adversarial text, language/format variants, corrections, false inference checks.

**Complete when:** classification is clearly advisory, uncertain inputs stay uncertain, and reviewers can correct results.

## Phase 4: Detection and case creation

**Dependencies:** policy-approved threshold semantics and minimum evidence quality.

**Expected modules:** deterministic cross-guild correlation, score explanation, case lifecycle and revision tracking.

**Tests:** independent guild counts, category weighting, time windows, duplicates, disputed/reversed evidence, threshold boundaries.

**Complete when:** every flag has explainable evidence and cannot dispatch an enforcement command.

## Phase 5: Server-specific alerts and local choices

**Dependencies:** bot adapter, alert settings, private channel permissions, alert retention.

**Expected modules:** per-guild alert outbox, two-button interaction, permission/membership checks, local decision storage.

**Tests:** exactly two primary buttons, guild isolation, replay, membership changes, hierarchy/permissions, ignore/reopen policy.

**Complete when:** local Ban User affects only its guild, Ignore is audited, delivery is deduplicated, and all failures are truthful.

## Phase 6: Global review and opt-in enforcement

**Dependencies:** reviewer authority, quorum decision, policy/legal review, per-guild explicit consent, emergency circuit breaker.

**Expected modules:** reviewer workflow, signed decision signal, installation registry, per-guild execution result state machine.

**Tests:** unauthorized review, quorum, revocation, non-opted-in skip, partial failures, retries, reversed approval.

**Complete when:** no enforcement occurs without approved decision plus local opt-in and fresh bot-side validation; results are reported per guild.

## Phase 7: Appeals, corrections, and operations

**Dependencies:** appeal and retention policies, operator staffing, recovery procedures.

**Expected modules:** appeal workflow, linked correction events, notification reconciliation, backup/restore, audit review tools.

**Tests:** reversal, corrected reason, pending retry cancellation, guild notification failure, backup recovery and access review.

**Complete when:** current views are corrected, historical transitions remain auditable, and affected guilds receive honest updates.

## Deployment progression

Use local mocks, isolated development, then staging with synthetic/test guilds and synthetic identities where possible. Production collection starts only after explicit privacy and participation controls are tested. Production global enforcement requires a separate readiness review and owner authorization; it is not implied by completion of earlier phases.
