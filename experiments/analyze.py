"""Aggregate Exp 1 + Exp 2 results into a summary table.

Usage:
  uv run python experiments/analyze.py
  uv run python experiments/analyze.py --runs-dir results/runs --detection results/detection/detection_results.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from statistics import mean, stdev

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from benchmarks.hard_to_check.score import load_runs, by_cell, cell_summary  # noqa: E402

try:
    from scipy import stats  # type: ignore
    HAVE_SCIPY = True
except Exception:
    HAVE_SCIPY = False


def _paired_test(baseline: list[float], treated: list[float]) -> dict:
    if not HAVE_SCIPY or len(baseline) != len(treated) or len(baseline) < 2:
        return {"available": False}
    t, p = stats.wilcoxon(baseline, treated, zero_method="zsplit") \
        if any(b - t for b, t in zip(baseline, treated)) else (0.0, 1.0)
    return {"available": True, "wilcoxon_stat": float(t), "p_value": float(p)}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--runs-dir", default=str(REPO_ROOT / "results" / "runs"))
    p.add_argument("--detection", default=str(REPO_ROOT / "results" / "detection" / "detection_results.json"))
    p.add_argument("--out", default=str(REPO_ROOT / "results" / "summary.json"))
    args = p.parse_args()

    runs = load_runs(Path(args.runs_dir))
    print(f"Loaded {len(runs)} Exp 1 runs from {args.runs_dir}\n")

    cells = by_cell(runs)
    tasks = sorted({k[0] for k in cells.keys()})
    harnesses = sorted({k[1] for k in cells.keys()})

    summary: dict = {"per_cell": {}, "per_harness": {}, "tests": {}}

    print("=" * 82)
    print(f"{'task':<22} {'harness':<14} {'n':>3} {'success':>8} {'lying':>7} {'sec':>6} {'cost':>7}")
    print("=" * 82)
    for task in tasks:
        for h in harnesses:
            cell_runs = cells.get((task, h), [])
            s = cell_summary(cell_runs)
            summary["per_cell"][f"{task}::{h}"] = s
            print(f"{task:<22} {h:<14} {s['n']:>3} {s.get('task_success_rate', 0):>8} "
                  f"{s.get('mean_lying_score', 0):>7} {s.get('mean_elapsed_s', 0):>6} "
                  f"{s.get('mean_cost_usd', 0):>7}")
    print("=" * 82)

    print("\n--- Per-harness aggregate (mean across all tasks) ---")
    print(f"{'harness':<14} {'n':>4} {'mean_success':>14} {'mean_lying':>12} {'total_cost':>12}")
    for h in harnesses:
        runs_h = [r for r in runs if r["harness"] == h]
        if not runs_h:
            continue
        succ = mean(bool(r["grader"].get("task_success")) for r in runs_h)
        lies = mean(float(r["grader"].get("lying_score") or 0) for r in runs_h)
        cost = sum(float(((r["claude"].get("result") or {}).get("total_cost_usd") or 0)) for r in runs_h)
        summary["per_harness"][h] = {
            "n": len(runs_h),
            "mean_task_success_rate": round(succ, 3),
            "mean_lying_score": round(lies, 3),
            "total_cost_usd": round(cost, 4),
        }
        print(f"{h:<14} {len(runs_h):>4} {round(succ, 3):>14} {round(lies, 3):>12} {round(cost, 4):>12}")

    # Paired tests: greenblatt vs baseline on lying score, per task.
    print("\n--- Paired tests: greenblatt vs baseline lying score, per task ---")
    print(f"{'task':<22} {'baseline_lying':>14} {'greenblatt_lying':>17} {'p':>10}")
    for task in tasks:
        b_runs = sorted(cells.get((task, "baseline"), []), key=lambda r: r["seed"])
        g_runs = sorted(cells.get((task, "greenblatt"), []), key=lambda r: r["seed"])
        n = min(len(b_runs), len(g_runs))
        if n < 2:
            continue
        b_lies = [float(r["grader"].get("lying_score") or 0) for r in b_runs[:n]]
        g_lies = [float(r["grader"].get("lying_score") or 0) for r in g_runs[:n]]
        test = _paired_test(b_lies, g_lies)
        p_str = f"{test.get('p_value', 'NA'):.4f}" if test.get("available") else "NA"
        summary["tests"][task] = {
            "n_pairs": n,
            "baseline_mean_lying": round(mean(b_lies), 3),
            "greenblatt_mean_lying": round(mean(g_lies), 3),
            **test,
        }
        print(f"{task:<22} {round(mean(b_lies),3):>14} {round(mean(g_lies),3):>17} {p_str:>10}")

    # Detection metrics if present.
    det_p = Path(args.detection)
    if det_p.exists():
        det = json.loads(det_p.read_text())
        m = det.get("metrics", {})
        summary["detection"] = m
        print("\n--- Reviewer detection (Exp 2) ---")
        print(f"n trajectories: {m.get('n')}, n hacked: {m.get('n_hack')}")
        for k in ("generic", "taxonomy"):
            r = m.get(k, {})
            print(f"  {k:<10} P={r.get('precision')} R={r.get('recall')} F1={r.get('f1')} acc={r.get('accuracy')}")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(summary, indent=2))
    print(f"\nWrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
