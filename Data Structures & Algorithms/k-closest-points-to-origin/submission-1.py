class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distance_dict = defaultdict(list)
        distances = []
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            distances.append(distance)
            points_distance_dict[distance].append(point)
        heapq.heapify(distances)
        res = []
        for _ in range(k):
            distance = heapq.heappop(distances)
            res.append(points_distance_dict[distance].pop())
        return res