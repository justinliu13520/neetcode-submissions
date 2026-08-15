class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store temp and index, temp to compare and index to calculate
        res = [0] * len(temperatures) # default to 0 because if we dont touch it, no warmer day

        for cur_index, cur_temp in enumerate(temperatures):
            while stack and cur_temp > stack[-1][0]:
                _, past_index = stack.pop()
                res[past_index] = cur_index - past_index
            stack.append([cur_temp,cur_index])
        return res
