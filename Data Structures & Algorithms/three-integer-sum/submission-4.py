class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            l,r = i + 1, len(nums)-1
            while l < r:
                target = -nums[i]
                total_sum = nums[l] + nums[r]
                if target == total_sum:
                    res.add(tuple(sorted([nums[i],nums[l],nums[r]])))
                    l += 1
                elif target > total_sum:
                    l += 1
                else:
                    r -= 1
        return list(res)