class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # because there is for sure a duplicate and all numbers are less than 
        # the length of the list, the values can be used as indexes. If there 
        # are duplicates, then they will point to the same index

        # fast and slow pointers can be used to find the cycle which is
        # bascially duplicates 
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: #duplicate/cycle found. This is saying they're pointing at the same value, but doesn't get index that value is at
                break
        
        slow2 = 0 # we use another slow pointer to actually find the value

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow