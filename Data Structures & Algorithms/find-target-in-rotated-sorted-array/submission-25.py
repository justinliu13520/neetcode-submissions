class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(m)
            if nums[m] == target:
                return m
            if nums[m] < nums[r]:
                if target > nums[m] and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1

        return -1