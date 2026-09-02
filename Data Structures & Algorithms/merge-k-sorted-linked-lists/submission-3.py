# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeTwoLists(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1

        cur_head = None
        if list1.val <= list2.val:
            cur_head = list1
            list1 = list1.next
        else:
            cur_head = list2
            list2 = list2.next
        res = cur_head
        while list1 or list2:
            if not list1:
                cur_head.next = list2
                list2 = list2.next
                cur_head = cur_head.next
            elif not list2:
                cur_head.next = list1
                list1 = list1.next
                cur_head = cur_head.next
            else:
                if list1.val <= list2.val:
                    cur_head.next = list1
                    list1 = list1.next
                    cur_head = cur_head.next
                else:
                    cur_head.next = list2
                    list2 = list2.next
                    cur_head = cur_head.next
        return res
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            list2 = lists.pop(0)
            list1 = lists.pop(0)
            merged = self.mergeTwoLists(list1,list2)
            lists.append(merged)
            
        return lists[0]