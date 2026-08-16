class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        longest = 1
        for n in nums:
            if n - 1 not in nums:
                cur_len = 1
                while n + 1 in nums:
                    cur_len += 1
                    longest = max(longest,cur_len)
                    n += 1
        return longest