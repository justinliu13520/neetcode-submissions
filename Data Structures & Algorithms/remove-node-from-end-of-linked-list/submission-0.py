# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_of_list = 0
        cur_node = head
        while cur_node:
            len_of_list += 1
            cur_node = cur_node.next if cur_node.next else None
        
        target = len_of_list - n
        # print(len_of_list, target)
        if target == 0:
            return head.next
        cur_node = head
        for i in range(len_of_list):
            # print(i,target,cur_node.val)
            if i == target-1:
                # print(cur_node.next.val, cur_node.next.next.val)
                if cur_node.next and cur_node.next.next:
                    # Normal case of setting next to node after the original next
                    cur_node.next = cur_node.next.next
                    cur_node = cur_node.next 
                    return head
                elif not cur_node.next.next:
                    # if the target is the last node
                    cur_node.next = None
                    return head
            else:
                # print("not the target")
                cur_node = cur_node.next

