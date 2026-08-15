class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]

        total_water = 0
        while l < r: 

            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])
                total_water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight,height[r])
                total_water += maxRight - height[r]

        return total_water