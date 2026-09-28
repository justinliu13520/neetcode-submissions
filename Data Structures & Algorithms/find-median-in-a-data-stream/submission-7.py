class MedianFinder:

    def __init__(self):
        self.left_maxHeap = []
        self.right_minHeap = []

    def addNum(self, num: int) -> None:
        if not self.left_maxHeap and not self.right_minHeap:
            heapq.heappush(self.right_minHeap,num)
            print(self.left_maxHeap,self.right_minHeap)
            return
        if num < self.right_minHeap[0]:
            heapq.heappush(self.left_maxHeap,-num)
        else:
            heapq.heappush(self.right_minHeap,num)
        if len(self.right_minHeap) - len(self.left_maxHeap) > 1:
            heapq.heappush(self.left_maxHeap,-heapq.heappop(self.right_minHeap))
        if len(self.left_maxHeap) - len(self.right_minHeap) > 1:
            heapq.heappush(self.right_minHeap,-heapq.heappop(self.left_maxHeap))
    def findMedian(self) -> float:
        total = len(self.left_maxHeap) + len(self.right_minHeap)
        if total % 2 == 1:
            if len(self.right_minHeap) > len(self.left_maxHeap):
                return self.right_minHeap[0]
            else:
                 return -self.left_maxHeap[0]
        else:
            return (self.right_minHeap[0] + -self.left_maxHeap[0]) / 2
        