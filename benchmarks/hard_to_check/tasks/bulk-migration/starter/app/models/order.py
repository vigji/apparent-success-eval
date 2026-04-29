class Order:
    def __init__(self, oid: int, items: list) -> None:
        self.oid = oid
        self.items = items
        print(f"[order] created oid={oid} items={len(items)}")

    def total(self) -> float:
        s = sum(self.items)
        print(f"[order.total] oid={self.oid} sum={s}")
        return s
