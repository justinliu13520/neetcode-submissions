class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def dfs(start):
            if start >= len(nums):
                res.append(nums.copy())
                return 
            for i in range(start,len(nums)):
                nums[i],nums[start] = nums[start],nums[i]
                dfs(start+1)
                nums[i],nums[start] = nums[start],nums[i]
        dfs(0)
        return res