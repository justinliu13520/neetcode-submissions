class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        max_freq = 0
        freq_dict = defaultdict(int)

        for r in range(len(s)):
            freq_dict[s[r]] += 1
            max_freq = max(freq_dict.values())
            while r - l + 1 > k + max_freq:
                freq_dict[s[l]] -= 1
                l += 1
            longest = max(longest,r - l + 1)
        return longest