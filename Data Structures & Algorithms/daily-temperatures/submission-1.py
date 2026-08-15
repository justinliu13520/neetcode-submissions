class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = deque()
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            if not temp_stack:
                temp_stack.append([i,current_temp])
            if current_temp <= temp_stack[len(temp_stack)-1][1]:
                temp_stack.append([i,current_temp])
            else:
                while temp_stack and current_temp > temp_stack[len(temp_stack)-1][1]:
                    last_temp = temp_stack.pop()
                    res[last_temp[0]] = i-last_temp[0]
                temp_stack.append([i,current_temp])
        for t in temp_stack:
            res[t[0]] = 0
        return res

