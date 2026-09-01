class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.val = value
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key : Node
        self.cap = capacity
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node):
        prev,next = node.prev, node.next
        node.prev.next, node.next.prev = next, prev
    def insert(self,node):
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next = node
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove and then move to end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            



