# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next # gets us to halfway point - 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next # we do next because second half
        slow.next = prev_node = temp = None # slice off second half

        while second: # swap
            temp = second.next
            second.next = prev_node 
            prev_node = second
            second = temp
        
        second = prev_node
        first = head
        while second:
            # 1    3   5
            # |  / |  /
            # | /  | /
            # 2    4
            # 1,3,5,4,2
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        