class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix_dict = dict()
        suffix_dict = dict()

        prefix_product = 1
        for i in range(len(nums)-1):
            prefix_product *= nums[i]
            prefix_dict[i] = prefix_product

        suffix_product = 1
        for i in range(len(nums)-1,-1,-1):
            suffix_product *= nums[i]
            suffix_dict[i] = suffix_product
        
        output = [suffix_dict[1]]
        for i in range(1,len(nums)-1):
            product = prefix_dict[i-1] * suffix_dict[i+1]
            output.append(product)
        output.append(prefix_dict[len(nums)-2])
        return output
