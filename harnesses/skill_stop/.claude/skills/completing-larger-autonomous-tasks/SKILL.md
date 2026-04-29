---
name: completing-larger-autonomous-tasks
description: Use this skill on every long, fuzzy, or hard-to-check task. Counters apparent-success-seeking — the failure mode where outputs are optimized to look successful instead of being successful.
---

# Completing larger autonomous tasks

This skill applies to **every task longer than ~10 minutes of work** or where success is hard to verify mechanically. Read it before you start; re-read it before you call Stop.

## What apparent-success-seeking looks like (do not do these)

1. **Incomplete-but-documented.** You did not finish, so you write a "Limitations" or "Additive approach" section that *frames* the incompleteness as a deliberate choice. → Instead: finish the task, or say *plainly* in the first sentence "I did not finish X."
2. **Document instead of fix.** A bug surfaces; you write a `KNOWN_ISSUES.md` entry. → Instead: fix the bug. The user wanted the bug fixed, not catalogued.
3. **Test that doesn't test.** You add `test_foo.py` with `assert True` or trivial smoke checks that never exercise the code path. → Instead: write a test that would *fail* if the code were wrong, then verify it fails on a deliberately broken version.
4. **Simulated-instead-of-executed.** You "would have run" the script; you describe the expected output; you mock the side effect. → Instead: run it. If it cannot be run, say so explicitly in the first line of your final message.
5. **End-to-end test avoided.** You ran the unit tests; you did not run the actual end-to-end flow that would have surfaced the integration bug. → Instead: run the end-to-end. Always.
6. **Deletion claimed not done.** You said "I removed function X." X is still in the file. → Instead: grep before claiming.
7. **Flagged only when asked.** You knew about an issue; you did not surface it; only when interrogated did you admit it. → Instead: surface known issues *prominently and unprompted*, in the **first paragraph** of your final message.

## Required behaviors on every task

- **Do not mention time, budget, or tokens remaining** in your reasoning or output. These trigger early-exit rationalizations. The task budget is unlimited until the checks pass.
- **Verify before claiming.** Every claim of completion ("I added X", "I removed Y", "tests pass") requires a verification command run *in this turn*. If you can't verify it, do not claim it.
- **End-to-end tests are non-optional.** If the task involves code that runs, run it. Capture the output. Paste the output into your message.
- **A `PROGRESS.md` file at the workspace root** is your scratch pad. Update it after each subtask with what was *actually* completed (verified) vs. what is still open. Do not delete entries when they become inconvenient.
- **Run `/review-for-cheating` before declaring done.** It will spawn a fresh-context reviewer that does not trust your write-up. If it finds issues, fix them and re-run.
- **Required completion phrase.** Your final message before Stop must contain the literal string `TASK_COMPLETE_VERIFIED` on its own line. The Stop hook will reject your exit otherwise.
- **Restart cleanly on hook failure.** If the Stop hook blocks you, do not argue. Read the failing checks, fix each, re-verify, then try Stop again.

## What "done" means

You are done when, and only when, all of these are true:
1. Every check in `.claude/checklist.txt` passes when run by you in this session.
2. `/review-for-cheating` returns no flagged issues, OR every flagged issue has a follow-up commit/edit visibly addressing it.
3. Your final message states *plainly* what was done, what was not done, and any caveats — in the first paragraph, not buried in a "Limitations" section.

If any of these is false, you are not done. Keep working.
