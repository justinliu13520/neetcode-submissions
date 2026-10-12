class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = dict()
        for i in range(len(nums)):
            if target - nums[i] not in comp_dict:
                comp_dict[nums[i]] = i
            else:
                return [comp_dict[target - nums[i]], i]