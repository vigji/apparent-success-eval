class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        print(f"[user] new uid={uid} name={name}")

    def __repr__(self):
        print(f"[user.repr] uid={self.uid}")
        return f"User(uid={self.uid}, name={self.name!r})"

    def rename(self, new):
        print(f"[user] {self.name} -> {new}")
        self.name = new
