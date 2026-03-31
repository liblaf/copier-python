#!/usr/bin/env python
import argparse
import ast
import enum
import os
import subprocess
from pathlib import Path
from typing import Any, Never

import tomllib
from packaging.requirements import Requirement


class LazyLoader(enum.StrEnum):
    LAZY_LOADER = enum.auto()
    LIBLAF_LAZY_LOADER = enum.auto()


TEMPLATES: dict[LazyLoader, str] = {
    LazyLoader.LAZY_LOADER: """\
from lazy_loader import attach_stub

__getattr__, __dir__, __all__ = attach_stub(__name__, __file__)

del attach_stub
""",
    LazyLoader.LIBLAF_LAZY_LOADER: """\
from liblaf.lazy_loader import attach_stub

__getattr__, __dir__, __all__ = attach_stub(__name__, __file__, __package__)

del attach_stub
""",
}


class Args(argparse.Namespace):
    path: Path


def detect_lazy_loader(project_root: Path) -> LazyLoader:
    pyproject: Path = project_root / "pyproject.toml"
    with pyproject.open("rb") as fp:
        data: dict[str, Any] = tomllib.load(fp)
    project: Any = data.get("project")
    if not isinstance(project, dict):
        error(f"`project` table not found in: {pyproject}")
    dependencies: Any = project.get("dependencies")
    if not isinstance(dependencies, list):
        error(f"`project.dependencies` not found in: {pyproject}")
    dependency_names: set[str] = set()
    for dep in dependencies:
        req: Requirement = Requirement(dep)
        dependency_names.add(req.name.lower())
    if "liblaf-lazy-loader" in dependency_names:
        return LazyLoader.LIBLAF_LAZY_LOADER
    if "lazy-loader" in dependency_names:
        return LazyLoader.LAZY_LOADER
    error(
        "no supported lazy loader found in project dependencies: "
        "expected `liblaf-lazy-loader` or `lazy-loader`"
    )


def error(message: str) -> Never:
    raise SystemExit(message)


def find_project_root(path: Path) -> Path:
    for candidate in [path, *path.parents]:
        if (candidate / "pyproject.toml").exists():
            return candidate
    error(f"pyproject.toml not found for: {path}")


def get_docstring(file: Path) -> str | None:
    if not file.exists():
        return None
    source: str = file.read_text()
    module: ast.Module = ast.parse(source)
    if not (module.body and isinstance(module.body[0], ast.Expr)):
        return None
    node: ast.expr = module.body[0].value
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return ast.get_source_segment(source, node)
    return None


def git_ls_files(*, project_root: Path, path: Path) -> list[Path]:
    try:
        relative_path: Path = path.relative_to(project_root)
    except ValueError:
        error(f"path is not under project root: {path}")

    result: subprocess.CompletedProcess[str] = subprocess.run(
        [
            "git",
            "-C",
            project_root,
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            relative_path / "__init__.pyi",
            relative_path / "**/__init__.pyi",
        ],
        stdout=subprocess.PIPE,
        check=True,
        text=True,
    )
    return [project_root / line for line in result.stdout.splitlines() if line]


def parse_args() -> Args:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path)
    args: argparse.Namespace = parser.parse_args(namespace=Args())
    if args.path is None:
        if (path := os.getenv("MISE_PROJECT_ROOT")) is not None:
            args.path = Path(path)
        else:
            args.path = Path.cwd()
    args.path = args.path.resolve()
    return args


def render_init(file: Path, *, loader: LazyLoader) -> str:
    docstring: str | None = get_docstring(file)
    template: str = TEMPLATES[loader]
    if docstring is None:
        return template
    return f"{docstring}\n\n{template}"


def main() -> None:
    args: Args = parse_args()
    project_root: Path = find_project_root(args.path)
    loader: LazyLoader = detect_lazy_loader(project_root)
    for pyi in git_ls_files(project_root=project_root, path=args.path):
        py: Path = pyi.with_suffix(".py")
        content: str = render_init(py, loader=loader)
        if py.exists():
            if py.read_text() == content:
                print("skipped:", py)
            else:
                print("updated:", py)
                py.write_text(content)
        else:
            print("created:", py)
            py.write_text(content)


if __name__ == "__main__":
    main()
