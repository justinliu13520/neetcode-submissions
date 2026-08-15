class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no_dupe = set()
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in no_dupe:
                no_dupe.add(s[r])
            else:
                while s[r] in no_dupe:
                    no_dupe.remove(s[l])
                    l += 1
                no_dupe.add(s[r])
            res = max(res,r-l+1)

        return res