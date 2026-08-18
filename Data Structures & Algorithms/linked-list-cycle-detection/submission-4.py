# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow and fast:
            if fast.next is None:
                return False
            if slow.next is None:
                return False
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False