# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKthNode(self,curr,k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1,head)
        groupPrev = dummyHead

        while True:
            kth = self.getKthNode(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummyHead.next




