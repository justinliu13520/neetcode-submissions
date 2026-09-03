class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set()

        for n in nums:
            num_set.add(n)

        for n in nums:
            if n - 1 not in num_set:
                cur_len = 0
                cur_num = n
                while cur_num in num_set:
                    cur_len += 1
                    cur_num += 1
                res = max(res,cur_len)
        return res
            