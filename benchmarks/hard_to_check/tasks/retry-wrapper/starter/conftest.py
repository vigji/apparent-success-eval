"""Test fixtures."""
import pytest


class FakeResponse:
    def __init__(self, status_code: int, headers: dict | None = None, body: str = "ok") -> None:
        self.status_code = status_code
        self.headers = headers or {}
        self.body = body


@pytest.fixture
def FakeResponse_cls():
    return FakeResponse
