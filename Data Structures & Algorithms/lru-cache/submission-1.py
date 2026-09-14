class LRUCache:

    def __init__(self, capacity: int):
        self.key_val = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.key_val:
            value = self.key_val.pop(key)
            self.key_val[key] = value
            return value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_val:
            self.key_val.pop(key)
        self.key_val[key] = value
        if len(self.key_val) > self.capacity:
            self.key_val.popitem(last=False)
        return None
