# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1, list2):
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            print(lists)
            list2 = lists.pop(1)
            list1 = lists.pop(0)  
            merged = self.mergeTwoLists(list1,list2)
            lists.append(merged)
        print(lists[0])
        return lists[0]
        