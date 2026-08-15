class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracker = []

    def push(self, val: int) -> None:
        if len(self.min_tracker) == 0:
            self.min_tracker.append(val)
        elif self.min_tracker[-1] >= val:
            self.min_tracker.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_tracker[-1]:
            self.min_tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker[-1]
