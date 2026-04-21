#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "tomlkit>=0.14.0",
# ]
# ///

from __future__ import annotations

import argparse
import dataclasses
import os
import shutil
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import tomlkit

MARKDOWN_TEMPLATE: str = """\
::: {module_path}
    options:
        toc_label: {module_path}
"""
MODULE_SYMBOL: str = '<code class="doc-symbol doc-symbol-toc doc-symbol-module"></code>'


class Args(argparse.Namespace):
    api_root: Path
    docs_dir: Path
    print_nav: bool
    src: Path


@dataclasses.dataclass
class Nav:
    module_path: str = ""
    index: str | None = None
    children: dict[str, Nav] = dataclasses.field(default_factory=dict)

    def add(self, parts: Sequence[str], full_doc_path: Path) -> None:
        if not parts:
            self.index = os.fspath(full_doc_path)
            return
        if parts[0] in self.children:
            child = self.children[parts[0]]
        else:
            child = type(self)(
                module_path=f"{self.module_path}.{parts[0]}"
                if self.module_path
                else parts[0]
            )
            self.children[parts[0]] = child
        child.add(parts[1:], full_doc_path)

    def dump(self) -> Any:
        children: list[Any] = []
        if self.index is not None:
            children.append(self.index)
        for _, child in sorted(self.children.items()):
            children.append(child.dump())
        if len(children) == 1:
            return children[0]
        return {f"{MODULE_SYMBOL} {self.module_path}": children}


def is_public(part: str) -> bool:
    return not part.startswith("_") or (part.startswith("__") and part.endswith("__"))


def parse_args() -> Args:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("src", nargs="?", default="src", type=Path)
    parser.add_argument("--api-root", default="reference/", type=Path)
    parser.add_argument("--docs-dir", default="docs/", type=Path)
    parser.add_argument("--print-nav", action="store_true")
    return parser.parse_args(namespace=Args())


def main() -> None:
    args: Args = parse_args()
    nav = Nav()
    shutil.rmtree(args.docs_dir / args.api_root, ignore_errors=True)
    for path in args.src.rglob("*.py"):
        relative: Path = path.relative_to(args.src)
        module_path: Path = relative.with_suffix("")
        parts: tuple[str, ...] = tuple(module_path.parts)
        if not all(is_public(part) for part in parts):
            continue
        doc_path: Path = relative.with_suffix(".md")
        if parts[-1] == "__init__":
            parts: tuple[str, ...] = parts[:-1]
            doc_path: Path = doc_path.with_name("README.md")
        elif parts[-1] == "__main__":
            continue
        doc_path: Path = args.api_root / doc_path
        full_doc_path: Path = args.docs_dir / doc_path
        full_doc_path.parent.mkdir(parents=True, exist_ok=True)
        full_doc_path.write_text(MARKDOWN_TEMPLATE.format(module_path=".".join(parts)))
        nav.add(parts, doc_path)
    print(tomlkit.dumps(nav.dump()))


if __name__ == "__main__":
    main()
