# Development standards

## Current maturity

The repository has 49 proposed feature specifications and repository tooling. It has no Rust workspace, Python adapter package, production APIs, database migrations, detection algorithms, application tests, binaries, or deployment artifacts. Do not create fake source files or claim a software build/test passed.

## Local setup and checks

Requirements for documentation work: Git, Python 3.10+, Node.js/npm, and optionally pre-commit.

```sh
python3 scripts/validate_repository.py
npx --yes markdownlint-cli2@0.24.0 '**/*.md'
python3 -m venv .venv-dev
. .venv-dev/bin/activate
python -m pip install pre-commit==4.3.0
pre-commit install
pre-commit run --all-files
```

For changes under `.github/workflows/`, install the pinned versions described in [CI/CD strategy](CI-CD-STRATEGY.md) and run `actionlint` and `zizmor`. Pre-commit hooks are convenience checks; CI is the independent gate.

## Style and review

Use UTF-8, LF newlines, final newlines, no trailing whitespace, and spaces according to `.editorconfig`. Markdown uses the root markdownlint configuration. YAML must parse. Keep links relative when they point inside the repository. Use Conventional Commit subjects and focused pull requests.

Documentation must label facts, proposals, future implementation, and unresolved policy. Keep the shared event, evidence, identity, case, error, idempotency, and audit standards canonical. Do not assert test evidence or algorithm accuracy without actual validation.

## Security boundary for future changes

SADA Core never receives a Discord bot token and never executes Discord moderation/configuration actions. Only Zyrix's Python adapter holds Discord credentials and performs a local action after rechecking guild consent, current case revision, membership, actor/bot permissions, role hierarchy, and exceptions. Local moderation and AntiNuke must continue if SADA is unavailable. Keep pull-request CI read-only, avoid real member data, and report vulnerabilities privately as described in [SECURITY.md](../../SECURITY.md).

## Future implementation conventions

When software is approved, first establish actual workspace/package structure, supported toolchains, test fixtures, dependency lockfiles, and operations ownership. Then update contribution instructions and CI to match real project configuration. Proposed Rust and Python checks are in [CI/CD strategy](CI-CD-STRATEGY.md); they are not current checks.
