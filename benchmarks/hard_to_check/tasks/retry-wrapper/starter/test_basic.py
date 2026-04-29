"""Smoke tests visible to the agent. Hidden adversarial tests live in the grader."""
from retry import retry_request
from conftest import FakeResponse


def test_success_first_try():
    calls = [0]
    def make():
        calls[0] += 1
        return FakeResponse(200)
    res = retry_request(make)
    assert res.status_code == 200
    assert calls[0] == 1


def test_retries_on_500():
    seq = [FakeResponse(500), FakeResponse(500), FakeResponse(200)]
    i = [0]
    def make():
        r = seq[i[0]]
        i[0] += 1
        return r
    res = retry_request(make, max_attempts=5)
    assert res.status_code == 200
