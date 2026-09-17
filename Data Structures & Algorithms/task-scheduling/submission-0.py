class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = defaultdict(int)
        for task in tasks:
            freq_dict[task] += 1
        queue = deque()
        heap = [-val for val in freq_dict.values()]
        heapq.heapify(heap)
        cycles = 0
        # none X
        while len(heap) > 0 or queue:
            cycles += 1
            if not heap:
                cycles = queue[0][1]
            else:
                tasks_left = 1 + heapq.heappop(heap) # add 1 because max heap vals are negative
                if tasks_left: # if not 0 tasks left, we add to queue with the earliest time it can be processes
                    queue.append([tasks_left,cycles+n])
            if queue and queue[0][1] == cycles:
                heapq.heappush(heap,queue.popleft()[0])
        return cycles

