class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seen_set = dict()
        begin = 0
        longest_substring = 0
        for end in range(len(s)):
            if s[end] in seen_set:
                begin = max(seen_set[s[end]]+1,begin)
            seen_set[s[end]] = end
            longest_substring = max(end-begin+1,longest_substring)
                
        return longest_substring
