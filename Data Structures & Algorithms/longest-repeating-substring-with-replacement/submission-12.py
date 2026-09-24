class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(s)):
            freq_dict[s[r]] += 1
            max_freq = max(freq_dict.values())

            if max_freq + k < r - l + 1:
                freq_dict[s[l]] -= 1
                l += 1
            max_len = max(max_len,r-l+1)
        return max_len