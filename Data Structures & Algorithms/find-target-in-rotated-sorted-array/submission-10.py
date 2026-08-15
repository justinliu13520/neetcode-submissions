class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l,r) -> int:
            while l <= r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        if nums[0] <= nums[-1]:
            return binary_search(0,len(nums)-1)

        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                return binary_search(l,r)
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]: # l -> middle, ascending numbers/second half
                if target < nums[l]: # has to be to the right of middle
                    l = m + 1
                elif target > nums[m]: # means middle number MIGHT not be greatest number
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] < nums[l]: # l -> middle, has the first number and last in between
                if target < nums[l] and target > nums[m]: # has to be to right of middle
                    l = m + 1
                elif  target > nums[l] and target > nums[m]: # has to be left of middle
                    r = m - 1
                elif target < nums[l] and target < nums[m]: # smaller than middle number
                    r = m - 1
                elif target == nums[l]:
                    return l
                else:
                    return -1
            # else:
            #     l = m + 1
        return -1


            

               


