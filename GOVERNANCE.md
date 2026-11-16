# Project governance

SADA is an independent open-source project associated with the Zyrix Dev name. This document describes a lightweight process for the current project; it does not claim that a formal foundation, board, or governance committee exists.

## Ownership and decision-making

The GitHub repository owner holds administrative control of the repository and is responsible for ensuring that releases, access, security response, and project decisions have accountable owners. Maintainers review contributions and may make routine documentation and engineering decisions within the published security principles. No individual names or additional maintainers are assigned by this document; see [MAINTAINERS.md](MAINTAINERS.md).

Decisions should be made in public issues or pull requests when doing so is safe. Security reports, private data, and sensitive operational details use private channels. A decision record should state context, options considered, selected choice, rationale, owner, and review trigger. Unresolved legal, privacy, data-sharing, or high-impact enforcement questions remain explicitly unresolved until approved.

## Maintainer responsibilities

Maintainers are expected to:

- Protect contributor and affected-user safety and follow the [Code of Conduct](CODE_OF_CONDUCT.md).
- Review technical correctness, privacy, security boundaries, dependency/license implications, and documentation accuracy.
- Keep CI and branch settings understandable and recoverable for a single-maintainer project.
- Avoid claiming implementation, validation, legal review, or security assurance that has not occurred.
- Triage private vulnerability reports and remove sensitive material from public surfaces where possible.
- Publish release notes and support policy if software releases begin.

## Appointment and removal

The repository owner may appoint additional maintainers based on sustained, constructive contributions, sound security judgment, responsiveness, and willingness to carry review/operations responsibilities. Appointment should be announced in a repository discussion or change record and reflected in `MAINTAINERS.md`, CODEOWNERS, and access controls. Maintainer access can be reduced or removed when responsibilities end, credentials are compromised, or project safety requires it; the change should be documented without disclosing private information.

## Technical proposals and breaking changes

Small corrections can be reviewed in ordinary pull requests. New features, data collection, externally visible APIs, schema changes, security-sensitive controls, and changes to shared contracts require an issue or design proposal describing alternatives, threat model, privacy/retention, compatibility, failure behavior, and rollout. Breaking changes require maintainer approval and a migration/deprecation plan before implementation or release. Reviewers should seek a second maintainer for high-impact decisions when available; a single-maintainer project must document that independent review was unavailable rather than imply quorum.

## Security-sensitive decisions

Changes that affect identity, evidence, cross-server sharing, reviewer authority, appeals, automated recommendations, enforcement, credentials, or tenant isolation require focused security review. High-impact actions remain human-authorized and local. SADA Core must never receive the Discord bot token or execute Discord moderation actions. Zyrix retains local action authority, and SADA outages must not disable normal moderation or AntiNuke. Legal/privacy review is needed where collection, retention, data residency, or user rights may be affected.

## Challenges and appeals

Contributors may question a decision by commenting on its issue or pull request with evidence, impact, and an alternative. Maintainers should respond with a reason, record unresolved disagreement, and reopen decisions when material facts change. If a contributor believes the process violated the Code of Conduct or was unsafe, they may raise that privately with the repository owner/maintainers. No independent appeals panel exists today; a maintainer involved in a complaint should not be the sole reviewer where another appropriate maintainer is available.

## License and contributions

Contributions are offered under Apache-2.0 as described in [CONTRIBUTING.md](CONTRIBUTING.md) and the [license](LICENSE). Project participation rules do not add conditions to downstream use of the licensed work.
