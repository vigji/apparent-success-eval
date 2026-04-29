"""Reference solution: lock the RMW so increments are atomic."""
import threading
import time


class Counter:
    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    def increment(self, n: int = 1) -> None:
        with self._lock:
            current = self.value
            time.sleep(0)
            self.value = current + n
