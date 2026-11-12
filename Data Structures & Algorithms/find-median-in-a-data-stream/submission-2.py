import heapq
class MedianFinder:
    # Divide the array into two parts
    # 2 heaps, minHeap for the top half, maxHeap for the bottom half
    # on add, negate and add to lower half (maxHeap)
    # if len(bottom) > len(top) + 1, heappop from bottom into top (make sure to make positive again)
    # median will be top of bottom if lengths don't match, average of top of each otherwise

    # Space O(n)
    def __init__(self):
        # minHeap
        self.top = []
        # maxHeap via negation
        self.bot = []
        heapq.heapify(self.top)
        heapq.heapify(self.bot)
        
    # Time O(log n/2) -> O(log n)
    def addNum(self, num: int) -> None:
        # Push into bottom unless value should be in the top half
        if self.top and num > self.top[0]:
            heapq.heappush(self.top, num)
        else:
            heapq.heappush(self.bot, -num)

        # Keep heaps balanced to maintain accurate median
        if len(self.bot) > len(self.top) + 1:
            heapq.heappush(self.top, -heapq.heappop(self.bot))
        if len(self.top) > len(self.bot) + 1:
            heapq.heappush(self.bot, -heapq.heappop(self.top))

    # O(1) Time
    def findMedian(self) -> float:
        if len(self.bot) > len(self.top):
            return -self.bot[0]
        elif len(self.bot) < len(self.top):
            return self.top[0]
        return (-self.bot[0] + self.top[0]) / 2

        