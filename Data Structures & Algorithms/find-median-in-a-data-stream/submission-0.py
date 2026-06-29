import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = [] 
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap,-num)
        elif num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap,-num)
            if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
                x = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap,-x)
        else:
            heapq.heappush(self.minHeap,num)
            if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
                x = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap,-x)

    def findMedian(self) -> float:

        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        elif len(self.maxHeap) - len(self.minHeap) == 1:
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()