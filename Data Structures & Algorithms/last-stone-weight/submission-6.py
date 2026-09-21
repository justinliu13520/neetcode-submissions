class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            biggest = heapq.heappop(stones)
            second_biggest = heapq.heappop(stones)
            if biggest == second_biggest:
                continue
            heapq.heappush(stones,biggest-second_biggest)
        return -stones[0] if stones else 0
