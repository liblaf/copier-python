from typing import Any

import nox

nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True
nox.options.tags = ["test"]
PYPROJECT: dict[str, Any] = nox.project.load_toml("pyproject.toml")
PYTHON_VERSIONS: list[str] = nox.project.python_versions(PYPROJECT)


def _install(s: nox.Session, *, resolution: str) -> None:
    s.install(
        "--exact",
        "--strict",
        "--editable",
        ".",
        "--group",
        "test",
        env={"UV_RESOLUTION": resolution},
    )


def _pytest(s: nox.Session, *args: str) -> None:
    s.run("pytest", *args, *s.posargs, env={"EAGER_IMPORT": "1"}, success_codes=[0, 5])


@nox.session(tags=["bench"])
def bench(s: nox.Session) -> None:
    _install(s, resolution="highest")
    _pytest(s, "-m", "benchmark", "--codspeed")


@nox.session(python=PYTHON_VERSIONS, tags=["test"])
@nox.parametrize(
    "resolution",
    [
        nox.param("highest", id="highest", tags=["highest"]),
        nox.param("lowest-direct", id="lowest-direct", tags=["lowest-direct"]),
    ],
)
def test(s: nox.Session, resolution: str) -> None:
    _install(s, resolution=resolution)
    _pytest(s, "--cov")
