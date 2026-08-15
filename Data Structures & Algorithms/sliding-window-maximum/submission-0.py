class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        if len(nums) == k:
            return [max(nums)]
        if len(nums) == 1:
            return nums
        if len(nums) == 0:
            return []
        
        res = []

        l = 0
        r = k
        while r <= len(nums):
            res.append(max(nums[l:r]))
            l += 1
            r += 1
        return res

