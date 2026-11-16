# CI/CD strategy

## Implemented repository checks

The active repository workflows are:

- `.github/workflows/ci.yml`: Markdown lint, documentation/index/link integrity, actionlint, YAML parsing, and pre-commit configuration validation.
- `.github/workflows/security.yml`: Gitleaks scans checked-out files and Git history; zizmor checks GitHub Actions workflows.
- `.github/workflows/scorecard.yml`: OpenSSF Scorecard runs for pushes to `main` and weekly on the default branch. It publishes an analysis using the job-scoped GitHub OIDC token.

All GitHub Actions are pinned to full commit SHAs and commented with verified release names. CI and security checks use read-only permissions. Scorecard gets only the OIDC permission it requires and runs only on trusted default-branch pushes or schedule, never on pull requests. There is no external-link availability gate because remote sites can rate-limit or fail temporarily; the local validator checks repository-relative links only.

## Prepared but not currently executable application checks

No application source or manifests exist. Do not claim the following checks have run until the respective workspace/package/migrations are added.

### Rust SADA Core

When a Rust workspace is introduced, require `cargo fmt --check`, `cargo clippy --all-targets --all-features -- -D warnings`, `cargo test`, `cargo audit`, `cargo deny check`, supported-platform compilation, build verification, and integration tests against disposable PostgreSQL. Commit and review `Cargo.lock` for binary/workspace builds. Test deterministic domain behavior, idempotent inbox/outbox processing, tenant isolation, migration compatibility, and failure recovery.

### Python Zyrix adapter

When the actual adapter/package and supported interpreter policy exist, configure a Python-version matrix from that policy, Ruff format/lint, type checking, unit/integration tests, dependency auditing, and packaging verification. The adapter alone receives Discord credentials; do not put credentials in build jobs or SADA Core.

### Database

Once migration files exist, run PostgreSQL integration tests from empty and prior supported schemas; migration-up and recovery/rollback exercises; schema compatibility checks; tenant-isolation tests; and backup/restore verification including evidence metadata and outbox consistency. Do not run destructive migration tests against production data.

## Future release and publishing pipeline

A future protected release workflow may run only from an approved `v*` tag after trusted-branch review. It should verify the source revision and migrations, build supported targets, generate release notes, checksums, SBOM, provenance/attestations, sign artifacts, scan container images only if containers are introduced, and publish through a restricted GitHub Environment with required approvers. Publishing keys must be unavailable to pull-request workflows. Pin release tooling and actions; record artifact digests and rollback steps. If a signing or publishing secret is compromised, disable the environment, revoke/rotate credentials, and publish corrected artifacts with a new version.

No deployment workflow, container image, package, executable, or release credential is configured in this repository. CD is intentionally deferred until an application and operator ownership exist.
