class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # maxHeap holding k smallest
        maxHeap = []

        heapq.heapify(maxHeap)

        for x, y in points:
            heapq.heappush(maxHeap, (-(x**2 + y**2), x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [[x, y] for dist, x, y in maxHeap]

        # Time O(n log k)
        # Space O(k)