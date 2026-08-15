class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i,h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                width = i - popped_i
                max_area = max(max_area,width*popped_h)
                start = popped_i
            stack.append([start,h])
        
        for stack_i, stack_h in stack:
            max_area = max(max_area,(len(heights)-stack_i)*stack_h)
        
        return max_area