class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if first number < last number, no rotation so return first number
        # find the mid point of first and last
        # if the number is bigger than the first number, we know the smaller number is to the right, so we move our left pointer int
        # vice versa, if the mid number is smaller than the right number, we move our right pointer in, but we include mid in right because it might be the smallest.
        if nums[0] < nums[-1]:
            return nums[0]
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            n = nums[mid]
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] < n and nums[l] > nums[r]: #numbers between are ascending, no way min
                l = mid + 1
            elif nums[l] > n:
                r = mid
            else:
                return min(nums[l],nums[r])
            
        return min(nums[l],nums[r])
