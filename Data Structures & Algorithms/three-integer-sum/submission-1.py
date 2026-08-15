class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return [[]]
        i = 0
        output = set()
        nums = sorted(nums)
        print(nums)
        while i < len(nums)-2:
            l = i + 1
            r = len(nums)-1
            target = -nums[i]
            while l < r:
                print("Index:",i,nums[i],nums[l],nums[r])
                if nums[l] + nums[r] == target:
                    output.add(tuple(sorted([nums[i],nums[r],nums[l]])))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            i += 1
        return list(output)
                