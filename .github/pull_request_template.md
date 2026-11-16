## Summary

<!-- Describe the change and why it is needed. -->

## Change type

- [ ] Documentation or repository tooling
- [ ] Future application implementation (only after the implementation phase is approved)
- [ ] Security-sensitive change
- [ ] Breaking change to a documented contract

## Validation

- [ ] `python3 scripts/validate_repository.py`
- [ ] Markdown lint (`npx --yes markdownlint-cli2@0.24.0 '**/*.md'`)
- [ ] Relevant pre-commit hooks (`pre-commit run --all-files`)
- [ ] Workflow changes checked with actionlint and zizmor
- [ ] No application behavior is claimed unless it exists and was verified

## Security and privacy review

<!-- List data, trust boundaries, permissions, retention, and failure behavior affected. Never paste real Discord member data or credentials. -->

## Checklist

- [ ] Internal links and documentation indexes are updated.
- [ ] New dependencies and their licenses are documented.
- [ ] SADA Core does not receive a Discord token or perform Discord moderation actions.
- [ ] Changes do not weaken local Zyrix moderation or AntiNuke during SADA outages.
