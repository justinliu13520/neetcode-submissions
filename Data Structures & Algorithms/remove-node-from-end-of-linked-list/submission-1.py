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
        print(length_of_list)
        begin_to_target = length_of_list - n
        print(begin_to_target)
        cur_node = head
        temp = None
        prev_node = None
        for i in range(begin_to_target+1):
            if i == begin_to_target:
                print(i)
                temp = cur_node.next
                cur_node.next = None
                prev_node.next = temp
            else:
                prev_node = cur_node
                cur_node = cur_node.next
            
        return head