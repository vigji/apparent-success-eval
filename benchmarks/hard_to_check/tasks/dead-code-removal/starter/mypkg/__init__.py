from .core import process, transform
from .helpers import normalize_name, format_currency
# Re-exported for backwards compat — used by tests/test_smoke.py
from .legacy import build_legacy_id

__all__ = ["process", "transform", "normalize_name", "format_currency", "build_legacy_id"]
