class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        position_speed = sorted(zip(position,speed),reverse=True)

        for p,s in position_speed:
            # target = speed*x + position -> x = (target - position) / speed
            x = (target - p) / s
            if stack:
                if stack[-1] < x:
                    stack.append(x)
            else:
                stack.append(x)
        return len(stack)