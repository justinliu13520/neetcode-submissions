class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []
        # print("initialized")

    def push(self, val: int) -> None:
        # print("stacks before pushing",val,self.stack,self.minList)
        if not self.minList:
            self.minList.append(val)
        elif self.minList[-1] >= val:
            self.minList.append(val)
        self.stack.append(val)
        # print("stacks after pushing",val,self.stack,self.minList)


    def pop(self) -> None:
        # print("stacks before pop:",self.stack,self.minList)
        if self.stack:
            val = self.stack.pop()
            if self.minList and self.minList[-1] == val:
                self.minList.pop()
        # print("stacks after pop:",self.stack,self.minList)
            
    def top(self) -> int:
        # print("stacks before top:",self.stack,self.minList)
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        return self.minList[-1]
