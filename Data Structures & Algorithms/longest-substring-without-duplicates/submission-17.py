class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_str_set = set()
        l = 0
        for r in range(len(s)):
            while sub_str_set and s[r] in sub_str_set:
                sub_str_set.remove(s[l])
                l += 1
            sub_str_set.add(s[r])
            max_len = max(max_len,len(sub_str_set))
        return max_len