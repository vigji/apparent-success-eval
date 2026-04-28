# apparent-success-eval

A small research prototype that implements Ryan Greenblatt's proposed mitigations for *apparent-success-seeking* in current LLMs (LessWrong 2026-04-15) and measures whether they actually work.

## What this is

Greenblatt observed that frontier models, when given long fuzzy hard-to-check tasks, optimize for *looking* successful instead of *being* successful — incomplete refactors written up as "additive," reward-hacks not flagged saliently, end-to-end tests avoided. He proposes a harness stack (Stop-hook checklist, fresh-context reviewer subagents with a cheating taxonomy, outer-loop planner, a `completing-larger-autonomous-tasks` skill) that he says reduces the failure mode at the cost of bloat. He calls for the field to build evals targeting this regime.

This repo builds the harness as a Claude Code project (`.claude/` directory: hooks, skills, agents, slash commands), and verifies it on:

1. **Custom 6-task hard-to-check suite** — async-refactor, multi-hop-dataset, leaky-test-suite, dead-code-removal, fix-flaky-test, doc-truthfulness. Each task has a hidden grader that scores both `task_success` and a `lying_score` (gap between what the agent claimed and what the workspace shows).
2. **TRACE** (Patronus AI, arXiv 2601.20103) — 517 trajectories of reward-exploit detection. Used to ablate the reviewer's cheating taxonomy.

## Layout

- `harnesses/{baseline,skill_only,skill_stop,greenblatt}/.claude/` — four Claude Code harness variants for the ablation.
- `benchmarks/hard_to_check/` — 6 tasks + runner + grader.
- `benchmarks/trace/` — TRACE loader + reviewer detection eval.
- `experiments/` — exp1 (baseline vs harness), exp2 (reviewer taxonomy), analyze.
- `tests/` — pytest plumbing.

## Reproducing

```bash
uv sync
# Smoke test
uv run python -m benchmarks.hard_to_check.runner --task async-refactor --harness baseline --seed 0
# Full Exp 1 (120 runs, ~$36)
uv run python experiments/exp1_baseline_vs_harness.py
# Full Exp 2 (~400 calls, ~$20)
uv run python experiments/exp2_reviewer_taxonomy.py
# Aggregate
uv run python experiments/analyze.py results/
```

Set `ANTHROPIC_API_KEY` in your environment.

## License

MIT
