class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #go through once to see which letter is the most common
        #go through again with that letter and keep incrementing until not that letter
        #use up k until letter reached again
        #if next letter after using up k is letter, increase substring by one and keep goin until not letter#
        #if not letter, move the beginning of window to not letter and keep going until letter
        if len(s) == 1:
            return 1
        freq_dict = dict()
        most_freq = 0
        begin = 0
        max_len = 0
        for end in range(len(s)):
            freq_dict[s[end]] = freq_dict.get(s[end],0) + 1
            most_freq = max(freq_dict.values()) if freq_dict else 0
            window_len = end - begin + 1
            if window_len - most_freq > k :            
                freq_dict[s[begin]] -= 1
                begin += 1
                window_len = end - begin + 1
            max_len = max(max_len,window_len)

        return max_len

        