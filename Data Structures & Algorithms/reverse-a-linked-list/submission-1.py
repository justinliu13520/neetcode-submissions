# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        # None -> 1 -> 2 -> 3, temp = None, prev_node = none
        # None <- 1 2 -> 3, temp = 1, move head to 2, prev_node = 1
        # None <- 1 <- 2 3, 
        temp = None
        prev_node = None
        while head != None:
            temp = head.next
            head.next = prev_node
            prev_node = head
            head = temp
        return prev_node