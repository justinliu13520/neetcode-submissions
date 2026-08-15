class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack to keep track of next greater height
        stack = []
        max_area = 0
        # loop to calculate the max area if we hit a right boundary
        # we need the index and height to put on to stack to know how far their boundaries are. The index in stack is the left boundary
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                popped_i, popped_h = stack.pop()
                max_area = max(max_area,popped_h*(i-popped_i))
                start = popped_i
            stack.append([start,h])
        # loop to calculate the max area of rectangles that didn't have a right boundary
        for stack_i, stack_h in stack:
            width = len(heights) - stack_i
            max_area = max(max_area,width*stack_h)
        return max_area