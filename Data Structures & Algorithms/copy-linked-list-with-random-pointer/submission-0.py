"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy #keys are the nodes in og, copy is val
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur] #get copy
            copy.next = oldToCopy[cur.next] #set copy's fields
            copy.random = oldToCopy[cur.random]
            cur = cur.next # net key
        return oldToCopy[head]