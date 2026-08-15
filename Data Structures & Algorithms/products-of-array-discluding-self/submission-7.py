class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1] * len(nums)
        suffix_sum = [1] * len(nums)

        product = 1
        for i in range(len(nums)-1):
            product *= nums[i]
            prefix_sum[i] = (product)
        print(prefix_sum)
        product = 1
        for j in range(len(nums)-1,0,-1):
            product *= nums[j]
            suffix_sum[j] = (product)
        print(suffix_sum)

        res = [suffix_sum[1]]
        for k in range(1,len(nums)-1):
            res.append(prefix_sum[k-1]*suffix_sum[k+1])
        res.append(prefix_sum[len(nums)-2])
        return res