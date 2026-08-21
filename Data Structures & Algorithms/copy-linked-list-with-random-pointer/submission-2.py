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
        original_to_copy = defaultdict(lambda: Node(0))
        original_to_copy[None] = None
        cur_head = head
        while cur_head:
            original_to_copy[cur_head].val = cur_head.val
            original_to_copy[cur_head].next = original_to_copy[cur_head.next]
            original_to_copy[cur_head].random = original_to_copy[cur_head.random]
            cur_head = cur_head.next
        return original_to_copy[head]