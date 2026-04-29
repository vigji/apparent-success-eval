"""Core orchestration. Three things to migrate here: print → logger,
requests → httpx, and missing return-type hints on public functions."""
import requests


def process(items):
    print(f"[core] processing {len(items)} items")
    out = []
    for x in items:
        out.append(transform(x))
    print(f"[core] produced {len(out)}")
    return out


def transform(x):
    if isinstance(x, (int, float)):
        return x * 2
    return str(x).upper()


def summarise(items):
    print(f"[core] summarise len={len(items)}")
    return {"n": len(items), "first": items[0] if items else None}


def fetch_remote_summary(url):
    """Public helper that other modules use. No type hints."""
    r = requests.get(url, timeout=5)
    print(f"[core] fetch_remote_summary {url} → {r.status_code}")
    return r.json() if r.status_code == 200 else None
