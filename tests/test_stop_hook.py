"""Test the Stop hook restart logic."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HOOK = REPO_ROOT / "harnesses" / "greenblatt" / ".claude" / "hooks" / "exit_checklist.sh"


def _run_hook(workspace: Path) -> tuple[int, str]:
    env = os.environ.copy()
    env["CLAUDE_PROJECT_DIR"] = str(workspace)
    proc = subprocess.run(
        ["bash", str(HOOK)],
        cwd=workspace,
        env=env,
        input="{}",
        capture_output=True,
        text=True,
        timeout=15,
    )
    return proc.returncode, proc.stdout


def test_no_checklist_allows_stop(tmp_path: Path) -> None:
    (tmp_path / ".claude").mkdir()
    rc, out = _run_hook(tmp_path)
    assert rc == 0
    assert out.strip() == ""


def test_passing_checklist_allows_stop(tmp_path: Path) -> None:
    claude = tmp_path / ".claude"
    claude.mkdir()
    (claude / "checklist.txt").write_text("true\necho ok\n")
    rc, out = _run_hook(tmp_path)
    assert rc == 0
    assert out.strip() == ""


def test_failing_checklist_blocks_stop(tmp_path: Path) -> None:
    claude = tmp_path / ".claude"
    claude.mkdir()
    (claude / "checklist.txt").write_text("true\nfalse\nls /this/does/not/exist\n")
    rc, out = _run_hook(tmp_path)
    # Stop-hook protocol: exit 0 with JSON on stdout = "block"
    assert rc == 0
    parsed = json.loads(out)
    assert parsed["decision"] == "block"
    assert "EXIT CHECKLIST FAILED" in parsed["reason"]
    assert "false" in parsed["reason"]


def test_attempts_bounded(tmp_path: Path) -> None:
    claude = tmp_path / ".claude"
    claude.mkdir()
    (claude / "checklist.txt").write_text("false\n")
    # Drive 9 attempts; on the 9th, hook should give up (allow Stop).
    for i in range(8):
        rc, out = _run_hook(tmp_path)
        assert rc == 0
        assert json.loads(out)["decision"] == "block"
    rc, out = _run_hook(tmp_path)
    assert rc == 0
    # On the 9th attempt the hook gives up: empty stdout = allow Stop.
    assert out.strip() == ""


def test_passing_resets_attempts(tmp_path: Path) -> None:
    claude = tmp_path / ".claude"
    claude.mkdir()
    (claude / "checklist.txt").write_text("false\n")
    rc, out = _run_hook(tmp_path)
    assert json.loads(out)["decision"] == "block"
    # Replace with passing checklist; attempts file should be deleted on pass.
    (claude / "checklist.txt").write_text("true\n")
    rc, out = _run_hook(tmp_path)
    assert rc == 0
    assert out.strip() == ""
    assert not (claude / "local" / "stop_attempts").exists()
