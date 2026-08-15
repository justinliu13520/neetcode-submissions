class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        position_dict = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in position_dict:
                l = max(l,position_dict[s[r]]+1)
            position_dict[s[r]] = r
            res = max(r-l+1,res)
        return res
