class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start):
            if start == len(nums):
                res.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]   # choose nums[i] as the next element
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]   # undo (swap back)

        dfs(0)
        return res