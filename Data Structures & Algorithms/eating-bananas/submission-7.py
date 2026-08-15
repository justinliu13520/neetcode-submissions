class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # when k = 1, that's the slowest rate
        # when k = max(piles), that's the fastest
        # for each i, we divide by k to find total time it takes for that i
        # we do ceilings because we dont go faster

        min_k = max(piles)
        left_k, right_k = 1, max(piles)

        while left_k <= right_k:
            mid_k = (left_k + right_k) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/mid_k)
            if total_time > h:
                left_k = mid_k + 1
            elif total_time <= h:
                min_k = min(min_k,mid_k)
                right_k = mid_k - 1

        return min_k