class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        def dfs(i,sum):
            if sum == target:
                res.append(combo.copy())
                return
            if sum > target or i >= len(nums):
                return
            sum += nums[i]
            combo.append(nums[i])
            dfs(i,sum)
            sum -= nums[i]
            combo.pop()
            dfs(i + 1,sum)
        dfs(0,0)
        return res