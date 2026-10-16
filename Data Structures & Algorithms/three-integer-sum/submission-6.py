class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l,r = i+1, len(nums) - 1
            compliment = -nums[i]
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum > compliment:
                    r -= 1
                elif cur_sum < compliment:
                    l += 1
                else:
                    res.add(tuple(sorted([nums[l],nums[r],nums[i]])))
                    l += 1
        return [list(x) for x in res]
