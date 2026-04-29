from mypkg import process, normalize_name, format_currency, build_legacy_id
from mypkg.config import get_default


def test_process():
    assert process([1, 2, 3]) == [2, 4, 6]


def test_normalize_name():
    assert normalize_name("  alice ") == "Alice"


def test_format_currency():
    assert format_currency(3.5).startswith("3.50")


def test_legacy_id():
    assert build_legacy_id("X", 42) == "X-000042"


def test_config_default():
    assert get_default() == 42
