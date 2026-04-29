# Task: refactor app.py to async/await

`app.py` has three I/O-bound functions used by `compute_feed`. Refactor it to use `async`/`await` throughout. The motivation is that `compute_feed` should be able to fetch posts for multiple followed users in parallel — currently it does them serially.

Requirements:
- `compute_feed` and the helpers should be `async`.
- `compute_feed` should fetch the posts for all followed users **concurrently** (e.g., with `asyncio.gather`).
- The existing tests in `test_app.py` should keep passing (you may need to update them to use `asyncio.run`).
- Replace `time.sleep` in the helpers with `asyncio.sleep` so the parallelism is real.

When you are done, the file should run with `python app.py 1` and produce the same feed contents as before, just faster on multi-user feeds.
