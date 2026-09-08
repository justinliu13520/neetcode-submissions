class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.keyStore.get(key,None) == None:
            return ""
        vals = self.keyStore[key]
        l,r = 0, len(vals) - 1
        possible_val = []
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                possible_val = vals[m]
                l = m + 1
            else:
                r = m - 1
        return possible_val[0] if len(possible_val) > 0 else ""
