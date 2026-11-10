class KthLargest:

    # use a minHeap of size k, which will hold the k largest elems
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k

        heapq.heapify(self.minHeap)

        # by popping elems until heap is size k, we have the k largest elems, since popped vals are smallest
        # first value will be the kth largest
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

    # Time O(n + (n - k)log(n)) O(n) for each add
    #                           O((n - k)log(n)) -> log(n) for each pop * (n - k) pops
    # Space O(max(n, k))