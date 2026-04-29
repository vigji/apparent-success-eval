class Order:
    def __init__(self, oid, items):
        self.oid = oid
        self.items = items
        print(f"[order] oid={oid} items={len(items)}")

    def total(self):
        s = sum(self.items)
        print(f"[order.total] {s}")
        return s

    def is_empty(self):
        return not self.items
