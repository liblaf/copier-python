#!/bin/bash
# This file is @generated by <https://github.com/liblaf/copier-python>.
# DO NOT EDIT!
set -o errexit
set -o nounset
set -o pipefail

function replace-mirrors() {
  local file="$1"
  if [[ -f $file ]]; then
    # ref: <https://github.com/astral-sh/uv/issues/6349#issuecomment-3076752818>
    sd 'https://(\S+)/packages\b' 'https://files.pythonhosted.org/packages' "$file"
    sd 'https://(\S+)/simple\b' 'https://pypi.org/simple' "$file"
  fi
}

if [[ -f 'pixi.lock' ]]; then
  pixi install
  replace-mirrors 'pixi.lock'
fi

if [[ -f 'uv.lock' ]]; then
  uv sync --all-extras --all-groups
  replace-mirrors 'uv.lock'
fi
