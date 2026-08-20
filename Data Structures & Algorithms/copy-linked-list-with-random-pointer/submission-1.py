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
        old_to_copy = {None:None}

        cur_node = head
        while cur_node:
            copy_node = Node(cur_node.val)
            old_to_copy[cur_node] = copy_node
            cur_node = cur_node.next
        cur_node = head
        while cur_node:
            copy_node = old_to_copy[cur_node]
            copy_node.next = old_to_copy[cur_node.next]
            copy_node.random = old_to_copy[cur_node.random]
            cur_node = cur_node.next
        return old_to_copy[head]



