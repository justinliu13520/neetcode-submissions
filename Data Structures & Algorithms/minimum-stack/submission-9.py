class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, val: int) -> None:
        if not self.minList:
            self.minList.append(val)
        elif self.minList[-1] >= val:
            self.minList.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.minList and self.minList[-1] == val:
                self.minList.pop()
            
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        return self.minList[-1]
