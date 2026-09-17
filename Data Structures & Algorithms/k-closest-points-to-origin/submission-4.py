class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = math.sqrt((point[0]*point[0]) + (point[1]*point[1]))
            heapq.heappush(heap,(-distance,point))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _,point in heap:
            res.append(point)
        return res
