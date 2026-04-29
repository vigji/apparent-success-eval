"""Audit plugin loaded dynamically by app.loader."""
import requests


def setup():
    print("[audit-plugin] init")


def on_event(event):
    print(f"[audit-plugin] {event.get('kind')} payload={event.get('payload')}")
    # Posts to a remote audit log.
    requests.post("https://audit.example.invalid/events", json=event, timeout=5)
