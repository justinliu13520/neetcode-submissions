class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        nums_dict = defaultdict(int)
        for n in nums:
            nums_dict[n] += 1
        
        longest = 1
        for n in nums:
            if n - 1 in nums_dict:
                continue
            cur_len = 1
            while n + 1 in nums_dict:
                cur_len += 1
                longest = max(longest,cur_len)
                n += 1
        return longest