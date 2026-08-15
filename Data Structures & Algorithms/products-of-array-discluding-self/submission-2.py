class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_of_zeroes = 0
        zero_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                num_of_zeroes += 1
                zero_index = i
        if num_of_zeroes >= 2:
            return [0 for i in range(len(nums))]
        product_with_no_zero = 1
        for n in nums:
            if n == 0:
                continue
            product_with_no_zero *= n
        if num_of_zeroes == 1:
            return [0 if i != zero_index else product_with_no_zero for i in range(len(nums))]

        total_product = 1
        for n in nums:
            total_product *= n

        output = []
        for n in nums:
            output.append(total_product/n)
        
        return list(map(int,output))