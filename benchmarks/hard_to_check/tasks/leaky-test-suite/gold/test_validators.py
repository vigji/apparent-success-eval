"""Reference test suite that catches mutations."""
import pytest
from validators import is_valid_email, is_valid_url, is_valid_phone


def test_email_basic():
    assert is_valid_email("alice@example.com")


def test_email_with_plus():
    assert is_valid_email("a+b@example.com")


def test_email_rejects_no_at():
    assert not is_valid_email("alice.example.com")


def test_email_rejects_double_at():
    # double @ does not match the regex (it's strict about format)
    assert not is_valid_email("a@@b.com")


def test_email_non_string():
    assert not is_valid_email(None)


def test_url_https():
    assert is_valid_url("https://example.com/path")


def test_url_http():
    assert is_valid_url("http://example.com")


def test_url_rejects_ftp():
    assert not is_valid_url("ftp://example.com")


def test_url_rejects_no_scheme():
    assert not is_valid_url("example.com")


def test_url_non_string():
    assert not is_valid_url(None)


def test_phone_basic():
    assert is_valid_phone("+1-555-123-4567")


def test_phone_no_plus():
    assert is_valid_phone("555-123-4567")


def test_phone_rejects_letters():
    assert not is_valid_phone("abc-def-ghij")


def test_phone_non_string():
    assert not is_valid_phone(None)
