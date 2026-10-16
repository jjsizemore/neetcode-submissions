class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() >= self.getCapacity():
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        res = self.arr[self.length - 1]
        self.arr[self.length - 1] = 0
        self.length -= 1

        return res

    def resize(self) -> None:
        self.arr.extend([0] * len(self.arr))

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return len(self.arr)