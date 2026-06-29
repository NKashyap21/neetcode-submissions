from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()
        while heap or q:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append([count,time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
            

        return time
