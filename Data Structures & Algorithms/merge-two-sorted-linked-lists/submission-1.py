# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        cur_node = head
        while list1 or list2:
            if list1 is None:
                cur_node.next = list2
                cur_node = cur_node.next
                list2 = list2.next
            elif list2 is None:
                cur_node.next = list1
                cur_node = cur_node.next
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    cur_node.next = list1
                    cur_node = cur_node.next
                    list1 = list1.next
                else:
                    cur_node.next = list2
                    cur_node = cur_node.next
                    list2 = list2.next
        
        return head
       