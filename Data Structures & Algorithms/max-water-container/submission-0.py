class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        
        l,r = 0, len(heights)-1
        max_area = 0
        # Area = width * min(heights[l],heights[r])
        while l < r:
            width = r-l
            area = width * min(heights[l],heights[r])
            if area > max_area:
                max_area = area
            if min(heights[l],heights[r]) is heights[l]:
                l += 1
            elif min(heights[l],heights[r]) is heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
            