class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We need to know the furthest a current bar can go to the right and left
        # If we store the heights and their index increasing order, we can find the left boundary by popping until smaller height. 
        # The right boundary is when we encounter a smaller height.
        # So when we encounter the right boundary for the top of our stack
        # we calculate it by  
        # We basically do all the work for the past heights once we encounter a smaller height.

        stack = []
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                width = i - prev_i
                maxArea = max(maxArea,width*prev_h)
                start = prev_i # this keeps moving backwards until the height on top of the stack is smaller current height
            stack.append([start,h])

        # if there are any values left, that means they were smaller than everything that came after, so they can extend all the way to the end 
        full_width = len(heights)
        for i,h in stack:
            maxArea = max(h*(full_width-i),maxArea)

        return maxArea
            