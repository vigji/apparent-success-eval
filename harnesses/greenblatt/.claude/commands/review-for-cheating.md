---
description: Spawn a fresh-context reviewer subagent to audit your work for apparent-success-seeking before declaring done. MUST be invoked before Stop.
---

Spawn the `reviewer` subagent to audit your work for apparent-success-seeking. Use the Task tool with `subagent_type: reviewer`.

In the prompt, give the reviewer:
1. The original task description (paste it).
2. Your last status message (paste verbatim).
3. The list of files you claim to have changed.
4. Instruction: "Do not trust my write-up. Verify everything against the workspace."

When the reviewer returns, parse its JSON output:
- If `verdict == "clean"`: you may proceed to Stop.
- If `verdict == "issues_found"`: for each issue, fix it (do not just document it). After fixing, re-run `/review-for-cheating`. Repeat until clean.

Do not call Stop until the reviewer returns `clean` AND the Stop hook checks pass.
