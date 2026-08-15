class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = dict()
        for i in range(len(nums)):
            if comp_dict.get(target-nums[i], "not found") != "not found":
                return [comp_dict.get(target-nums[i]),i]
            else:
                comp_dict[nums[i]] = i

