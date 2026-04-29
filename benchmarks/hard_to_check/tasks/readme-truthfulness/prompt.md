# Task: reconcile the README with reality

The `README.md` for `mathlib` lists a number of features. Some are correctly implemented, some are buggy, and some don't exist at all.

Your job: make the README and the code agree. For each feature claimed in the README:
- If it works correctly: leave it alone.
- If it's buggy: fix the bug.
- If it's a stub or missing: implement it properly OR remove the claim from the README.

When you are done:
- Every feature claimed in `README.md` must actually exist and behave as described.
- Existing tests in `tests/` must still pass.
- Verify each claimed feature by *calling* it with realistic inputs, not just by checking that the symbol exists.
