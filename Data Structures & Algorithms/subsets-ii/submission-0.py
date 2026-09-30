class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.add(tuple(subset.copy()))
                return
            subset.append(nums[i])
            # while i + 1 < len(nums) and nums[i] == nums[i+1]:
            #     i += 1
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return list(res)