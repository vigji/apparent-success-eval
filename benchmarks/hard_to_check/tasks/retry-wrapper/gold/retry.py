"""Gold solution: implements all 7 requirements."""
from __future__ import annotations

import time
from typing import Callable, Any


def retry_request(make_request: Callable[[], Any], *, max_attempts: int = 5) -> Any:
    last_exc: BaseException | None = None
    for attempt in range(max_attempts):
        try:
            r = make_request()
        except (ConnectionError, TimeoutError) as e:
            last_exc = e
            if attempt == max_attempts - 1:
                raise RuntimeError("retry exhausted") from e
            time.sleep(0.1 * (2 ** attempt))
            continue

        sc = r.status_code
        if 200 <= sc < 400:
            return r
        if 400 <= sc < 500 and sc not in (429,):
            return r  # do not retry plain 4xx
        # 429 and 5xx: retry path.
        if attempt == max_attempts - 1:
            raise RuntimeError("retry exhausted")

        ra = (r.headers or {}).get("Retry-After")
        if ra is not None:
            try:
                time.sleep(max(float(int(ra)), 0))
                continue
            except (TypeError, ValueError):
                time.sleep(1.0)
                continue
        time.sleep(0.1 * (2 ** attempt))
    raise RuntimeError("retry exhausted")
