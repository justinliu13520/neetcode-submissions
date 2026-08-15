# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur_node = ListNode()
        res_head = cur_node
        while l1 or l2 or carry:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            cur_node_val = l1_val + l2_val + carry
            if cur_node_val >= 10:
                cur_node_val -= 10
                carry = 1
            else:
                carry = 0
            tmp = ListNode(cur_node_val)
            cur_node.next = tmp
            cur_node = cur_node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return res_head.next
            