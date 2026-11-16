# Security policy

SADA is currently a documentation-only repository. No SADA service, API, database, adapter, detection algorithm, or release artifact is available to attack or audit. The architecture describes future proposals, not operational security controls.

## Report a vulnerability privately

Please do not publish vulnerabilities, exploit details, credentials, real Discord member information, private conversations, or sensitive evidence in public issues, pull requests, discussions, or CI logs.

Use GitHub **Private vulnerability reporting** at <https://github.com/zyrixdevs/SADA/security/advisories/new> if it is enabled. The repository issue-template contact link also points there. If GitHub does not offer the private report form, do not fall back to a public issue; ask the repository owner through an established private GitHub contact route to enable private reporting. No security email address is published by this project.

A useful report includes:

- Affected branch, commit, file, or future component (if relevant).
- Impact and realistic threat scenario.
- Reproduction steps using synthetic or isolated test data.
- Any prerequisites, permissions, or configuration needed.
- Suggested mitigation, if known.

Do not attach live credentials, private server data, member identifiers, unredacted evidence, or weaponized samples. Share only the minimum sanitized information necessary.

## Triage and disclosure

The repository owner/maintainers will assess scope, severity, reproducibility, affected versions, and whether the report concerns an implemented component or only a design proposal. They should acknowledge the report when capacity permits, coordinate a fix and disclosure timeline with the reporter, and document the resolution without exposing sensitive data. This project has no staffed security response team or guaranteed response-time SLA at this stage.

If a finding concerns a proposed design rather than running software, maintainers should correct the relevant architecture, threat model, or security decision register and clearly label the change as a documentation correction.

## Supported versions

There are no releases or supported software versions yet. Once releases exist, this policy must name the supported release window and how security fixes are delivered before production use is encouraged.

## Future security gates

Before SADA handles real guild or member data, the project needs a maintained vulnerability-reporting route, accountable response owners, dependency and secret scanning, security review of the implementation, tenant-isolation tests, incident response procedures, and a published release support policy. See [repository setup](docs/engineering/GITHUB-REPOSITORY-SETUP.md) for GitHub features requiring owner action.
