import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = [(-val,key) for key,val in counter.items()]

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            val,key = heapq.heappop(heap)
            res.append(key)
        return res