class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = defaultdict(int)

        for task in tasks:
            freq_dict[task] += 1

        max_heap = []
        for val in freq_dict.values():
            max_heap.append(-val)
        heapq.heapify(max_heap)

        q = deque()
        cycles = 0

        while max_heap or q:
            cycles += 1

            if not max_heap:
                cycles = q[0][1]
            else:
                tasks_left = 1 + heapq.heappop(max_heap)
                if tasks_left:
                    q.append([tasks_left,cycles+n])
            if q and q[0][1] == cycles:
                heapq.heappush(max_heap,q.popleft()[0])
        return cycles                    