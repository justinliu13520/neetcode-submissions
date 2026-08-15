class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1
            while l < r:
                target = -nums[i]
                if target == nums[l] + nums[r]:
                    res.add(tuple(sorted([nums[i],nums[l],nums[r]])))
                    l += 1
                elif target > nums[l] + nums[r]:
                    l += 1
                else:
                    r -= 1
        return list(res)