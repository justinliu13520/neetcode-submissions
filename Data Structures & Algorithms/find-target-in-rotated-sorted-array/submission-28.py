class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            m = (l+r) // 2
            mid_num = nums[m]
            print(mid_num)
            if mid_num == target:
                return m
            elif mid_num <= nums[r]:
                if mid_num < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if mid_num > target and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1