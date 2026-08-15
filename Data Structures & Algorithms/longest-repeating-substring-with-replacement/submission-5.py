class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = defaultdict(int)
        l = 0 
        longest = 0
        max_freq = 0
        for r in range(len(s)):
            freq_dict[s[r]] += 1
            max_freq = max(freq_dict.values())

            while r - l + 1 > max_freq + k:
                freq_dict[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest