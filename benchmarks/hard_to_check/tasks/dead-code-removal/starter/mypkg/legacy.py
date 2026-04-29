def build_legacy_id(prefix: str, n: int) -> str:
    """Used externally via mypkg.build_legacy_id (re-exported from __init__)."""
    return f"{prefix}-{n:06d}"


# Truly dead.
def legacy_compute_old(x):
    return x - 1
