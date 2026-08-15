class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        res = max_k
        while min_k <= max_k:
            middle_k = min_k + ((max_k - min_k)) // 2
            time_to_eat = 0
            print(middle_k)
            for p in piles:
                time_to_eat += math.ceil(p/middle_k)
            print("time to eat:",time_to_eat)
            if time_to_eat > h:
                min_k = middle_k + 1
            elif time_to_eat <= h:
                res = middle_k
                max_k = middle_k - 1
            else:
                print(min_k, max_k)
                return middle_k
        return res