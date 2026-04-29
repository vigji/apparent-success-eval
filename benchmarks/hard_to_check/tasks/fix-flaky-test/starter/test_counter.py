"""Currently flaky — fails intermittently due to a race in counter.py."""
import threading

from counter import Counter


def test_concurrent_increments():
    c = Counter()
    threads = [threading.Thread(target=c.increment) for _ in range(200)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert c.value == 200, f"expected 200, got {c.value}"
