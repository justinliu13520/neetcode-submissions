class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = dict()
        for i in nums:
            if dup_dict.get(i,"not found") == "not found":
                dup_dict[i] = "found"
            else:
                return True
        return False