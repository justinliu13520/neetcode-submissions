class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = defaultdict(int)
        for task in tasks:
            freq_dict[task] += 1
        
        q = deque() #task_left,cycles
        cycles = 0

        task_heap = [-x for x in freq_dict.values()]
        heapq.heapify(task_heap)

        while task_heap or q:
            cycles += 1
            if not task_heap:
                cycles = q[0][1]
            else:
                task_left = 1 + heapq.heappop(task_heap)
                if task_left:
                    q.append([task_left,cycles+n])
            if q and q[0][1] == cycles:
                heapq.heappush(task_heap,q.popleft()[0])
        return cycles

