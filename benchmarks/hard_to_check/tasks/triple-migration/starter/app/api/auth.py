"""Auth helpers — also using requests."""
import requests


def exchange_code(code):
    r = requests.post("https://auth.example.invalid/token",
                       data={"code": code}, timeout=5)
    print(f"[auth] exchange_code → {r.status_code}")
    return r.json().get("access_token") if r.status_code == 200 else None


def whoami(token):
    r = requests.get("https://auth.example.invalid/me",
                      headers={"Authorization": f"Bearer {token}"}, timeout=5)
    print(f"[auth] whoami → {r.status_code}")
    return r.json() if r.status_code == 200 else None
