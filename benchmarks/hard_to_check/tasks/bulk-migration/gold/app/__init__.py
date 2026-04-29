"""Top-level app package."""
from log_setup import logger
# Bootstrap diagnostic — gets emitted once on import.
logger.info("[boot] app package loaded")

from .core import process, transform  # noqa: E402
from .utils import normalize_path, slugify  # noqa: E402

__all__ = ["process", "transform", "normalize_path", "slugify"]
