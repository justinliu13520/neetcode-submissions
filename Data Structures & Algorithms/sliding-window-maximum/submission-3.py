class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0
        q = deque()

        while r < len(nums):
            # we are storing the index in q
            # If the last number in queue is smaller than the current
            # we dont need it because we're looking for the max in the window
            while q and nums[r] > nums[q[-1]]: 
                q.pop()
            q.append(r)

            # if left index is greater than the first index in queue,
            # then we have moved on from the previous window and need to
            # not append it for the new window
            if l > q[0]:
                q.popleft()
            
            # we compare r + 1 because once we reach window of k size
            # we'll always be adding a new max. So this is just for the 
            # building the initial window and then after adding the new 
            # max of each window and incrementing l as right always increases
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

            