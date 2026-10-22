class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        # print(cars)

        stack = []
        for p,s in cars:
            # y = mx + b
            # target = s * x + p
            x = (target - p) / s
            if not stack:
                stack.append(x)
            else:
                if x > stack[-1]:
                    stack.append(x)
        return len(stack)