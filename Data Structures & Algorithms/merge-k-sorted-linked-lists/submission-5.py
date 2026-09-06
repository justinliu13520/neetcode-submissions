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
        # merging 2 linked list is easy. If we can break this problem down into
        # that, then this would be a little easier. If i were to merge the first two lists, and compare it to the next list and repeat it, then we would be able to accumlate the sort. The question is how? If we were to append the merged of the first two to the end of ths list and while we have more than 1 item, then we keep merging and return the last item in the list
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            lists.append(self.mergeTwoLists(list1,list2)) 
        return lists[0]