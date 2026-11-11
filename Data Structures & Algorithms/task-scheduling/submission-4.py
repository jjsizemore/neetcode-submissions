class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time = 0
        # count tasks
        # set them up in a maxHeap keyed by count left to do
        # heappop the task with max num left
        # when heap task is successful, add the task to a queue in tuple (time + n, task, numLeft)
        # time += 1
        # check if task at beginning of queue is ready based on item[0] >= time
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord("A")] += 1
        # -timesLeft, task #, time ready to run
        maxHeap = [(-freq, idx, 0) for idx, freq in enumerate(count) if freq > 0]

        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            # put tasks that are ready to be run back in the heap
            while q and q[0][2] <= time:
                heapq.heappush(maxHeap, q.popleft())

            if maxHeap:
                (count, idx, readyTime) = heapq.heappop(maxHeap)
                if not count:
                    continue

                # complete 1 run of this task; counts are negative
                count += 1
                # Need to add n + 1 time so that n cycles will have passed
                readyTime = time + n + 1
                if count != 0:
                    q.append((count, idx, readyTime))

            time += 1

        return time

        # Time O(n log 26) -> O(n), n = total # task runs
        # Space O(1) -> const space for count, heap, queue, max 26 each