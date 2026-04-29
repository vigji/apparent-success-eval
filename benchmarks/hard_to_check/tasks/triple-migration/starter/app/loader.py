"""Plugin loader."""
import importlib
import pkgutil
from . import plugins


def load_all():
    loaded = {}
    for info in pkgutil.iter_modules(plugins.__path__):
        mod = importlib.import_module(f"app.plugins.{info.name}")
        if hasattr(mod, "setup"):
            mod.setup()
        loaded[info.name] = mod
    print(f"[loader] loaded {len(loaded)} plugins")
    return loaded
