# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        prev_node = slow.next = None
        temp = None
        while second_head:
            temp = second_head.next
            second_head.next = prev_node
            prev_node = second_head
            second_head = temp
        
        second_head = prev_node
        first_head = head

        while second_head:
            temp1 = first_head.next
            temp2 = second_head.next

            first_head.next = second_head
            second_head.next = temp1

            first_head = temp1
            second_head = temp2








