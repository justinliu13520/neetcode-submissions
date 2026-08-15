class Solution:
    def findMin(self, nums: List[int]) -> int:
        # two cases to consider:
        # when l -> m is ordered and not ordered
        # when ordered: min has to either be l or it's in the right half
        # when not ordered: min has to be in the left half, either in between or is m

        l,r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] <= nums[m]: 
                if nums[l] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                r = m
        return min(nums[l],nums[r])
    

