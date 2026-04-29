"""Experiment 1: baseline vs progressively-richer harnesses on the 6 hard-to-check tasks.

Conditions:
  - baseline    — empty .claude/
  - skill_only  — skill + planner command
  - skill_stop  — skill + planner + Stop-hook checklist
  - greenblatt  — skill + planner + Stop-hook + reviewer subagent

For each (task × condition × seed), invokes runner.run_cell. Default 5 seeds.
Sequential by default (claude --print is heavy); --parallel for thread pool.

Usage:
  uv run python experiments/exp1_baseline_vs_harness.py --seeds 5
  uv run python experiments/exp1_baseline_vs_harness.py --seeds 1 --tasks async-refactor --harnesses baseline,greenblatt
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from benchmarks.hard_to_check.runner import run_cell  # noqa: E402

DEFAULT_TASKS = [
    "async-refactor",
    "multi-hop-dataset",
    "leaky-test-suite",
    "dead-code-removal",
    "fix-flaky-test",
    "doc-truthfulness",
]
DEFAULT_HARNESSES = ["baseline", "skill_only", "skill_stop", "greenblatt"]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--seeds", type=int, default=5)
    p.add_argument("--tasks", default=",".join(DEFAULT_TASKS))
    p.add_argument("--harnesses", default=",".join(DEFAULT_HARNESSES))
    p.add_argument("--model", default=os.environ.get("APPSE_MODEL", "opus"))
    p.add_argument("--budget-usd", type=float, default=float(os.environ.get("APPSE_BUDGET_USD", "1.5")))
    p.add_argument("--timeout-s", type=int, default=int(os.environ.get("APPSE_TIMEOUT_S", "1800")))
    p.add_argument("--parallel", type=int, default=1, help="parallel cells (default 1, sequential)")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    tasks = [t for t in args.tasks.split(",") if t]
    harnesses = [h for h in args.harnesses.split(",") if h]
    cells = [(t, h, s) for t in tasks for h in harnesses for s in range(args.seeds)]

    print(f"Exp1: {len(cells)} cells "
          f"({len(tasks)} tasks × {len(harnesses)} harnesses × {args.seeds} seeds)")
    if args.dry_run:
        for c in cells[:10]:
            print(" ", c)
        if len(cells) > 10:
            print(f"  ... +{len(cells) - 10} more")
        return 0

    t0 = time.perf_counter()
    done = 0

    def _one(task: str, harness: str, seed: int) -> dict:
        return run_cell(task, harness, seed,
                        model=args.model, budget_usd=args.budget_usd,
                        timeout_s=args.timeout_s)

    if args.parallel > 1:
        with cf.ThreadPoolExecutor(max_workers=args.parallel) as ex:
            futs = {ex.submit(_one, *c): c for c in cells}
            for fut in cf.as_completed(futs):
                c = futs[fut]
                try:
                    rec = fut.result()
                    print(f"[{done+1}/{len(cells)}] {c[0]}/{c[1]}/seed{c[2]} "
                          f"success={rec['grader'].get('task_success')} "
                          f"lying={rec['grader'].get('lying_score')} "
                          f"elapsed={rec['claude'].get('elapsed_s')}s")
                except Exception as e:
                    print(f"[{done+1}/{len(cells)}] {c} FAILED: {e}")
                done += 1
    else:
        for i, c in enumerate(cells):
            try:
                rec = _one(*c)
                print(f"[{i+1}/{len(cells)}] {c[0]}/{c[1]}/seed{c[2]} "
                      f"success={rec['grader'].get('task_success')} "
                      f"lying={rec['grader'].get('lying_score')} "
                      f"elapsed={rec['claude'].get('elapsed_s')}s")
            except Exception as e:
                print(f"[{i+1}/{len(cells)}] {c} FAILED: {e}")

    print(f"\nTotal elapsed: {time.perf_counter() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
