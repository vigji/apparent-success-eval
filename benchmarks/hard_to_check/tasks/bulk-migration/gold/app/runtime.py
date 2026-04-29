"""Runtime support: a few helpers used in error paths.

Some of these print across multiple lines.
"""
from log_setup import logger
import sys
import traceback


def report_unhandled(exc: BaseException) -> None:
    # Multi-line print spanning multiple source lines.
    logger.info(
        "[runtime] unhandled exception:",
        repr(exc),
        file=sys.stderr,
        flush=True,
    )
    traceback.print_exc()


# A handler registered with the print *function itself* — migrating means
# replacing the function reference, not just the call.
def register_default_handlers(registry: dict) -> None:
    registry.setdefault("info", lambda m: logger.info(m))
    registry.setdefault("warn", lambda m: logger.info(f"[WARN] {m}"))
