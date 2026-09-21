class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        res = []
        while len(res) != k:
            res.append(heapq.heappop(nums))
        return -res[-1]