class TimeMap:

    def __init__(self):
        # dict where the key is the person and the values are [values, timestamp]
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.storage.get(key,"") == "":
            return ""
        values = self.storage[key]
        l,r = 0, len(values) - 1
        possible_index = -1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                possible_index = m
                l = m + 1
            else:
                r = m - 1
        return values[possible_index][0] if possible_index != -1 else ""
