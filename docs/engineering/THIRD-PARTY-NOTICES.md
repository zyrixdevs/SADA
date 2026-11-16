# Third-party notices

This repository currently contains Markdown documentation, policy text, and CI configuration; it has no vendored application dependencies or third-party binary assets.

## Included text

- [`CODE_OF_CONDUCT.md`](../../CODE_OF_CONDUCT.md) adapts the [Contributor Covenant 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution is included in that file.
- [`LICENSE`](../../LICENSE) is the unmodified Apache License 2.0 text from the Apache Software Foundation. The project license identifier is `Apache-2.0`.

## CI and development tools

The workflows pin actions to source commit SHAs and name the corresponding release in comments. Tools run by CI/local instructions include markdownlint-cli2 (MIT), pre-commit-hooks (MIT), pre-commit (MIT), actionlint (MIT), zizmor (MIT), Gitleaks (MIT), and OpenSSF Scorecard (Apache-2.0). These are fetched/executed as tools; their binaries/source are not redistributed in this repository. The secret scanner has one exact path-and-value allowlist for a synthetic example identifier, not a credential. Review upstream license files before adding, vendoring, or distributing third-party code or assets.

The list describes current declared tooling, not a complete software SBOM. When application manifests and release artifacts exist, generate an SBOM from those actual dependency inputs and review license compatibility before publishing.
