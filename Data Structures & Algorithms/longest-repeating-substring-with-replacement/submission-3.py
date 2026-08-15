class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_len = 0
        max_freq = 0
        l = 0
        freq_dict = defaultdict(int)


        for r in range(len(s)):
            freq_dict[s[r]] += 1
            max_freq = max(freq_dict.values())

            while r - l + 1 > max_freq + k:
                freq_dict[s[l]] -= 1
                l += 1
            longest_len = max(longest_len,r-l+1)
        return longest_len