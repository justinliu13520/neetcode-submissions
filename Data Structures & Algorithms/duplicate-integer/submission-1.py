class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_dict = defaultdict(int)
        for n in nums:
            if dupe_dict.get(n,0) != 0:
                return True
            dupe_dict[n] += 1
        return False
