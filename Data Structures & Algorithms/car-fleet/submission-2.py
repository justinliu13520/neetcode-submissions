class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        stack = []
        for pos, spd in cars:
            x = ((target - pos) / spd)
            if len(stack) == 0:
                stack.append(x)
            else:
                if stack[-1] < x:
                    stack.append(x)
        return len(stack)