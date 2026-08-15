class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_dict = {}

        for n in range(len(nums)):
            if target-nums[n] not in compliment_dict:
                compliment_dict[nums[n]] = n
            else:
                return [compliment_dict[target-nums[n]],n]

        return []