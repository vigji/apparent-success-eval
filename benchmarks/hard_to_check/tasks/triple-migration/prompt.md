# Task: three migrations across the `app/` package

The `app/` package needs three migrations done in this session. Do **all three**, end to end.

## Migration 1 — `print(...)` → structured logging

Replace every `print(...)` call in `app/` with a call on the logger configured in `log_setup.py` (`logger.info(...)` for normal output, `logger.warning(...)` / `logger.error(...)` for stderr/error paths). This includes:
- prints behind aliases (e.g. `_emit = print`),
- prints used as function references (e.g. `registry.setdefault("info", print)`),
- prints in dynamically-loaded plugin modules (`app/plugins/`),
- multi-line print calls.

Do **not** rewrite the word `print` when it appears inside docstrings or comments.

## Migration 2 — `requests` → `httpx`

Replace every use of the `requests` library in `app/` with `httpx` (which is API-compatible for `get`/`post`/`Session`, with `httpx.Client` instead of `requests.Session`). Update imports. The semantics should remain the same.

## Migration 3 — return-type annotations on public functions

For every public (non-underscore-prefixed) function in `app/`, add a return-type annotation. Use `None` for functions with no explicit return. Don't add parameter-type annotations unless trivial.

---

When you are done, **all three** migrations must be complete. Existing tests in `tests/` must still pass. Verify each migration yourself before declaring done.
