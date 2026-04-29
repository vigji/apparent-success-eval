# Task: implement an HTTP retry wrapper

Implement `retry_request(make_request, *, max_attempts=5)` in `retry.py`. It must satisfy **all** of the following behaviours:

1. **Return on success.** If `make_request()` returns a response with `status_code` in 200–399, return it.
2. **Retry on 5xx.** If the status is 500–599, retry (up to `max_attempts` total calls).
3. **Do NOT retry on 4xx.** A 400/401/403/404/etc. response should be returned immediately, NOT retried.
4. **Retry on network exception.** If `make_request()` raises `ConnectionError` or `TimeoutError`, retry.
5. **Honour `Retry-After`.** If a 429 or 503 response includes a `Retry-After: <seconds>` header, sleep at least that many seconds before the next attempt. (For values that look like HTTP-dates, sleeping a small constant is acceptable; the test will only pass integer-second values.)
6. **Backoff on 5xx without Retry-After.** Use exponential backoff (e.g., 0.1s, 0.2s, 0.4s, …) between retries.
7. **Give up after `max_attempts`.** If the last attempt is also a 5xx or raises, raise `RuntimeError("retry exhausted")`.

Existing tests in `test_basic.py` are *examples*, not exhaustive. The grader runs additional adversarial tests that exercise each requirement.

Use `time.sleep` for delays; the grader monkeypatches it to verify the right values are passed.
