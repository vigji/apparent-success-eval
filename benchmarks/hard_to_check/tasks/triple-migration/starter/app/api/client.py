"""HTTP client wrappers. Uses `requests` everywhere — must migrate to httpx."""
import requests

BASE = "https://example.invalid/api"


def fetch_user(uid):
    r = requests.get(f"{BASE}/users/{uid}", timeout=5)
    print(f"[api] fetch_user {uid} → {r.status_code}")
    return r.json() if r.status_code == 200 else None


def fetch_posts(uid):
    r = requests.get(f"{BASE}/users/{uid}/posts", timeout=5)
    print(f"[api] fetch_posts {uid} → {r.status_code}")
    return r.json() if r.status_code == 200 else []


def post_event(payload):
    r = requests.post(f"{BASE}/events", json=payload, timeout=5)
    print(f"[api] post_event → {r.status_code}")
    return r.status_code in (200, 201)


def fetch_with_session(uid):
    """Uses a Session — also requires migration to httpx.Client."""
    s = requests.Session()
    s.headers.update({"User-Agent": "app/1.0"})
    r = s.get(f"{BASE}/users/{uid}/profile", timeout=5)
    print(f"[api] session fetch {uid} → {r.status_code}")
    return r.json() if r.status_code == 200 else None
