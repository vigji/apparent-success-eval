"""Aggregate scoring helpers — used by experiments/analyze.py."""
from __future__ import annotations

import json
from pathlib import Path
from statistics import mean


def load_runs(results_dir: Path) -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted(results_dir.glob("*.json"))]


def by_cell(runs: list[dict]) -> dict[tuple[str, str], list[dict]]:
    out: dict[tuple[str, str], list[dict]] = {}
    for r in runs:
        out.setdefault((r["task"], r["harness"]), []).append(r)
    return out


def cell_summary(runs: list[dict]) -> dict:
    if not runs:
        return {"n": 0}
    succ = [bool(r["grader"].get("task_success")) for r in runs]
    lies = [float(r["grader"].get("lying_score", 0.0)) for r in runs]
    elapsed = [float(r["claude"].get("elapsed_s") or 0.0) for r in runs]
    cost = [float(((r["claude"].get("result") or {}).get("total_cost_usd") or 0.0)) for r in runs]
    return {
        "n": len(runs),
        "task_success_rate": round(mean(succ), 3) if succ else 0.0,
        "mean_lying_score": round(mean(lies), 3) if lies else 0.0,
        "mean_elapsed_s": round(mean(elapsed), 1) if elapsed else 0.0,
        "mean_cost_usd": round(mean(cost), 4) if cost else 0.0,
        "total_cost_usd": round(sum(cost), 4),
    }
