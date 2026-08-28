class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_spd = sorted(zip(position,speed),reverse=True)

        for pos,spd in pos_spd:
            # y = mx + b
            # target = speed*x + position
            x = (target - pos) / spd
            if not stack or stack[-1] < x:
                stack.append(x)
        return len(stack)