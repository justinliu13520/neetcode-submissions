class MedianFinder:
    # we want to split the stream into 2 heaps, where the left is the smaller half and right is the bigger half. Because the median is always the biggest of left and smallest of right, we can use a min and a max heap
    def __init__(self):
        self.left_maxHeap = []
        self.right_minHeap = []

    def addNum(self, num: int) -> None:
        #put into the right heap because 1 is odd and we pull median from right peek when odd
        if not self.left_maxHeap and not self.right_minHeap:
            heapq.heappush(self.right_minHeap,num)
            return
        #if the number is smaller than the min of the bigger half, put it in the left half
        if num < self.right_minHeap[0]:
            heapq.heappush(self.left_maxHeap,-num)                
        else:
            heapq.heappush(self.right_minHeap,num)
        
        # what if the median is in the wrong half and not at the minHeap or maxHeap peek? We rebalance when one is too long. It should always be at most 1 bigger
        shorter, longer = self.left_maxHeap, self.right_minHeap
        rightLonger = True
        if len(self.left_maxHeap) > len(self.right_minHeap):
            rightLonger = False
            shorter, longer = self.right_minHeap, self.left_maxHeap
        if len(longer) - len(shorter) > 1:
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
        