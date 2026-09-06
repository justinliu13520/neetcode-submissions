class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[index, height]
        max_area = 0
        for cur_index,cur_height in enumerate(heights):
            left_boundary = cur_index
            while stack and cur_height < stack[-1][1]:
                popped_i, popped_height = stack.pop()
                width = cur_index - popped_i
                max_area = max(max_area,width*popped_height)
                left_boundary = popped_i
            stack.append([left_boundary,cur_height])

        for stack_i,stack_h in stack:
            max_area = max(max_area,(len(heights)-stack_i)*stack_h)
        return max_area


