class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_dict = {}
        l = 0
        longest_len = 0
        for r in range(len(s)):
            if letter_dict.get(s[r],-1) != -1:
                l = max(letter_dict[s[r]]+1,l)
            letter_dict[s[r]] = r
            longest_len = max(longest_len,r-l+1)
        return longest_len
