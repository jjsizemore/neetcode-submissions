class MinHeap:
    
    def __init__(self):
        # start with dummy value so that index math works out to be left child of a node is at parent idx * 2
        #     parent  l child                         1
        #        |     |                          2       3
        # [0, 1, 2, 3, 4, 5]                    4   5   6   7
        self.heap = [None]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return root
        

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        # only have to call for top half bc there's nowhere for leaves to go
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)
        
    def _bubble_up(self, index):
        parent_idx = index // 2
        while index > 1 and self.heap[index] < self.heap[parent_idx]:
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx
            parent_idx = index // 2

    def _bubble_down(self, index):
        child_idx = index * 2
        while child_idx < len(self.heap):
            # right child exists in heap and is smaller
            if child_idx + 1 < len(self.heap) and self.heap[child_idx + 1] < self.heap[child_idx]:
                child_idx += 1

            if self.heap[child_idx] >= self.heap[index]:
                return

            self.heap[child_idx], self.heap[index] = self.heap[index], self.heap[child_idx]
            index = child_idx
            child_idx = index * 2

        