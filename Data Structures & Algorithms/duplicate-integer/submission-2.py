class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = defaultdict(int)
        for n in nums:
            if freq_dict.get(n,0) == 0:
                freq_dict[n] += 1
                continue
            return True
        return False