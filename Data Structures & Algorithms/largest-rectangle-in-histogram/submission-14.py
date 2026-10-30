class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i,h in enumerate(heights):
            cur_start = i
            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                width = i - popped_i
                max_area = max(max_area,width*popped_h)
                cur_start = popped_i
            stack.append([cur_start,h])
        
        for stack_i,stack_h in stack:
            width = len(heights) - stack_i
            max_area = max(max_area,width*stack_h)
        return max_area