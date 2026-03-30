<div align="center" markdown>

![Copier Python](https://socialify.git.ci/liblaf/copier-python/image?custom_language=Python&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2Fcopier-org%2Fcopier%2Frefs%2Fheads%2Fmaster%2Fimg%2Flogo.svg&name=1&owner=1&pattern=Transparent&pulls=1&stargazers=1&theme=Auto)

**[Browse the template files »](https://github.com/liblaf/copier-python/tree/main/template)**

[![Made with Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)
[![MegaLinter](https://github.com/liblaf/copier-python/actions/workflows/mega-linter.yaml/badge.svg)](https://github.com/liblaf/copier-python/actions/workflows/mega-linter.yaml)
[![Release PR](https://github.com/liblaf/copier-python/actions/workflows/release-pr.yaml/badge.svg)](https://github.com/liblaf/copier-python/actions/workflows/release-pr.yaml)
[![Copier Update](https://github.com/liblaf/copier-python/actions/workflows/copier-update.yaml/badge.svg)](https://github.com/liblaf/copier-python/actions/workflows/copier-update.yaml)

[Changelog](https://github.com/liblaf/copier-python/blob/main/CHANGELOG.md) · [Template Files](https://github.com/liblaf/copier-python/tree/main/template) · [Report Bug](https://github.com/liblaf/copier-python/issues) · [Request Feature](https://github.com/liblaf/copier-python/issues)

![Rule](https://cdn.jsdelivr.net/gh/andreasbm/readme/assets/lines/rainbow.png)

</div>

## 🐍 What Is `copier-python`?

`copier-python` is the Python layer in the `liblaf` Copier stack. It adds packaging, typed source layout, documentation, testing, benchmarking, and PyPI publishing on top of the shared repository and release foundations.

> [!IMPORTANT]
> This template depends on [`gh:liblaf/copier-shared`](https://github.com/liblaf/copier-shared) and [`gh:liblaf/copier-release`](https://github.com/liblaf/copier-release). Apply the stack in that order: shared → release → python.

If you want the real source of truth for generated files, start in [`template/`](https://github.com/liblaf/copier-python/tree/main/template). This repository README documents the template itself; the generated project README comes from [`template/README.md.jinja`](https://github.com/liblaf/copier-python/blob/main/template/README.md.jinja).

## ✨ What You Get

- 📦 A modern Python package layout under `src/`, including `py.typed`, version stubs, and lazy-loader-friendly package exports.
- ⚙️ A `pyproject.toml` wired for PEP 621 metadata, `uv` dependency groups, Hatchling builds, and Hatch VCS versioning.
- 🧪 A `noxfile.py` with multi-version test sessions, dependency resolution variants, and optional benchmark sessions.
- 📚 Docs scaffolding with Zensical, MkDocs Material, mkdocstrings, GitHub-friendly Markdown, and Read the Docs configuration.
- 🚀 Release automation that fits the rest of the `liblaf` Copier stack, including changelog generation, draft releases, and PyPI publishing through OIDC.
- 🔁 Copier-friendly update paths so the generated repository can be refreshed later without redoing the whole setup by hand.

## 🚀 Apply The Template

After applying the shared and release templates, add the Python layer with:

```bash
copier copy --trust gh:liblaf/copier-python .
```

## 🔄 Update The Template

To refresh the Python layer in an existing repository:

```bash
copier recopy --trust --answers-file '.config/copier/.copier-answers.python.yaml'
```

The generated repository usually keeps separate Copier answers files for each layer, so scheduled update workflows can refresh the whole stack over time.

## 🧱 Template Stack

- 🧰 [`gh:liblaf/copier-shared`](https://github.com/liblaf/copier-shared): repository hygiene, common automation, editor settings, and shared project metadata.
- 🏷️ [`gh:liblaf/copier-release`](https://github.com/liblaf/copier-release): release PRs, changelog generation, Git tags, GitHub Releases, and publish orchestration.
- 🐍 [`gh:liblaf/copier-python`](https://github.com/liblaf/copier-python): Python packaging, docs, tests, benchmarks, and PyPI workflow wiring.

## 🚢 Release Workflow

In a generated project, the default release flow looks like this:

1. Push commits using Conventional Commits.
2. `release-pr.yaml` creates a release PR with the changelog and updated version.
3. Merge the release PR yourself, or approve it and let [`mergery[bot]`](https://github.com/apps/mergery) merge it once the button is green.
4. `release-draft.yaml` creates a draft release.
5. `python-release.yaml` builds the package, publishes it to PyPI with GitHub OIDC, and uploads release assets to the draft release.
6. `release-publish.yaml` publishes the draft release after 6 hours so the release jobs have enough time to finish.

## 🛠️ Post Setup

### 📚 Read the Docs

1. Visit <https://app.readthedocs.org/dashboard/import/>.
2. Follow the prompts to import the generated repository.
3. Configure these settings:

| Location | Value |
| --- | --- |
| `Setup > Settings > Default version` | `stable` |
| `Setup > Settings` | Enable `Build pull requests for this project` |
| `Setup > Addons > Analytics` | Enable |
| `Setup > Addons > Link previews` | Enable |
| `Building > Pull request builds` | Enable `Build pull requests for this project` |
| `Building > Pull request builds` | Enable `Show build overview in a comment` |

4. Add this automation rule:

| Field | Value |
| --- | --- |
| `Description` | `Semantic Versioning` |
| `Match` | `SemVer versions` |
| `Version type` | `Tag` |
| `Action` | `Activate version` |

### 📦 PyPI Trusted Publishing

1. Visit <https://pypi.org/manage/account/publishing/>.
2. Create a trusted publisher for the generated repository.
3. Point it at the GitHub Actions release workflow created by this template stack.

This template publishes with GitHub OIDC, so you do not need a long-lived PyPI API token.

## 🤝 Contributing

To improve the template, edit the files under [`template/`](https://github.com/liblaf/copier-python/tree/main/template) and the small helper files around it, then keep commit messages in Conventional Commits format so the release automation can do its job cleanly.

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
