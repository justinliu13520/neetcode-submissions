class MedianFinder:

    def __init__(self):
        self.left_maxheap = []
        self.right_minheap = []

    def addNum(self, num: int) -> None:
        if not self.left_maxheap and not self.right_minheap:
            heapq.heappush(self.right_minheap,num)
            return
        if num >= self.right_minheap[0]:
            heapq.heappush(self.right_minheap,num)
        else:
            heapq.heappush(self.left_maxheap,-num)
        if len(self.right_minheap) - len(self.left_maxheap) > 1:
            heapq.heappush(self.left_maxheap,-heapq.heappop(self.right_minheap))
        if len(self.left_maxheap) - len(self.right_minheap) > 1:
            heapq.heappush(self.right_minheap,-heapq.heappop(self.left_maxheap))
    def findMedian(self) -> float:
        if len(self.right_minheap) > len(self.left_maxheap):
            return self.right_minheap[0]
        elif len(self.left_maxheap) > len(self.right_minheap):
            return -self.left_maxheap[0]
        else:
            return (-self.left_maxheap[0] + self.right_minheap[0]) / 2
        