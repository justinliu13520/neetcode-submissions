class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            biggest = heapq.heappop_max(stones)
            next_biggest = heapq.heappop_max(stones)
            if biggest == next_biggest:
                continue
            val = biggest - next_biggest
            heapq.heappush_max(stones,val)
        return stones[0] if len(stones) == 1 else 0