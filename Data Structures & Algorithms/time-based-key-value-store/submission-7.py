class TimeMap:

    def __init__(self):
        self.val_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.val_store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.val_store.get(key,0) == 0:
            return ""

        vals = self.val_store[key]

        l,r = 0,len(vals)-1
        possible_kv = [""]
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                possible_kv = vals[m]
                l = m + 1
            else:
                r = m - 1
        return possible_kv[0]
        
