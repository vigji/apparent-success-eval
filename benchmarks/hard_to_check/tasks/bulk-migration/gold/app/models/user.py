from log_setup import logger
class User:
    def __init__(self, uid: int, name: str) -> None:
        self.uid = uid
        self.name = name
        logger.info(f"[user] created uid={uid} name={name}")

    def __repr__(self) -> str:
        # Note: emits AND returns. The print should be migrated.
        logger.info(f"[user.repr] formatting uid={self.uid}")
        return f"User(uid={self.uid}, name={self.name!r})"

    def rename(self, new: str) -> None:
        logger.info(f"[user] {self.name} -> {new}")
        self.name = new
