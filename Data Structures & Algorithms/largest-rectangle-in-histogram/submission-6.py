class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index,height)
        max_area = 0


        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                popped_i, popped_h = stack.pop()
                width = i - popped_i
                max_area = max(width*popped_h,max_area)
                start = popped_i
            stack.append([start,h])

        for stack_pair in stack:
            width = len(heights) - stack_pair[0]
            height = stack_pair[1]
            max_area = max(width*height,max_area)

        return max_area