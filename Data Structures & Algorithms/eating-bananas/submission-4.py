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
                res = middle_k # found possible solution, but try to find smaller by setting the right bound to be 1 smaller
                # we can keep going because if we don't find something smaller that works, we remember res still and we'll get out of the while loop eventually
                max_k = middle_k - 1
        return res