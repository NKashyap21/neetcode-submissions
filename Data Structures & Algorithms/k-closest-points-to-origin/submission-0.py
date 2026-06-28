import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_d = [(-(x**2+y**2),(x,y)) for x,y in points]
        heap = points_d[:k]
        heapq.heapify(heap)

        for dist,(x,y) in points_d[k:]:
            if dist > heap[0][0]:
                heapq.heapreplace(heap,(dist,(x,y)))
        
        res = []
        while heap:
            dist,(x,y) = heapq.heappop(heap)
            res.append([x,y])
        return res 
