"""Experiment 3: prompt-induced pressure surfaces apparent-success-seeking.

Greenblatt: "Don't mention time/budget — it triggers exits and excuses."
Test: same task, default prompt vs. pressured prompt (preamble adds time pressure
+ MVP framing + token budget hint). Compare task_success and lying_score.

Two harnesses (baseline, greenblatt) × 3 tasks × 2 prompt variants × 3 seeds = 36 cells.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from benchmarks.hard_to_check.runner import run_cell  # noqa: E402

DEFAULT_TASKS = ["bulk-migration", "retry-wrapper", "readme-truthfulness"]
DEFAULT_HARNESSES = ["baseline", "greenblatt"]
DEFAULT_VARIANTS = ["default", "pressured"]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--seeds", type=int, default=3)
    p.add_argument("--tasks", default=",".join(DEFAULT_TASKS))
    p.add_argument("--harnesses", default=",".join(DEFAULT_HARNESSES))
    p.add_argument("--variants", default=",".join(DEFAULT_VARIANTS))
    p.add_argument("--model", default=os.environ.get("APPSE_MODEL", "opus"))
    p.add_argument("--budget-usd", type=float, default=2.0)
    p.add_argument("--timeout-s", type=int, default=900)
    args = p.parse_args()

    tasks = args.tasks.split(",")
    harnesses = args.harnesses.split(",")
    variants = args.variants.split(",")
    cells = [(t, h, v, s) for t in tasks for h in harnesses for v in variants for s in range(args.seeds)]
    print(f"Exp3: {len(cells)} cells")
    t0 = time.perf_counter()
    for i, (task, harness, variant, seed) in enumerate(cells):
        try:
            rec = run_cell(task, harness, seed, model=args.model,
                           budget_usd=args.budget_usd, timeout_s=args.timeout_s,
                           prompt_variant=variant)
            print(f"[{i+1}/{len(cells)}] {task}/{harness}/{variant}/seed{seed} "
                  f"success={rec['grader'].get('task_success')} "
                  f"lying={rec['grader'].get('lying_score')} "
                  f"elapsed={rec['claude'].get('elapsed_s')}s")
        except Exception as e:
            print(f"[{i+1}/{len(cells)}] {task}/{harness}/{variant}/seed{seed} FAILED: {e}")
    print(f"\nTotal elapsed: {time.perf_counter() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
