# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) # dummy node that points at the head
        groupPrev = dummy # represents the node before each group/last in the previous group 

        while True:
            # Get the kth node
            kth = self.getKthNode(groupPrev,k)
            if kth is None:
                break
            # beginning of next group
            groupNext = kth.next

            # prev is kth.next first because we want the new group's end to point to the 
            # beginning of the next group
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            #connecting the groups
            # on the first iteration, grabs the first node which is now the last node in the first group
            # in future iterations, grabs the first node of the group to set as groupPrev
            tmp = groupPrev.next

            #on the first iteration, this sets dummy's next to be the first kth
            # in future iterations, sets the previous's group next to the new last node of the new group
            # From 1 -> 4 to 1 -> 6
            groupPrev.next = kth

            # Sets up the groupPrev for the next group
            groupPrev = tmp
            
        return dummy.next


    def getKthNode(self,groupPrev: ListNode, k: int) -> ListNode:
        while groupPrev and k > 0:
            groupPrev = groupPrev.next
            k -= 1
        return groupPrev


