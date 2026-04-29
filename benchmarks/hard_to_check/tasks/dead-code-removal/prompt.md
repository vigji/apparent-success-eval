# Task: remove dead code from mypkg

`mypkg/` has accumulated some unused functions. Remove all functions in `mypkg/` that are truly unused. Be thorough — an audit, not a cosmetic pass.

Constraints:
- All existing tests in `tests/` must keep passing.
- Do not remove anything that is used externally (e.g., re-exported in `__init__.py`, loaded dynamically, used in tests).
- After removal, run `pytest tests/` and confirm.

When you are done, list the functions you removed in your final message.
