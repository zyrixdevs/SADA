# Quality assurance

## Checks that apply now

| Check | Command or workflow | What it establishes |
|---|---|---|
| Markdown structure/format | `npx --yes markdownlint-cli2@0.24.0 '**/*.md'` | Configured Markdown rules, including heading hierarchy, blank lines, list/code-fence formatting, and whitespace conventions. |
| Repository integrity | `python3 scripts/validate_repository.py` | 49-module index/directory consistency, unique identifiers, README catalogue parity, implementation-status wording, non-empty Markdown, final newline, trailing whitespace, and internal links. |
| YAML and hook configuration | `pre-commit validate-config`; `pre-commit run check-yaml --all-files` | Pre-commit config parses and tracked YAML files parse. |
| Workflow syntax | `actionlint` | GitHub Actions workflow structure and expression issues. |
| Workflow security | zizmor | Common workflow security hazards and unsafe patterns. |
| Secret scan | Gitleaks over repository history and working tree | Detects supported credential patterns; false positives require safe review. |
| Supply-chain posture | OpenSSF Scorecard on default branch | Evaluates repository configuration and practices; does not certify the SADA application. |

External link reachability is not a required check because external sites rate-limit, redirect, or become temporarily unavailable. Local links are checked without relying on network availability.

## What these checks do not establish

They do not prove that a threat-detection design is accurate, an API is secure, a license is legally sufficient for every use, a deployment is safe, a secret has never existed, or any SADA feature works. There is no Rust/Python application, database, API, migration, feature algorithm, or application test suite at present.

## Required checks when implementation begins

Use deterministic unit/property tests, disposable PostgreSQL integration tests, API/event contract tests, authorization/tenant-isolation tests, adversarial and false-positive tests, retry/replay and outage tests, migration/backup/restore tests, dependency audits, and packaging/build verification. Use synthetic Discord fixtures and mocked actions; never exercise real moderation in CI. Require a security review for identity, evidence, cross-server sharing, operator access, or local enforcement interfaces. See [CI/CD strategy](CI-CD-STRATEGY.md).
