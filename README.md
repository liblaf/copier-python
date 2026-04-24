<div align="center" markdown>

![Copier Python](https://socialify.git.ci/liblaf/copier-python/image?custom_language=Python&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2Fcopier-org%2Fcopier%2Frefs%2Fheads%2Fmaster%2Fimg%2Flogo.svg&name=1&owner=1&pattern=Transparent&pulls=1&stargazers=1&theme=Auto)

**[Explore the template files »](https://github.com/liblaf/copier-python/tree/main/template)**

[![Made with Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)
[![MegaLinter](https://github.com/liblaf/copier-python/actions/workflows/shared-mega-linter.yaml/badge.svg)](https://github.com/liblaf/copier-python/actions/workflows/shared-mega-linter.yaml)
[![Release PR](https://github.com/liblaf/copier-python/actions/workflows/release-pr.yaml/badge.svg)](https://github.com/liblaf/copier-python/actions/workflows/release-pr.yaml)
[![Copier Update](https://github.com/liblaf/copier-python/actions/workflows/shared-copier-update.yaml/badge.svg)](https://github.com/liblaf/copier-python/actions/workflows/shared-copier-update.yaml)

[Changelog](https://github.com/liblaf/copier-python/blob/main/CHANGELOG.md) · [Template Files](https://github.com/liblaf/copier-python/tree/main/template) · [Report Bug](https://github.com/liblaf/copier-python/issues) · [Request Feature](https://github.com/liblaf/copier-python/issues)

![Rule](https://cdn.jsdelivr.net/gh/andreasbm/readme/assets/lines/rainbow.png)

</div>

## 🐍 What Is `copier-python`?

`copier-python` is the Python layer in the `liblaf` Copier stack. It turns the shared repository and release foundations into a typed Python package with source layout, docs, tests, benchmarks, generated reference pages, and PyPI publishing through GitHub OIDC.

> [!IMPORTANT]
> Apply [`gh:liblaf/copier-shared`](https://github.com/liblaf/copier-shared), then [`gh:liblaf/copier-release`](https://github.com/liblaf/copier-release), then this template. The Python layer reads shared answers from `.config/copier/.copier-answers.shared.yaml`.

The generated files live under [`template/`](https://github.com/liblaf/copier-python/tree/main/template). The README that generated projects receive is [`template/README.md.jinja`](https://github.com/liblaf/copier-python/blob/main/template/README.md.jinja).

## ✨ What You Get

- 📦 PEP 621 package metadata, Hatchling builds, Hatch VCS versioning, and a `src/` layout with `py.typed`.
- 🧰 `uv` dependency groups for build, docs, lint, nox, and tests.
- 🧪 A `noxfile.py` that discovers supported Python versions and runs highest plus lowest-direct dependency resolutions.
- 📚 Zensical, MkDocs Material, mkdocstrings, Read the Docs, and generated API reference pages.
- 📈 GitHub Actions for tests, coverage, benchmark sessions, docs deployment, and Python release publishing.
- 🔁 Copier answer files and update workflows that let generated repositories keep the stack refreshed.

## 🚀 Apply The Template

After applying the shared and release layers, add the Python layer:

```bash
copier copy --trust gh:liblaf/copier-python .
```

To refresh an existing generated repository:

```bash
copier recopy --trust --answers-file '.config/copier/.copier-answers.python.yaml'
```

## 🧱 Template Stack

- 🧰 [`gh:liblaf/copier-shared`](https://github.com/liblaf/copier-shared): repository hygiene, shared automation, editor settings, and project metadata.
- 🏷️ [`gh:liblaf/copier-release`](https://github.com/liblaf/copier-release): release PRs, changelog generation, tags, GitHub Releases, and publish orchestration.
- 🐍 [`gh:liblaf/copier-python`](https://github.com/liblaf/copier-python): Python packaging, docs, tests, benchmarks, and PyPI workflow wiring.

## 🚢 Release Workflow

In a generated project, the default release flow is:

1. Push commits using Conventional Commits.
2. `release-pr.yaml` opens a release PR with the changelog and next version.
3. Merge the release PR, or approve it and let [`mergery[bot]`](https://github.com/apps/mergery) merge it when checks pass.
4. `release-publish.yaml` creates the tag and publishes the GitHub Release from the merged release PR.
5. The published GitHub Release triggers `python-release.yaml`, which builds the package, publishes to PyPI with OIDC, and uploads distributions as release assets.

This flow assumes immutable GitHub Releases are disabled for generated repositories, so release assets can be attached after the release is published.

## 🛠️ Post Setup

### 📚 Read the Docs

Import the generated repository at <https://app.readthedocs.org/dashboard/import/> and keep `stable` as the default version. The generated [`template/.readthedocs.yaml`](https://github.com/liblaf/copier-python/blob/main/template/.readthedocs.yaml) installs with `uv`, builds with `zensical build`, and publishes the generated `site/` directory.

### 📦 PyPI Trusted Publishing

Create a trusted publisher at <https://pypi.org/manage/account/publishing/> for the generated repository and point it at `.github/workflows/python-release.yaml`. The workflow uses GitHub OIDC, so it does not need a long-lived PyPI API token.

## 🤝 Contributing

Edit files under [`template/`](https://github.com/liblaf/copier-python/tree/main/template) for generated output, and edit [`mise-tasks/`](https://github.com/liblaf/copier-python/tree/main/mise-tasks) for helper behavior used by generated projects. Keep commit messages in Conventional Commit format so the release stack can produce clean changelogs.

[![PR Welcome](https://img.shields.io/badge/%F0%9F%A4%AF%20PR%20WELCOME-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge)](https://github.com/liblaf/copier-python/pulls)

[![Contributors](https://gh-contributors-gamma.vercel.app/api?repo=liblaf/copier-python)](https://github.com/liblaf/copier-python/graphs/contributors)

## 🔗 More Copier Templates

<!-- tangerine-start: projects/copier.md -->

- **[Shared](https://github.com/liblaf/copier-shared)** - ✨ Automated code quality, repository hygiene, and project-wide defaults for the rest of the template stack.
- **[Release](https://github.com/liblaf/copier-release)** - 🚀 Release PRs, changelog generation, tags, GitHub Releases, and publishing automation.
- **[Python](https://github.com/liblaf/copier-python)** - 🐍 Python packaging, docs, tests, benchmarks, and PyPI workflow wiring.
- **[Rust](https://github.com/liblaf/copier-rust)** - 🦀 Rust project template with modern tooling and CI/CD.
- **[TypeScript](https://github.com/liblaf/copier-typescript)** - 🚀 TypeScript project template with modern runtime, tooling, and release automation.

<!-- tangerine-end -->

---

#### 📝 License

Copyright © 2024 [liblaf](https://github.com/liblaf). <br />
This project is [MIT](https://github.com/liblaf/copier-python/blob/main/LICENSE) licensed.
