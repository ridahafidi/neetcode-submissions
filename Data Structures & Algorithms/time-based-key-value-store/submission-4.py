class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((timestamp, value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return "" 
        arr = self.m[key]
        ans = ""
        for t, value in arr:
            if t <= timestamp:
                ans = value
            else:
                break
        return ans
