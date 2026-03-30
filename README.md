<div align="center"><a name="readme-top"></a>

![copier-python](https://socialify.git.ci/liblaf/copier-python/image?custom_language=Python&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2Fcopier-org%2Fcopier%2Frefs%2Fheads%2Fmaster%2Fimg%2Flogo.svg&name=1&owner=1&pattern=Transparent&pulls=1&stargazers=1&theme=Auto)

[![Made with Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)

[Changelog](https://github.com/liblaf/copier-python/blob/main/CHANGELOG.md) · [Report Bug](https://github.com/liblaf/copier-python/issues) · [Request Feature](https://github.com/liblaf/copier-python/issues)

![Rule](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

</div>

## ✨ Features

- 🐍 Bootstraps a modern Python project on a typed `src/` layout.
- 🧱 Designed to layer on top of [`gh:liblaf/copier-shared`](https://github.com/liblaf/copier-shared) and [`gh:liblaf/copier-release`](https://github.com/liblaf/copier-release).
- ⚡ Uses `uv` for dependency management and `mise` for repeatable local tasks.
- ✅ Ships with `nox`, `pytest`, coverage, Ruff, import-linter, and shared repository defaults.
- 📚 Generates docs with Zensical, MkDocs Material, mkdocstrings, GitHub Pages, and Read the Docs.
- 🚀 Builds with Hatchling plus Hatch VCS and publishes to PyPI and GitHub Releases.
- 🧪 Includes benchmark workflow wiring with CodSpeed.

## 🧱 Template Stack

This template is the Python layer of a three-template setup:

1. [`gh:liblaf/copier-shared`](https://github.com/liblaf/copier-shared)
2. [`gh:liblaf/copier-release`](https://github.com/liblaf/copier-release)
3. `gh:liblaf/copier-python`

Apply them in that order. `copier-python` expects the shared project metadata and release automation from the first two templates to already exist.

## 🚀 Create a Project

```bash
copier copy gh:liblaf/copier-shared .
copier copy gh:liblaf/copier-release .
copier copy gh:liblaf/copier-python .
```

To refresh the Python layer later:

```bash
copier recopy --answers-file '.config/copier/.copier-answers.python.yaml'
```

The generated repository will also keep the answers files from the shared and release templates, so automated Copier update workflows can refresh the full stack.

## 🧰 What You Get

- `pyproject.toml` with PEP 621 metadata, dependency groups, Hatchling packaging, and Hatch VCS versioning.
- `noxfile.py` with reusable test sessions across declared Python versions plus tagged dependency-resolution variants.
- `.config/mise/conf.d/50-python.toml` with ready-to-run tasks such as `install`, `lint`, `docs:build`, `docs:serve`, `gen:init`, and `upgrade`.
- `zensical.toml`, `.readthedocs.yaml`, and Python-specific GitHub Actions workflows for docs, tests, benchmarks, and publishing.
- A typed package skeleton under `src/` with `py.typed`, version stubs, and lazy-loader friendly `__init__.py` generation from `__init__.pyi`.

## ⌨️ Local Development

After generating a project from this template, the usual workflow is:

```bash
mise run install
mise run lint
nox
mise run docs:serve
```

Useful extra commands:

- `mise run docs:build` to build the docs site locally.
- `mise run gen:init` to regenerate `__init__.py` files from `__init__.pyi` stubs.
- `mise run upgrade` to refresh dependencies from lockfiles.
- `nox --tags bench` to run benchmark sessions when the project contains benchmarks.

## 🔄 Release Workflow

For repositories bootstrapped with `copier-release`, the default release flow is:

1. Conventional Commits on `main` trigger `release-pr.yaml`, which opens a release PR with an updated changelog.
2. Review and approve the release PR, or wait for the scheduled auto-review. [`mergery[bot]`](https://github.com/apps/mergery) merges the PR.
3. After the release PR is merged, `release-draft.yaml` creates a draft release.
4. `python-release.yaml` builds the package, publishes it to PyPI with OIDC, and uploads the release assets to the draft release.
5. `release-publish.yaml` publishes the draft release after 6 hours, which gives the release jobs time to finish.

## 🛠️ Post Setup

### Read the Docs

1. Visit <https://app.readthedocs.org/dashboard/import/>.
2. Follow the prompts to import the repository.
3. In project settings, configure:

| Location                             | Value                                         |
| ------------------------------------ | --------------------------------------------- |
| `Setup > Settings > Default version` | `stable`                                      |
| `Setup > Settings`                   | Enable `Build pull requests for this project` |
| `Setup > Addons > Analytics`         | Enable                                        |
| `Setup > Addons > Link previews`     | Enable                                        |
| `Building > Pull request builds`     | Enable `Build pull requests for this project` |
| `Building > Pull request builds`     | Enable `Show build overview in a comment`     |

4. Add an automation rule with:

| Field          | Value                 |
| -------------- | --------------------- |
| `Description`  | `Semantic Versioning` |
| `Match`        | `SemVer versions`     |
| `Version type` | `Tag`                 |
| `Action`       | `Activate version`    |

### PyPI Publish

1. Visit <https://pypi.org/manage/account/publishing/>.
2. Add a trusted publisher for the generated repository.
3. Use the GitHub Actions workflow and environment from the generated release setup:

| Field              | Value              |
| ------------------ | ------------------ |
| `Workflow name`    | `Python / Release` |
| `Environment name` | `PyPI`             |

The remaining form fields should match the GitHub owner, repository, and PyPI project name generated for your package.

## 🤝 Contributing

Contributions are welcome. If you want to improve the template, update the files under [`template/`](https://github.com/liblaf/copier-python/tree/main/template) and any shared helper files used during generation, then keep commit messages in Conventional Commits format so the release automation can do its job.

[![PR Welcome](https://img.shields.io/badge/%F0%9F%A4%AF%20PR%20WELCOME-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge)](https://github.com/liblaf/copier-python/pulls)

[![Contributors](https://contrib.nn.ci/api?repo=liblaf/copier-python)](https://github.com/liblaf/copier-python/graphs/contributors)

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
