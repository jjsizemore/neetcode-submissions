class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [stone * -1 for stone in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            x, y = heapq.heappop(minHeap) * -1, heapq.heappop(minHeap) * -1
            print(f'x: {x}, y: {y}')

            if x == y:
                continue
            heapq.heappush(minHeap, abs(x - y) * -1)

        return -minHeap[0] if minHeap else 0

        # Time O(n log n), n = # stones, log n for each heappush. heapify is optimal at O(n) ammortized
        # Space O(n)
