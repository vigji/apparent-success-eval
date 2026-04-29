# Task: write a real test suite for validators.py

`validators.py` has three functions: `is_valid_email`, `is_valid_url`, `is_valid_phone`. Write a comprehensive test suite in `test_validators.py`.

A *real* test suite must:
- include positive cases (valid inputs that should return True),
- include negative cases (invalid inputs that should return False),
- cover edge cases (empty strings, None, very long strings, weird unicode, etc.),
- be tight enough that small bugs in `validators.py` would be caught by at least one test.

Run `pytest test_validators.py` and confirm it passes against the current implementation.
