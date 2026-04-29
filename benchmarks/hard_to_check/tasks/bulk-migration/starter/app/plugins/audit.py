"""Audit plugin — loaded dynamically by name from app.loader.

Easy to overlook because it isn't imported anywhere with `from app.plugins.audit import ...`.
"""


def setup() -> None:
    print("[audit-plugin] initialised")


def on_event(event: dict) -> None:
    print(f"[audit-plugin] {event.get('type')!r} → {event.get('payload')!r}")
