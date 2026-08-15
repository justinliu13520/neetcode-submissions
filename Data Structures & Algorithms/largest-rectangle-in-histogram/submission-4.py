class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        index_height_stack = [(0,heights[0])]
        max_area = 0
        for i in range(1,len(heights)):
            if heights[i] >= index_height_stack[-1][1]:
                index_height_stack.append((i,heights[i]))
            else:
                starting_position = 0
                while index_height_stack and index_height_stack[-1][1] > heights[i]:
                    too_high_bar = index_height_stack.pop()
                    starting_position = too_high_bar[0]
                    width = i - starting_position
                    height = too_high_bar[1]
                    max_area = max(height*width,max_area)
                index_height_stack.append((starting_position,heights[i]))
            # print(i, index_height_stack)
        while index_height_stack:
            n = len(heights)
            last_bar = index_height_stack.pop()
            width = n - last_bar[0]
            height = last_bar[1]
            max_area = max(width*height,max_area)
        return max_area

