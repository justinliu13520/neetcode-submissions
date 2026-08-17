class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = [nums[0]]
        suffix_list = deque([nums[-1]])

        # prefix_list
        for i in range(1,len(nums)):
            prefix_list.append(prefix_list[i-1]*nums[i])
        for j in range(len(nums)-2,-1,-1):
            suffix_list.appendleft(nums[j]*suffix_list[0])
        # print(prefix_list,suffix_list)
        res = [suffix_list[1]]
        for k in range(1,len(nums)-1):
            res.append(prefix_list[k-1]*suffix_list[k+1])
        res.append(prefix_list[-2])
        return res