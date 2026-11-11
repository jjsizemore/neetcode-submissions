class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minHeap of size k will work, smallest/kth largest will be at front, smaller nums will have been popped

        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return heapq.heappop(minHeap)

        # Time O(n log k) n items each getting heappushed into a k size heap at log k time
        # Space O(k)