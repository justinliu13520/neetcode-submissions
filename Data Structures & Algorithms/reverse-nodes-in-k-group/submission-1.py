# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        groupPrev = dummyNode

        while True:
            kth = self.getKth(groupPrev,k)
            if not kth: # if there's no k, less than k so break out
                break
            groupNext = kth.next # where next group starts
            curr = groupPrev.next # on the intial, this would be the first node because the dummy node's next is the head
            # after the first group, this would be the first node in the group because groupPrev.next points at the next group's first
            prev = kth.next # kth.next because we want the first node in a group to point to the next group
            while curr != groupNext: # reverse up to the next group
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next # this was the first node in the next group. We save it so we can set it to be the next group's previous
            groupPrev.next = kth # set the previous group to the next head of the reversed group
            groupPrev = temp # set the groupPrev to be the new tail of the just reversed group
        return dummyNode.next
    def getKth(self,curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr






