# SADA — Security Intelligence Platform

[![CI](https://github.com/zyrixdevs/SADA/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/zyrixdevs/SADA/actions/workflows/ci.yml)
[![Security checks](https://github.com/zyrixdevs/SADA/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/zyrixdevs/SADA/actions/workflows/security.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

**Open-source status:** repository and architecture documentation are public. **Maturity:** documentation/repository foundation only. No SADA application, feature, production schema, or API is implemented. CI badges report repository checks only; they do not indicate application tests or a security audit.

SADA is a proposed independent, open-source security intelligence platform for explicitly participating Discord communities, designed to work alongside Zyrix Bot.

## Mission and vision

Help communities make explainable security decisions while preserving local authority, consent, privacy, correction rights and human accountability. A signal is a review lead, not proof. A score never authorizes punishment.

## Architecture overview

Rust is proposed for independent SADA Core; PostgreSQL is proposed as the authoritative structured store with durable inbox/outbox, versioned events, idempotency, and shared audit. A future Python Zyrix adapter would own Discord credentials, event capture, consent controls, local permission checks, and every Discord action. SADA Core must never receive the Discord bot token or execute moderation/configuration actions. SADA outages must not disable ordinary Zyrix moderation or AntiNuke. Start with an independently deployable modular API/worker and PostgreSQL; add brokers or caches only when measured requirements justify them.

## Technology decisions

- **Rust:** proposed language for the independent SADA Core; no Rust workspace exists.
- **Python:** proposed for the Zyrix adapter; no SADA adapter package exists in this repository.
- **PostgreSQL:** proposed authoritative structured database; no migrations exist.
- **Durable inbox/outbox and versioned contracts:** proposed reliability model; no service/API is running.
- **NATS/Redis:** deferred until requirements and operating costs justify them.
- **GitHub Actions:** currently validates repository documentation, integrity, workflow safety, and secrets; it does not build application software.

- [System architecture](docs/system-architecture/README.md)
- [Security and governance](docs/security-and-governance/README.md)
- [Shared standards](docs/shared-standards/README.md)
- [Implementation roadmap and open decisions](docs/implementation-roadmap/README.md)
- [Full documentation index](docs/README.md)
- [Engineering standards and CI/CD plan](docs/engineering/README.md)

## Feature modules

The catalogue contains 49 proposed feature specifications. None is operational. Browse by category in the [documentation index](docs/README.md).

### Existing feature modules (1–19)

- [Global Ban System](docs/global-ban-system/README.md)
- [Threat Intelligence Network](docs/threat-intelligence-network/README.md)
- [Threat DNA](docs/threat-dna/README.md)
- [Early Raid Detection](docs/early-raid-detection/README.md)
- [Scam and Phishing Intelligence](docs/scam-and-phishing-intelligence/README.md)
- [Security Health Monitor](docs/security-health-monitor/README.md)
- [Suspicious Admin Activity](docs/suspicious-admin-activity/README.md)
- [Emergency Response Playbooks](docs/emergency-response-playbooks/README.md)
- [Attack Impact Simulator](docs/attack-impact-simulator/README.md)
- [Ban Evasion Intelligence](docs/ban-evasion-intelligence/README.md)
- [Incident Timeline](docs/incident-timeline/README.md)
- [Evidence Vault](docs/evidence-vault/README.md)
- [Trust and Reliability Engine](docs/trust-and-reliability-engine/README.md)
- [Security Advisory Network](docs/security-advisory-network/README.md)
- [Attack Campaign Tracker](docs/attack-campaign-tracker/README.md)
- [Security Simulation Mode](docs/security-simulation-mode/README.md)
- [Incident Recovery Assistant](docs/incident-recovery-assistant/README.md)
- [Threat Intelligence API](docs/threat-intelligence-api/README.md)
- [Security Observatory](docs/security-observatory/README.md)

### Bot, integration and identity security (20–26)

- [Bot Security Intelligence](docs/bot-security-intelligence/README.md)
- [OAuth and Third-Party App Security](docs/oauth-and-third-party-app-security/README.md)
- [Bot Permission Drift Detection](docs/bot-permission-drift-detection/README.md)
- [Bot Compromise Early Warning](docs/bot-compromise-early-warning/README.md)
- [Integration Supply Chain Intelligence](docs/integration-supply-chain-intelligence/README.md)
- [Administrative Identity Protection](docs/administrative-identity-protection/README.md)
- [Privilege Escalation Path Analyzer](docs/privilege-escalation-path-analyzer/README.md)

### Attack prevention and detection (27–35)

- [Destructive Action Circuit Breaker](docs/destructive-action-circuit-breaker/README.md)
- [Invite Link Security Monitor](docs/invite-link-security-monitor/README.md)
- [Staff and Support Impersonation Detection](docs/staff-and-support-impersonation-detection/README.md)
- [Social Engineering Attack Detection](docs/social-engineering-attack-detection/README.md)
- [Advanced Spam Evasion Detection](docs/advanced-spam-evasion-detection/README.md)
- [Mass Mention and Role Abuse Protection](docs/mass-mention-and-role-abuse-protection/README.md)
- [Raid Source and Entry Analysis](docs/raid-source-and-entry-analysis/README.md)
- [Moderation Audit Integrity Monitor](docs/moderation-audit-integrity-monitor/README.md)
- [Configuration Drift Detection](docs/configuration-drift-detection/README.md)

### Malware, phishing and malicious content (36–40)

- [Malicious Attachment Intelligence](docs/malicious-attachment-intelligence/README.md)
- [QR Code Threat Detection](docs/qr-code-threat-detection/README.md)
- [Short Link and Redirect Security](docs/short-link-and-redirect-security/README.md)
- [Malicious File Campaign Correlation](docs/malicious-file-campaign-correlation/README.md)
- [External Threat Feed Intelligence](docs/external-threat-feed-intelligence/README.md)

### SADA platform and infrastructure security (41–47)

- [SADA API Abuse Protection](docs/sada-api-abuse-protection/README.md)
- [Tenant Isolation Security](docs/tenant-isolation-security/README.md)
- [SADA Operator Activity Monitoring](docs/sada-operator-activity-monitoring/README.md)
- [Secret and Credential Exposure Monitor](docs/secret-and-credential-exposure-monitor/README.md)
- [Dependency Vulnerability Intelligence](docs/dependency-vulnerability-intelligence/README.md)
- [Secure Build and Release Verification](docs/secure-build-and-release-verification/README.md)
- [Security Patch and Exposure Advisory](docs/security-patch-and-exposure-advisory/README.md)

### Advanced security intelligence (48–49)

- [Threat Intelligence Expiration and Revocation](docs/threat-intelligence-expiration-and-revocation/README.md)
- [AI Security and Prompt Injection Protection](docs/ai-security-and-prompt-injection-protection/README.md)

## Security principles

Separate opt-in for submission, intelligence reception, alerts and enforcement; all off by default. Minimize data; preserve provenance and uncertainty; require human review for high-impact decisions; support appeals/reversals; no public accused-user list. Zyrix rechecks local consent, membership, permissions and role hierarchy. SADA has no Discord token and no moderation API access. Outage never disables local moderation or AntiNuke.

## Roadmap

Governance/contracts -> Rust/PostgreSQL -> Python adapter -> incident/evidence/case/review -> intelligence -> detection/simulation -> controlled response/recovery -> sensitive intelligence and public surfaces. See [phases](docs/implementation-roadmap/01-project-phases.md) and [dependencies](docs/implementation-roadmap/02-feature-dependencies.md).

## Documentation and engineering

The [documentation index](docs/README.md) links all 49 proposed feature modules, shared architecture, standards, security governance, and engineering guidance. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md) before opening a change. See [SUPPORT.md](SUPPORT.md) for help. Contributions should distinguish repository facts from proposals and link canonical shared contracts. Repository checks are described in [quality assurance](docs/engineering/QUALITY-ASSURANCE.md).

## Vulnerability reporting

Do not publish credentials, real Discord member information, private conversation content, or sensitive evidence in public issues. Follow [SECURITY.md](SECURITY.md) and use GitHub private vulnerability reporting if the repository owner has enabled it. No security email address or staffed response team is published.

## Open-source license and attribution

SADA is offered under the **Apache License 2.0** (`SPDX-License-Identifier: Apache-2.0`); see [LICENSE](LICENSE), [NOTICE](NOTICE), [CITATION.cff](CITATION.cff), and [Zyrix Dev attribution conditions](ZYRIX-DEV-CONDITIONS.md). The Apache license permits reuse and modification subject to its terms, including preservation of applicable notices. This is not a custom Zyrix Dev license and does not require downstream users to follow internal organization rules. Contribution rules apply to work submitted to this repository. No legal review is claimed.

## Current limitations

There is no SADA Rust Core, Python adapter, application code, database schema/migrations, live API, deployment, executable detection engine, or software release. The 49 feature modules are design specifications; their algorithms and data models are proposals, not validated behavior. CI status badges cover repository checks only. GitHub security settings described in the repository setup guide require manual owner action.
