class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cons_dict = {}
        longest = 1
        nums = set(nums)
        for n in nums:
            cons_dict[n] = 0
        
        for n1 in nums:
            cur_length = 1
            if cons_dict[n1] != 0:
                continue
            if n1-1 not in nums:
                cons_dict[n1] = 1                
                next_num = n1 + 1
                while next_num in nums:
                    cons_dict[next_num] = 1
                    cur_length += 1
                    next_num += 1
            longest = max(longest,cur_length)
        
        return longest