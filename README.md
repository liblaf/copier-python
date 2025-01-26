<div align="center"><a name="readme-top"></a>

<img height="120" src="https://raw.githubusercontent.com/copier-org/copier/refs/heads/master/img/logo.svg" />
<img height="120" src="https://gw.alipayobjects.com/zos/kitchen/qJ3l3EPsdW/split.svg" />
<img height="120" src="https://api.iconify.design/devicon/python.svg" />

<h1>Copier Python</h1>

This repository provides a robust Python project template with advanced features including lazy loading, comprehensive linting, and flexible package management. It offers a streamlined development experience with automated initialization scripts, customizable build configurations, and support for modern Python tooling.

[![][copier-shield]][copier-link] <br />
[![][github-contributors-shield]][github-contributors-link]
[![][github-forks-shield]][github-forks-link]
[![][github-stars-shield]][github-stars-link]
[![][github-issues-shield]][github-issues-link]
[![][github-license-shield]][github-license-link]

[Changelog](./CHANGELOG.md) · [Report Bug][github-issues-link] · [Request Feature][github-issues-link]

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

</div>

[copier-link]: https://github.com/copier-org/copier
[copier-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json
[github-contributors-link]: https://github.com/liblaf/copier-python/graphs/contributors
[github-contributors-shield]: https://img.shields.io/github/contributors/liblaf/copier-python
[github-forks-link]: https://github.com/liblaf/copier-python/forks
[github-forks-shield]: https://img.shields.io/github/forks/liblaf/copier-python
[github-issues-link]: https://github.com/liblaf/copier-python/issues
[github-issues-shield]: https://img.shields.io/github/issues/liblaf/copier-python
[github-license-link]: https://github.com/liblaf/copier-python/blob/main/LICENSE
[github-license-shield]: https://img.shields.io/github/license/liblaf/copier-python
[github-stars-link]: https://github.com/liblaf/copier-python/stargazers
[github-stars-shield]: https://img.shields.io/github/stars/liblaf/copier-python

## ✨ Features

- 🛠️ **Automated Initialization:** The `gen-init.sh` script automatically generates `__init__.py` files using `lazy_loader`, simplifying the process of setting up Python packages;
- 📜 **Customizable Project Templates:** The repository provides flexible Jinja templates for `pyproject.toml` and `Justfile`, allowing for easy customization of project configurations;
- 🔧 **Integrated Linting and Building:** The `Justfile` includes commands for linting (using `ruff`) and building Python packages, ensuring code quality and consistency;
- 📦 **Package Manager Support:** The project supports both `pixi` and `uv` package managers, with configurations for `pixi` included in the `pyproject.toml` template;
- 📄 **License Flexibility:** The repository includes a default MIT License but allows for customization through the `copier.yaml` configuration, making it easy to adapt to different licensing needs;
- 🧩 **Stub File Integration:** The `__builtins__.pyi` file provides type hints and integrates with tools like `pyright` for enhanced static type checking;
- 🔄 **Version Control Ready:** The `copier.yaml` file ensures that the repository is set up for version control, with options to skip existing files and manage project-specific answers.

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-black?style=flat-square

## 📦 Installation

To install `gh:liblaf/copier-python`, run the following command:

```bash
$ copier copy --trust gh:liblaf/copier-python .
```

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-black?style=flat-square

## ⌨️ Local Development

You can use Github Codespaces for online development:

[![][github-codespace-shield]][github-codespace-link]

Or clone it for local development:

```bash
$ git clone https://github.com/liblaf/copier-python.git
$ cd copier-python
```

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[github-codespace-shield]: https://github.com/codespaces/badge.svg
[github-codespace-link]: https://codespaces.new/liblaf/copier-python
[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-black?style=flat-square

## 🤝 Contributing

Contributions of all types are more than welcome, if you are interested in contributing code, feel free to check out our GitHub [Issues][github-issues-link] to get stuck in to show us what you’re made of.

[![][pr-welcome-shield]][pr-welcome-link]

[![][github-contrib-shield]][github-contrib-link]

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[github-issues-link]: https://github.com/liblaf/copier-python/issues
[pr-welcome-shield]: https://img.shields.io/badge/%F0%9F%A4%AF%20PR%20WELCOME-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge
[pr-welcome-link]: https://github.com/liblaf/copier-python/pulls
[github-contrib-shield]: https://contrib.rocks/image?repo=liblaf%2Fcopier-python
[github-contrib-link]: https://github.com/liblaf/copier-python/graphs/contributors
[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-black?style=flat-square

## 🔗 Links

### More Copier Templates

- **[Copier Python](https://github.com/liblaf/copier-python)** - 🚀 A comprehensive Python project template with automated workflows, CI/CD integration, and modern development tools. Features include MegaLinter for code quality, Copier for template updates, and Renovate for dependency management. Perfect for building scalable Python packages with best practices! 🐍✨
- **[Copier Release](https://github.com/liblaf/copier-release)** - 🚀 Automated GitHub Repository Management Toolkit: A comprehensive set of workflows and templates for automating repository maintenance, PR management, and release processes. Includes Copier updates, MegaLinter integration, and Release Please automation. Perfect for maintaining clean, consistent, and efficient GitHub repositories! 🛠️✨
- **[Copier Share](https://github.com/liblaf/copier-share)** - 🤖✨ A comprehensive GitHub repository template with automated workflows for PR management, repository maintenance, and code quality checks. Features include auto-merging PRs, Copier updates, label synchronization, and MegaLinter integration for consistent code standards. Perfect for maintaining clean, efficient, and well-organized repositories! 🚀🔧
- **[Copier Typescript](https://github.com/liblaf/copier-typescript)** - 🚀 A robust TypeScript project template with automated workflows, CI/CD pipelines, and comprehensive linting. Features include auto-PR management, copier updates, and MegaLinter integration for code quality. Perfect for scalable, maintainable, and efficient TypeScript projects! 🛠️✨

### Credits

- **copier** - <https://github.com/copier-org/copier>

<div align="right">

[![][back-to-top]](#readme-top)

</div>

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-black?style=flat-square
