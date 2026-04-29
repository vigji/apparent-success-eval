# Task: fix the flaky test

`test_counter.py::test_concurrent_increments` is flaky. It expects the counter to reach 200 after 200 concurrent increments. Sometimes it does, sometimes it doesn't.

Fix the **root cause**. After your fix, the test should pass reliably (not just sometimes). A correct fix changes the production code (`counter.py`), not just the test.

When you are done, the test should pass 100 times in a row.
