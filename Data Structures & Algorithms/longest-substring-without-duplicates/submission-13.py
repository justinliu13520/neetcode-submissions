class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_window = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while cur_window and s[r] in cur_window:
                cur_window.remove(s[l])
                l += 1
            cur_window.add(s[r])
            res = max(res,len(cur_window))
        return res