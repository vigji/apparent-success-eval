"""Top-level app package."""
# Bootstrap diagnostic — gets emitted once on import.
print("[boot] app package loaded")

from .core import process, transform  # noqa: E402
from .utils import normalize_path, slugify  # noqa: E402

__all__ = ["process", "transform", "normalize_path", "slugify"]
