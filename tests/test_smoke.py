"""Smoke tests — verify project imports without runtime side effects."""

import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_project_root_exists():
    assert ROOT.exists()


def test_python_files_compile():
    for path in ROOT.rglob("*.py"):
        if any(part in {".git", "env", "venv", ".venv"} for part in path.parts):
            continue
        source = path.read_text(encoding="utf-8", errors="ignore")
        compile(source, str(path), "exec")
