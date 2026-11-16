# SADA — Security Intelligence Platform

**Status: documentation and architecture blueprint only. No SADA application, feature, schema, or API is implemented.**

SADA is a proposed independent, open-source security intelligence platform for explicitly participating Discord communities, designed to work alongside Zyrix Bot.

## Mission and vision

Help communities make explainable security decisions while preserving local authority, consent, privacy, correction rights and human accountability. A signal is a review lead, not proof. A score never authorizes punishment.

## Architecture overview

Rust is proposed for SADA Core; PostgreSQL for authoritative structured records; durable inbox/outbox, versioned events, idempotency and audit for reliability. A Python Zyrix adapter owns Discord events, consent, live local checks and every action. Start as independent modular API/worker and PostgreSQL; defer NATS/Redis until measured need.

- [System architecture](docs/system-architecture/README.md)
- [Security and governance](docs/security-and-governance/README.md)
- [Shared standards](docs/shared-standards/README.md)
- [Implementation roadmap and open decisions](docs/implementation-roadmap/README.md)
- [Full documentation index](docs/README.md)

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

## Contributing and security reporting

Documentation must distinguish existing facts from proposals and link shared contracts. Production implementation is outside this blueprint task. Report vulnerabilities privately to the project security contact once published; do not include real guild/member data in public issues or test production servers.
