class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output_list = set()
        nums = sorted(nums)
        
        for i in range(len(nums)-2):
            l, r =i+1, len(nums)-1
            target = -nums[i]
            while l < r:
                if target == nums[l] + nums[r]:
                    output_list.add(tuple(sorted([nums[i],nums[l],nums[r]])))
                    l += 1
                elif target > nums[l] + nums[r]:
                    l += 1
                else:
                    r -= 1
        return list(output_list)