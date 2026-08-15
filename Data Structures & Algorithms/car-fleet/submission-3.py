class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position,speed),reverse=True)
        for p,s in cars:
            # y = mx + b
            # target = speed * x + position
            x = (target - p) / s
            if len(stack) == 0:
                stack.append(x)
            else:
                if stack[-1] >= x:
                    continue
                else:
                    stack.append(x)
        return len(stack)