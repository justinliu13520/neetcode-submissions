class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [i,h]
        max_area = 0

        for cur_i,cur_h in enumerate(heights):
            start_i = cur_i
            while stack and stack[-1][1] > cur_h:
                stack_i, stack_h = stack.pop()
                width = cur_i - stack_i
                max_area = max(max_area,width*stack_h)
                start_i = stack_i
            stack.append([start_i,cur_h])
        
        for stack_i,stack_h in stack:
            width = len(heights) - stack_i
            max_area = max(max_area,width*stack_h)
        return max_area
