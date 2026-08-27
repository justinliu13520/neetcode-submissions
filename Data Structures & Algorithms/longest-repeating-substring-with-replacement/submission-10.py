class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freq_dict = defaultdict(int)
        max_freq = 0
        for r in range(len(s)):
            freq_dict[s[r]] += 1
            max_freq = max(freq_dict.values())
            
            while max_freq + k < r - l + 1:
                freq_dict[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res