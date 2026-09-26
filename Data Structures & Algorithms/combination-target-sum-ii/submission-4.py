class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        combo = []
        candidates = sorted(candidates)

        def dfs(i,sum):
            if sum == target:
                res.add(tuple(combo.copy()))
                return
            if i >= len(candidates) or sum > target:
                return
            
            combo.append(candidates[i])
            sum += candidates[i]
            dfs(i+1,sum)

            combo.pop()
            sum -= candidates[i]
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j,sum)
        dfs(0,0)
        return [list(x) for x in res]