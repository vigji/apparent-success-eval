"""Experiment 2: reviewer-prompt ablation (taxonomy vs generic) on Exp 1 trajectories.

Thin wrapper around benchmarks.trace.run_detection — the dataset is the Exp 1
output, and the comparison is "does Greenblatt's cheating taxonomy in the
reviewer system prompt improve hack-detection over a generic 'are there problems?'
prompt?"

Run experiments/exp1_baseline_vs_harness.py first; this consumes its results/runs.

Usage:
  uv run python experiments/exp2_reviewer_taxonomy.py
  uv run python experiments/exp2_reviewer_taxonomy.py --max-runs 50
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from benchmarks.trace.run_detection import main  # noqa: E402


if __name__ == "__main__":
    sys.exit(main())
