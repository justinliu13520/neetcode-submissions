class TimeMap:
    def __init__(self):
        self.key_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        
        values = self.key_store[key]
        l,r = 0,len(values)-1

        res = []
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m]
                l = m + 1
            else:
                r = m - 1
        return res[1] if len(res) > 0 else ""
