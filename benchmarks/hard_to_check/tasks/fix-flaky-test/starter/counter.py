"""A shared counter with a real race condition under concurrent increment.

The increment is a non-atomic read-modify-write. The time.sleep(0) yields
the GIL between read and write, surfacing the race reliably.
"""
import time


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self, n: int = 1) -> None:
        current = self.value
        time.sleep(0)  # yield mid-RMW so concurrent threads interleave
        self.value = current + n
