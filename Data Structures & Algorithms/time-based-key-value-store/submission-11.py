class TimeMap:

    def __init__(self):
        self.key_val_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_val_store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_val_store:
            return ""

        values = self.key_val_store[key]
        l,r = 0,len(values)-1
        possible_val = -1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                possible_val = m
                l = m + 1
            else:
                r = m - 1
        return values[possible_val][1] if possible_val != -1 else ""
