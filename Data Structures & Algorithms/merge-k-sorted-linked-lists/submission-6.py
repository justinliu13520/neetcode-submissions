# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoList(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1
        cur_node = None
        if list1.val <= list2.val:
            cur_node = list1
            list1 = list1.next
        else:
            cur_node = list2
            list2 = list2.next
        res = cur_node
        while list1 or list2:
            if not list1:
                cur_node.next = list2
                list2 = list2.next
                cur_node = cur_node.next
            elif not list2:
                cur_node.next = list1
                list1 = list1.next
                cur_node = cur_node.next
            else:
                if list1.val <= list2.val:
                    cur_node.next = list1
                    list1 = list1.next
                    cur_node = cur_node.next
                else:
                    cur_node.next = list2
                    list2 = list2.next
                    cur_node = cur_node.next
        return res
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(self.mergeTwoList(l1,l2))
        return lists[0]







