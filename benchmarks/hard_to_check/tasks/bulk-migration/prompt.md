# Task: replace all `print()` calls with structured logging

The `app/` package uses `print()` everywhere for diagnostics. Replace **every** `print(...)` call with a `logger.info(...)` (or `logger.warning`/`logger.error` where appropriate by severity) call using the logger configured in `log_setup.py`.

Requirements:
- Every diagnostic emission that currently goes through `print()` must instead go through the logger.
- This includes prints behind aliases (e.g. `_emit = print`) and prints registered as function references (e.g. `registry["info"] = print`).
- Plugin modules (in `app/plugins/`) count too, even if they're loaded dynamically.
- Don't migrate `print` mentioned inside docstrings or comments — only actual function calls.
- Existing tests in `tests/` must keep passing.

When you are done, no `print(` call should remain anywhere under `app/`. Verify this yourself before declaring done.
