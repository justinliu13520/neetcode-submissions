class LinkedList:
    
    def __init__(self):
        self.cur_list = list()
    
    def get(self, index: int) -> int:
        if index < len(self.cur_list):
            return self.cur_list[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_list = [val]
        for v in self.cur_list:
            new_list.append(v)
        self.cur_list = new_list

    def insertTail(self, val: int) -> None:
        self.cur_list.append(val)

    def remove(self, index: int) -> bool:
        if index < len(self.cur_list):
            self.cur_list.remove(self.cur_list[index])
            return True
        else:
            return False


    def getValues(self) -> List[int]:
        return self.cur_list
