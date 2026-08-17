# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        prev_node = None
        while head:
            temp = head.next
            head.next = prev_node
            prev_node = head
            head = temp
        return prev_node