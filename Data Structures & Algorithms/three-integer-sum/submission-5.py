class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            target = -(nums[i])
            while l < r:
                if target < nums[l] + nums[r]:
                    r -= 1
                elif target > nums[l] + nums[r]:
                    l += 1
                else:
                    res.add(tuple(sorted([nums[l],nums[r],nums[i]])))
                    l += 1
            
        return list(res)
