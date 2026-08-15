class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                popped_i, _ = stack.pop()
                res[popped_i] = i - popped_i
            stack.append([i,t])
        return res