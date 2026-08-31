# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        cur_node = head
        len_of_list = 0
        while cur_node:
            len_of_list += 1
            cur_node = cur_node.next
        if len_of_list == n:
            return head.next
        cur_node = head

        for i in range(len_of_list):
            if i == len_of_list - n - 1:
                temp = cur_node.next.next
                cur_node.next.next = None
                cur_node.next = temp
                break
            cur_node = cur_node.next
        return head

