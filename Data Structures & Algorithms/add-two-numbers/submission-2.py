# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit = l1.val + l2.val
        carry = 0
        if digit >= 10:
            carry = 1
            digit = digit % 10
        l1 = l1.next
        l2 = l2.next
        cur_head = ListNode(digit)
        dummy_head = cur_head
        while l1 or l2 or carry:
            if l1 and l2:
                digit = l1.val + l2.val + carry
                carry = 0
                if digit >= 10:
                    carry = 1
                    digit = digit % 10
                cur_head.next = ListNode(digit)
                l1 = l1.next
                l2 = l2.next
            elif l2:
                digit = l2.val + carry
                carry = 0
                if digit >= 10:
                    carry = 1
                    digit = digit % 10
                cur_head.next = ListNode(digit)
                l2 = l2.next
            elif l1:
                digit = l1.val + carry
                carry = 0
                if digit >= 10:
                    carry = 1
                    digit = digit % 10
                cur_head.next = ListNode(digit)
                l1 = l1.next
            else:
                cur_head.next = ListNode(carry)
                carry = 0
            cur_head = cur_head.next
        return dummy_head