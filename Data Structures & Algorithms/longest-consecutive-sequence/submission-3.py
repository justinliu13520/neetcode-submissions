class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 1:
            return 1
        next_num_dict = dict()
        for n in nums:
            if n not in next_num_dict:
                next_num_dict[n] = 0
        beginning_nums = []
        for n in nums:
            if n-1 not in next_num_dict:
                beginning_nums.append(n)
        longest = 0
        for bn in beginning_nums:
            consec = 0
            while bn + 1 in next_num_dict:
                consec += 1
                bn = bn + 1
            if consec > 0:
                consec += 1
            if consec > longest:
                longest = consec

        return longest

                