---
description: Decompose the current task into verifiable subtasks before starting work. Counters end-to-end-avoidance and incomplete-but-documented.
---

You are at the **start** of a task. Before writing any code:

1. Read the task description carefully.
2. Read `.claude/checklist.txt` — these are the ground-truth completion criteria. Every subtask you produce must map to one or more of these checks.
3. Decompose the task into **3–7 verifiable subtasks**. For each subtask, name:
   - the change it makes,
   - the *anti-success-seeking* check that proves it was actually done (e.g., "grep shows the old function name no longer exists", "running `pytest -k new_test` exits 0 with the test actually executing"),
   - which checklist item(s) it advances.
4. Write this decomposition into `PROGRESS.md` at the workspace root. Format:

```markdown
# Plan
- [ ] Subtask 1: <change> — verify with `<command>` — checklist items: <ids>
- [ ] Subtask 2: ...
```

5. Do **not** start coding until `PROGRESS.md` is written. The plan is the contract.
6. As you complete each subtask, mark `[x]` *and* paste the verification command output below the line. If the verification fails, do not mark it complete.

If the task seems too vague to decompose, that is itself a finding — write `# Underspecified` at the top of `PROGRESS.md` with the specific ambiguity, and then make the most reasonable decomposition you can. Do not stall.
