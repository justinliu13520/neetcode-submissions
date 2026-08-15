class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no_repeat = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in no_repeat:
                no_repeat.remove(s[l])
                l += 1
            no_repeat.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
