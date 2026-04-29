"""Runtime helpers."""
import sys


def report_unhandled(exc):
    # Multi-line print spanning several lines.
    print(
        "[runtime] unhandled:",
        repr(exc),
        file=sys.stderr,
        flush=True,
    )


def register_default_handlers(registry):
    # Function-reference uses of `print` — migration must replace these too.
    registry.setdefault("info", print)
    registry.setdefault("warn", lambda m: print(f"[WARN] {m}"))
