class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-x for x in stones]
        heapq.heapify(negative_stones)

        while len(negative_stones) > 1:
            biggest = heapq.heappop(negative_stones)
            next_biggest = heapq.heappop(negative_stones)
            if biggest == next_biggest:
                continue
            heapq.heappush(negative_stones,biggest-next_biggest)
        return -negative_stones[0] if len(negative_stones) == 1 else 0
