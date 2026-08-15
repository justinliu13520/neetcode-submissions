class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l ,r = 0, len(heights)-1

        maxWater = 0
        while l < r:
            base = r - l
            height = min(heights[l],heights[r])
            maxWater = max(maxWater,base*height)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater