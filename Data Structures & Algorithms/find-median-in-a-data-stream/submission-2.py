class MedianFinder:

    def __init__(self):
        self.left_maxHeap = []
        self.right_minHeap = []

    def addNum(self, num: int) -> None:
        if not self.left_maxHeap and not self.right_minHeap:
            heapq.heappush(self.right_minHeap,num)
            return
        if num < self.right_minHeap[0]:
            heapq.heappush(self.left_maxHeap,-num)                
        else:
            heapq.heappush(self.right_minHeap,num)
        shorter, longer = self.left_maxHeap, self.right_minHeap
        rightLonger = True
        if len(self.left_maxHeap) > len(self.right_minHeap):
            rightLonger = False
            shorter, longer = self.right_minHeap, self.left_maxHeap
        while len(longer) - len(shorter) > 1:
            if rightLonger:
                heapq.heappush(self.left_maxHeap,-heapq.heappop(self.right_minHeap))
            else:
                heapq.heappush(self.right_minHeap,-heapq.heappop(self.left_maxHeap))
        

    def findMedian(self) -> float:
        total_len = len(self.left_maxHeap) + len(self.right_minHeap)
        if total_len % 2:
            if len(self.left_maxHeap) <= len(self.right_minHeap):
                return self.right_minHeap[0]  
            else:
                return -self.left_maxHeap[0]                          
        else:
            return (-self.left_maxHeap[0] + self.right_minHeap[0]) / 2
        