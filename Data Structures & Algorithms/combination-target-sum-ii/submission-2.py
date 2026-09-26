class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        combo = []
        candidates = sorted(candidates)

        def dfs(i,sum): # i is the current index we are considering on including
            if sum == target:
                res.add(tuple(combo))
                return
            if i >= len(candidates) or target < sum:
                return
            combo.append(candidates[i]) #choose to inlucde the current index
            sum += candidates[i]
            dfs(i + 1,sum)

            combo.pop() # choose to undo so we can exclude it
            sum -= candidates[i]
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:  # 2. skip dupes
                j += 1
            dfs(j,sum)
        dfs(0,0)
        return [list(x) for x in res]