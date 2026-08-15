class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if middle smaller than right, middle to end is in order
        # if middle bigger than right, smallest is to the right
        # depending on the target, go left or right
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            print(nums, l, m, r)
            if nums[m] == target:
                return m
            elif l == r and nums[l] != target:
                return -1
            elif nums[m] < nums[r]: # middle to right in order
                if nums[m] < target and target <= nums[r]:
                    # target between middle and right
                    l = m + 1
                else:
                    # has to be on left since not in right side
                    r = m - 1
            elif nums[m] > nums[r]: # middle to right not in order
                if nums[m] > target and target >= nums[l]:
                    # the left side is sorted, and target between left and middle
                    r = m - 1
                else:
                    l = m + 1

            
        return -1