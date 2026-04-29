"""Lightweight input validators."""
import re

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
URL_RE = re.compile(r"^https?://[A-Za-z0-9.-]+(?:/[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]*)?$")
PHONE_RE = re.compile(r"^\+?[0-9]{1,3}[-. ]?\(?[0-9]{1,4}\)?[-. ]?[0-9]{3,4}[-. ]?[0-9]{3,4}$")


def is_valid_email(s: str) -> bool:
    if not isinstance(s, str):
        return False
    return bool(EMAIL_RE.match(s))


def is_valid_url(s: str) -> bool:
    if not isinstance(s, str):
        return False
    return bool(URL_RE.match(s))


def is_valid_phone(s: str) -> bool:
    if not isinstance(s, str):
        return False
    return bool(PHONE_RE.match(s))
