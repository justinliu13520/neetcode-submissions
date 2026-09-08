class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[index, temp]
        res = [0] * len(temperatures)

        for cur_i, cur_t in enumerate(temperatures):
            while stack and stack[-1][1] < cur_t:
                popped_i, _ = stack.pop()
                res[popped_i] = cur_i - popped_i
            stack.append([cur_i,cur_t])
        return res