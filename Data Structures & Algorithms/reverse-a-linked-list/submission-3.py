# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        temp = prev_node = None
        while cur_node:
            temp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp
        return prev_node