class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                product *= nums[j]
            output.append(product)
            product = 1
        return output