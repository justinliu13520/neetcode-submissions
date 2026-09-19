class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            biggest = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if biggest == second:
                continue
            heapq.heappush(stones,biggest - second)
        return -stones[0] if len(stones) > 0 else 0
