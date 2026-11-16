# Contributing to SADA

Thank you for helping improve SADA. **This repository currently contains architecture and engineering documentation only.** There is no Rust core, Python adapter, database migration set, production API, detection engine, or application test suite to build. Do not infer that proposed designs are implemented.

## Before opening a pull request

1. Search existing issues and documentation to avoid duplicate work.
2. For a feature proposal, describe the problem, affected modules, signals/data required, authorization, privacy/retention, misuse cases, human-review needs, failure behavior, and acceptance criteria.
3. For a security vulnerability, do not open a public issue. Follow [SECURITY.md](SECURITY.md).
4. Do not submit real Discord member data, private conversation content, credentials, tokens, webhook URLs, or production evidence.

## Repository setup

The current repository needs Git, Python 3.10 or newer, and Node.js/npm to run all local documentation checks. No SADA package installation or service startup is available.

```sh
git clone https://github.com/zyrixdevs/SADA.git
cd SADA
python3 scripts/validate_repository.py
npx --yes markdownlint-cli2@0.24.0 '**/*.md'
```

Optional local hooks:

```sh
python3 -m venv .venv-dev
. .venv-dev/bin/activate
python -m pip install pre-commit==4.3.0
pre-commit install
pre-commit run --all-files
```

The hooks improve local feedback but are not the sole quality gate; GitHub Actions independently runs repository checks. Workflow contributors should also run [actionlint](https://github.com/rhysd/actionlint) and [zizmor](https://github.com/zizmorcore/zizmor) as described in [engineering standards](docs/engineering/DEVELOPMENT-STANDARDS.md).

## Branches and commits

Create a branch from the current target branch. Use a short descriptive prefix such as `docs/`, `chore/`, `fix/`, or `feat/`. Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit subjects, for example:

- `docs: clarify tenant isolation boundaries`
- `chore: pin workflow analysis tools`
- `fix: correct local documentation link`

Keep each pull request focused. Do not force-push a shared branch without coordination.

## Documentation standards

- Label content as existing repository fact, proposal, future implementation, or unresolved decision.
- Reuse canonical event, identity, evidence, case, API error, idempotency, and audit contracts; avoid inventing a second shared platform contract.
- Link related modules and verify local Markdown links.
- Give concrete examples, field types, constraints, failure behavior, and security/false-positive handling where applicable.
- Never claim a feature, test, algorithm, audit, or release exists unless it has been implemented and verified.
- Preserve all 49 current feature modules and update both documentation indexes when a module is intentionally added or retired.
- Keep examples synthetic and secrets non-sensitive.

## Future Rust SADA Core contributions

No Rust workspace exists yet. When approved implementation begins, use the workspace's declared supported toolchain and crate layout. Expected checks are formatting, Clippy with warnings denied, unit/integration/security tests, dependency review (`cargo audit` and `cargo deny`), and supported-target builds. Keep domain logic deterministic and separate from I/O. Never add Discord bot tokens, Discord moderation API credentials, or direct Discord ban/kick/timeout/configuration execution to SADA Core.

## Future Python Zyrix adapter contributions

No SADA adapter package exists in this repository. When it is introduced, document the actual supported Python versions and package layout before adding setup instructions or a CI matrix. Expected checks include Ruff, type checking, unit/integration tests, packaging validation, and dependency security checks. The adapter alone owns Discord credentials and actions; it must recheck current local consent, membership, permissions, role hierarchy, case revision, and guild exceptions. SADA downtime must not impair ordinary local moderation or AntiNuke.

## Pull request process

- Explain what changes and which docs/contracts it affects.
- Complete the pull request checklist and include commands/results for applicable checks.
- Call out unresolved design choices instead of silently selecting policy.
- Expect review for security boundaries, compatibility, privacy, and maintainability.
- Maintainers may request revisions, defer a proposal, or close it with a reason. See [GOVERNANCE.md](GOVERNANCE.md) for decisions and challenges.

Contributions are submitted under [Apache-2.0](LICENSE), subject to the terms there. See [Zyrix Dev attribution conditions](ZYRIX-DEV-CONDITIONS.md) for the distinction between downstream license terms and project contribution rules.
