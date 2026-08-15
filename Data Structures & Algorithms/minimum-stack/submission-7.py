class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = None
        self.minList = list()


    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        if self.min >= val:
            self.min = min(self.min,val)
            self.minList.append(self.min)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minList[len(self.minList)-1]:
            self.minList.pop()
            if len(self.minList) == 0:
                self.min = None
                return
            self.min = self.minList[len(self.minList)-1]

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        
        return self.min
