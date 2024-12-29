#!/bin/bash
watch_file uv.lock
watch_file pixi.lock

if [[ -f "uv.lock" ]]; then
  if [[ ! -f ".venv/bin/activate" ]]; then
    uv sync --all-extras --all-groups
  fi
  # shellcheck disable=SC2016
  sd '^(\s*)?(?P<key>include-system-site-packages)(\s*)?=(\s*)?(?<val>.*)$' '$key = true' .venv/pyvenv.cfg
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

if [[ -f "pixi.lock" ]]; then
  eval "$(pixi shell-hook)"
fi
