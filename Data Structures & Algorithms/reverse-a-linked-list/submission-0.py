# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# None    A -> B -> None
# None <- A    B -> None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        cur_node = head
        prev_node = None
        tmp = None
        while cur_node.next is not None:
            # store cur_node's next pointer
            # point cur_node's next to previous
            # set cur_node to be what the next pointer was pointing at
            tmp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = tmp
        cur_node.next = prev_node
        return cur_node

