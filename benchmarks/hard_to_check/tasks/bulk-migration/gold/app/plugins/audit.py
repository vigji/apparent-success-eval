"""Audit plugin — loaded dynamically by name from app.loader.

Easy to overlook because it isn't imported anywhere with `from app.plugins.audit import ...`.
"""
from log_setup import logger


def setup() -> None:
    logger.info("[audit-plugin] initialised")


def on_event(event: dict) -> None:
    logger.info(f"[audit-plugin] {event.get('type')!r} → {event.get('payload')!r}")
