class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int) # keeps track of highest count of each letter
        res = 0
        l = 0
        maxf = 0 # we want maxFreq because maxFreq + k is the longest substring possible with replacements

        for r in range(len(s)):
            count[s[r]] += 1 
            maxf = max(count.values()) # we see if we need to update maxFreq with the new letter seen

            while (r - l + 1) - maxf > k: 
                # len of cur substring can not be greater than most frequent + k
                # because most frequent with k replacements would be the longest we 
                # can have at the moment
                count[s[l]] -= 1 # decrease because we're sliding our cur substring in
                l += 1
            res = max(res, r - l + 1) # compare the cur length to the cur longest

        return res