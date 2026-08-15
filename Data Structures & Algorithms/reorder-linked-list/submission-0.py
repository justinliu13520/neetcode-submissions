# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        
        # 1. Get length
        len_list = 0
        curr = head
        while curr:
            len_list += 1
            curr = curr.next
        
        # 2. Find the split point
        # We want to stop at the node just before the second half
        prev_to_second = head
        for _ in range((len_list - 1) // 2):
            prev_to_second = prev_to_second.next
        
        # This is the "Sever Point" - THE MOST IMPORTANT PART
        second_half_head = prev_to_second.next
        prev_to_second.next = None 
        
        # 3. Reverse the second half
        prev_node = None
        curr = second_half_head
        while curr:
            tmp = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = tmp
        second_half_head = prev_node # prev_node is the new head of the reversed half

        # 4. Merge (Using a simple zipper)
        first_ptr = head
        second_ptr = second_half_head
        
        while second_ptr:
            # Save the next steps
            tmp1 = first_ptr.next
            tmp2 = second_ptr.next
            
            # Connect first to second
            first_ptr.next = second_ptr
            
            # Connect second to the rest of first (unless first is done)
            if tmp1:
                second_ptr.next = tmp1
            
            # Move pointers forward
            first_ptr = tmp1
            second_ptr = tmp2