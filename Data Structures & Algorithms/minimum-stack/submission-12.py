class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        if not self.min_vals:
            self.min_vals.append(val)
        elif self.min_vals[-1] >= val:
            self.min_vals.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_vals[-1]:
            self.min_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
