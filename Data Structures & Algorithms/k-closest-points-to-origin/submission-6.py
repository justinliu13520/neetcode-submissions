class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = math.sqrt((point[0]*point[0])+(point[1]*point[1]))
            heap.append([distance,point])
        heapq.heapify(heap)

        res = []
        while len(res) != k:
            res.append(heapq.heappop(heap)[1])
        return res