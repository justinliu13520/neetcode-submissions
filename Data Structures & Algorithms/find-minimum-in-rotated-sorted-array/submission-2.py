class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1]:
            return nums[0]

        # middle smaller than both -> record middle and do r = m -1
        # middle bigger than both -> l = m + 1
        # middle bigger than left, smaller than right -> r = m - 1
        l = 0
        r = len(nums) - 1
        res = 100001
        while l <= r:
            if l + 1 == r and nums[l] > nums[r]:
                return nums[r]
            m = l + (r-l)//2
            print(nums,"middle:",nums[m],"left:",nums[l],"right:",nums[r])
            if nums[m] <= nums[l] and nums[m] <= nums[r]:
                print("middle smaller than both")
                res = min(res,nums[m])
                r = m - 1
            elif nums[m] > nums[l] and nums[m] > nums[r]:
                print("middle bigger than both")
                l = m + 1
            elif nums[m] > nums[l] and nums[m] < nums[r]: # 1 3 5
                print("middle is in order")
                r = m - 1
            # 5 1 3 / 3 5 1 / 1 3 5 
        return res