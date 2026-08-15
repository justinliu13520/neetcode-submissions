class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_list = [1 for _ in range(len(nums))]
        prefix_list = [1 for _ in range(len(nums))]

        suffix_product = 1
        for i in range(len(nums)-1,-1,-1):
            suffix_product *= nums[i]
            suffix_list[i] *= (suffix_product)
        print(suffix_list)
    
        prefix_product = 1
        for j in range(len(nums)):
            prefix_product *= nums[j]
            prefix_list[j] *= (prefix_product)
        print(prefix_list)

        output_list = [suffix_list[1]]
        for k in range(1,len(nums)-1):
            output_list.append(prefix_list[k-1]*suffix_list[k+1])
        output_list.append(prefix_list[len(nums)-2])
        return output_list