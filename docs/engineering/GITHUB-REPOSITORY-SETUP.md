# GitHub repository setup

This document lists **manual repository-owner actions**. Committing configuration does not enable GitHub settings, and no settings are claimed enabled here. GitHub interface labels can change; use the linked official documentation if a menu has moved.

## Branch rules for `main`

In repository **Settings → Rules → Rulesets** (or branch protection settings), create a ruleset targeting `main`:

- Require changes to enter through a pull request.
- Require the workflow job checks `Documentation quality`, `Workflow and YAML validation`, `Repository integrity`, `GitHub Actions security analysis`, and `Secret scan` after GitHub has recorded a successful run. GitHub may display each context with its workflow name; select the exact job contexts shown in the ruleset UI. Scorecard is informational and scheduled, so do not require it for each pull request.
- Require conversation resolution.
- Block force pushes and branch deletion.
- Do not require an approving review while there is only one maintainer; GitHub does not allow a contributor to approve their own pull request. Add a required independent approval when a second maintainer is appointed.
- Keep a repository-administrator bypass available for recovery, with any use documented. Do not make normal owner contribution dependent on a non-existent reviewer.
- Do not require signed commits or linear history until the owner has confirmed the team can reliably meet those requirements.

Test the ruleset with a normal pull request and a recovery scenario. Avoid locking out the sole owner.

## Security features to enable manually

1. **Private vulnerability reporting:** Open **Settings → Code security and analysis → Private vulnerability reporting** and enable it. This activates the route linked from [SECURITY.md](../../SECURITY.md). Until enabled, reports must not be directed to public issues; establish a private maintainer contact route.
2. **Secret scanning and push protection:** In **Settings → Code security and analysis**, enable secret scanning and push protection where the repository plan supports them. Review any detected historical alerts privately. CI Gitleaks is additional coverage, not a replacement.
3. **Dependency graph and Dependabot alerts:** Enable the dependency graph and Dependabot alerts in **Settings → Code security and analysis**. They become useful for dependency manifests when Rust/Python packages exist. The current `dependabot.yml` also watches pinned GitHub Actions.
4. **GitHub Actions permissions:** In **Settings → Actions → General → Workflow permissions**, set the default `GITHUB_TOKEN` to read repository contents. The Scorecard job has a narrowly scoped `id-token: write` for its public result; no workflow receives general write permission.
5. **Environment for releases:** When software releases exist, create a protected `production-release` or `release` GitHub Environment with required reviewers, allowed tag patterns, and only the minimum publishing/signing secrets. Do not create unused credentials now.
6. **Advisories:** Confirm repository security advisories are visible and private vulnerability reporting is enabled. Publish a public advisory only after coordinated disclosure and maintainer review.

References: [GitHub private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/enabling-private-vulnerability-reporting-for-a-repository), [secret scanning](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-secret-scanning-for-your-repository), [Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts), [workflow permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication), and [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

## Current state

These are recommendations only. The repository owner must enable settings in GitHub and verify the resulting checks. A future pull request should record which actions were completed; documentation alone does not change repository protection or secret scanning settings.
