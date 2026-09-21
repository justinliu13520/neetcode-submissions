from _heapq import heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = defaultdict(int)
        for task in tasks:
            freq_dict[task] += 1
        
        max_heap = [-x for x in freq_dict.values()]
        heapq.heapify(max_heap)
        q = deque()
        cycles = 0
        while max_heap or q:
            cycles += 1
            if not max_heap:
                cycles = q[0][1]
            else:
                task_left = 1 + heapq.heappop(max_heap)
                if task_left:
                    q.append([task_left,cycles+n])
            if q and q[0][1] == cycles:
                heapq.heappush(max_heap,q.popleft()[0])
        return cycles

