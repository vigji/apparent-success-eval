class Event:
    def __init__(self, kind, payload):
        self.kind = kind
        self.payload = payload
        print(f"[event] {kind!r} payload={payload}")

    def render(self):
        return f"<{self.kind}>{self.payload}</{self.kind}>"
