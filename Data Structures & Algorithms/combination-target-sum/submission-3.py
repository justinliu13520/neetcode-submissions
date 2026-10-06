class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def dfs(i,sum):
            if sum == target:
                res.append(combo.copy())
                return
            if i >= len(nums) or sum > target:
                return
            combo.append(nums[i])
            sum += nums[i]
            dfs(i,sum)
            combo.pop()
            sum -= nums[i]
            dfs(i+1,sum)
        dfs(0,0)
        return res