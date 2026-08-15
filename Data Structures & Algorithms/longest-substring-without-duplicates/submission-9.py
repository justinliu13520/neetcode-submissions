class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_window = set()
        max_length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in cur_window:
                cur_window.remove(s[l])
                l += 1

            cur_window.add(s[r])
            max_length = max(r-l+1,max_length)

        return max_length
