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

| Module | Status |
|---|---|
| [Global Ban System](docs/global-ban-system/README.md) | Proposed feature specification |
| [Threat Intelligence Network](docs/threat-intelligence-network/README.md) | Proposed feature specification |
| [Threat DNA](docs/threat-dna/README.md) | Proposed feature specification |
| [Early Raid Detection](docs/early-raid-detection/README.md) | Proposed feature specification |
| [Scam and Phishing Intelligence](docs/scam-and-phishing-intelligence/README.md) | Proposed feature specification |
| [Security Health Monitor](docs/security-health-monitor/README.md) | Proposed feature specification |
| [Suspicious Admin Activity](docs/suspicious-admin-activity/README.md) | Proposed feature specification |
| [Emergency Response Playbooks](docs/emergency-response-playbooks/README.md) | Proposed feature specification |
| [Attack Impact Simulator](docs/attack-impact-simulator/README.md) | Proposed feature specification |
| [Ban Evasion Intelligence](docs/ban-evasion-intelligence/README.md) | Proposed feature specification |
| [Incident Timeline](docs/incident-timeline/README.md) | Proposed feature specification |
| [Evidence Vault](docs/evidence-vault/README.md) | Proposed feature specification |
| [Trust and Reliability Engine](docs/trust-and-reliability-engine/README.md) | Proposed feature specification |
| [Security Advisory Network](docs/security-advisory-network/README.md) | Proposed feature specification |
| [Attack Campaign Tracker](docs/attack-campaign-tracker/README.md) | Proposed feature specification |
| [Security Simulation Mode](docs/security-simulation-mode/README.md) | Proposed feature specification |
| [Incident Recovery Assistant](docs/incident-recovery-assistant/README.md) | Proposed feature specification |
| [Threat Intelligence API](docs/threat-intelligence-api/README.md) | Proposed feature specification |
| [Security Observatory](docs/security-observatory/README.md) | Proposed feature specification |

## Security principles

Separate opt-in for submission, intelligence reception, alerts and enforcement; all off by default. Minimize data; preserve provenance and uncertainty; require human review for high-impact decisions; support appeals/reversals; no public accused-user list. Zyrix rechecks local consent, membership, permissions and role hierarchy. SADA has no Discord token and no moderation API access. Outage never disables local moderation or AntiNuke.

## Roadmap

Governance/contracts -> Rust/PostgreSQL -> Python adapter -> incident/evidence/case/review -> intelligence -> detection/simulation -> controlled response/recovery -> sensitive intelligence and public surfaces. See [phases](docs/implementation-roadmap/01-project-phases.md) and [dependencies](docs/implementation-roadmap/02-feature-dependencies.md).

## Contributing and security reporting

Documentation must distinguish existing facts from proposals and link shared contracts. Production implementation is outside this blueprint task. Report vulnerabilities privately to the project security contact once published; do not include real guild/member data in public issues or test production servers.
