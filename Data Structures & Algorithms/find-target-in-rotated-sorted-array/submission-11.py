class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]: # first half in order
                if target > nums[mid]: # case where the middle number is not the biggest
                    l = mid + 1
                elif target < nums[l]: # in between l and middle
                    l = mid + 1
                else:
                    r = mid - 1
            else: # first half not in order, transitioning from biggest -> smallest
                if target < nums[mid]: # case where it's between transition
                    r = mid - 1
                elif target > nums[r]: # bigger than r means in the 
                    r = mid - 1
                else: # not in transition, between middle and right boundary
                    l = mid + 1
        return -1