class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in compliment_dict:
                compliment_dict[nums[i]] = i
            else:
                return [compliment_dict[comp],i]