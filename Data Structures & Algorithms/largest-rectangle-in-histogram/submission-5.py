class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index,height)
        max_area = 0
        for i,h in enumerate(heights):
            start = i # we do start = i because we know
            while stack and stack[-1][1] > h: #right boundary
                popped_i, popped_h = stack.pop()
                width = i - popped_i
                max_area = max(max_area,popped_h*width)
                start = popped_i # we move the index back until we're bigger than what's in the stack
            stack.append((start,h))

        for s in stack:
            s_index, s_height = s
            width = len(heights)-s_index
            max_area = max(width*s_height,max_area)
        return max_area

