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

        length_of_list = 0
        while cur_node:
            cur_node = cur_node.next   
            length_of_list += 1
        if length_of_list == n:
            return head.next
        begin_to_target = length_of_list - n
        cur_node = head
        for i in range(begin_to_target+1):
            if i == begin_to_target-1:
                print(i)
                cur_node.next = cur_node.next.next
                break
            else:
                cur_node = cur_node.next
        return head