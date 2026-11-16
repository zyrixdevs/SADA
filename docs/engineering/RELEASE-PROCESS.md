# Release process

## Current state

SADA has no software releases, package, binary, container image, deployment target, release signing key, or supported-version window. The current repository state is documentation and CI infrastructure only. Do not tag or publish placeholder artifacts.

## Future release gate

When an application release is authorized, maintainers should:

1. Confirm release scope, supported platforms, versioning policy, operator, security contact, and support window.
2. Verify CI on the exact reviewed commit: formatter/lint, tests, security/dependency checks, PostgreSQL migrations and restore, tenant-isolation tests, and packaging/build checks.
3. Review dependency licenses, vulnerability findings, changelog, migration notes, privacy/retention behavior, and unresolved critical risks.
4. Create a signed or protected `vX.Y.Z` tag from an approved commit. Restrict publishing to the trusted release workflow and protected GitHub Environment.
5. Generate release notes, artifacts, checksums, SBOM, provenance/attestation, and release signatures; publish only formats that actually exist.
6. Verify artifact signatures/digests and installation instructions from a clean environment. Record the exact source commit and workflow run.
7. Publish rollback guidance and support window; monitor reports; revoke/reissue artifacts if a release credential or artifact integrity is compromised.

Never expose signing or publishing credentials to pull requests. SADA Core must not receive Discord bot tokens. Deployment is a later operational decision, not part of current CI.
