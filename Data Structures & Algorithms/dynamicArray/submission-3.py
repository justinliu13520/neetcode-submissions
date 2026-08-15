class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = dict()
        for i in range(capacity):
            self.index[i] = "empty"


    def get(self, i: int) -> int:
        return self.index[i]

    def set(self, i: int, n: int) -> None:
        self.index[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        
        self.index[self.getSize()] = n

    def popback(self) -> int:
        val = self.index[self.getSize() - 1]
        self.index[self.getSize() - 1] = "empty"
        return val

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        for i in range(len(self.index),self.capacity):
            self.index[i] = "empty"

    def getSize(self) -> int:
        size = 0
        for i in range(self.capacity):
            if i in self.index and self.index[i] != "empty":
                size += 1
        return size
    
    def getCapacity(self) -> int:
        return self.capacity
