class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # increasing monotonic stack that acts as our right boundary
        max_area = 0
        stack = [] # [index,height]
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                width = i - popped_i
                max_area = max(max_area,popped_h*width)
                start = popped_i
            stack.append([start,h])
        
        for stack_i,stack_h in stack:
            width = len(heights) - stack_i
            max_area = max(max_area,width*stack_h)
        
        return max_area
