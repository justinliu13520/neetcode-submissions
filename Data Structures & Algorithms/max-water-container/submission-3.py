class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            height = min(heights[l],heights[r])
            base = r - l
            max_area = max(max_area,base*height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area