"""Test runner workspace setup (does NOT call claude — just verifies plumbing)."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from benchmarks.hard_to_check.runner import setup_workspace  # noqa: E402


def test_setup_workspace_baseline(tmp_path: Path) -> None:
    setup_workspace("async-refactor", "baseline", tmp_path)
    assert (tmp_path / ".claude" / "settings.json").exists()
    assert (tmp_path / "app.py").exists()
    assert (tmp_path / "test_app.py").exists()
    # Baseline: no checklist (per-task checklist still copied for grading purposes? we always copy)
    assert (tmp_path / ".claude" / "checklist.txt").exists()


def test_setup_workspace_greenblatt(tmp_path: Path) -> None:
    setup_workspace("async-refactor", "greenblatt", tmp_path)
    claude = tmp_path / ".claude"
    assert (claude / "settings.json").exists()
    assert (claude / "hooks" / "exit_checklist.sh").exists()
    assert (claude / "skills" / "completing-larger-autonomous-tasks" / "SKILL.md").exists()
    assert (claude / "agents" / "reviewer.md").exists()
    assert (claude / "commands" / "plan-and-decompose.md").exists()
    assert (claude / "commands" / "review-for-cheating.md").exists()
    assert (claude / "checklist.txt").exists()
    # Hook must be executable.
    import os, stat
    mode = (claude / "hooks" / "exit_checklist.sh").stat().st_mode
    assert mode & stat.S_IXUSR


def test_setup_workspace_unknown_task(tmp_path: Path) -> None:
    import pytest
    with pytest.raises(SystemExit):
        setup_workspace("nope", "baseline", tmp_path)


def test_setup_workspace_unknown_harness(tmp_path: Path) -> None:
    import pytest
    with pytest.raises(SystemExit):
        setup_workspace("async-refactor", "nope", tmp_path)
