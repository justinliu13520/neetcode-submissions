class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_dict = {}

        for n in nums:
            n_dict[n] = n
        
        max_len = 0
        for n in nums:
            if n - 1 not in n_dict:
                cur_len = 0
                cur_n = n
                while cur_n in n_dict:
                    cur_len += 1
                    cur_n += 1
                max_len = max(max_len,cur_len)
        return max_len