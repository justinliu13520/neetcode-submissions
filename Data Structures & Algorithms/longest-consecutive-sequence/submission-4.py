class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Turn the list into a set so we dont do extra work for the same number

        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set: # We check if n is the first in a possible sequence
                length = 1 # Sequence's current length is 1
                while n + length in num_set: # n + length finds the next number in the sequence
                    length += 1 # This updates the while loop to look for the next number in the sequence
                longest = max(longest,length) # compares the current longest to the current length

        return longest
