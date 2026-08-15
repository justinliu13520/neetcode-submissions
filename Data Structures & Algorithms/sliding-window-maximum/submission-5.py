class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # to keep track of the max in each window, we can use a queue
        # the queue allows us to get rid of non maxes in O(1) and maxes
        # not in the current window anymore
        # The front of the queue will always hold the biggest number
        output = []
        l = r = 0
        q = deque()

        while r < len(nums):

            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
