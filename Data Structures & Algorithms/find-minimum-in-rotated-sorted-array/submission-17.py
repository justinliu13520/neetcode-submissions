class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        res = 1001
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            m = (l + r) // 2
            res = min(res,nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res