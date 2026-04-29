"""Logger configuration available for the migration."""
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
if not logger.handlers:
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s"))
    logger.addHandler(h)
