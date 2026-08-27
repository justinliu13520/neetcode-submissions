class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq_set = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while seq_set and s[r] in seq_set:
                seq_set.remove(s[l])
                l += 1
            seq_set.add(s[r])
            res = max(res,r-l+1)
        return res