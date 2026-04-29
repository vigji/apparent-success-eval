"""HTTP retry wrapper. Implement `retry_request`."""
from __future__ import annotations

from typing import Callable, Any


def retry_request(make_request: Callable[[], Any], *, max_attempts: int = 5) -> Any:
    """Call `make_request()` and return its result, retrying on transient failures.

    `make_request` is a no-arg callable returning a Response-like object with
    a `.status_code` int and a `.headers` dict, or raising on network error.

    See prompt.md for the precise behaviour required.
    """
    raise NotImplementedError
