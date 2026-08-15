class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2,3,4,5,6] l = m + 1
        # [6,1,2,3,4,5] not ordered left -> nums[l] > target or target > nums[m]
        # [3,4,5,6,1,2] ordered left -> nums[r] < target or target < nums[m]
        l,r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]: # <= because if case is one long, we need to move our left
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1