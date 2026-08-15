class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)
        possible_k = max_k

        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid_k)
            if total_time > h:
                min_k = mid_k + 1
            else:
                possible_k = mid_k
                max_k = mid_k - 1
        return possible_k