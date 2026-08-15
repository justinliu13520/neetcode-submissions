class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest_vals = []

    def push(self, val: int) -> None:
        if len(self.smallest_vals) == 0:
            self.smallest_vals.append(val)
        elif self.smallest_vals[-1] >= val:
            self.smallest_vals.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.smallest_vals[-1] == popped:
            self.smallest_vals.pop()
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.smallest_vals[-1]
